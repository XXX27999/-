# UHeadMountedDisplayFunctionLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### IsHeadMountedDisplayEnabled

Returns whether or not we are currently using the head mounted display.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsHeadMountedDisplayConnected

Returns whether or not the HMD hardware is connected and ready to use.  It may or may not actually be in use.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableHMD

Switches tofrom using HMD and stereo rendering.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` | (in) 'true' to enable HMD stereo; 'false' otherwise |

**Return**

- Type: 
- Description: _None_

### GetHMDDeviceName

Returns the name of the device, so scripts can modify their behaviour appropriately

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetHMDWornState

Returns the worn state of the device.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetOrientationAndPosition

Grabs the current orientation and position for the HMD.  If positional tracking is not available, DevicePosition will be a zero vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeviceRotation | `FRotator &` | (out) The device's current rotation |
| DevicePosition | `FVector &` | (out) The device's current position, in its own tracking space |

**Return**

- Type: 
- Description: _None_

### HasValidTrackingPosition

If the HMD supports positional tracking, whether or not we are currently being tracked

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetNumOfTrackingSensors

If the HMD has multiple positional tracking sensors, return a total number of them currently connected.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTrackingSensorParameters

If the HMD has a positional sensor, this will return the game-world location of it, as well as the parameters for the bounding region of tracking.
	  This allows an in-game representation of the legal positional tracking range.  All values will be zeroed if the sensor is not available or the HMD does not support it.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | `FVector &` | (out) Origin, in world-space, of the sensor |
| Rotation | `FRotator &` | (out) Rotation, in world-space, of the sensor |
| LeftFOV | `float &` | (out) Field-of-view, left from center, in degrees, of the valid tracking zone of the sensor |
| RightFOV | `float &` | (out) Field-of-view, right from center, in degrees, of the valid tracking zone of the sensor |
| TopFOV | `float &` | (out) Field-of-view, top from center, in degrees, of the valid tracking zone of the sensor |
| BottomFOV | `float &` | (out) Field-of-view, bottom from center, in degrees, of the valid tracking zone of the sensor |
| Distance | `float &` | (out) Nominal distance to sensor, in world-space |
| NearPlane | `float &` | (out) Near plane distance of the tracking volume, in world-space |
| FarPlane | `float &` | (out) Far plane distance of the tracking volume, in world-space |
| IsActive | `bool &` | (out) True, if the query for the specified sensor succeeded. |
| Index | `int32` | (in) Index of the tracking sensor to query |

**Return**

- Type: 
- Description: _None_

### GetPositionalTrackingCameraParameters

If the HMD has a positional sensor, this will return the game-world location of it, as well as the parameters for the bounding region of tracking.
	  This allows an in-game representation of the legal positional tracking range.  All values will be zeroed if the sensor is not available or the HMD does not support it.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CameraOrigin | `FVector &` |  |
| CameraRotation | `FRotator &` |  |
| HFOV | `float &` | (out) Field-of-view, horizontal, in degrees, of the valid tracking zone of the sensor |
| VFOV | `float &` | (out) Field-of-view, vertical, in degrees, of the valid tracking zone of the sensor |
| CameraDistance | `float &` | (out) Nominal distance to sensor, in world-space |
| NearPlane | `float &` | (out) Near plane distance of the tracking volume, in world-space |
| FarPlane | `float &` | (out) Far plane distance of the tracking volume, in world-space |

**Return**

- Type: 
- Description: _None_

### IsInLowPersistenceMode

Returns true, if HMD is in low persistence mode. 'false' otherwise.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableLowPersistenceMode

Switches between low and full persistence modes.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` | (in) 'true' to enable low persistence mode; 'false' otherwise |

**Return**

- Type: 
- Description: _None_

### ResetOrientationAndPosition

Resets orientation by setting roll and pitch to 0, assuming that current yaw is forward direction and assuming
	  current position as a 'zero-point' (for positional tracking).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Yaw | `float` | (in) the desired yaw to be set after orientation reset. |
| Options | `EOrientPositionSelector :: Type` | (in) specifies either position, orientation or both should be reset. |

**Return**

- Type: 
- Description: _None_

### SetClippingPlanes

Sets near and far clipping planes (NCP and FCP) for stereo rendering. Similar to 'stereo ncp= fcp' console command, but NCP and FCP set by this
	  call won't be saved in .ini file.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Near | `float` | (in) Near clipping plane, in centimeters |
| Far | `float` | (in) Far clipping plane, in centimeters |

**Return**

- Type: 
- Description: _None_

### GetScreenPercentage

Returns screen percentage to be used in VR mode.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWorldToMetersScale

Sets the World to Meters scale, which changes the scale of the world as perceived by the player

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | `UObject *` |  |
| NewScale | `float` | Specifies how many Unreal units correspond to one meter in the real world |

**Return**

- Type: 
- Description: _None_

### GetWorldToMetersScale

Returns the World to Meters scale, which corresponds to the scale of the world as perceived by the player

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SetTrackingOrigin

Sets current tracking origin type (eye level or floor level).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | `TEnumAsByte < EHMDTrackingOrigin :: Type >` |  |

**Return**

- Type: 
- Description: _None_

### GetTrackingOrigin

Returns current tracking origin type (eye level or floor level).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVRFocusState

Returns current state of VR focus.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bUseFocus | `bool &` | (out) if set to true, then this App does use VR focus. |
| bHasFocus | `bool &` | (out) if set to true, then this App currently has VR focus. |

**Return**

- Type: 
- Description: _None_

### IsSpectatorScreenModeControllable

Return true if spectator screen mode control is available.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSpectatorScreenMode

Sets the social screen mode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Mode | [ESpectatorScreenMode](../../cppenum/E/ES/ESpectatorScreenMode.md) | (in) The social screen Mode. |

**Return**

- Type: 
- Description: _None_

### SetSpectatorScreenTexture

Change the texture displayed on the social screen

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTexture | `UTexture *` |  |

**Return**

- Type: 
- Description: _None_

### SetSpectatorScreenModeTexturePlusEyeLayout

Setup the layout for ESpectatorScreenMode::TexturePlusEye.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EyeRectMin | `FVector2D` |  |
| EyeRectMax | `FVector2D` |  |
| TextureRectMin | `FVector2D` |  |
| TextureRectMax | `FVector2D` |  |
| bDrawEyeFirst | `bool` |  |
| bClearBlack | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
