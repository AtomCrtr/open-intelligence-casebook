"""Hand-calculated synthetic tests, plus integrity checks on the real public subset."""
import hashlib
import re

import pytest

from tools import reproduce_results as reproduction


def test_unknown_origin_is_bounded_instead_of_imputed():
    # Synthetic fixture: identified 80+20, unknown 25, total 125.
    rows = [{'year': '2017', 'cn8': 'toy', 'partner': p, 'role': role, 'net_mass_100kg': m}
            for p, role, m in [('A', 'identified', '80'), ('B', 'identified', '20'),
                               ('U', 'unidentified', '25'), ('ALL', 'total', '125'),
                               ('MISSING', 'identified', '')]]
    result = reproduction.titanium(rows)[0]
    assert result['hhi_identified_normalized'] == 6800
    assert result['identified_coverage_pct'] == 80
    assert result['hhi_lower_bound_total'] == 4352
    assert result['hhi_upper_bound_total'] == 7312
    with pytest.raises(ValueError, match='Duplicate'):
        reproduction.titanium(rows + rows[:1])
    rows[0]['net_mass_100kg'] = '-1'
    with pytest.raises(ValueError, match='Invalid mass'):
        reproduction.titanium(rows)


def test_graph_counts_isolates_and_removes_campaign_edges_only():
    # All fixtures here are authored for testing; no upstream data is redistributed.
    objects = [{'id': p, 'type': t} for p, t in [('c', 'campaign'), ('a', 'domain-name'),
                                               ('b', 'domain-name'), ('isolated', 'domain-name')]]
    objects += [{'id': str(i), 'type': 'relationship', 'source_ref': a, 'target_ref': b,
                 'relationship_type': kind}
                for i, (a, b, kind) in enumerate([('c', 'a', 'uses'), ('c', 'b', 'uses'),
                                                 ('a', 'b', 'amplifies')])]
    results = reproduction.portal([{'domain': 'EXAMPLE[.]ORG ', 'create date': '01/03/2024'},
                                   {'domain': 'example.org', 'create date': ''}], {'objects': objects})
    assert results['domaines_distincts'] == 1
    assert results['domaines_mars_2024'] == 1
    assert results['stix_noeuds'] == 4
    assert results['composante_principale'] == 3
    assert results['composante_sans_liens_campagne'] == 2
    assert results['relations_sans_liens_campagne'] == 1
    assert results['composante_sans_uses'] == 2
    objects[-1]['target_ref'] = 'absent'
    with pytest.raises(ValueError, match='absent node'):
        reproduction.portal([], {'objects': objects})


def test_changed_source_bytes_are_rejected():
    payload = b'authored fixture'
    record = {'source_id': 'toy', 'byte_size': len(payload), 'sha256': hashlib.sha256(payload).hexdigest()}
    assert reproduction.verified_bytes(payload, record) == payload
    with pytest.raises(ValueError, match='Source bytes differ'):
        reproduction.verified_bytes(b'Authored fixture', record)


def test_real_titanium_subset_recomputes_all_twelve_comparisons():
    results = reproduction.reproduce_titanium()
    assert len(results) == 12
    bars = next(r for r in results if r['cn8'] == '81089030' and r['year'] == '2017')
    assert (bars['identified_coverage_pct'], bars['hhi_lower_bound_total'], bars['hhi_upper_bound_total']) == (97.77, 2860, 3060.3)


def test_evidence_maps_have_exactly_the_provenance_claims():
    for slug, prefix in [('case-01-titanium', 'C1'), ('case-02-portal-kombat', 'C2'),
                         ('case-03-gnss-interference', 'C3'), ('case-04-xz-utils', 'C4')]:
        case = reproduction.ROOT/'cases'/slug
        claims = {r['claim_id'] for r in reproduction.read_csv(case/'provenance.csv')}
        evidence_map = (case/'evidence-map.md').read_text()
        ids = re.findall(r'^\| (' + prefix + r'-PUB-\d+) \|', evidence_map, re.M)
        assert set(ids) == claims
        assert len(ids) == len(claims)
        anchors = re.findall(r'<a id="(c\d-pub-\d+)"></a>', evidence_map)
        assert set(anchors) == {claim.lower() for claim in claims}
        assert len(anchors) == len(claims)
        report_links = re.findall(r'\]\(evidence-map\.md#(c\d-pub-\d+)\)',
                                  (case/'report.md').read_text())
        assert set(report_links) == set(anchors)
