# FRootMotionExtractionStep

Struct defining a RootMotionExtractionStep.
  When extracting RootMotion we can encounter looping animations (wrap around), or different animations.
  We break those up into different steps, to help with RootMotion extraction,
  as we can only extract a contiguous range per AnimSequence.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| AnimSequence | `UAnimSequence *` | AnimSequence ref |
| StartPosition | `float` | Start position to extract root motion from. |
| EndPosition | `float` | End position to extract root motion to. |
