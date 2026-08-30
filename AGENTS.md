# LooksWise Agent Instructions

1. Read `spec/architecture/ARCHITECTURE.md` and `spec/architecture/ARCHITECTURE-LOCK.md` before implementing anything.
2. Read the active Work Item in `spec/work-orders/` and `spec/development-state/frontier-state.json`.
3. Implement only a dependency-eligible Work Item assigned to the implementation frontier.
4. Never modify frozen architecture documents during ordinary implementation.
5. Never invent new domain authority by bypassing explicit module boundaries.
6. Never bind application/domain code directly to a specific AI provider or LLM vendor.
7. Never treat a prompt as the canonical representation of a professional Look; the Transformation Recipe is authoritative.
8. Every implementation claim must have evidence: tests, contracts, fixtures, measurements, screenshots, or equivalent objective artifacts.
9. One Work Item per implementation branch/PR. Do not combine unrelated Work Items.
10. Keep generated media and large binary artifacts out of git unless explicitly required; use stable artifact references in tests/specifications.
11. If the architecture is insufficient, stop implementation and issue an Architecture Change Request rather than silently changing the architecture.
12. Do not add Zeck-specific contracts in v1.0. The architecture intentionally leaves execution-engine integration behind a future adapter boundary.
