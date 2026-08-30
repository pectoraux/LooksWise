# LooksWise

LooksWise is a cross-platform visual transformation platform. Its primary abstraction is a **Look**: a versioned, reusable transformation that can be applied to an AppearanceState across live camera, photos, video, commerce try-on, professional workflows, and external developer applications.

LooksWise is not architecturally dependent on a specific LLM, image model, video model, vendor gateway, or AI provider. Providers implement capabilities behind adapters. LLMs are optional planning/intelligence participants; deterministic and specialist rendering paths must remain possible without an LLM.

## Core loop

```text
AppearanceState + Professional/Brand-authored Transformation
                    ↓
                 Simulation
                    ↓
         Community / Professional Opinion
                    ↓
             Book / Buy / Share
                    ↓
              Real-world outcome
                    ↓
          Fidelity measurement + learning
                    ↓
               Better simulation
```

## Product surfaces

- Consumer app: Look browsing, live camera, photo/video editing, sharing, social validation, FYP recommendations, try-on and booking.
- Professional Studio: author, test, publish and version Looks; expose real services; collect evidence and outcome calibration.
- Commerce Platform: product representation and virtual try-on APIs.
- Developer Platform: API/SDK access to LooksWise transformation capabilities.
- Reality Engine: learns mapping from digital simulations to observed real-world outcomes.

## Current architecture status

Architecture v1.0 is intended to be frozen before implementation. Zeck is deliberately **not** a dependency in this architecture. A future execution-engine adapter may be introduced through an Architecture Change Request after Zeck reaches a stable release.

## Repository governance

The development process adapts the proven WorkflowOS governance model:

- frozen architecture + immutable architecture versions
- repository-resident requirements and acceptance criteria
- dependency-aware Work Items
- one Work Item per implementation branch/PR
- declared change surfaces
- evidence over implementation claims
- automated verification before architect review
- architect-only approval/merge gate
- machine-readable development state for resumability
- architecture changes only through explicit Architecture Change Requests

Start with `AGENTS.md`, `IMPLEMENTATION.md`, `docs/ARCHITECT-RUNBOOK.md`, `docs/WORKER-RUNBOOK.md`, and `spec/development-state/`.
