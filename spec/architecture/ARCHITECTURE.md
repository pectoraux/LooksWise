# LooksWise Architecture

**Version:** 1.0
**Status:** FROZEN BASELINE

## 1. Purpose

LooksWise is a provider-independent visual transformation platform. A Look is a reusable transformation authored by a professional, brand, platform operator, or user and represented as a versioned Transformation Recipe. The platform applies the recipe to an AppearanceState through capability implementations, verifies constraints, records provenance, enables social validation and commercial action, and learns from real-world outcomes.

## 2. Core abstractions

### 2.1 AppearanceState

The canonical structured representation of the visible state of a person/scene. It may reference identity, face, hair, skin, body, hands, feet, clothing, accessories, pose and environment representations. It is versioned and confidence-bearing.

### 2.2 Look

The primary consumer-facing object. A Look packages a presentation layer around one or more Transformation Recipes and may be published, discovered, applied live, rendered to media, shared, remixed where permitted, exposed through APIs, used for commerce, or mapped to a real-world service.

### 2.3 Transformation

A semantic transformation from one AppearanceState to another. Formally: `T(AppearanceState, Context) -> AppearanceState`.

### 2.4 Transformation Recipe

The authoritative, versioned, machine-readable definition of a Transformation. A recipe consists of nodes, parameters, constraints, target regions, dependencies, assets and supported execution modes. Prompts are optional authoring aids and never the canonical representation.

### 2.5 Capability

A semantic operation such as face tracking, makeup transfer, hair shape transfer, garment transfer, identity preservation, temporal consistency or physical-fit estimation. Implementations of capabilities are replaceable.

### 2.6 Reality Engine

A subsystem that records, models and learns the relationship between simulated transformations and observed real-world outcomes. It must expose evidence tiers and uncertainty rather than inventing physical certainty.

## 3. High-level topology

```text
                 ┌────────────────────────────┐
                 │     LooksWise Clients      │
                 │ iOS / Android / Web / SDKs │
                 └──────────────┬─────────────┘
                                │
                 ┌──────────────▼─────────────┐
                 │   Experience/API Layer     │
                 │ camera/editor/feed/try-on  │
                 │ social/booking/commerce     │
                 └──────────────┬─────────────┘
                                │
                 ┌──────────────▼─────────────┐
                 │       Looks Domain         │
                 │ Look / Recipe / Service    │
                 │ Opinion / Commerce / UGC   │
                 └──────────────┬─────────────┘
                                │
        ┌───────────────────────┼────────────────────────┐
        ▼                       ▼                        ▼
┌───────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Appearance    │     │ Transformation   │     │ Reality Engine   │
│ Platform      │     │ Engine           │     │                  │
│               │     │ compiler/runtime │     │ outcomes/fit     │
└───────┬───────┘     └────────┬─────────┘     └────────┬─────────┘
        │                      │                        │
        └──────────────────────┼────────────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Capability Layer     │
                    │ CV / AR / 3D / GenAI │
                    │ physics / evaluation │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Provider Adapters    │
                    │ direct / hosted /    │
                    │ local / gateways     │
                    └──────────────────────┘
```

## 4. Domain modules

The initial modular-monolith boundaries are:

`/identity`, `/appearance`, `/looks`, `/transformations`, `/capabilities`, `/media`, `/social`, `/recommendations`, `/professionals`, `/marketplace`, `/commerce`, `/bookings`, `/reality`, `/medical-aesthetics`, `/provenance`, `/providers`, `/llm`, `/api`, `/analytics`, `/moderation`, `/notifications`, `/audit`.

Each module owns its domain state and business rules. Cross-module interaction occurs through explicit interfaces/events.

## 5. Social validation

A consumer can publish a Look application or transformation result as a Social Look Post. Other users can like it, comment, save, remix where permitted, or share it externally.

Authors can define an **Opinion Audience Policy** for each post:

- all eligible users;
- a selected audience;
- optional gender-based eligibility control where legally and product-policy permissible.

