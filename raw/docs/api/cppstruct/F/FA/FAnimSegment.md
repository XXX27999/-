# FAnimSegment

this is anim segment that defines what animation and how

## Fields

| Name | Type | Description |
| --- | --- | --- |
| AnimReference | `UAnimSequenceBase *` | Anim Reference to play - only allow AnimSequence or AnimComposite |
| StartPos | `float` | Start Pos within this AnimCompositeBase |
| AnimStartTime | `float` | Time to start playing AnimSequence at. |
| AnimEndTime | `float` | Time to end playing the AnimSequence at. |
| AnimPlayRate | `float` | Playback speed of this animation. If you'd like to reverse, set -1 |
| LoopingCount | `int32` |  |
