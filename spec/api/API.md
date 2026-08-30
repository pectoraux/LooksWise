# LooksWise Platform API

## Design principle

Expose semantic capabilities. Never require developers to select a model merely to invoke a LooksWise capability.

## Core resources

`/v1/appearance-profiles`
`/v1/looks`
`/v1/transformations`
`/v1/render-jobs`
`/v1/media`
`/v1/try-on`
`/v1/products`
`/v1/professionals`
`/v1/services`
`/v1/bookings`
`/v1/social-posts`
`/v1/recommendations`
`/v1/fidelity`
`/v1/webhooks`

## Example

```http
POST /v1/looks/apply
Idempotency-Key: ...

{
  "look_id": "look_123",
  "input": { "media_id": "media_456" },
  "runtime": "photo_high_fidelity"
}
```

The response returns a job/resource identifier and normalized execution metadata, not provider credentials.

## Async lifecycle

```text
accepted → processing → verifying → completed
                            └──────→ failed
```

Webhooks deliver terminal state transitions.

## API products

1. Transform API: apply Looks/Recipes to images/video.
2. Live API: runtime configuration and compatible Look packages.
3. Discovery API: Look search/recommendation/compatibility.
4. Try-On API: product and composite Look try-on.
5. Social API: publish/like/comment/share hooks for embedded experiences.
6. Professional API: Look authoring and service synchronization.
7. Fidelity API: evidence and outcome data for eligible partners.
