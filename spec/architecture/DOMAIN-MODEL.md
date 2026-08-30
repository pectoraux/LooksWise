# LooksWise Domain Model

```text
Person ──1:1── AppearanceState (versioned)
Professional ──1:N── ProfessionalLook
Brand ──1:N── Product
Look ──1:N── TransformationVersion
TransformationVersion ──1:N── Node
Node ──uses── Capability
Capability ──implemented-by── CapabilityImplementation
Implementation ──provided-by── Provider
Simulation ──uses── LookVersion + AppearanceStateVersion
SocialLookPost ──references── Simulation
ServiceSpecification ──references── LookVersion + Simulation
Booking ──fulfills── ServiceSpecification
Purchase ──references── Product/Look
Outcome ──references── Simulation + Service/Purchase
FidelityMeasurement ──compares── Prediction + Outcome
```

Primary invariants are defined in `ARCHITECTURE-LOCK.md`.
