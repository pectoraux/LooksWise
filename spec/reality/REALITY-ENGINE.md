# Reality Engine

The Reality Engine exists to make LooksWise increasingly faithful to the real world.

## Core entities

`Prediction`, `Observation`, `Outcome`, `RealityMeasurement`, `MaterialProfile`, `FitProfile`, `FidelityMeasurement`, `CalibrationModel`, `EvidenceTier`.

## Learning loop

```text
Simulation → Service/Purchase → Observed Outcome → Difference Analysis
→ Calibration Dataset → Updated Capability/Recipe Parameters → Validation
```

## Evidence tiers

- T0: generative approximation
- T1: model-evaluated
- T2: professional-approved
- T3: demonstrated from verified before/after evidence
- T4: real-world outcome calibrated
- T5: repeatedly validated for the relevant subject/product/context class

The product must expose evidence tier and uncertainty. Higher tiers require stronger evidence; no model may claim physical certainty merely because it produces a photorealistic image.

## Physical behaviour learning

For garments and other physical transformations, the Reality Engine may learn relationships among body dimensions, geometry, materials, construction, stretch, weight, drape, friction, movement and observed outcomes. Measurements and outcome data require explicit permission and appropriate data governance.
