# Implementation Guide

## Authoritative order

1. `spec/architecture/ARCHITECTURE.md`
2. `spec/architecture/ARCHITECTURE-LOCK.md`
3. `spec/requirements.md`
4. `spec/work-items.md`
5. `spec/dependency-graph.md`
6. `spec/development-state/*`
7. individual `spec/work-orders/*.md`

## Implementation protocol

For each eligible Work Item:

1. Create one branch for the Work Item.
2. Read its architecture constraints, requirements, acceptance criteria and expected change surfaces.
3. Implement only within those surfaces unless an approved change is recorded.
4. Add/update automated verification.
5. Open one PR for the Work Item.
6. Attach objective evidence to the Work Item/PR.
7. Verification must pass before architect review.
8. Architect review can approve, request changes, block, or require an architecture change.
9. Only the architect is the merge authority.
10. After merge, update the machine-readable development state and frontier.

## Assurance profiles

- `LIGHT`: low-risk docs/UI-only changes.
- `STANDARD`: normal product/backend work.
- `HIGH_ASSURANCE`: media-processing, privacy, commerce, recommendation, or provider-routing work.
- `CRITICAL`: medical-aesthetic, identity, consent, payments, security, or reality-calibration infrastructure.

Assurance profiles add verification depth; they never weaken authority rules.

## Parallel implementation

Parallelism is allowed only when Work Items are dependency-eligible and their declared change surfaces do not conflict. Shared contracts should be implemented first to unlock parallel vertical work.
