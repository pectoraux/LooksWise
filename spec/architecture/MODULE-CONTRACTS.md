# LooksWise Module Contracts v1.0

This document makes the module boundaries implementable. Modules own their persisted state and invariants. Other modules interact through application interfaces and domain events, never by importing another module's persistence internals.

## Module ownership

| Module | Owns | Publishes/Consumes |
|---|---|---|
| identity | User, tenant, session, role | consent, authorization context |
| appearance | AppearanceState, region taxonomy, analysis versions | media-created, appearance-updated |
| looks | Look, LookVersion, presentation metadata | look-published, look-withdrawn |
| transformations | Transformation, Recipe, node/edge, constraints, composition | render-requested, plan-compiled |
| capabilities | Capability definitions, implementations, compatibility | capability-registered |
| providers | provider adapters, model metadata, health/cost/capability observations | provider-health-changed |
| media | MediaAsset, DerivedArtifact, storage references | artifact-created |
| social | SocialPost, likes, comments, saves, audience policy | engagement events |
| moderation | reports, blocks, moderation decisions, abuse signals | moderation state events |
| recommendations | candidate generation/ranking features and feed sessions | recommendation-served |
| professionals | Professional, professional Look authoring state | professional-look events |
| marketplace | service offerings and service specifications | service-requested |
| bookings | booking lifecycle and booking references | booking events |
| commerce | Merchant, Product, Try-On Asset, purchase attribution | try-on events |
| reality | Prediction, Observation, Outcome, Fidelity, CalibrationModel | fidelity-updated |
| medical-aesthetics | medical simulation records and safeguards | medical-simulation events |
| provenance | artifact lineage and provenance records | provenance-created |
| api | external resource mapping, API auth, idempotency, pagination | API events |
| llm | optional intent/authoring assistance | suggestion-created |
| analytics | non-authoritative product analytics | telemetry events |
| notifications | delivery requests and provider adapters | notification events |
| audit | append-oriented audit events | audit records |

## Forbidden dependencies

- Domain modules must not import provider SDKs directly.
- Domain modules must not read another module's tables directly.
- Frontends must not implement authoritative authorization, ranking eligibility, consent, or workflow decisions.
- LLM responses are suggestions or plans; they do not become persisted domain truth without domain validation/approval.
- Public API DTOs must not expose provider-specific request formats as the required contract.

## Core ports

```text
AppearanceRepository
LookRepository
TransformationRepository
CapabilityRegistry
ProviderRegistry
ArtifactStore
JobQueue
AuthorizationService
ConsentService
ProvenanceWriter
ModerationService
RecommendationService
FidelityService
```

Every port has a domain-facing interface and one or more adapters. Adapters are the only place where infrastructure/provider specifics appear.

## Domain events

Events must be versioned, contain an event id and aggregate id, and be safe to process more than once. Consumers must use idempotency keys derived from the event identity.
