# UCineCameraComponent

A specialized version of a camera component, geared toward cinematic usage.

## Parents

- [UCameraComponent](./UCameraComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FilmbackSettings | [FCameraFilmbackSettings](../../cppstruct/F/FC/FCameraFilmbackSettings.md) | Controls the filmback of the camera. |
| LensSettings | [FCameraLensSettings](../../cppstruct/F/FC/FCameraLensSettings.md) | Controls the camera's lens. |
| FocusSettings | [FCameraFocusSettings](../../cppstruct/F/FC/FCameraFocusSettings.md) | Controls the camera's focus. |
| CurrentFocalLength | `float` | Current focal length of the camera (i.e. controls FoV, zoom) |
| CurrentAperture | `float` | Current aperture, in terms of f-stop (e.g. 2.8 for f2.8) |
| CurrentFocusDistance | `float` | Read-only. Control this value via FocusSettings. |
| FilmbackPresets | `TArray < FNamedFilmbackPreset >` | List of available filmback presets |
| LensPresets | `TArray < FNamedLensPreset >` | List of available lens presets |
| DefaultFilmbackPresetName | `FString` | Name of the default filmback preset |
| DefaultLensPresetName | `FString` | Name of the default lens preset |
| DefaultLensFocalLength | `float` | Default focal length (will be constrained by default lens) |
| DefaultLensFStop | `float` | Default aperture (will be constrained by default lens) |

## Functions

### GetHorizontalFieldOfView

Returns the horizonal FOV of the camera with current settings.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVerticalFieldOfView

Returns the vertical FOV of the camera with current settings.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetFilmbackPresetName

Returns the filmback name of the camera with the current settings.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetFilmbackPresetByName

Set the current preset settings by preset name.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPresetName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetLensPresetName

Returns the lens name of the camera with the current settings.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLensPresetByName

Set the current lens settings by preset name.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPresetName | `FString &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
