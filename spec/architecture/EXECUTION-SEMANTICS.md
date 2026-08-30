# LooksWise Execution Semantics v1.0

## Execution object

Every transformation execution has:

```text
ExecutionRequest
→ ExecutionPlan
→ ExecutionAttempt(s)
→ VerificationResult
→ Artifact(s)
→ ExecutionResult
```

## Request requirements

A request identifies:

- input AppearanceState or source media;
- Look/Recipe version or explicit transformation;
- runtime (`live`, `photo`, `video`, `high_fidelity`, `try_on`);
- constraints;
- caller/tenant;
- consent scope;
- idempotency key for asynchronous requests.

## Planning

The compiler resolves recipe nodes into semantic capability requirements. Provider/model selection happens only after capability eligibility is established. Hard constraints include authorization, consent, runtime support, privacy policy, provider availability, quotas and safety policy. Performance/cost preferences are applied only among eligible implementations.

## Determinism

Same immutable Recipe version + same input contract + same capability implementation version + equivalent runtime configuration must produce equivalent plans. Rendered pixels may differ when an implementation is probabilistic, but plan identity and constraint/provenance bindings remain deterministic.

## Job states

```text
ACCEPTED
→ QUEUED
→ PLANNING
→ EXECUTING
→ VERIFYING
→ COMPLETED
```

Failure states are terminal for the attempt and may create a retry attempt without changing the original execution identity:

```text
FAILED_TRANSIENT
FAILED_PERMANENT
REJECTED_POLICY
REJECTED_UNSUPPORTED
CANCELLED
```

## Verification gate

A result is not `VERIFIED` merely because a renderer returned media. Verification checks required constraints, required provenance, runtime-specific quality checks and evidence requirements. Unsupported or failed checks result in explicit downgrade/failure metadata.

## Provenance

The execution result references immutable identities for input, recipe, capability implementation, provider/model, renderer/runtime version and consent scope.
