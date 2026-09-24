# ALevelBounds

Defines level bounds
  Updates bounding box automatically based on actors transformation changes or holds fixed user defined bounding box
  Uses only actors where AActor::IsLevelBoundsRelevant() == true

## Parents

- [AActor](./AActor.md)
- FEditorTickableLevelBounds

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bAutoUpdateBounds | `bool` | Whether to automatically update actor bounds based on all relevant actors bounds belonging to the same level |
| bCalWithoutLandscapeSpline | `bool` |  |

## Functions

### SaveLevelBoudns

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CaculateFoliageLevelBounds

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CaculateLandscapeLevelBounds

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
