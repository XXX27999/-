# UAnimCompress_RemoveLinearKeys

## Parents

- [UAnimCompress](./UAnimCompress.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaxPosDiff | `float` | Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| MaxAngleDiff | `float` | Maximum angle difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| MaxScaleDiff | `float` | Maximum Scale difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| MaxEffectorDiff | `float` | As keys are tested for removal, we monitor the effects all the way down to the end effectors.<br>	  If their position changes by more than this amount as a result of removing a key, the key will be retained.<br>	  This value is used for all bones except the end-effectors parent. |
| MinEffectorDiff | `float` | As keys are tested for removal, we monitor the effects all the way down to the end effectors.<br>	  If their position changes by more than this amount as a result of removing a key, the key will be retained.<br>	  This value is used for the end-effectors parent, allowing tighter restrictions near the end of a skeletal chain. |
| EffectorDiffSocket | `float` | Error threshold for End Effectors with Sockets attached to them.<br>	  Typically more important bone, where we want to be less aggressive with compression. |
| ParentKeyScale | `float` | A scale value which increases the likelihood that a bone will retain a key if it's parent also had a key at the same time position.<br>	  Higher values can remove shaking artifacts from the animation, at the cost of compression. |
| bRetarget | `uint32` | true = As the animation is compressed, adjust animated nodes to compensate for compression error.<br>	  false= Do not adjust animated nodes. |
| bActuallyFilterLinearKeys | `uint32` | Controls whether the final filtering step will occur, or only the retargetting after bitwise compression.<br>	   If both this and bRetarget are false, then the linear compressor will do no better than the underlying bitwise compressor, extremely slowly. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
