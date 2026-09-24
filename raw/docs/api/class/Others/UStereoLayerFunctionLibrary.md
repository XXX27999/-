# UStereoLayerFunctionLibrary

StereoLayer Extensions Function Library

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### SetSplashScreen

Set splash screen attributes

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture *` | (in) A texture to be used for the splash. B8R8G8A8 format. |
| Scale | `FVector2D` | (in) Scale of the texture. |
| Offset | `FVector2D` | (in) Position from which to start rendering the texture. |
| bShowLoadingMovie | `bool` |  |
| bShowOnSet | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ShowSplashScreen

Show the splash screen and override the VR display

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HideSplashScreen

Hide the splash screen and return to normal display.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableAutoLoadingSplashScreen

Enablesdisables splash screen to be automatically shown when LoadMap is called.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAutoShowEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
