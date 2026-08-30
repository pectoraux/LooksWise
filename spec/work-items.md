# LooksWise Work Items v1.0

Each Work Item is one independently reviewable implementation unit. It must reference the frozen Architecture Version 1.0, named requirements, named acceptance criteria, dependencies, change surfaces, verification, and explicit out-of-scope boundaries.

## Phase 1 — Foundation

### W001 — Modular monolith and repository foundation
Requirements: platform foundation
Dependencies: none
Acceptance: PLAT-AC-01, PLAT-AC-02
Surfaces: repository root, runtime, shared interfaces, workers, test harness, architecture checks
Verification: unit tests, architecture-boundary tests, job idempotency tests

### W002 — Identity, consent, privacy and tenant boundaries
Requirements: LW-CORE-001, LW-SOC-003, LW-SOC-005, consent/privacy baseline
Dependencies: W001
Acceptance: ID-AC-01, ID-AC-02, ID-AC-03
Surfaces: identity, authorization, consent, privacy
Verification: API authorization matrix, consent/revocation tests, media-access tests

### W003 — Media, object storage and asynchronous job substrate
Requirements: LW-CORE-005, LW-MEDIA-001, LW-MEDIA-002
Dependencies: W001, W002
Acceptance: PLAT-AC-02, ID-AC-03
Surfaces: media, storage, jobs
Verification: upload/access tests, async lifecycle tests, duplicate-job tests

### W004 — Core domain persistence
Requirements: LW-CORE-001, LW-CORE-002, LW-PRO-002, LW-REAL-001
Dependencies: W002, W003
Acceptance: CORE-AC-01, CORE-AC-05
Surfaces: core domain schemas/migrations
Verification: migration tests, immutability constraints, repository tests

## Phase 2 — Transformation Substrate

### W005 — AppearanceState engine
Requirements: LW-CORE-001, LW-CORE-004
Dependencies: W004
Acceptance: CORE-AC-01, CORE-AC-03
Surfaces: appearance, region taxonomy, analysis contracts
Verification: schema/contract tests, versioning tests, region fixture tests

### W006 — Look and Transformation Recipe model
Requirements: LW-CORE-002, LW-CORE-003, LW-CORE-004
Dependencies: W004, W005
Acceptance: CORE-AC-01, CORE-AC-03, CORE-AC-05
Surfaces: looks, transformations, composition, contracts
Verification: schema validation, plan-equivalence tests, version immutability tests

### W007 — Capability registry and provider adapters
Requirements: LW-CORE-003, provider-independence invariant
Dependencies: W004, W006
Acceptance: CORE-AC-02
Surfaces: capabilities, providers, adapters
Verification: adapter contract tests, provider-swap tests, static boundary checks

### W008 — Transformation compiler/runtime
Requirements: LW-CORE-003, LW-CORE-004, LW-CORE-005
Dependencies: W005, W006, W007
Acceptance: CORE-AC-01, CORE-AC-03, CORE-AC-04
Surfaces: transformation compiler/runtime, execution, provenance
Verification: deterministic plan tests, constraint propagation tests, provenance tests

### W009 — Professional Look authoring backend
Requirements: LW-PRO-001, LW-PRO-002
Dependencies: W006, W008
Acceptance: PRO-AC-01, PRO-AC-02
Surfaces: professionals, looks, transformations
Verification: authoring workflow tests, approval/publish/versioning tests

## Phase 3 — Social and Consumer Creation

### W010 — Social Look posts and opinion policies
Requirements: LW-SOC-001..004, LW-SOC-006
Dependencies: W002, W006, W003
Acceptance: SOC-AC-01, SOC-AC-02, SOC-AC-03, SOC-AC-04
Surfaces: social, moderation interfaces, API
Verification: API/UI policy matrix, engagement tests, external-share accounting tests

### W011 — Moderation, safety and anti-abuse controls
Requirements: LW-SOC-005
Dependencies: W010
Acceptance: SOC-AC-05
Surfaces: moderation, social, audit
Verification: abuse simulations, rate-limit tests, block/report tests, audit tests

### W012 — Look recommendation and For You ranking
Requirements: LW-DISC-004, LW-DISC-005
Dependencies: W005, W006, W010
Acceptance: FEED-AC-02, FEED-AC-04
Surfaces: recommendations, analytics
Verification: ranking feature tests, eligibility filter tests, offline evaluation fixtures

### W013 — Photo/video editor runtime
Requirements: LW-MEDIA-001, LW-MEDIA-002, LW-MEDIA-003
Dependencies: W003, W008
Acceptance: MEDIA-AC-01, MEDIA-AC-02, MEDIA-AC-03
Surfaces: media, transformations, provenance
Verification: image/video integration tests, temporal QA tests, non-destructive rerender tests

### W014 — Live camera Look runtime
Requirements: LW-DISC-003, LW-MEDIA-004
Dependencies: W005, W006, W007
Acceptance: FEED-AC-03, MEDIA-AC-04
Surfaces: runtimes/live, appearance, capabilities
Verification: capability compatibility tests, mocked device-runtime tests, unsupported-mode tests

