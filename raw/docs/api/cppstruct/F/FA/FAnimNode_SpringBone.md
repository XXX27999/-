# FAnimNode_SpringBone

Simple controller that replaces or adds to the translationrotation of a single bone.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SpringBone | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| bLimitDisplacement | `bool` | Limit the amount that a bone can stretch from its ref-pose length. |
| MaxDisplacement | `float` | If bLimitDisplacement is true, this indicates how long a bone can stretch beyond its length in the ref-pose. |
| SpringStiffness | `float` | Stiffness of spring |
| SpringDamping | `float` | Damping of spring |
| ErrorResetThresh | `float` | If spring stretches more than this, reset it. Useful for catching teleports etc |
| bNoZSpring_DEPRECATED | `bool` | If true, Z position is always correct, no spring applied |
| bTranslateX | `bool` | If true take the spring calculation for translation in X |
| bTranslateY | `bool` | If true take the spring calculation for translation in Y |
| bTranslateZ | `bool` | If true take the spring calculation for translation in Z |
| bRotateX | `bool` | If true take the spring calculation for rotation in X |
| bRotateY | `bool` | If true take the spring calculation for rotation in Y |
| bRotateZ | `bool` | If true take the spring calculation for rotation in Z |
