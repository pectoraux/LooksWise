# LooksWise Data Model v1.0

This document defines the minimum authoritative fields needed by implementers. Physical schemas may normalize or denormalize these fields but may not remove their semantics.

## AppearanceState

`id`, `version`, `subjectId`, `sourceMediaRefs`, `regions`, `identityRepresentationRefs`, `confidence`, `createdAt`.

Each region has `regionType`, `representationRef`, `confidence`, and `analysisVersion`.

## Look / LookVersion

`Look` identifies the durable consumer object. `LookVersion` contains immutable transformation references, presentation metadata, creator attribution, publication state, runtime capabilities, evidence tier and provenance.

## TransformationRecipe

`id`, `version`, `inputs`, `nodes`, `edges`, `constraints`, `assets`, `supportedRuntimes`, `validationState`.

## SocialPost

`id`, `authorId`, `lookVersionId`, `resultArtifactId`, `visibilityPolicy`, `opinionAudiencePolicy`, `engagementCounters`, `moderationState`, `externalDistributionState`, timestamps.

## Outcome

`id`, `simulationId`, `serviceOrProductRef`, `observedArtifactRefs`, `measurementRefs`, `context`, `consentScope`, `evidenceRefs`, `evaluationStatus`, timestamps.

## Fidelity

`id`, `simulationId`, `dimensionScores`, `aggregateScore` (optional), `evidenceTier`, `uncertainty`, `calibrationModelVersion`, evaluator version, timestamps.

## Product / Try-On Asset

`productId`, merchant id, SKU, category, targetRegions, assetRefs, geometry/material metadata, supportedRuntimes, evidence tier, version.

## ServiceSpecification

`id`, professional/service reference, exact LookVersion/RecipeVersion, simulation artifact, requested parameters/constraints, fulfillment metadata, booking reference.
