# LooksWise Public API Contracts v1.0

The public API is versioned by major path (`/v1`). Breaking changes require a new version.

## Authentication

API clients authenticate with a tenant-scoped credential. User-facing delegated access uses short-lived tokens. Credentials are never passed to capability providers as domain data.

## Common request rules

- JSON request/response for control-plane operations.
- Multipart or signed object-storage upload for large media.
- `Idempotency-Key` required for asynchronous mutating requests.
- Pagination uses opaque cursor tokens.
- Errors use `{code, message, requestId, details?}` without provider secret/error leakage.

## Core endpoint groups

```text
POST /v1/appearance-profiles
GET  /v1/appearance-profiles/{id}

GET  /v1/looks
GET  /v1/looks/{id}
POST /v1/looks/{id}/apply
POST /v1/looks/{id}/simulate

POST /v1/transformations
GET  /v1/transformations/{id}

POST /v1/media
POST /v1/media/transform
POST /v1/video/transform

POST /v1/try-on
POST /v1/products

GET  /v1/recommendations
POST /v1/social-posts
POST /v1/social-posts/{id}/likes
POST /v1/social-posts/{id}/comments
POST /v1/social-posts/{id}/shares

POST /v1/professionals/looks
POST /v1/services/specifications
POST /v1/bookings

GET  /v1/fidelity/{simulationId}
GET  /v1/jobs/{id}
POST /v1/webhooks/endpoints
```

## Job contract

A successful async acceptance returns `jobId`, `status`, `createdAt`, `resourceType`, `resourceId`, and a polling URL. Terminal completion is delivered through a signed webhook with event id, job id, status, resource reference and provenance digest.

## API invariants

- No endpoint requires a provider/model id.
- API responses may expose normalized implementation metadata for transparency, but clients cannot rely on a specific provider/model being present.
- Authorization, consent, social-audience policy and medical-aesthetic safeguards are re-evaluated server-side on every mutating request.