Gender is a visibility/control attribute for participation, not a score dimension and not an assertion that one gender has superior judgment. Server-side policy evaluation is authoritative. The platform must support reporting, blocking, moderation, rate limits, anti-brigading and abuse controls.

The author can separately choose whether to expose the post to external social sharing. External platforms are uncontrolled opinion channels and are clearly represented as such.

## 6. Feed and browsing

The consumer feed is a Look discovery surface with two-dimensional navigation:

- vertical swipe: move between professionals/creators or algorithmically ranked Look streams;
- horizontal swipe: explore Looks from the current professional/creator;
- live camera overlay: apply the current Look in real time;
- For You ranking: recommendations use interaction history, explicit preferences, context, Look compatibility and safety/eligibility constraints.

The feed algorithm recommends Looks first, then professionals/brands attached to those Looks.

## 7. Media model

The platform supports live camera, image, video and high-fidelity rendering. Live rendering prioritizes low latency; high-fidelity rendering prioritizes fidelity and verification. Media edits are non-destructive and represented as graphs where practical.

## 8. Reality learning

Every outcome may record predicted result, observed result, measurements, context, product/material metadata, professional identity, consent scope and evaluation deltas. Reality Engine models are trained/evaluated only from data within the applicable consent and governance scope.

Clothing fit evolves through evidence tiers from appearance-only to measurement-based fit to physical simulation. The UI must not present low-evidence output as physical certainty.

## 9. Provider/model independence

Domain modules consume semantic capabilities. Capability implementations are accessed through provider adapters. A provider may be a direct API, model host, local runtime, specialist vendor, gateway such as OpenRouter, or future implementation. The product must not assume any provider is permanent.

LLMs are optional and may perform intent interpretation, Look search planning, authoring assistance, explanation and other non-authoritative tasks. LLMs do not own domain truth or workflow state.

## 10. Developer platform

LooksWise exposes transformation capabilities through REST/HTTP APIs, webhooks, and SDKs. Supported concepts include appearance analysis, Look discovery, Look application, photo/video transformation, product try-on, professional/marketplace integration, service booking hooks, fidelity/evaluation, and event streams.

The API is capability-oriented rather than model-oriented.

## 11. Commerce

A product can be transformed into a machine-readable Try-On Asset with target regions, geometry/appearance information, product metadata, and evidence tier. Products can be tried on individually or as a composite Look. Merchant applications can invoke APIs without implementing their own visual transformation stack.

## 12. Medical-aesthetic boundary

Plastic-surgery and other medical-aesthetic simulation is an isolated vertical with stricter consent, disclaimers, clinician attribution where applicable, evidence tiers, anatomical plausibility checks, audit logging and regulatory review. Consumer inspiration mode is distinct from clinical planning mode. The platform must not guarantee surgical outcomes.

## 13. Security and privacy

AppearanceState, biometric-like representations, measurements, social-opinion controls, service outcomes and medical-aesthetic records are separately classified data. Tenant/user authorization is enforced server-side. Media access uses scoped tokens. Consent is explicit and revocable where applicable. Retention and deletion policies are first-class.

## 14. Provenance

Every generated artifact records source media, AppearanceState version, Look/Recipe version, capability implementation, provider/model metadata, execution identity, evaluation results and consent scope. Export can include compatible content provenance credentials where supported.

## 15. Initial deployment shape

A modular monolith with background workers is the initial topology. Object storage holds media artifacts; PostgreSQL holds authoritative domain state; a queue/worker layer handles asynchronous transformation jobs; caches may accelerate feed, asset and capability lookups. Services may later be extracted without changing domain contracts.

## 16. External distribution

LooksWise supports optional external distribution of immutable Looks through target-specific adapters and packages. A distribution package may target a social/effect platform, web share, QR/deep link, or embedded experience. External publication/engagement is never authoritative over LooksWise Look state or controlled opinion. The platform must survive external target capability/review changes without invalidating the canonical Look.

## 17. Client surfaces

The cross-platform product surface includes consumer clients, professional Look Studio, merchant/product management surfaces, and developer-facing SDK/examples. Shared semantic contracts are platform-neutral; camera/AR and rendering primitives may be platform-specific.
