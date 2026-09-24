# UKismetInternationalizationLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### SetCurrentCulture

Set the current culture.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Culture | `FString &` | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| SaveToConfig | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Return**

- Type: 
- Description: _None_

### GetCurrentCulture

Get the current culture as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCurrentLanguage

Set only the current language (for localization).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Culture | `FString &` | The language to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| SaveToConfig | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Return**

- Type: 
- Description: _None_

### GetCurrentLanguage

Get the current language (for localization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCurrentLocale

Set only the current locale (for internationalization).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Culture | `FString &` | The locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| SaveToConfig | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Return**

- Type: 
- Description: _None_

### GetCurrentLocale

Get the current locale (for internationalization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCurrentLanguageAndLocale

Set the current language (for localization) and locale (for internationalization).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Culture | `FString &` | The language and locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| SaveToConfig | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Return**

- Type: 
- Description: _None_

### SetCurrentAssetGroupCulture

Set the given asset group category culture from an IETF language tag (eg, "zh-Hans-CN").

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetGroup | `FName` | The asset group to set the culture for. |
| Culture | `FString &` | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| SaveToConfig | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Return**

- Type: 
- Description: _None_

### GetCurrentAssetGroupCulture

Get the given asset group category culture.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetGroup | `FName` | The asset group to get the culture for. |

**Return**

- Type: 
- Description: _None_

### ClearCurrentAssetGroupCulture

Clear the given asset group category culture.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetGroup | `FName` | The asset group to clear the culture for. |
| SaveToConfig | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
