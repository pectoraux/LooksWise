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
    'spec/architecture/TRANSFORMATION-DSL.md',
    'spec/architecture/REGION-TAXONOMY.md',
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

req_text=(root/'spec/requirements.md').read_text()
req_ids=set(re.findall(r'LW-[A-Z]+-[0-9]{3}', req_text))
ac_text=(root/'spec/acceptance-criteria.md').read_text()
ac_ids=set(re.findall(r'\b([A-Z]+-AC-[0-9]{2})\b', ac_text))

wi_text=(root/'spec/work-items.md').read_text()
wids=re.findall(r'^### (W\d{3})\b', wi_text, re.M)
expected=[f'W{i:03d}' for i in range(1,30)]
if wids != expected:
    raise SystemExit(f'work items must be exactly contiguous W001..W029; found {wids}')

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
    # Every backticked repository path referenced by a Work Order must exist.
    for ref in re.findall(r'`([^`]+)`', wob):
        if ref.startswith(('spec/', 'docs/', '.github/')) and '*' not in ref and not (root/ref).exists():
            raise SystemExit(f'{wid}: missing referenced repository path {ref}')

# Verify dependency references and acceptance references are defined.
deps=[]
for dep_field in re.findall(r'^Dependencies: (.+)$', wi_text, re.M):
    if dep_field != 'none': deps += re.findall(r'W\d{3}', dep_field)
unknown=sorted(set(deps)-set(wids))
if unknown: raise SystemExit('unknown dependency ids: '+', '.join(unknown))

for wid in wids:
    block=re.search(rf'^### {wid}.*?(?=^### W\d+|\Z)', wi_text, re.M|re.S).group(0)
    acfield=re.search(r'^Acceptance: (.+)$', block, re.M).group(1)
    for ac in re.findall(r'\b[A-Z]+-AC-[0-9]{2}\b', acfield):
        if ac not in ac_ids:
            raise SystemExit(f'{wid}: undefined acceptance criterion {ac}')

trace=(root/'spec/requirement-traceability.md').read_text()
for req in sorted(req_ids):
    row=re.search(rf'^\| {re.escape(req)} \| (.+) \|$', trace, re.M)
    if not row or row.group(1).strip()=='UNMAPPED':
        raise SystemExit(f'unmapped requirement: {req}')

state=json.loads((root/'spec/development-state/frontier-state.json').read_text())
model=json.loads((root/'spec/development-state/governance-model.json').read_text())
program=json.loads((root/'spec/development-state/program-state.json').read_text())
if not (state['architectureVersion']==model['architectureVersion']==program['architectureVersion']=='1.0'):
    raise SystemExit('architecture version mismatch')
for wid in state['frontier']:
    if wid not in state['workItems'] or state['workItems'][wid]['status'] != 'READY':
        raise SystemExit(f'frontier item is not READY: {wid}')
if set(state['workItems']) != set(wids):
    raise SystemExit('frontier state Work Items must exactly match spec Work Items')

for path in sorted((root/'spec/contracts').glob('*.json')):
    data=json.loads(path.read_text())
    if '$schema' not in data or '$id' not in data:
        raise SystemExit(f'contract missing schema metadata: {path}')

print('spec artifact set + traceability checks: OK')
