# LooksWise Dependency Graph v1.0

```text
W001 Foundation
  → W002 Identity/consent/privacy
  → W003 Media/storage/jobs
  → W004 Core persistence
      → W005 AppearanceState
      → W006 Look/Transformation
          → W007 Capability/provider abstraction
          → W008 Transformation compiler/runtime
              → W009 Professional authoring
      → W010 Social posts/policies
          → W011 Moderation/anti-abuse
      → W012 Recommendations/For You
      → W013 Photo/video editor
      → W014 Live camera runtime
      → W015 Service specifications
      → W016 Commerce Try-On
      → W017 Developer API/webhooks
      → W018 Reality outcomes
          → W019 Fidelity/calibration

W008 + W014 + W019 → W021 Makeup
W008 + W014 + W019 → W022 Hair/Barber
W008 + W016 + W018 + W019 → W023 Fashion/Garment
W010 + W011 + W012 + W013 + W014 → W024 Consumer Look Browser
W016 + W017 → W025 Merchant/developer examples
W020 + W019 → W026 Medical-aesthetic validation
W014 + W017 + W024 → W027 Cross-platform clients and SDKs
W006 + W008 + W024 + W027 → W029 External distribution/effect packaging
W019 + W024 + W025 + W026 + W027 + W029 → W030 End-to-end production proof
```

Dependency authority is `spec/development-state/frontier-state.json`; this graph is the human-readable mirror.
