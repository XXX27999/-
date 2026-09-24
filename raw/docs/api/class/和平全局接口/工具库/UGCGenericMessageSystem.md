# UGCGenericMessageSystem

广播信息接口库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCGenericMessageSystem.Messages |  |  |
| UGCGenericMessageSystem.GlobalMessageListeners |  |  |
| UGCGenericMessageSystem.ObjectMessageListeners |  |  |
| UGCGenericMessageSystem.Messages.UGC.Player |  | 玩家相关消息 |
| UGCGenericMessageSystem.Messages.UGC.Player.PlayerEnter |  | 玩家进入游戏<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| UGCGenericMessageSystem.Messages.UGC.Player.PlayerExit |  | 玩家退出游戏<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| UGCGenericMessageSystem.Messages.UGC.Player.PlayerLost |  | 玩家掉线<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| UGCGenericMessageSystem.Messages.UGC.Player.PlayerReconnect |  | 玩家重连进入游戏<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn |  | 玩家角色相关的消息 |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PawnSpawn |  | 玩家角色首次出生<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PreTakeDamage |  | 玩家角色受到伤害前（最终伤害计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色，不指定则接收所有角色消息<br>@param VictimPlayer ASTExtraBaseCharacter @造成伤害的玩家角色<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PostTakeDamage |  | 玩家角色受到伤害后（最终伤害计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色，不指定则接收所有角色消息<br>@param VictimPlayer ASTExtraBaseCharacter @造成伤害的玩家角色<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PreRecoverHealth |  | 玩家角色受到治疗前（最终治疗计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色<br>@param RecoverValue float @预治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PostRecoverHealth |  | 玩家角色受到治疗后（最终治疗计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色<br>@param RecoverValue float @实际治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PawnDefeat |  | 玩家角色被击败<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param VictimPlayerKey number @被击败玩家的 PlayerKey<br>@param InstigatorPlayerKey number @击败玩家的 PlayerKey<br>@param DamageType EDamageType @伤害类型 |
| UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PawnRespawn |  | 玩家角色重生<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| UGCGenericMessageSystem.Messages.UGC.FakePlayer |  | 假人玩家相关消息 |
| UGCGenericMessageSystem.Messages.UGC.FakePlayer.FakePlayerEnter |  | 假人玩家进入游戏<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @假人玩家的 PlayerKey<br>@param AIController number @假人玩家的 控制器 |
| UGCGenericMessageSystem.Messages.UGC.MobPawn |  |  |
| UGCGenericMessageSystem.Messages.UGC.MobPawn.Spawn |  | 怪物角色首次出生<br>生效范围：服务器&客户端<br>ListenedObject：指定生成的怪物，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @怪物 |
| UGCGenericMessageSystem.Messages.UGC.MobPawn.PreTakeDamage |  | 怪物角色受到伤害前（最终伤害计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @怪物<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| UGCGenericMessageSystem.Messages.UGC.MobPawn.PostTakeDamage |  | 怪物角色受到伤害后（最终伤害计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @怪物<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| UGCGenericMessageSystem.Messages.UGC.MobPawn.PreRecoverHealth |  | 怪物角色受到治疗前（最终治疗计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色<br>@param RecoverValue float @预治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| UGCGenericMessageSystem.Messages.UGC.MobPawn.PostRecoverHealth |  | 怪物角色受到治疗后（最终治疗计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色<br>@param RecoverValue float @实际治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| UGCGenericMessageSystem.Messages.UGC.MobPawn.PostBeKilled |  | 怪物角色被击杀<br>生效范围：服务器&客户端<br>ListenedObject：指定被击杀怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物<br>@param Killer Controller @击杀该怪物的玩家控制器 |
| UGCGenericMessageSystem.Messages.UGC.MobPawn.StateChange |  | 怪物角色状态变化<br>生效范围：服务器&客户端<br>ListenedObject：指定改变状态的怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物<br>@param OldState EUGCMobState @变化前的状态<br>@param NewState EUGCMobState @变化后的状态 |
| UGCGenericMessageSystem.Messages.UGC.MobSpawner |  | 刷怪器相关的消息 |
| UGCGenericMessageSystem.Messages.UGC.MobSpawner.WaveStart |  | 刷怪管理器波次开始<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobSpawnerManager AUGCMobSpawnerManager @波次所属的刷怪管理器<br>@param WaveIndex number |
| UGCGenericMessageSystem.Messages.UGC.MobSpawner.WaveEnd |  | 刷怪管理器波次结束<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobSpawnerManager AUGCMobSpawnerManager @波次所属的刷怪管理器<br>@param WaveIndex number |
| UGCGenericMessageSystem.Messages.UGC.MobSpawner.AllWaveEnd |  | 刷怪管理器所有波次结束<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物 |
| UGCGenericMessageSystem.Messages.UGC.MobSpawner.AllMobDie |  | 刷怪管理器所有波次的怪物死亡<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物 |
| UGCGenericMessageSystem.Messages.UGC.Client |  |  |
| UGCGenericMessageSystem.Messages.UGC.Client.MainUI |  |  |
| UGCGenericMessageSystem.Messages.UGC.Client.MainUI.InitMainUI |  | 初始化和平 MainUI<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param PC Controller @初始化 MainUI 的玩家控制器 |
| UGCGenericMessageSystem.Messages.UGC.Game |  |  |
| UGCGenericMessageSystem.Messages.UGC.Game.GameEnd |  | 游戏结束<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| UGCGenericMessageSystem.Messages.UGC.Game.GameStart |  | 游戏开始<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| UGCGenericMessageSystem.Messages.UGC.GamePart |  |  |
| UGCGenericMessageSystem.Messages.UGC.GamePart.GamePartLoaded |  | GamePart 加载完成。在此消息回调中执行 GetGamePartGlobalActor 以确保 GamePart 对象可用。<br>生效范围：服务器&客户端<br>ListenedObject：无，全局事件<br>@param GamePart string @加载完成的 GamePart 模块 |
| UGCGenericMessageSystem.Messages.UGC.GamePart.GamePartLoadedForPlayer |  | GamePart 加载完成。在此消息回调中执行 GetGamePartGlobalActor 以确保 GamePart 对象可用。<br>ForPlayer 可区分不同客户端上运行的 GamePart 模块。<br>生效范围：服务器&客户端<br>ListenedObject：无，全局事件<br>@param GamePart string @加载完成的 GamePart 模块<br>@param PlayerController PlayerController @加载完成的 GamePart 模块所属的客户端玩家控制器 |
| UGCGenericMessageSystem.Messages.UGC.Weapon |  | 枪械相关的消息 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.BulletHit |  | 枪械的子弹命中<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械<br>@param Data FBulletHitInfoUploadData @命中数据 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.Fire |  | 枪械开火<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.StopFire |  | 枪械停火<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.PostEquipWeapon |  | 枪械装备<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param bIsEquip boolean @是否装备<br>@param Player ASTExtraCharacter @持有者<br>@param Weapon ASTExtraWeapon @当前武器 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.Reload |  | 枪械换弹<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.ScopeIn |  | 枪械开镜<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.ScopeOut |  | 枪械关镜<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| UGCGenericMessageSystem.Messages.UGC.Weapon.SwitchWeapon |  | 枪械切换<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param NewGun ASTExtraShootWeapon @新武器<br>@param OldGun ASTExtraShootWeapon @老武器<br>@param Player ASTExtraCharacter @持有者 |
| UGCGenericMessageSystem.Messages.UGC.Attribute |  |  |
| UGCGenericMessageSystem.Messages.UGC.Attribute.GlobalAttrChanged |  | 全局属性改变<br>生效范围：服务器<br>ListenedObject：监听的属性，不指定监听的属性则接收所有属性消息<br>@param OwnerActor AActor @属性所有者<br>@param AttrName string @属性名<br>@param CurValue number @属性值 |
| UGCGenericMessageSystem.Messages.UGC.LevelFlow |  |  |
| UGCGenericMessageSystem.Messages.UGC.LevelFlow.LevelBegin |  | 关卡开始<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param int CurrentStage @当前关卡数 |
| UGCGenericMessageSystem.Messages.UGC.LevelFlow.GameBegin |  | 游戏开始<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| UGCGenericMessageSystem.Messages.UGC.Task |  |  |
| UGCGenericMessageSystem.Messages.UGC.Task.TaskCreated |  | 任务模板中所有任务初始化完毕<br>生效范围：服务器&客户端<br>ListenedObject：指定任务监听器，不指定则接受所有任务监听器消息 |
| UGCGenericMessageSystem.Messages.UGC.PersistEffect |  |  |
| UGCGenericMessageSystem.Messages.UGC.PersistEffect.ApplyPersistEffect |  | PersistEffect挂载到UPersistBaseComponent<br>生效范围：服务器&客户端<br>ListenedObject：指定UPersistBaseComponent，不指定则接收所有UPersistBaseComponent消息<br>@param PE UPersistEffectBase @当前挂载的PersistEffect |
| UGCGenericMessageSystem.Messages.UGC.PersistEffect.UnApplyPersistEffect |  | PersistEffect从UPersistBaseComponent上卸载<br>生效范围：服务器&客户端<br>ListenedObject：指定UPersistBaseComponent，不指定则接收所有UPersistBaseComponent消息<br>@param PE UPersistEffectBase @当前卸载的PersistEffect |
| UGCGenericMessageSystem.Messages.UGC.PersistEffect.ChangeState |  | PersistEffectSkill的状态改变<br>生效范围：服务器&客户端<br>ListenedObject：指定UPersistEffectSkill，不指定则接收所有UPersistEffectSkill消息<br>@param PESkill UPersistEffectSkill @当前改变状态的PersistEffectSkill<br>@param EventType EPSkillEventSkillStateEvent @当前改变后的状态 |
| UGCGenericMessageSystem.Messages.UGC.Team |  | 队伍相关 |
| UGCGenericMessageSystem.Messages.UGC.Team.TeammateLogin |  | 有队员加入队伍<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @加入队伍玩家的PlayerKey<br>@param TeamID number @队伍ID |
| UGCGenericMessageSystem.Messages.UGC.AirDrop |  |  |
| UGCGenericMessageSystem.Messages.UGC.AirDrop.SuccessfullyGeneratedAirDrop |  | 成功生成AirDrop<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param InsID number @空投箱实例ID<br>@param AirDropBox BP_UGCAirDropBox_GamePart_C @空投箱 |
| UGCGenericMessageSystem.Messages.UGC.AirDrop.SuccessfullyDestroyedAirDrop |  | 成功销毁AirDrop<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param InsID number @空投箱实例ID |
| UGCGenericMessageSystem.Messages.UGC.AirDrop.SuccessfullyPickedUpAirDrop |  | 成功拾取AirDrop<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param InsID number @空投箱实例ID |
| UGCGenericMessageSystem.Messages.UGC.TowerWave |  | 塔防波次相关消息 |
| UGCGenericMessageSystem.Messages.UGC.TowerWave.WaveChanged |  | 波次变化（客户端本地通知）<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param CurrentWaveIndex number @当前波次索引（从0开始，-1=未开始）<br>@param TotalWaveCount number @总波次数 |
| UGCGenericMessageSystem.Messages.UGC.TowerWave.StateChanged |  | 波次状态变化（客户端本地通知）<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param CurrentWaveIndex number @当前波次索引<br>@param WaveState number @波次状态（EWaveState枚举值） |
| UGCGenericMessageSystem.Messages.UGC.TowerWave.CountdownChanged |  | 倒计时变化（客户端本地通知）<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param Countdown number @剩余倒计时（秒） |
| UGCGenericMessageSystem.Messages.UGC.TowerWave.AllComplete |  | 所有波次完成<br>生效范围：服务器&客户端<br>ListenedObject：无，全局事件<br>@param TotalWaveCount number @总波次数 |
| UGCGenericMessageSystem.Messages.UGC.TowerWave.RequestRoundEnd |  | 请求回合结束（所有波次完成后触发）<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| UGCGenericMessageSystem.UserDefinedMessages.UGC.UGCDSShutDownManager.DSCloseNotify |  | DS关闭前通知<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param DSRemainingTime table @DS剩余时间，唯一key: DSRemainingTime |

