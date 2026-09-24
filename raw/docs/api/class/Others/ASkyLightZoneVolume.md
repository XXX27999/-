# ASkyLightZoneVolume

ASkyLightZoneVolume - 天光区域Volume Actor

  放置在场景中覆盖一个区域，区域内的组件根据自身 ReorganizationTags 的 isInterior 分组
  被设置不同的 SkyLightIntensityScale 值。

  isInterior 分组说明：
    有 Interior tag = 室内（应用室内参数）
    None (未勾选)   = 室外（应用室外参数）
    无 isInterior 分组 = 不处理

## Parents

- [AVolume](./AVolume.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| IndoorSkyLightIntensityScale | `float` | 室内组件的 SkyLightIntensityScale 目标值（天光强度缩放） |
| IndoorMinSkyVisibility | `float` | 室内组件的 MinSkyVisibility 目标值（最小天空可见度） |
| OutdoorSkyLightIntensityScale | `float` | 室外组件的 SkyLightIntensityScale 目标值（天光强度缩放） |
| OutdoorMinSkyVisibility | `float` | 室外组件的 MinSkyVisibility 目标值（最小天空可见度） |
| Priority | `int32` | 优先级，重叠区域时高优先级覆盖低优先级 |
| bShowAffectedActors | `bool` | 是否在编辑器中显示受影响Actor的高亮边界框<br>	  使用 LineBatcher 绘制，不受G键（ShowFlags）影响<br>	  颜色说明：蓝色=室内，橙色=室外，绿色=同时室内外，灰色=未分类 |
| InfoTextComponent | `UTextRenderComponent *` | 编辑器中显示的文本标注组件（显示当前参数信息） |

## Functions

### ApplyToOverlappingComponents

一键应用：将此Volume的参数设置到区域内所有组件
	  根据组件的 ReorganizationTags isInterior 分组决定应用室内还是室外参数

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
