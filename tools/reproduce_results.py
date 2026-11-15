"""Recompute selected published results from their data, using only Python's stdlib."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with Path(path).open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle))


def titanium(rows):
    groups = defaultdict(list)
    seen = set()
    for row in rows:
        key = row['year'], row['cn8'], row['partner']
        if key in seen:
            raise ValueError(f'Duplicate input: {key}')
        seen.add(key)
        if row['net_mass_100kg'] == '':
            continue  # Missing is not an observed zero.
        mass = float(row['net_mass_100kg'])
        if not math.isfinite(mass) or mass < 0:
            raise ValueError('Invalid mass')
        if row['role'] not in {'identified', 'unidentified', 'total'}:
            raise ValueError('Unknown partner role')
        groups[key[:2]].append((row['partner'], row['role'], mass))
    output = []
    for (year, cn8), values in sorted(groups.items()):
        totals = [mass for _, role, mass in values if role == 'total']
        known = {partner: mass for partner, role, mass in values if role == 'identified' and mass > 0}
        if len(totals) != 1 or not known or totals[0] <= 0:
            raise ValueError('Missing total or identified masses')
        total = totals[0]
        identified = math.fsum(known.values())
        unknown = math.fsum(mass for _, role, mass in values if role == 'unidentified')
        # Match the historical methodology: unknown share rounded to 0.001 percentage point.
        u = round(100 * unknown / total, 3)
        normalized = [100 * mass / identified for mass in known.values()]
        fraction = 1 - u / 100
        if not 0 < fraction <= 1 or identified > total * 1.00001:
            raise ValueError('Inconsistent coverage')
        hhi = math.fsum(share * share for share in normalized)
        lower = hhi * fraction**2
        upper = lower + 2 * u * max(normalized) * fraction + u*u
        output.append({'cn8': cn8, 'year': year,
                       'identified_coverage_pct': round(100 * identified / total, 3),
                       'unidentified_share_pct': u,
                       'hhi_identified_normalized': round(hhi, 1),
                       'hhi_lower_bound_total': round(lower, 1),
                       'hhi_upper_bound_total': round(upper, 1),
                       'largest_partner': max(known, key=known.get),
                       'largest_share_pct': round(max(normalized), 2)})
    return output


def giant(nodes, edges):
    adjacency = {node: set() for node in nodes}
    for edge in edges:
        a, b = edge['source_ref'], edge['target_ref']
        if a not in adjacency or b not in adjacency:
            raise ValueError('Relationship references an absent node')
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(nodes)
    largest = 0
    while unseen:
        stack = [unseen.pop()]
        size = 0
        while stack:
            node = stack.pop()
            size += 1
            neighbours = adjacency[node] & unseen
            unseen -= neighbours
            stack.extend(neighbours)
        largest = max(largest, size)
    return largest


def portal(domains, bundle):
    dates = [datetime.strptime(row['create date'].strip(), '%d/%m/%Y').date().isoformat()
             if row['create date'].strip() else '' for row in domains]
    objects = bundle['objects']
    ids = [item['id'] for item in objects]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate STIX object')
    nodes = {item['id']: item for item in objects if item['type'] != 'relationship'}
    edges = [item for item in objects if item['type'] == 'relationship']
    campaigns = {node for node, item in nodes.items() if item['type'] == 'campaign'}
    without_campaign_edges = [edge for edge in edges if edge['source_ref'] not in campaigns
                              and edge['target_ref'] not in campaigns]
    return {'domaines_viginum': len(domains),
            'domaines_distincts': len({r['domain'].strip().lower().replace('[.]', '.') for r in domains}),
            'domaines_dates': sum(bool(date) for date in dates),
            'domaines_non_dates': sum(not date for date in dates),
            'domaines_mars_2024': sum(date.startswith('2024-03') for date in dates),
            'stix_noeuds': len(nodes), 'stix_relations': len(edges),
            'composante_principale': giant(nodes, edges),
            'composante_sans_liens_campagne': giant(nodes, without_campaign_edges),
            'relations_sans_liens_campagne': len(without_campaign_edges),
            'composante_sans_amplifies': giant(nodes, [e for e in edges if e['relationship_type'] != 'amplifies']),
            'composante_sans_uses': giant(nodes, [e for e in edges if e['relationship_type'] != 'uses'])}


def verified_bytes(data, record):
    if len(data) != record['byte_size'] or hashlib.sha256(data).hexdigest() != record['sha256']:
        raise ValueError(f"Source bytes differ: {record['source_id']}")
    return data


def reproduce_titanium(root=ROOT):
    case = root/'cases/case-01-titanium'
    manifest = json.loads((case/'data/reproduction_manifest.json').read_text())
    data = case/'data/reproduction_masses.csv'
    if hashlib.sha256(data.read_bytes()).hexdigest() != manifest['sha256']:
        raise ValueError('Titanium input hash differs')
    results = titanium(read_csv(data))
    expected = {(r['cn8'], r['year']): r for r in read_csv(case/'data/uncertainty.csv')}
    if {(r['cn8'], r['year']) for r in results} != set(expected):
        raise ValueError('Titanium series missing or unexpected')
    for r in results:
        for field, value in expected[r['cn8'], r['year']].items():
            if field not in {'cn8', 'year'} and float(r[field]) != float(value):
                raise ValueError(f'Titanium mismatch: {r["cn8"]}, {r["year"]}, {field}')
    for published in read_csv(case/'data/key_metrics.csv'):
        for year in ['2017', '2025']:
            result = next(r for r in results if r['cn8'] == published['cn8'] and r['year'] == year)
            if result['hhi_identified_normalized'] != float(published['hhi_'+year]) or result['largest_share_pct'] != float(published['part_'+year+'_pct']):
                raise ValueError('Published metric differs from recomputation')
    return results


def reproduce_portal(root=ROOT, local_files=None):
    case = root/'cases/case-02-portal-kombat'
    records = json.loads((case/'data/reproduction_sources.json').read_text())
    payloads = {}
    for record in records:
        if local_files:
            data = (local_files/(record['source_id']+'.bin')).read_bytes()
        else:
            request = Request(record['url'], headers={'User-Agent': 'OpenIntelligenceCasebook/reproduction'})
            with urlopen(request, timeout=30) as response:
                data = response.read(record['byte_size']+1)
        payloads[record['source_id']] = verified_bytes(data, record)
    domains = list(csv.DictReader(io.StringIO(payloads['S-008'].decode('utf-8-sig'))))
    results = portal(domains, json.loads(payloads['S-031']))
    expected = {r['metric']: int(r['value']) for r in read_csv(case/'data/key_metrics.csv')}
    if any(value != expected[name] for name, value in results.items()):
        raise ValueError('Portal Kombat differs from published metrics')
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('case', choices=['titanium', 'portal'])
    parser.add_argument('--local-files', type=Path, help='External directory with S-008.bin and S-031.bin')
    args = parser.parse_args()
    result = reproduce_titanium() if args.case == 'titanium' else reproduce_portal(local_files=args.local_files)
    print(json.dumps({'status': 'PASS', 'case': args.case, 'results': result}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
