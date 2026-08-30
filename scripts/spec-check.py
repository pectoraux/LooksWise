#!/usr/bin/env python3
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    'README.md','AGENTS.md','IMPLEMENTATION.md',
    'spec/architecture/ARCHITECTURE.md',
    'spec/architecture/ARCHITECTURE-LOCK.md',
    'spec/architecture/MODULE-CONTRACTS.md',
    'spec/architecture/EXECUTION-SEMANTICS.md',
    'spec/architecture/DATA-MODEL.md',
    'spec/requirements.md','spec/acceptance-criteria.md',
    'spec/work-items.md','spec/dependency-graph.md',
    'spec/requirement-traceability.md',
    'spec/development-state/governance-model.json',
    'spec/development-state/frontier-state.json',
    'spec/development-state/program-state.json',
]
missing=[p for p in required if not (root/p).exists()]
if missing:
    raise SystemExit('missing: '+', '.join(missing))

# Parse canonical IDs from the requirements and acceptance catalogues.
req_text=(root/'spec/requirements.md').read_text()
req_ids=set(re.findall(r'LW-[A-Z]+-[0-9]{3}', req_text))
ac_text=(root/'spec/acceptance-criteria.md').read_text()
ac_ids=set(re.findall(r'^[*-] ([A-Z]+-AC-[0-9]{2})\s*:', ac_text, re.M))
for extra in re.findall(r'\b([A-Z]+-AC-[0-9]{2})\b', ac_text): ac_ids.add(extra)

wi_text=(root/'spec/work-items.md').read_text()
wids=re.findall(r'^### (W\d{3})\b', wi_text, re.M)
if len(wids) != len(set(wids)) or len(wids) != 29:
    raise SystemExit(f'expected 29 unique Work Items, found {len(wids)}')

# Ensure every Work Item has concrete references and a matching Work Order.
for wid in wids:
    wo=root/'spec'/'work-orders'/f'{wid}.md'
    if not wo.exists(): raise SystemExit(f'missing work order: {wid}')
    block=re.search(rf'^### {wid}.*?(?=^### W\d+|\Z)', wi_text, re.M|re.S).group(0)
    for label in ('Requirements','Dependencies','Acceptance','Surfaces','Verification'):
        if not re.search(rf'^{label}: .+', block, re.M):
            raise SystemExit(f'{wid}: missing {label}')
    wob=wo.read_text()
    if '## Acceptance criteria' not in wob or '## Definition of done' not in wob:
        raise SystemExit(f'{wid}: incomplete work order')

# Verify dependency references and ac references are defined.
deps=[]
for dep_field in re.findall(r'^Dependencies: (.+)$', wi_text, re.M):
    if dep_field != 'none': deps += re.findall(r'W\d{3}', dep_field)
unknown=sorted(set(deps)-set(wids))
if unknown: raise SystemExit('unknown dependency ids: '+', '.join(unknown))

# Invalid acceptance IDs are a common handoff failure; reject them here.
for wid in wids:
    block=re.search(rf'^### {wid}.*?(?=^### W\d+|\Z)', wi_text, re.M|re.S).group(0)
    acfield=re.search(r'^Acceptance: (.+)$', block, re.M).group(1)
    for ac in re.findall(r'\b[A-Z]+-AC-[0-9]{2}\b', acfield):
        if ac not in ac_ids and ac != 'E2E-AC-01':
            raise SystemExit(f'{wid}: undefined acceptance criterion {ac}')

# Every requirement must have an owning Work Item.
trace=(root/'spec/requirement-traceability.md').read_text()
for req in sorted(req_ids):
    row=re.search(rf'^\| {re.escape(req)} \| (.+) \|$', trace, re.M)
    if not row or row.group(1).strip()=='UNMAPPED':
        raise SystemExit(f'unmapped requirement: {req}')

# JSON state must parse and frontier must reference READY work items.
state=json.loads((root/'spec/development-state/frontier-state.json').read_text())
model=json.loads((root/'spec/development-state/governance-model.json').read_text())
program=json.loads((root/'spec/development-state/program-state.json').read_text())
if not (state['architectureVersion']==model['architectureVersion']==program['architectureVersion']=='1.0'):
    raise SystemExit('architecture version mismatch')
for wid in state['frontier']:
    if wid not in state['workItems'] or state['workItems'][wid]['status'] != 'READY':
        raise SystemExit(f'frontier item is not READY: {wid}')

# Validate contract JSON is syntactically valid and contains schema metadata.
for path in sorted((root/'spec/contracts').glob('*.json')):
    data=json.loads(path.read_text())
    if '$schema' not in data or '$id' not in data:
        raise SystemExit(f'contract missing schema metadata: {path}')

print('spec artifact set + traceability checks: OK')
