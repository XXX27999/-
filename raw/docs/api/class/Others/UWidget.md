# UWidget

This is the base class for all wrapped Slate controls that are exposed to UObjects.

## Parents

- UVisual

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Slot | `UPanelSlot *` | The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget. |
| CachedPanel_ForGC | `UPanelWidget *` |  |
| ToolTipText | `FText` | Tooltip text to show when the user hovers over the widget with the mouse |
| ToolTipWidget | `UWidget *` | Tooltip widget to show when the user hovers over the widget with the mouse |
| IgnorePixelSnapping | `bool` |  |
| RelatedStyleWidgetName | `FName` |  |
| RelatedStyleWidget | `TWeakObjectPtr < UWidget >` |  |
| RenderTransform | [FWidgetTransform](../../cppstruct/F/FW/FWidgetTransform.md) | The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget. |
| RenderTransformPivot | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | The render transform pivot controls the location about which transforms are applied.<br>	  This value is a normalized coordinate about which things like rotations will occur. |
| bIsVariable | `uint8` | Allows controls to be exposed as variables in a blueprint.  Not all controls need to be exposed<br>	  as variables, so this allows only the most useful ones to end up being exposed. |
| bCreatedByConstructionScript | `uint8` | Flag if the Widget was created from a blueprint |
| bIsEnabled | `uint8` | Sets whether this widget can be modified interactively by the user |
| bOverride_Cursor | `uint8` |  |
| bIsVolatile | `uint8` | Engine modify End<br><br>	  If true prevents the widget or its child's geometry or layout information from being cached.  If this widget<br>	  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile<br>	  instead of invalidating it every frame, which would prevent the invalidation panel from actually<br>	  ever caching anything. |
| bWriteSceneZBuffer | `uint8` |  |
| bUseAsSOCOccluder | `uint8` |  |
| UsedLayerPolicy | `uint8` | DrawLayer's policy, 0: default, 1: prevent increasing layer to force batch |
| PreservedLayerNum | `uint8` |  |
| FixedLayerPolicy | `uint8` | DrawLayer's policy, 0: default, 1: Fixed layer to force batch |
| FixedLayerNum | `uint8` |  |
| IngoreRectMove | `uint8` |  |
| CareRectMove | `uint8` |  |
| Cursor | `TEnumAsByte < EMouseCursor :: Type >` | The cursor to show when the mouse is over the widget |
| Clipping | [EWidgetClipping](../../cppenum/E/EW/EWidgetClipping.md) | Controls how the clipping behavior of this widget.  Normally content that overflows the<br>	  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content<br>	  from being seen.<br><br>	  NOTE: Elements in different clipping spaces can not be batched together, and so there is a<br>	  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent<br>	  content from showing up outside its bounds. |
| Visibility | [ESlateVisibility](../../cppenum/E/ES/ESlateVisibility.md) | The visibility of the widget |
| RenderOpacity | `float` | The opacity of the widget |
| Navigation | `UWidgetNavigation *` | The navigation object for this widget is optionally created if the user has configured custom<br>	  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions<br>	  can occur between widgets. |
| bCatchVisibilityChangedEvent | `bool` | True if you want to enable auto destroy user widget stragegy |
| NativeBindings | `TArray < UPropertyBinding * >` | Native property bindings. |
| AreaTypeFlags | `int32` |  |
| ZValue | `int32` |  |
| bLogTraceVisibilityChange | `uint8` | Engine modify Start |
| bHiddenInDesigner | `uint8` | Stores the design time flag setting if the widget is hidden inside the designer |
| bExpandedInDesigner | `uint8` | Stores the design time flag setting if the widget is expanded inside the designer |
| bLockedInDesigner | `uint8` | Stores the design time flag setting if the widget is locked inside the designer |
| DesignerFlags | `TEnumAsByte < EWidgetDesignFlags :: Type >` | Any flags used by the designer at edit time. |
| DisplayLabel | `FString` | The friendly name for this widget displayed in the designer and BP graph. |
| bStyleHidding | `bool` |  |
| bStyleRemove | `bool` |  |
| bStyleInsertInvBox | `bool` |  |
| bStyleInsertRetainerBox | `bool` |  |

## Functions

### SetRenderTransform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTransform | [FWidgetTransform](../../cppstruct/F/FW/FWidgetTransform.md) |  |

**Return**

- Type: 
- Description: _None_

### SetRenderScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Scale | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### SetRenderShear

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Shear | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### SetRenderAngle

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Angle | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetRenderTranslation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Translation | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### SetRenderTransformPivot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Pivot | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### GetIsEnabled

Gets the current enabled status of the widget

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIsEnabled

Sets the current enabled status of the widget

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInIsEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetToolTipText

Sets the tooltip text for the widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InToolTipText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### SetToolTip

Sets a custom widget as the tooltip of the widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### SetCursor

