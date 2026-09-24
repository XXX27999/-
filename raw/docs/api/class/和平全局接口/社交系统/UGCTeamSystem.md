# UGCTeamSystem

队伍系统接口库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCTeamSystem.OnTeamMemberJoinDelegate |  | 有玩家加入当前局内玩法队伍时触发<br>生效范围：客户端<br>@param UID number @加入者的 UID |
| UGCTeamSystem.OnTeamMemberLeaveDelegate |  | 有玩家离开当前局内玩法队伍时触发<br>生效范围：客户端<br>@param UID number @离开者的 UID |
| UGCTeamSystem.OnTeamIDChangedDelegate |  | 自己的局内玩法队伍变更时触发<br>生效范围：客户端<br>@param TeamID number @变更后的队伍 ID |
| UGCTeamSystem.OnTeamMemberChangedDelegate |  | 局内玩法队伍成员变更时触发<br>生效范围：服务器<br>@param PlayerKey number @发生变更的玩家 PlayerKey<br>@param OldTeamID number\|nil @变更前的队伍 ID，首次入队为 nil<br>@param NewTeamID number\|nil @变更后的队伍 ID，玩家退出 DS 时为 nil |
| UGCTeamSystem.OnInviteReceivedDelegate |  | 收到他人发来的局内玩法组队邀请时触发<br>生效范围：客户端<br>@param InviterUID number @邀请者 UID<br>@param NickName string @邀请者昵称<br>@param IconUrl string @邀请者头像 URL<br>@param Gender number @邀请者性别，0=隐藏/未知，1=男，2=女 |
| UGCTeamSystem.NotifyInviteToJoinLobbyTeamDelegate |  | 通知被邀请加入大厅队伍<br>生效范围：客户端<br>@param InviteToJoinLobbyTeamToken table @邀请到大厅队伍的 Token。InviteToJoinLobbyTeamToken.InviterUID int @邀请者 UID |
| UGCTeamSystem.NotifyRequestToJoinLobbyTeamDelegate |  | 通知请求加入大厅队伍<br>生效范围：客户端<br>@param RequestToJoinLobbyTeamToken table @请求加入大厅队伍的 Token。RequestToJoinLobbyTeamToken.TeamID int @队伍 ID |

## Functions

### GetTeamComponent

【废弃】获取队伍组件
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTeamPlayersNumber

获取局内玩法队伍人数设置
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ChangePlayerTeamID

改变玩家 TeamID
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |
| TeamID | `number` | 队伍 ID |

**Return**

_None_

### LeaveTeam

主动退出当前局内玩法队伍
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### KickMember

将指定玩家踢出局内玩法队伍，仅队长可用
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetPlayerKey | `number` | 被踢玩家 PlayerKey |

**Return**

_None_

### InviteInGamePlayer

邀请同 DS 玩家加入当前局内玩法组队
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetUID | `number` | 被邀请玩家 UID |

**Return**

_None_

### InviteLobbyFriend

邀请大厅好友加入当前 DS 局内玩法组队
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FriendUID | `number` | 被邀请好友 UID |

**Return**

_None_

### RespondInvite

响应局内玩法组队邀请，接受时自动完成入队
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InviterUID | `number` | 邀请者 UID |
| Accept | `boolean` | true=接受 / false=拒绝 |

**Return**

_None_

### GetTeamLeaderPlayerKeyInGame

获取当前所在局内玩法队伍的队长 PlayerKey
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUIDsByTeamID

根据TeamID获取对应队伍里所有的玩家UID
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeysByTeamID

根据TeamID获取对应队伍里所有的玩家PlayerKey，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |
| bReturnAsLuaTable | `boolean` | 是否以LuaTable返回 |

**Return**

- Type: 
- Description: _None_

### GetAIPlayerKeysByTeamID

根据 TeamID 获取对应队伍里所有的假人玩家 AIPlayerKey，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |
| bReturnAsLuaTable | `boolean` | 是否以LuaTable返回 |

**Return**

- Type: 
- Description: _None_

### GetPlayerControllersByTeamID

根据TeamID获取对应队伍里所有的玩家PlayerController
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |

**Return**

- Type: 
- Description: _None_

### GetPlayerPawnsByTeamID

根据TeamID获取对应队伍里所有的玩家PlayerPawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |

**Return**

- Type: 
- Description: _None_

### GetPlayerStatesByTeamID

根据TeamID获取对应队伍里所有的玩家PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |

**Return**

- Type: 
- Description: _None_

### GetLobbyTeamUIDsByUID

【废弃】请使用 UGCTeamSystem.GetLobbyTeammateUIDsByUID
根据玩家的UID获取其大厅里组队的成员 UID 列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |
| bReturnAsLuaTable | `boolean` | 是否以LuaTable返回 |

**Return**

- Type: 
- Description: _None_

### GetLobbyTeammateUIDsByUID

根据玩家的UID获取其大厅里组队的成员 UID 列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |
| bReturnAsLuaTable | `boolean` | 是否以LuaTable返回 |

**Return**

- Type: 
- Description: _None_

### GetDynamicLobbyTeammateUIDsByUID

