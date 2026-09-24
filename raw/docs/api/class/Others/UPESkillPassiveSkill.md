# UPESkillPassiveSkill

被动技能实体

## Parents

- [UPersistEffectSkill](./UPersistEffectSkill.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaxActivationCount | `int32` | 最大激活次数，-1表示无限制 |

## Functions

_None_

## Event

| Name | Type | Description |
| --- | --- | --- |
| OnStackChange_BP |  | 生效范围：服务器&客户端<br>	  当 被动技能 堆叠层数变化时调用，比如技能被合并时 |
| CanClientRPCActivate_BP |  | 生效范围：服务器<br>	  当 pes.BlockPassiveSkillClientRPC 开关关闭时，由蓝图决定是否允许客户端 RPC 激活被动技能 |

## Delegate

_None_

## Language

cpp
