# LooksWise Development Workflow — Adapted from WorkflowOS

WorkflowOS establishes the pattern we are adopting: frozen architecture, requirement/criterion traceability, dependency-aware Work Items, evidence-based verification, architect review, deterministic governance, one Work Item per branch/PR, and repository-resident machine-readable state. LooksWise applies those controls to a product rather than to a software-development workflow.

## Lifecycle

```text
Architecture Draft
  ↓
Architecture Review
  ↓
Architecture Freeze
  ↓
Requirements + Acceptance Criteria
  ↓
Dependency Graph
  ↓
Implementation Frontier
  ↓
Work Order
  ↓
Implementation Agent
  ↓
PR
  ↓
Automated Verification
  ↓
Architect Review
  ├─ Changes Requested → Implementation
  ├─ Architecture Change Required → ACR
  └─ Approved → Merge
  ↓
State Finalization
  ↓
Next Eligible Work Item
```

## Governance rules

- Architecture v1.0 is immutable once frozen.
- Requirements and acceptance criteria live in the repository.
- Every Work Item names dependencies, change surfaces, acceptance and verification.
- The implementation agent never becomes the authority over completion.
- Verification evidence must support the acceptance criteria it claims to prove.
- Only the architect approves/merges implementation work.
- Architecture changes require a new immutable architecture version.
- Parallel Work Items are allowed only when dependency-eligible and non-conflicting.

## LooksWise-specific assurance

Media processing, social opinion controls, recommendation, provider routing, commerce, identity/appearance, Reality Engine learning and medical aesthetics receive elevated assurance. Medical aesthetics and identity/consent changes are critical-assurance work.
