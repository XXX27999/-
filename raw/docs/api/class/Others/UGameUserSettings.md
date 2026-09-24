# UGameUserSettings

Stores user settings for a game (for example graphics and sound settings), with the ability to save and load to and from a file.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bUseVSync | `bool` | Whether to use VSync or not. (public to allow UI to connect to it) |
| ResolutionSizeX | `uint32` | Game screen resolution width, in pixels. |
| ResolutionSizeY | `uint32` | Game screen resolution height, in pixels. |
| LastUserConfirmedResolutionSizeX | `uint32` | Game screen resolution width, in pixels. |
| LastUserConfirmedResolutionSizeY | `uint32` | Game screen resolution height, in pixels. |
| IsBorderless | `bool` | Is game window borderless added by windzjliu |
| BorderlessMode | `int32` |  |
| WindowPosX | `int32` | Window PosX |
| WindowPosY | `int32` | Window PosY |
| FullscreenMode | `int32` | Game window fullscreen mode<br>	 	0 = Fullscreen<br>	 	1 = Windowed fullscreen<br>	 	2 = Windowed |
| LastConfirmedFullscreenMode | `int32` | Last user confirmed fullscreen mode setting. |
| PreferredFullscreenMode | `int32` | Fullscreen mode to use when toggling between windowed and fullscreen. Same values as r.FullScreenMode. |
| Version | `uint32` | All settings will be wiped and set to default if the serialized version differs from UE_GAMEUSERSETTINGS_VERSION. |
| AudioQualityLevel | `int32` |  |
| FrameRateLimit | `float` | Frame rate cap |
| DesiredScreenWidth | `int32` | Desired screen width used to calculate the resolution scale when user changes display mode |
| bUseDesiredScreenHeight | `bool` | If true, the desired screen height will be used to scale the render resolution automatically. |
| DesiredScreenHeight | `int32` | Desired screen height used to calculate the resolution scale when user changes display mode |
| LastRecommendedScreenWidth | `float` | Result of the last benchmark; calculated resolution to use. |
| LastRecommendedScreenHeight | `float` | Result of the last benchmark; calculated resolution to use. |
| LastCPUBenchmarkResult | `float` | Result of the last benchmark (CPU); -1 if there has not been a benchmark run |
| LastGPUBenchmarkResult | `float` | Result of the last benchmark (GPU); -1 if there has not been a benchmark run |
| LastCPUBenchmarkSteps | `TArray < float >` | Result of each individual sub-section of the last CPU benchmark; empty if there has not been a benchmark run |
| LastGPUBenchmarkSteps | `TArray < float >` | Result of each individual sub-section of the last GPU benchmark; empty if there has not been a benchmark run |
| LastGPUBenchmarkMultiplier | `float` | Multiplier used against the last GPU benchmark |
| bUseHDRDisplayOutput | `bool` | HDR |
| HDRDisplayOutputNits | `int32` | HDR |

## Functions

### ApplySettings

Applies all current user settings to the game and saves to permanent storage (e.g. file), optionally checking for command line overrides.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bCheckForCommandLineOverrides | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ApplyNonResolutionSettings

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ApplyResolutionSettings

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bCheckForCommandLineOverrides | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetScreenResolution

Returns the user setting for game screen resolution, in pixels.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLastConfirmedScreenResolution

Returns the last confirmed user setting for game screen resolution, in pixels.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDesktopResolution

Returns user's desktop resolution, in pixels.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetScreenResolution

Sets the user setting for game screen resolution, in pixels.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Resolution | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) |  |

**Return**

- Type: 
- Description: _None_

### GetIsBorderless

IsBorderless getter and setter added by windzjliu

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIsBorderless

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsBorderless | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetBorderlessMode

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBorderlessMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBorderlessMode | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetFullscreenMode

Returns the user setting for game window fullscreen mode.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLastConfirmedFullscreenMode

Returns the last confirmed user setting for game window fullscreen mode.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetFullscreenMode

