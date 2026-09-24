# FAnimNode_PoseSnapshot

Provide a snapshot pose, either from the internal named pose cache or via a supplied snapshot

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Mode | [ESnapshotSourceMode](../../../cppenum/E/ES/ESnapshotSourceMode.md) | How to access the snapshot |
| SnapshotName | `FName` | The name of the snapshot previously stored with SavePoseSnapshot |
| Snapshot | `FPoseSnapshot` | Snapshot to use. This should be populated at first by calling SnapshotPose |
