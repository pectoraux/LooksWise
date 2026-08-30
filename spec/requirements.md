# LooksWise Requirements v1.0

## Core platform
- LW-CORE-001: Maintain versioned AppearanceState representations.
- LW-CORE-002: Maintain versioned Looks and Transformation Recipes.
- LW-CORE-003: Compile recipes into capability execution plans.
- LW-CORE-004: Preserve identity and explicit constraints.
- LW-CORE-005: Preserve provenance for every derived artifact.

## Social validation
- LW-SOC-001: Users can publish Look results as social posts.
- LW-SOC-002: Eligible viewers can like/comment/save according to post visibility.
- LW-SOC-003: Authors can define audience eligibility, including optional gender-based restriction where permissible.
- LW-SOC-004: Likes/comments are distinct from private simulation telemetry.
- LW-SOC-005: Social posts support moderation, reporting, blocking, rate limits and anti-abuse controls.
- LW-SOC-006: Posts can be shared externally with explicit uncontrolled-opinion labeling.

## Discovery
- LW-DISC-001: Provide vertical Look browsing.
- LW-DISC-002: Provide horizontal same-professional Look browsing.
- LW-DISC-003: Apply the current Look to live camera preview when supported.
- LW-DISC-004: Provide a personalized For You Look feed.
- LW-DISC-005: Ranking must distinguish taste, compatibility, safety and eligibility.

## Media/editor
- LW-MEDIA-001: Support photo transformation.
- LW-MEDIA-002: Support video transformation with temporal consistency controls.
- LW-MEDIA-003: Support non-destructive Look composition.
- LW-MEDIA-004: Support live camera runtime for compatible Looks.

## Professional marketplace
- LW-PRO-001: Professionals can author Looks from structured controls and/or before-after demonstrations.
- LW-PRO-002: Professionals can version, publish and withdraw Looks.
- LW-PRO-003: Looks can map to real professional services.
- LW-PRO-004: Users can request/book a service using the exact Look version applied.

## Commerce
- LW-COM-001: Merchants can register Try-On Assets.
- LW-COM-002: Users can try products on images and supported live camera/video surfaces.
- LW-COM-003: Products can compose into Looks.
- LW-COM-004: Developer integrations can consume commerce try-on through APIs/SDKs.

## Reality Engine
- LW-REAL-001: Record predicted-vs-observed outcomes with consent.
- LW-REAL-002: Model physical/appearance behaviour for garments and other categories over time.
- LW-REAL-003: Expose evidence tier and uncertainty.
- LW-REAL-004: Feed validated outcomes back into recipe/rendering calibration.

## API/SDK
- LW-API-001: Expose core transformations through API.
- LW-API-002: Expose async jobs/webhooks.
- LW-API-003: Expose Look discovery/recommendation capabilities.
- LW-API-004: Expose image/video editing capabilities.
- LW-API-005: Expose product try-on.
- LW-API-006: Provide cross-platform SDK contracts.

## Medical aesthetics
- LW-MED-001: Isolate medical-aesthetic transformations in a dedicated module.
- LW-MED-002: Provide explicit simulation disclaimers and evidence tiers.
- LW-MED-003: Enforce anatomical plausibility checks where supported.
- LW-MED-004: Keep clinical planning separate from consumer inspiration.

## External distribution
- LW-DIST-001: Looks can be packaged for supported external social/effect distribution targets without changing the canonical Look/Recipe.
- LW-DIST-002: External distribution status is separated from LooksWise publication and in-product opinion state.
- LW-DIST-003: Distribution adapters tolerate target-specific capabilities/review requirements and never make external platforms authoritative over LooksWise domain state.