### W024 — Consumer Look browsing experience
Requirements: LW-DISC-001..005, LW-SOC-001..006
Dependencies: W010, W011, W012, W013, W014
Acceptance: FEED-AC-01, FEED-AC-02, SOC-AC-01, SOC-AC-04
Surfaces: consumer application
Verification: browser/mobile E2E tests, navigation fixtures, social validation tests

## Phase 4 — Marketplace and Commerce

### W015 — Professional services and service specifications
Requirements: LW-PRO-003, LW-PRO-004
Dependencies: W009, W006
Acceptance: PRO-AC-03, PRO-AC-04
Surfaces: professionals, marketplace, bookings
Verification: exact-version binding tests, service specification contract tests

### W016 — Commerce product Try-On
Requirements: LW-COM-001, LW-COM-002, LW-COM-003
Dependencies: W005, W007, W008
Acceptance: COM-AC-01, COM-AC-02, COM-AC-03
Surfaces: commerce, capabilities
Verification: API contract tests, asset compatibility tests, composite provenance tests

### W017 — Developer Platform API and webhooks
Requirements: LW-API-001..005
Dependencies: W006, W008, W016
Acceptance: API-AC-01, API-AC-02, API-AC-03, API-AC-04, API-AC-05
Surfaces: api, contracts
Verification: contract tests, auth/authorization tests, webhook signature/idempotency tests

### W025 — Merchant/developer integration examples
Requirements: LW-COM-004, LW-API-006
Dependencies: W017
Acceptance: API-AC-05, API-AC-06
Surfaces: examples, sdk
Verification: example integration E2E tests

## Phase 5 — Reality Learning

### W018 — Reality Engine outcome model
Requirements: LW-REAL-001, LW-REAL-003
Dependencies: W003, W015, W016
Acceptance: REAL-AC-01, REAL-AC-03
Surfaces: reality, marketplace, commerce
Verification: consented outcome fixtures, evidence-tier tests

### W019 — Fidelity and calibration loop
Requirements: LW-REAL-002, LW-REAL-003, LW-REAL-004
Dependencies: W018, W008
Acceptance: REAL-AC-02, REAL-AC-03, REAL-AC-04
Surfaces: reality, evaluation
Verification: prediction/observation tests, calibration gating tests, historical reproducibility tests

## Phase 6 — Verticalization

### W021 — Makeup vertical
Requirements: makeup capability subset of LW-CORE-003, LW-MEDIA-001
Dependencies: W008, W014, W019
Acceptance: CORE-AC-01, MEDIA-AC-01
Surfaces: verticals/makeup
Verification: representative transformation fixtures, constraint/provenance tests

### W022 — Hair and barber vertical
Requirements: hair capability subset of LW-CORE-003, LW-MEDIA-001
Dependencies: W008, W014, W019
Acceptance: CORE-AC-01, MEDIA-AC-01
Surfaces: verticals/hair
Verification: representative hairstyle fixtures, identity/provenance tests

### W023 — Fashion and garment vertical
Requirements: LW-COM-001..004, LW-REAL-002, LW-REAL-004
Dependencies: W008, W016, W018, W019
Acceptance: COM-AC-01, COM-AC-02, REAL-AC-02, REAL-AC-04
Surfaces: verticals/fashion
Verification: garment compatibility tests, evidence-tier tests, physical-behavior calibration fixtures

## Phase 7 — Medical Aesthetics and Cross-platform

### W020 — Medical-aesthetic domain boundary
Requirements: LW-MED-001..004
Dependencies: W005, W008, W018
Acceptance: MED-AC-01, MED-AC-02, MED-AC-03, MED-AC-04
Surfaces: medical-aesthetics, moderation, provenance
Verification: API isolation tests, disclaimer tests, plausibility gate tests, authorization tests

### W026 — Medical-aesthetic validation package
Requirements: LW-MED-001..004
Dependencies: W020, W019
Acceptance: MED-AC-01, MED-AC-02, MED-AC-03, MED-AC-04
Surfaces: tests, verticals/medical-aesthetics
Verification: adversarial safeguards, auditability, plausibility regression suite

### W027 — Cross-platform clients and SDKs
Requirements: LW-API-006, LW-MEDIA-004, LW-DISC-001..003
Dependencies: W014, W017, W024
Acceptance: API-AC-06, FEED-AC-01, FEED-AC-03
Surfaces: iOS, Android, Web, React Native, Flutter, SDK contracts
Verification: contract compatibility suite plus platform smoke tests

## Phase 8 — Production Proof


### W029 — External distribution and effect packaging
Requirements: LW-DIST-001..003, LW-SOC-006
Dependencies: W006, W008, W024, W027
Acceptance: DIST-AC-01, DIST-AC-02
Surfaces: distribution, social, share/export
Verification: package contract tests, target-adapter isolation tests, external-state separation tests

### W030 — End-to-end LooksWise lifecycle
Requirements: all v1.0 requirements
Dependencies: W019, W024, W025, W026, W027, W029
Acceptance: E2E-AC-01 plus all mandatory criteria exercised by the seeded scenario
Surfaces: E2E fixtures, evidence, docs
Verification: full production-like lifecycle test and evidence package
