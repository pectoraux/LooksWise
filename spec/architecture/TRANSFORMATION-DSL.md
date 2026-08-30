# LooksWise Transformation DSL v1.0

The Transformation DSL is the canonical machine-readable representation of a Look transformation. A prompt may assist authoring, but a prompt is never authoritative.

## 1. Top-level shape

A Transformation Recipe MUST contain:

- `id`: stable transformation identifier;
- `version`: positive immutable version number;
- `inputs`: declared required and optional input resources;
- `nodes`: ordered semantic transformation operations;
- `edges`: explicit data/dependency relationships;
- `constraints`: preservation, prohibition and execution constraints;
- `supportedRuntimes`: one or more of `live`, `photo`, `video`, `high_fidelity`, `try_on`.

Optional top-level fields include `assets` and `validationState`.

Unknown top-level fields MUST NOT be relied upon by the core compiler unless a versioned extension is explicitly registered.

## 2. Node contract

Each node MUST contain:

- `id`: unique within the recipe;
- `operation`: stable semantic capability/operation identifier;
- `target`: one or more stable region identifiers or a declared non-spatial scope;
- `parameters`: operation-specific structured parameters;
- `constraints`: optional node-local constraints.

A node MAY declare `dependsOn` for explicit ordering when the graph edge itself is insufficient for human-readable intent.

Examples of semantic operations include:

- `identity.preserve`
- `face.track`
- `makeup.base`
- `makeup.contour`
- `makeup.blush`
- `makeup.eye-shadow`
- `makeup.eyeliner`
- `makeup.mascara`
- `makeup.lip`
- `hair.shape`
- `hair.color`
- `hair.volume`
- `garment.replace`
- `garment.color`
- `garment.material`
- `skin.finish`
- `jewelry.apply`
- `body.appearance-transform`
- `relight.scene`

The list is extensible through registered capability identifiers; implementations must not invent vendor-specific operation identifiers in a published recipe.

## 3. Region targeting

Targets MUST use stable semantic identifiers from `spec/architecture/REGION-TAXONOMY.md`.

A renderer may internally map regions to landmarks, masks, meshes or other representations, but those implementation details are not recipe authority.

## 4. Edges

An edge MUST contain `from` and `to` node identifiers and MAY contain `kind`.

Supported edge kinds are:

- `data`: output of one node is required by another;
- `ordering`: the destination must execute after the source;
- `constraint`: the source establishes a condition consumed by the destination.

The compiler MUST reject references to missing nodes and cycles unless a future DSL version explicitly introduces iterative semantics.

## 5. Constraints

Constraints are explicit policy, not prompt prose.

Supported constraint groups include:

- `preserve`: attributes that must remain unchanged;
- `prohibit`: transformations that must not occur;
- `quality`: required verification/quality thresholds;
- `runtime`: execution/runtime constraints;
- `consent`: required consent scopes.

A recipe MUST NOT encode a transformation prohibition only as natural-language text.

## 6. Assets

Assets reference immutable or versioned platform resources. Assets may represent products, textures, reference media, geometry, patterns or professional-authored calibration artifacts.

Recipes reference assets by stable IDs; raw binary content is stored outside the recipe.

## 7. Runtime compatibility

`live` recipes MUST be executable by a live-compatible capability set.

A recipe that contains only high-fidelity capabilities MUST NOT be silently downgraded into live execution. The runtime compiler must report `UNSUPPORTED` or an explicit approximation/downgrade result.

## 8. Validation lifecycle

Recommended lifecycle:

```text
DRAFT
  ↓
VALIDATING
  ├── REJECTED
  └── VALID
       ↓
PUBLISHED (domain lifecycle, not a recipe mutation)
```

Validation MUST check:

- schema validity;
- node/edge references;
- region identifiers;
- runtime capability compatibility;
- constraint completeness;
- asset references;
- prohibition of vendor-specific domain authority;
- reproducibility/provenance requirements.

## 9. Compilation

Compilation resolves a recipe into a semantic execution plan.

The compiler MUST NOT select a provider merely because the recipe contains a provider/model name. Provider selection occurs after capability eligibility and policy constraints are evaluated.

The compiled plan records:

- recipe identity/version;
- normalized node ordering;
- capability requirements;
- selected runtime;
- hard constraints;
- provenance inputs.

The plan identity is deterministic for equivalent immutable inputs, recipe version, capability implementation versions and runtime configuration.

## 10. Professional authoring

Before/after inference may propose nodes and parameters, but an inferred recipe remains `DRAFT` until a professional or authorized owner explicitly approves it.

Once published, a recipe version is immutable. Corrections create a new version.
