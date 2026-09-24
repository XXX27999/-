# UPlatformEventsComponent

Component to handle receiving notifications from the OS about platform events.

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

_None_

## Functions

### IsInLaptopMode

Check whether a convertible laptop is laptop mode.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsInTabletMode

Check whether a convertible laptop is laptop mode.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SupportsConvertibleLaptops

Check whether the platform supports convertible laptops.

	  Note: This does not necessarily mean that the platform is a convertible laptop.
	  For example, convertible laptops running Windows 7 or older will return false,
	  and regular laptops running Windows 8 or newer will return true.

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
| PlatformChangedToLaptopModeDelegate |  | This is called when a convertible laptop changed into laptop mode. |
| PlatformChangedToTabletModeDelegate |  | This is called when a convertible laptop changed into tablet mode. |

## Language

cpp
