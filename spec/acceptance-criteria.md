# LooksWise Acceptance Criteria v1.0

Every criterion is objective, testable where practical, and must have traceable evidence before the owning Work Item can be approved. A Work Item may not cite an undefined criterion.

## Foundation and security

- PLAT-AC-01: Repository checks prove the agreed module boundaries are present and architecture-fence checks fail when ordinary implementation changes frozen architecture files.
- PLAT-AC-02: Background jobs expose durable states, retry/idempotency behavior, and a test demonstrating duplicate submission does not create duplicate logical effects.
- ID-AC-01: Authenticated requests cannot read or mutate another tenant's protected resources through any exposed backend path.
- ID-AC-02: Consent grants are scoped, auditable, enforceable at read/write/learning boundaries, and revocable without leaving the revoked grant effective for new processing.
- ID-AC-03: Media is accessed through scoped authorization, deletion semantics are tested, and protected raw media is not exposed through unscoped public URLs.

## Core transformation platform

- CORE-AC-01: The same AppearanceState/Recipe versions with compatible inputs compile to semantically equivalent execution plans.
- CORE-AC-02: A capability implementation/provider can be swapped in tests without changing domain recipe contracts or API request schemas.
- CORE-AC-03: Identity-preservation and explicit transformation constraints are carried from recipe through execution and are present in verification results.
- CORE-AC-04: Every derived artifact records source media, AppearanceState version, Look/Recipe version, implementation/provider metadata, execution identity, and consent scope.
- CORE-AC-05: Frozen Look/Recipe versions are immutable while withdrawn versions remain historically addressable.

## Social validation

- SOC-AC-01: A Social Look Post can be published with a Look version and result artifact, and eligible viewers can like/comment/save only when visibility and opinion-audience policy permit.
- SOC-AC-02: Audience policy is enforced server-side on every like/comment path, including direct API calls, and unauthorized attempts are denied without leaking restricted participation state.
- SOC-AC-03: Gender-based opinion restrictions, where enabled by product/legal policy, act only as participation eligibility rules and never modify ranking/beauty scores or claim objective superiority.
- SOC-AC-04: External share events are recorded separately from controlled in-product opinions and cannot inflate in-product like/comment counts.
- SOC-AC-05: Reporting, blocking, comment controls, rate limits, anti-brigading signals, moderation state and abuse audit records are testable through API paths.

## Discovery

- FEED-AC-01: Vertical navigation advances to the next eligible professional/creator stream; horizontal navigation resolves to the next eligible Look from the current professional/creator; tests cover boundary conditions.
- FEED-AC-02: For You ranking consumes declared interaction signals and applies hard eligibility/safety/visibility filters before ranking candidates.
- FEED-AC-03: Live camera runtime can identify whether a Look is supported, attach the correct runtime package, and fail gracefully for unsupported Looks.
- FEED-AC-04: Ranking distinguishes preference/taste signals from compatibility, eligibility and safety filters in both stored feature definitions and evaluation output.

## Media/editor

- MEDIA-AC-01: Photo transformation jobs preserve constraints and complete provenance and expose deterministic terminal job states.
- MEDIA-AC-02: Video transformation jobs retain a temporal-consistency evaluation result and surface failures/downgrades instead of silently presenting unstable output as verified.
- MEDIA-AC-03: Non-destructive edits store an editable graph/recipe representation and can rerender from the original source without destructive flattening.
- MEDIA-AC-04: Live runtime enforces declared latency/quality capability constraints and does not invoke unsupported high-fidelity-only operations in a live session.

## Professional marketplace

- PRO-AC-01: A professional can create a structured Look/Recipe and can generate a before/after inference proposal that remains draft until explicitly approved.
- PRO-AC-02: A professional can publish, version and withdraw Looks; published versions cannot be mutated in place.
- PRO-AC-03: A published Look can map to one or more service offerings with pricing/availability metadata without changing the authoritative recipe version.
- PRO-AC-04: A service request created from a simulation contains the exact Look/Recipe version and reference artifact used by the customer.

## Commerce

- COM-AC-01: A merchant can register a Try-On Asset with required target-region and product metadata and render it against a compatible AppearanceState through the API.
- COM-AC-02: Supported photo/live/video try-on paths declare their fidelity/runtime capabilities and reject unsupported combinations explicitly.
- COM-AC-03: Multiple Try-On Assets can compose into a Look while retaining per-product provenance and purchase attribution.
- COM-AC-04: Merchant/client integrations can invoke try-on without selecting or naming a model/provider.

## Reality Engine and calibration

- REAL-AC-01: A consented outcome links the originating simulation to a service/product and observed result with timestamps, evidence references and consent scope.
- REAL-AC-02: Physical/appearance behavior models can store measurements/material/context features and produce a versioned prediction with uncertainty.
- REAL-AC-03: Every reality-dependent output exposes its evidence tier and uncertainty; low-evidence results cannot be represented as verified physical outcomes.
- REAL-AC-04: Calibration updates are gated by evidence/quality thresholds, versioned, reproducible and do not silently change historical results.

## Developer platform

- API-AC-01: Public API requests are expressed in LooksWise domain/capability terms and contain no required provider/model selection.
- API-AC-02: Async requests return durable job identifiers, support idempotency, and expose authenticated/signed webhook completion events.
- API-AC-03: Discovery API exposes Look search/recommendation/compatibility without exposing internal ranking implementation as a required client contract.
- API-AC-04: Photo/video editing APIs support uploads/references, async rendering, provenance and result retrieval through stable versioned contracts.
- API-AC-05: Try-On API supports product and composite Look flows with evidence/fidelity information.
- API-AC-06: SDK contracts remain semantically aligned with the versioned API schemas across Web, iOS, Android, React Native and Flutter targets.

## Medical aesthetics

- MED-AC-01: Medical-aesthetic transformations are rejected or routed to the isolated module when invoked through ordinary beauty/fashion transformation APIs.
- MED-AC-02: Medical-aesthetic outputs display required disclaimers, evidence tier, uncertainty and clinician attribution fields where applicable.
- MED-AC-03: Unsupported/implausible transformations can be blocked or downgraded by an explicit plausibility evaluator whose decision is persisted.
- MED-AC-04: Clinical-planning workflows are separately authorized and cannot be represented as consumer inspiration workflows.

## Production proof

- E2E-AC-01: A seeded professional can publish a Look, a consumer can apply it, publish a social opinion post, share externally, create a service/try-on action, record a consented outcome, update fidelity, and repeat the same flow through the public API.

## External distribution

- DIST-AC-01: A published LookVersion can produce a target-specific distribution package without mutating the canonical Look/Recipe or provenance chain.
- DIST-AC-02: External distribution success/failure and external engagement are stored separately from in-product publication and controlled opinion state.
