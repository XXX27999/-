# UAnimBlueprintGeneratedClass

## Parents

- UBlueprintGeneratedClass
- IAnimClassInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BakedStateMachines | `TArray < FBakedAnimationStateMachine >` |  |
| TargetSkeleton | `USkeleton *` | Target skeleton for this blueprint class |
| AnimNotifies | `TArray < FAnimNotifyEvent >` | A list of anim notifies that state machines (or anything else) may reference |
| RootAnimNodeIndex | `int32` |  |
| OrderedSavedPoseIndices | `TArray < int32 >` |  |
| SyncGroupNames | `TArray < FName >` |  |
| bFMPrecomputeDone | `bool` | 预计算标记：编辑器编译蓝图时（PostCompile）扫描并写入，打包后序列化到.uasset，<br>	   运行时加载后直接读取正确值，无需再次扫描。<br>	   编辑器未编译时为false，懒初始化逻辑会在首次CollectFunctionModule时兜底扫描。 |
| bHasAnyFunctionModule | `bool` | 预计算缓存：该动画蓝图类（含父类继承链）是否含有任何FunctionModule属性。<br>	   仅在bFMPrecomputeDone为true时有效。打包后序列化到.uasset，运行时直接使用。 |
| AnimBlueprintP4Revision | `int32` | 打包构建时（Cook 阶段）写入的 P4 文件修订版本号。<br>	   由 Cook 钩子通过 ISourceControlModule 查询并写入，打包客户端可直接读取。<br>	   -1 表示未写入（编辑器本地编译或旧版本资产）。<br>	   用于回放加载时检测录制时的蓝图版本与当前编辑器版本是否一致。 |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
