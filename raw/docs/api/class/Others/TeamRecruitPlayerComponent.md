# TeamRecruitPlayerComponent

组队招募玩家组件

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TeamRecruitPlayerComponent.OnPublishRecruitSuccessDelegate |  | 招募发布成功通知<br>生效范围：客户端 |
| TeamRecruitPlayerComponent.OnRecruitWithdrawnOrExpiredDelegate |  | 招募被撤回或过期通知<br>生效范围：客户端 |
| TeamRecruitPlayerComponent.OnQueryRecruitListResultDelegate |  | 招募列表查询结果通知<br>生效范围：客户端<br>@param Recruits FRecruitInfo[]\|nil @招募信息数组，查询失败时为 nil |

## Functions

### PublishRecruit

发布招募，30 秒冷却
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeclarationIndex | `number` | 宣言文案序号（1~6） |
| TargetIndex | `number` | 队伍目标文案序号（1~6） |
| IsGlobalScope | `boolean` | 招募范围，false=本局，true=全局 |

**Return**

_None_

### WithdrawRecruit

撤回招募
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### QueryRecruitList

请求刷新招募列表，5 秒冷却
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsGlobalScope | `boolean` | 招募范围筛选，false=本局，true=全局 |
| TargetIndex | `number` | 队伍目标文案序号（1~6） |

**Return**

_None_

### JoinRecruitedTeam

申请加入招募队伍，5 秒冷却
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RecruitID | `string` | 目标招募 ID |

**Return**

_None_

### CanPublishRecruit

查询是否可发布招募（用于按钮灰显与倒计时显示）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CanRefreshList

查询是否可刷新招募列表（用于按钮灰显与倒计时显示）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CanJoinTeam

查询是否可申请入队（用于按钮灰显与倒计时显示）
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsRecruiting

查询当前所在局内玩法队伍是否正处于招募状态
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
