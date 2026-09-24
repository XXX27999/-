# FAnimNode_HandIKRetargeting_UE5

Node to handle re-targeting of Hand IK bone chain.
  It looks at position in Mesh Space of Left and Right IK bones, and moves Left and Right IK bones to those.
  based on HandFKWeight. (0 = favor left hand, 1 = favor right hand, 0.5 = equal weight).
  This is used so characters of different proportions can handle the same props.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| RightHandFK | `FBoneReference` | Bone for Right Hand FK |
| LeftHandFK | `FBoneReference` | Bone for Left Hand FK |
| RightHandIK | `FBoneReference` | Bone for Right Hand IK |
| LeftHandIK | `FBoneReference` | Bone for Left Hand IK |
| IKBonesToMove | `TArray < FBoneReference >` | IK Bones to move. |
| HandFKWeight | `float` | Which hand to favor. 0.5 is equal weight for both, 1 = right hand, 0 = left hand. |
