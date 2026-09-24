# FAnimNode_ModifyBoneWithFunction

此动画节点可调用指定的动画蓝图函数，用于热更修复动画Pose
  用法：
  1、添加ModifyBoneWithFunction动画节点，
  2、配置CallFunctionName指定函数名（不可与现有函数重名），点编译回创建出指定函数
  3、进入函数进行骨骼数据修改，注：
 		 函数输入的Context可用于获取某个骨骼的数据（GetBoneTransformLocalSpace、GetBoneTransformComponentSpace）
 		 函数输入的Additional Pose BPContext可用于获取附加Pose里的数据（节点支持额外输入多个附加Pose）
 		 函数输出为需要修改的骨骼数组，每个元素为骨骼名和其对应的ComponentSpaceTransform
 		 输出的骨骼数据需要按骨骼Index正向排序（即按骨架中的骨骼从上到下的顺序排序）

## Fields

| Name | Type | Description |
| --- | --- | --- |
| AdditionalPoses | `TArray < FComponentSpacePoseLink >` | Each layer's blended pose |
| FunctionName | `FName` |  |
| CachedPrototypeFunction | `UFunction *` |  |