根据玩家的UID获取其大厅里组队的成员 UID 列表。跟 UGCTeamSystem.GetLobbyTeammateUIDsByUID 不同的是，此接口会返回动态组队（UGCTeamSystem.InviteToJoinLobbyTeam、UGCTeamSystem.RequestToJoinLobbyTeam）的成员 UID 列表，而 UGCTeamSystem.GetLobbyTeammateUIDsByUID 以及其他接口只会返回从大厅进入战斗对局那一刻的该玩家在大厅组队的成员 UID 列表。
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |

**Return**

- Type: 
- Description: _None_

### GetLobbyTeamKeysByPlayerKey

【废弃】请使用 UGCTeamSystem.GetLobbyTeammatePlayerKeysByPlayerKey
根据玩家的 PlayerKey 获取其大厅里组队的成员 PlayerKey 列表，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |

**Return**

- Type: 
- Description: _None_

### GetLobbyTeammatePlayerKeysByPlayerKey

根据玩家的 PlayerKey 获取其大厅里组队的成员 PlayerKey 列表，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |

**Return**

- Type: 
- Description: _None_

### InviteToJoinLobbyTeam

邀请玩家加入（我的）大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InviteeUID | `number` | 被邀请玩家 UID |

**Return**

_None_

### RespondToInvitingToJoinLobbyTeam

响应加入大厅队伍的邀请
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ResponseOfBeingInvitedToJoinLobby | `EResponseOfBeingInvitedToJoinLobby` | 被邀请加入大厅队伍的响应类型：EResponseOfBeingInvitedToJoinLobby |
| InviteToJoinLobbyTeamToken | `table` | 邀请到大厅队伍的 Token |

**Return**

_None_

### RequestToJoinLobbyTeam

玩家请求加入大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamMemberUID | `number` | 大厅队伍中的玩家 UID |

**Return**

_None_

### RespondToRequestingToJoinLobbyTeam

队长响应被加入大厅队伍的请求
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ResponseOfBeingRequestedToJoinLobby | `EResponseOfBeingRequestedToJoinLobby` | 被请求加入大厅队伍的响应类型：EResponseOfBeingRequestedToJoinLobby |
| RequestToJoinLobbyTeamToken | `table` | 请求加入大厅队伍的 Token |

**Return**

_None_

### QuitLobbyTeam

玩家主动退出大厅队伍
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### KickFromLobbyTeam

队长将指定玩家踢出大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetUID | `number` | 被踢玩家的 UID |

**Return**

_None_

### TransferLobbyTeamLeader

队长转让大厅队长身份给指定玩家
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLeaderUID | `number` | 新队长的 UID |

**Return**

_None_

### GetTeamIDs

获取所有队伍的 ID
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bReturnAsLuaTable | `boolean` | 是否以LuaTable返回 |

**Return**

- Type: 
- Description: _None_

### GetPlayerList

获取所有玩家信息列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bWithOB? | `boolean` | 是否包含 OB |

**Return**

- Type: 
- Description: _None_

### GetTeamSizeByID

【废弃】请使用 UGCTeamSystem.GetTeamSizeByTeamID
获取队伍中的玩家数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |

**Return**

- Type: 
- Description: _None_

### GetTeamSizeByTeamID

获取队伍中的玩家数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |

**Return**

- Type: 
- Description: _None_

### GetTeamLeaderKeyByTeamID

通过队伍编号获取队长PlayerKey列表（每个在大厅点击开始游戏的玩家都会被设置为队长，例如四人匹配，队伍里只有一个队长，三人匹配，再随机匹配一个队友，三人里面点击开始游戏的是队长，随机匹配的那个队友也是队长，属于他自己那个小队的队长）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |

**Return**

- Type: 
- Description: _None_

### GetIsLeaderOrNotByPlayerKey

通过玩家PlayerKey查询身份
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |

**Return**

- Type: 
- Description: _None_

### GetAllTeammatePlayerState

获取所有队友的的PlayerState
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bExcludeSelf | `boolean` | 是否排除玩家自身 |
| bReturnAsLuaTable | `boolean` | 是否以LuaTable返回 |

**Return**

- Type: 
- Description: _None_

### GetTeammatePlayerStateByPlayerKey

获取指定PlayerKey队友的的PlayerState
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |

**Return**

- Type: 
- Description: _None_

### IsTeamIDValid

判断TeamID是否合法
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | TeamID |

**Return**

- Type: 
- Description: _None_

### GetTeamIDByPlayerKey

根据PlayerKey获取队伍ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |

**Return**

- Type: 
- Description: _None_

### GetTeammateIndexByPlayerKey

根据PlayerKey获取队友ID(头顶标号)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `ASTExtraPlayerState` | 玩家 PlayerState |
| PlayerKey | `number` | 玩家 PlayerKey |

**Return**

- Type: 
- Description: _None_

### GetAllTeammateIndex

获取所有队友的的队友ID(头顶标号)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `ASTExtraPlayerState` | 玩家 PlayerState |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeyByTeammateIndex

根据队友ID(头顶标号)获取队友PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `ASTExtraPlayerState` | 玩家 PlayerState |
| TeammateIndex | `number` | 队友ID |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua
