#!/usr/bin/env python3
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
state = json.loads((root/'spec/development-state/frontier-state.json').read_text())
model = json.loads((root/'spec/development-state/governance-model.json').read_text())
program = json.loads((root/'spec/development-state/program-state.json').read_text())
assert state['architectureVersion'] == model['architectureVersion'] == program['architectureVersion'] == '1.0'
assert model['architectureStatus'] == 'FROZEN'
assert model['authority']['merge'] == 'architect'
assert state['frontier'], 'frontier must not be empty'

wi_text=(root/'spec/work-items.md').read_text()
wids=set(re.findall(r'^### (W\d{3})\b', wi_text, re.M))
assert len(wids)==29
for wid in state['frontier']:
    assert wid in state['workItems'], f'frontier references unknown Work Item {wid}'
    assert state['workItems'][wid]['status'] == 'READY', f'frontier item is not READY: {wid}'

# Validate that a READY item has no unsatisfied dependency in state.
for wid, entry in state['workItems'].items():
    if entry['status'] != 'READY':
        continue
    for dep in entry.get('dependencies', []):
        assert state['workItems'].get(dep, {}).get('status') == 'VERIFIED', f'{wid} READY before dependency {dep} VERIFIED'

assert set(wids) == set(state['workItems']), 'state Work Items must exactly match spec Work Items'

# Architecture/lock files must not be marked mutable in implementation docs.
lock=(root/'spec/architecture/ARCHITECTURE-LOCK.md').read_text()
assert '**Status:** FROZEN' in lock and '**Architecture Version:** 1.0' in lock
print('governance state + frontier checks: OK')
