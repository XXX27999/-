# UGCStringTextUtility

文本系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### ExportText

导出对象文本，会根据传入的对象类型打印关键信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `string` | 文本对象 |

**Return**

- Type: 
- Description: _None_

### TrimStartOrEnd

修剪字符串的起始和结尾，根据传入的TrimStart和TrimEnd去除字符串头尾的空白字符

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| TrimStart | `boolean` | 是否修剪起始 |
| TrimEnd | `boolean` | 是否修剪结尾 |

**Return**

- Type: 
- Description: _None_

### SplitToArray

将字符串按照分隔符分割成数组

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| Separator | `string` | 分隔符 |

**Return**

- Type: 
- Description: _None_

### StartsWith

判断字符串是否以指定的前缀开头

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| InPrefix | `string` | 前缀 |
| SearchCase | [ESearchCase](../../cppenum/E/ES/ESearchCase.md) | 是否区分大小写 |

**Return**

- Type: 
- Description: _None_

### EndWith

判断字符串是否以指定的后缀结尾

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| InSuffix | `string` | 后缀 |
| SearchCase | [ESearchCase](../../cppenum/E/ES/ESearchCase.md) | 是否区分大小写 |

**Return**

- Type: 
- Description: _None_

### InsertIntoString

在字符串的指定位置插入内容

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceStr | `string` | 源字符串 |
| Content | `string` | 插入内容 |
| Position | `number` | 插入位置 |

**Return**

- Type: 
- Description: _None_

### JoinArrayIntoString

将字符串数组连接成字符串

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStrArray | `table` | 字符串数组 |
| Separator | `string` | 分隔符 |

**Return**

- Type: 
- Description: _None_

### SplitToCharArray

将字符串分割成字符数组

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |

**Return**

- Type: 
- Description: _None_

### ComposedOfDigits

判断字符串是否由数字组成

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |

**Return**

- Type: 
- Description: _None_

### LeftChop

截断字符串的前n个字符

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| Count | `number` | 字符数 |

**Return**

- Type: 
- Description: _None_

### LeftPad

在字符串的左侧填充空白字符使得字符串长度达到指定的长度

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| StrLen | `number` | 指定的长度 |

**Return**

- Type: 
- Description: _None_

### RightChop

截断字符串的后n个字符

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| Count | `number` | 字符数 |

**Return**

- Type: 
- Description: _None_

### RightPad

在字符串的右侧填充空白字符使得字符串长度达到指定的长度

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStr | `string` | 字符串 |
| StrLen | `number` | 指定的长度 |

**Return**

- Type: 
- Description: _None_

### LogTree

打印变量,特别是对table类型做树形输出,仅DEV打印

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Desc | `string` | 变量描述 |
| Var | `any` | 要输出的变量,可以是任何类型table, bool, number, nil |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua
