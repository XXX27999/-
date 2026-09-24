# UNavLinkCustomComponent

Encapsulates NavLinkCustomInterface interface, can be used with Actors not relevant for navigation

   Additional functionality:
   - can be toggled
   - can create obstacle area for easierforced separation of link end points
   - can broadcast state changes to nearby agents

## Parents

- [UNavRelevantComponent](./UNavRelevantComponent.md)
- INavLinkCustomInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NavLinkUserId | `uint32` | link Id assigned by navigation system |
| EnabledAreaClass | `TSubclassOf < UNavArea >` | area class to use when link is enabled |
| DisabledAreaClass | `TSubclassOf < UNavArea >` | area class to use when link is disabled |
| LinkRelativeStart | [FVector](../../cppstruct/F/FV/FVector.md) | start point, relative to owner |
| LinkRelativeEnd | [FVector](../../cppstruct/F/FV/FVector.md) | end point, relative to owner |
| LinkDirection | `TEnumAsByte < ENavLinkDirection :: Type >` | direction of link |
| bLinkEnabled | `uint32` | is link currently in enabled state? (area class) |
| bNotifyWhenEnabled | `uint32` | should link notify nearby agents when it changes state to enabled |
| bNotifyWhenDisabled | `uint32` | should link notify nearby agents when it changes state to disabled |
| bCreateBoxObstacle | `uint32` | if set, box obstacle area will be added to generation |
| ObstacleOffset | [FVector](../../cppstruct/F/FV/FVector.md) | offset of simple box obstacle |
| ObstacleExtent | [FVector](../../cppstruct/F/FV/FVector.md) | extent of simple box obstacle |
| ObstacleAreaClass | `TSubclassOf < UNavArea >` | area class for simple box obstacle |
| BroadcastRadius | `float` | radius of state change broadcast |
| BroadcastInterval | `float` | interval for state change broadcast (0 = single broadcast) |
| BroadcastChannel | `TEnumAsByte < ECollisionChannel >` | trace channel for state change broadcast |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
