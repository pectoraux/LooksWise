# Contract Index

The JSON Schemas in this directory define wire-level shapes for core resources. Implementers must treat these schemas as minimum contract shapes; domain invariants that JSON Schema cannot express live in the architecture/acceptance documents and must have executable tests.

Planned canonical schema set:

- appearance-state.schema.json
- capability.schema.json
- execution-contract.schema.json
- look.schema.json
- transformation.schema.json
- social-post.schema.json
- try-on.schema.json
- service-outcome.schema.json
- service-specification.schema.json
- fidelity.schema.json
- opinion-policy.schema.json

Schema identifiers use the `https://lookswise.dev/schemas/` namespace and are versioned without mutating an already-published schema contract.
