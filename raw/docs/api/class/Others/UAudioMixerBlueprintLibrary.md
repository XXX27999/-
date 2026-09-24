# UAudioMixerBlueprintLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### AddMasterSubmixEffect

Adds a submix effect preset to the master submix.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| SubmixEffectPreset | `USoundEffectSubmixPreset *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveMasterSubmixEffect

Removes a submix effect preset from the master submix.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| SubmixEffectPreset | `USoundEffectSubmixPreset *` |  |

**Return**

- Type: 
- Description: _None_

### ClearMasterSubmixEffects

Clears all master submix effects.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### AddSourceEffectToPresetChain

Adds source effect entry to preset chain. Only effects the instance of the preset chain

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PresetChain | `USoundEffectSourcePresetChain *` |  |
| Entry | [FSourceEffectChainEntry](../../cppstruct/F/FS/FSourceEffectChainEntry.md) |  |

**Return**

- Type: 
- Description: _None_

### RemoveSourceEffectFromPresetChain

Adds source effect entry to preset chain. Only affects the instance of preset chain.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PresetChain | `USoundEffectSourcePresetChain *` |  |
| EntryIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetBypassSourceEffectChainEntry

Set whether or not to bypass the effect at the source effect chain index.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PresetChain | `USoundEffectSourcePresetChain *` |  |
| EntryIndex | `int32` |  |
| bBypassed | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetNumberOfEntriesInSourceEffectChain

Returns the number of effect chain entries in the given source effect chain.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PresetChain | `USoundEffectSourcePresetChain *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
