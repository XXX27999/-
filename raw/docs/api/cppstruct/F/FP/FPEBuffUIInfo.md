# FPEBuffUIInfo

Buff的UI信息

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BuffName | `FName` | Buff的名字 |
| OverwriteBuffName | `FName` | 覆盖的Buff名字，该字段不为空时UI优先显示覆盖的Buff名字 |
| BuffDetail | `FString` | Buff的描述 |
| OverwriteBuffDetail | `FString` | 覆盖的Buff描述，该字段不为空时UI优先显示覆盖的Buff描述 |
| BuffIcon | [FSoftObjectPath](../FS/FSoftObjectPath.md) | Buff的图标 |
| OverwriteBuffIcon | [FSoftObjectPath](../FS/FSoftObjectPath.md) | 覆盖的Buff图标，该字段不为空时UI优先显示覆盖的Buff图标 |
| bShowUI | `bool` | Buff是否显示表示当前状态的图标在UI上 |
