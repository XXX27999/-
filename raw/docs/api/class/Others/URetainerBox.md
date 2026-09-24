# URetainerBox

The Retainer Box renders children widgets to a render target first before
  later rendering that render target to the screen.  This allows both frequency
  and phase to be controlled so that the UI can actually render less often than the
  frequency of the main game render.  It also has the side benefit of allow materials
  to be applied to the render target after drawing the widgets to apply a simple post process.

   Single Child
   Caching  Performance

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DisableCache | `bool` |  |
| RenderOnInvalidation | `bool` | Should this widget redraw the contents it has every time it receives an invalidation request<br>	  from it's children, similar to the invalidation panel. |
| RenderOnPhase | `bool` | Should this widget redraw the contents it has every time the phase occurs. |
| Phase | `int32` | The Phase this widget will draw on.<br><br>	  If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.<br>	  If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every<br>	  other frame.  So in a 60Hz game, the UI would render at 30Hz. |
| PhaseCount | `int32` | The PhaseCount controls how many phases are possible know what to modulus the current frame<br>	  count by to determine if this is the current frame to draw the widget on.<br><br>	  If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.<br>	  If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every<br>	  other frame.  So in a 60Hz game, the UI would render at 30Hz. |
| bHittestRecordOpt | `bool` |  |
| bUsedForTickAdapter | `bool` |  |
| MaxRendersPerSecond | `int32` | The maximum number of times this widget will redraw the contents it has every second. |
| EffectMaterial | `UMaterialInterface *` | The effect to optionally apply to the render target.  We will set the texture sampler based on the name<br>	  set in the @TextureParameter property.<br><br>	  If you want to adjust transparency of the final image, make sure you set Blend Mode to AlphaComposite (Pre-Multiplied Alpha)<br>	  and make sure to multiply the alpha you're apply across the surface to the color and the alpha of the render target, otherwise<br>	  you won't see the expected color. |
| TextureParameter | `FName` | The texture sampler parameter of the @EffectMaterial, that we'll set to the render target. |

## Functions

### EnableCachedRender

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetRenderPhase

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPhase | `int32` |  |
| InPhaseCount | `int32` |  |

**Return**

- Type: 
- Description: _None_

### EnableHittestRecordOpt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetUsedForTickAdapter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RequestRender

Requests the retainer redrawn the contents it has.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetEffectMaterial

Get the current dynamic effect material applied to the retainer box.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEffectMaterial

Set a new effect material to the retainer widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EffectMaterial | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetTextureParameter

Sets the name of the texture parameter to set the render target to on the material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TextureParameter | `FName` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