Sets the cursor to show over the widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCursor | `EMouseCursor :: Type` |  |

**Return**

- Type: 
- Description: _None_

### ResetCursor

Resets the cursor to use on the widget, removing any customization for it.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsVisible

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVisibility

Gets the current visibility of the widget.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUVisibility

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLocalVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldVisibility | `ESlateVisibility` |  |
| NewVisibility | `ESlateVisibility` |  |
| Widget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### SetLocalVisibilityWithoutPCUIStyle

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldVisibility | `ESlateVisibility` |  |
| NewVisibility | `ESlateVisibility` |  |
| Widget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### GetPCVisibility

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPCVisible

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetVisibility

Sets the visibility of the widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVisibility | [ESlateVisibility](../../cppenum/E/ES/ESlateVisibility.md) |  |

**Return**

- Type: 
- Description: _None_

### SetAdvancedCollapsed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsAdvancedCollapsed | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetRenderOpacity

Gets the current visibility of the widget.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetRenderOpacity

Sets the visibility of the widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOpacity | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetClipping

Gets the clipping state of this widget.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetClipping

Sets the clipping state of this widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InClipping | [EWidgetClipping](../../cppenum/E/EW/EWidgetClipping.md) |  |

**Return**

- Type: 
- Description: _None_

### ForceVolatile

Sets the forced volatility of the widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bForce | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsVolatile

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsHovered

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWriteSceneZBuffer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInWriteSceneZBuffer | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetUseAsSOCOccluder

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInUseAsSOCOccluder | `bool` |  |

**Return**

- Type: 
- Description: _None_

### HasKeyboardFocus

Checks to see if this widget currently has the keyboard focus

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasMouseCapture

Checks to see if this widget is the current mouse captor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetKeyboardFocus

Sets the focus to this widget.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasUserFocus

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### HasAnyUserFocus

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasFocusedDescendants

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasUserFocusedDescendants

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### SetUserFocus

Sets the focus to this widget for a specific user

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### ForceLayoutPrepass

Forces a pre-pass.  A pre-pass caches the desired size of the widget hierarchy owned by this widget.
	  One pre-pass is already happens for every widget before Tick occurs.  You only need to perform another
	  pre-pass if you are adding child widgets this frame and want them to immediately be visible this frame.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### InvalidateLayoutAndVolatility

Invalidates the widget from the view of a layout caching widget that may own this widget.
	  will force the owning widget to redraw and cache children on the next paint pass.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDesiredSize

Gets the widgets desired size.
	  NOTE: The underlying Slate widget must exist and be valid, also at least one pre-pass must
	        have occurred before this value will be of any use.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAllNavigationRules

Sets the widget navigation rules for all directions. This can only be called on widgets that are in a widget tree.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rule | `EUINavigationRule` | The rule to use when navigation is taking place |
| WidgetToFocus | `FName` | When using the Explicit rule, focus on this widget |

**Return**

- Type: 
- Description: _None_

### SetNavigationRule

Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Direction | `EUINavigation` |  |
| Rule | `EUINavigationRule` | The rule to use when navigation is taking place |
| WidgetToFocus | `FName` | When using the Explicit rule, focus on this widget |

**Return**

- Type: 
- Description: _None_

### GetParent

Gets the parent widget

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RemoveFromParent

Removes the widget from its parent widget.  If this widget was added to the player's screen or the viewport
	  it will also be removed from those containers.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCachedGeometry

Gets the last geometry used to Tick the widget.  This data may not exist yet if this call happens prior to
	  the widget having been tickedpainted, or it may be out of date, or a frame behind.

	  We recommend not to use this data unless there's no other way to solve your problem.  Normally in Slate we
	  try and handle these issues by making a dependent widget part of the hierarchy, as to avoid frame behind
	  or what are referred to as hysteresis problems, both caused by depending on geometry from the previous frame
	  being used to advise how to layout a dependent object the current frame.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCachedAllottedGeometry

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIgnorePixelSnapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Ignore | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetOwningPlayer

Gets the player controller associated with this UI.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddAdvancedCollapsedCount

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Num | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### SubAdvancedCollapsedCount

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Num | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### GetAdvancedCollapsedCount

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetWidgetOutlineName

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsCachedWidgetValid

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
| bIsEnabledDelegate |  | A bindable delegate for bIsEnabled |
| ToolTipTextDelegate |  | A bindable delegate for ToolTipText |
| ToolTipWidgetDelegate |  | A bindable delegate for ToolTipWidget |
| VisibilityDelegate |  | A bindable delegate for Visibility |
| IgnorePixelSnappingDelegate |  |  |
| OnWidgetVisibilityChanged |  |  |
| OnWidgetSlateVisibilityChanged |  |  |
| OnWidgetIsEnabledSet |  |  |

## Language

cpp
