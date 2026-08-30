# LooksWise Region Taxonomy v1.0

AppearanceState regions are semantic targets. Implementations may use different geometric representations, but the semantic identifiers are stable.

```text
head
head.face
head.face.skin
head.face.forehead
head.face.brows
head.face.eyes
head.face.eye.left
head.face.eye.right
head.face.nose
head.face.cheeks
head.face.lips
head.face.teeth
head.face.jaw
head.face.ears
head.hair
head.scalp
neck
torso
torso.chest
torso.shoulders
torso.waist
arm.left
arm.right
hand.left
hand.right
leg.left
leg.right
foot.left
foot.right
body.full
clothing.upper
clothing.lower
clothing.full
accessories.head
accessories.face
accessories.ear
accessories.neck
accessories.hand
accessories.body
accessories.foot
environment.background
environment.lighting
environment.scene
```

A capability declares which semantic regions it supports. A transformation recipe may target one or more regions. Region aliases may be introduced in future architecture versions but existing identifiers remain stable.
