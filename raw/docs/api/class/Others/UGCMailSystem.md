# UGCMailSystem

邮件系统库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCMailSystem.MailListUpdateDelegate |  | 玩家邮件列表更新时触发<br>非PIE时，仅在玩家刚进入玩法时触发一次，玩家在局内时后台发送的邮件，会在下一局进入时更新<br>@param UID int @UID<br>@param MailList UGCMailInfo[] @邮件列表 |
| UGCMailSystem.ClaimMailsResultDelegate |  | 收到领取邮件奖励结果后触发<br>@param UID int @UID<br>@param ItemList table @奖励物品列表<br>@param ClaimedMailIDs int[] @已领取的邮件ID数组<br>@param FailedResults table<ID,EUGCMailOperationFailedReason> @失败邮件 |
| UGCMailSystem.ReadMailsResultDelegate |  | 收到标记邮件已阅读结果后触发<br>@param UID int @UID<br>@param ReadMailIDs int[] @已阅读的邮件ID数组<br>@param FailedResults table<ID,EUGCMailOperationFailedReason> @失败邮件 |
| UGCMailSystem.DeleteReadMailsResultDelegate |  | 收到删除已读邮件结果后触发<br>@param UID int @UID<br>@param DeletedMailIDs int[] @已删除的邮件ID数组<br>@param FailedResults table<ID,EUGCMailOperationFailedReason> @失败邮件 |

## Functions

### IsMailSystemEnabled

获取邮件系统是否开启，PIE下默认开启
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMailList

获取指定玩家的邮件列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `int` | UID |

**Return**

- Type: 
- Description: _None_

### GetMailInfo

获取指定玩家的邮件信息
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `int` | UID |
| MailID | `int` | 邮件ID |

**Return**

- Type: 
- Description: _None_

### ClaimMailAward

请求领取指定玩家的邮件奖励
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `int` | UID |
| MailIDs | `int[]` | 邮件ID数组 |

**Return**

_None_

### ReadMail

请求标记指定玩家的邮件已读
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `int` | UID |
| MailIDs | `int[]` | 邮件ID数组 |

**Return**

_None_

### DeleteReadMail

请求删除指定玩家的已读邮件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `int` | UID |
| MailIDs | `int[]` | 邮件ID数组 |

**Return**

_None_

### PIESendMail

发送邮件, 仅PIE环境有效
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `int` | UID |
| Title | `string` | 邮件标题 |
| Content | `string` | 邮件内容 |
| ExpireTime | `int` | 过期时间 |
| Attachments | `table` | 附件 {[ItemID]=Count, ...} |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
