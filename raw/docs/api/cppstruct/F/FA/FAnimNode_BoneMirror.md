# FAnimNode_BoneMirror

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Source | `FPoseLink` | The source pose |
| AutoLRConfigs | `TArray < FBoneMirrorConfig_AutoLR >` |  |
| GivenNameConfigs | `TArray < FBoneMirrorConfig_GivenName >` |  |
| Configs | `TArray < FBoneMirrorConfig >` |  |
| PreviewBoneMirrorMapData | `TArray < FBoneMirrorMapData >` | 程序自动生成的镜像骨骼对，仅用于编辑器下检查是否符合预期，不可修改。<br>	  骨骼名字以_INVALID结尾说明没有对应的镜像骨骼，这些都不会被列入实际镜像列表中 |
| bMirror | `bool` |  |
| bResetChild | `bool` |  |