## Functions

### ListenObjectMessage

监听对象的广播信息，作用包含ListenUserDefinedObjectMessage，正常仅调用本接口即可
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ListenedObject | [UObject](../../Others/UObject.md) | 被监听对象 |
| Message | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| Listener | [UObject](../../Others/UObject.md) | 监听对象 |
| Callback | `function` | 监听对象监听到广播后调用的回调函数 |

**Return**

- Type: 
- Description: _None_

### BroadcastUserDefinedObjectMessage

广播自定义的对象消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ListenedObject | [UObject](../../Others/UObject.md) | 被监听对象 |
| Message | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| ... | `any` | 自定义事件参数 |

**Return**

_None_

### ListenGlobalMessage

监听全局的广播信息，作用包含ListenUserDefinedGlobalMessage，正常仅调用本接口即可
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Message | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| Listener | [UObject](../../Others/UObject.md) | 监听对象 |
| Callback | `function` | 监听对象监听到广播后调用的回调函数 |

**Return**

- Type: 
- Description: _None_

### ListenUserDefinedGlobalMessage

监听自定义的全局广播信息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Message | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| Listener | [UObject](../../Others/UObject.md) | 监听对象 |
| Callback | `function` | 监听对象监听到广播后调用的回调函数 |

**Return**

- Type: 
- Description: _None_

