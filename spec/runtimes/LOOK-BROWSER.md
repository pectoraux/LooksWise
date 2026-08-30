# LooksWise Look Browser v1.0

## Interaction contract

The browser is a two-dimensional discovery surface with a live preview.

- Vertical swipe advances to the next eligible professional/creator stream.
- Horizontal swipe advances through the eligible Looks belonging to the current professional/creator.
- When the user enters an algorithmically ranked stream, each vertical transition resolves a new stream key deterministically from the feed session cursor.
- A Look is previewed on the user's camera when its runtime capability is compatible with the current device and capture mode.
- A Look may be viewed without camera access; live preview is an enhancement, not a requirement for feed correctness.
- Save, like, comment, share and booking actions are associated with the exact Look version presented.

## Feed session state

A feed session stores an opaque session id, ranking context version, candidate cursor, current professional/creator, current Look version, safety/eligibility policy version and exposure timestamp.

## Ranking boundary

Recommendation service returns an ordered candidate list after hard eligibility/visibility/safety filtering. The client cannot reorder or bypass those filters.