Sets the user setting for the game window fullscreen mode. See UGameUserSettings::FullscreenMode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFullscreenMode | `EWindowMode :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetPreferredFullscreenMode

Returns the user setting for game window fullscreen mode.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetVSyncEnabled

Sets the user setting for vsync. See UGameUserSettings::bUseVSync.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsVSyncEnabled

Returns the user setting for vsync.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsScreenResolutionDirty

Checks if the Screen Resolution user setting is different from current

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsFullscreenModeDirty

Checks if the FullscreenMode user setting is different from current

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsVSyncDirty

Checks if the vsync user setting is different from current system setting

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ConfirmVideoMode

Mark current video mode settings (fullscreenmoderesolution) as being confirmed by the user

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RevertVideoMode

Revert video mode (fullscreenmoderesolution) back to the last user confirmed values

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBenchmarkFallbackValues

Set scalability settings to sensible fallback values, for use when the benchmark fails or potentially causes a crash

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAudioQualityLevel

Sets the user's audio quality level setting

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| QualityLevel | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetAudioQualityLevel

Returns the user's audio quality level setting

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetFrameRateLimit

Sets the user's frame rate limit (0 will disable frame rate limiting)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLimit | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetFrameRateLimit

Gets the user's frame rate limit (0 indiciates the frame rate limit is disabled)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetOverallScalabilityLevel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetOverallScalabilityLevel

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetResolutionScaleInformation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CurrentScaleNormalized | `float &` |  |
| CurrentScaleValue | `int32 &` |  |
| MinScaleValue | `int32 &` |  |
| MaxScaleValue | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### GetResolutionScaleInformationEx

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CurrentScaleNormalized | `float &` |  |
| CurrentScaleValue | `float &` |  |
| MinScaleValue | `float &` |  |
| MaxScaleValue | `float &` |  |

**Return**

- Type: 
- Description: _None_

### SetResolutionScaleValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScaleValue | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetResolutionScaleValueEx

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScaleValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetResolutionScaleNormalized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScaleNormalized | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetViewDistanceQuality

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetViewDistanceQuality

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetShadowQuality

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetShadowQuality

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAntiAliasingQuality

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetAntiAliasingQuality

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTextureQuality

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetTextureQuality

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetVisualEffectQuality

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetVisualEffectQuality

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPostProcessingQuality

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetPostProcessingQuality

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetFoliageQuality

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetFoliageQuality

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsDirty

Checks if any user settings is different from current

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ValidateSettings

Validates and resets bad user settings to default. Deletes stale user settings file if necessary.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LoadSettings

Loads the user settings from persistent storage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bForceReload | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SaveSettings

Save the user settings to persistent storage (automatically happens as part of ApplySettings)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetToCurrentSettings

This function resets all settings to the current system settings

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetToDefaults

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDefaultResolutionScale

Gets the desired resolution quality based on DesiredScreenWidthHeight and the current screen resolution

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRecommendedResolutionScale

Gets the recommended resolution quality based on LastRecommendedScreenWidthHeight and the current screen resolution

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDefaultResolution

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDefaultWindowPosition

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDefaultWindowMode

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGameUserSettings

Returns the game local machine settings (resolution, windowing mode, scalability settings, etc...)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RunHardwareBenchmark

Runs the hardware benchmark and populates ScalabilityQuality as well as the last benchmark results config members, but does not apply the settings it determines. Designed to be called in conjunction with ApplyHardwareBenchmarkResults

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorkScale | `int32` |  |
| CPUMultiplier | `float` |  |
| GPUMultiplier | `float` |  |

**Return**

- Type: 
- Description: _None_

### ApplyHardwareBenchmarkResults

Applies the settings stored in ScalabilityQuality and saves settings

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SupportsHDRDisplayOutput

Whether the curently running system supports HDR display output

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableHDRDisplayOutput

Enables or disables HDR display output. Can be called again to change the desired nit level

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |
| DisplayNits | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetCurrentHDRDisplayNits

Returns 0 if HDR isn't supported or is turned off

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsHDREnabled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnGameUserSettingsUINeedsUpdate |  |  |

## Language

cpp