### BroadcastUserDefinedGlobalMessage

广播自定义的全局消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| ... | `any` | 自定义事件参数 |

**Return**

_None_

### UnListenMessage

解除监听对象以及全局的广播信息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Listener | `UObject\|number` | 监听对象/监听ID |
| Message | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |

**Return**

_None_

### GetRemoteMessageHandle

获取远程消息句柄
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 消息名称 |

**Return**

- Type: 
- Description: _None_

### SendServerMessage

从客户端发送消息到服务器
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 消息名称 |
| ... | `any` | 消息参数 |

**Return**

_None_

### SendAllClientMessage

从服务器广播消息到客户端
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 消息名称 |
| ... | `any` | 消息参数 |

**Return**

_None_

### SendClientMessage

从服务器发送消息到客户端
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 消息名称 |
| PlayerKey | `number` | 玩家的 PlayerKey |
| ... | `any` | 消息参数 |

**Return**

_None_

### ListenRemoteMessage

监听远程消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 消息名称 |
| Callback | `function\|UGCCommonDelegate` | 回调函数或委托 |
| CallbackOwner | `table\|UObject\|nil` | 回调函数的所有者 |

**Return**

_None_

### UnListenRemoteMessage

取消监听远程消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 消息名称 |
| Callback | `function\|UGCCommonDelegate` | 回调函数或委托 |
| CallbackOwner | `table\|UObject\|nil` | 回调函数的所有者 |

**Return**

_None_

### RegisterUserDefinedMessage

注册自定义消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |

**Return**

- Type: 
- Description: _None_

### ClearAllListeners

清理所有用户自定义消息监听器(全局 + 对象)。
保护用途:对局退出 / 重新进入 LoadMap 前主动清空监听表,
使其中持有的 WeakObjectPtr 弱引用随 Lua GC 释放,
避免上一局残留监听器引用已销毁的 UObject / ULevel。
生效范围:服务器&客户端

**Parameters**

_None_

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
