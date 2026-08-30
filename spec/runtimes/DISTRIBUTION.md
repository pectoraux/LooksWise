# LooksWise External Distribution v1.0

LooksWise treats external social/effect platforms as distribution targets, not authorities over LooksWise domain state.

## Distribution objects

`DistributionTarget`, `DistributionPackage`, `DistributionAttempt`, `ExternalShare`.

A distribution package references an immutable LookVersion and contains only the target-compatible rendering assets, metadata, attribution and provenance required by that external platform.

## Requirements

- LooksWise can generate a shareable link/media package for supported targets.
- External-platform publication state is never confused with LooksWise Look publication state.
- Platform-specific effect packaging is adapter-based and optional because external platforms may change capabilities or require manual review.
- A Look remains usable in LooksWise even when an external distribution attempt fails.
- External engagement is not counted as controlled LooksWise opinion unless a future approved integration explicitly supplies verified metrics.
