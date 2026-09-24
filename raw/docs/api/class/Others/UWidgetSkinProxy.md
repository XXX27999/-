# UWidgetSkinProxy

The user widget proxy, using this proxy to activate widget skin for an user widget.

## Parents

- [UObject](./UObject.md)
- IWidgetSkinProxyInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bHideBeforeLoadSkin | `bool` |  |
| ActiveSkins | `TArray < UUserWidgetSkin * >` |  |

## Functions

### ApplySkin

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SkinPathPtr | `TSoftClassPtr < UUserWidgetSkin >` |  |
| bAsyncLoad | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RevertSkin

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SkinPathPtr | `TSoftClassPtr < UUserWidgetSkin >` |  |

**Return**

- Type: 
- Description: _None_

### RevertRevertableSkin

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetActiveSkins

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRevertableSkin

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ContainsSkin

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSkin | `UUserWidgetSkin *` |  |

**Return**

- Type: 
- Description: _None_

### GetOwnerUserWidget

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

cpp
