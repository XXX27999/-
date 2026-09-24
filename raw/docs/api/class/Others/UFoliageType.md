# UFoliageType

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UpdateGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) | A GUID that is updated every time the foliage type is modified,<br>	   so foliage placed in the level can detect the FoliageType has changed. |
| Density | `float` | Foliage instances will be placed at this density, specified in instances per 1000x1000 unit area |
| DensityAdjustmentFactor | `float` | The factor by which to adjust the density of instances. Values >1 will increase density while values <1 will decrease it. |
| Radius | `float` | The minimum distance between foliage instances |
| Scaling | [EFoliageScaling](../../cppenum/E/EF/EFoliageScaling.md) | Specifies foliage instance scaling behavior when painting. |
| ScaleX | [FFloatInterval](../../cppstruct/F/FF/FFloatInterval.md) | Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's X Scale property |
| ScaleY | [FFloatInterval](../../cppstruct/F/FF/FFloatInterval.md) | Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Y Scale property |
| ScaleZ | [FFloatInterval](../../cppstruct/F/FF/FFloatInterval.md) | Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Z Scale property |
| VertexColorMaskByChannel | [FFoliageVertexColorChannelMask](../../cppstruct/F/FF/FFoliageVertexColorChannelMask.md) |  |
| VertexColorMask_DEPRECATED | `TEnumAsByte < enum FoliageVertexColorMask >` | When painting on static meshes, foliage instance placement can be limited to areas where the static mesh has values in the selected vertex color channel(s).<br>	   This allows a static mesh to mask out certain areas to prevent foliage from being placed there |
| VertexColorMaskThreshold_DEPRECATED | `float` | Specifies the threshold value above which the static mesh vertex color value must be, in order for foliage instances to be placed in a specific area |
| VertexColorMaskInvert_DEPRECATED | `uint32` | When unchecked, foliage instances will be placed only when the vertex color in the specified channel(s) is above the threshold amount.<br>	   When checked, the vertex color must be less than the threshold amount |
| ZOffset | [FFloatInterval](../../cppstruct/F/FF/FFloatInterval.md) | Specifies a range from minimum to maximum of the offset to apply to a foliage instance's Z location |
| AlignToNormal | `uint32` | Whether foliage instances should have their angle adjusted away from vertical to match the normal of the surface they're painted on<br>	   If AlignToNormal is enabled and RandomYaw is disabled, the instance will be rotated so that the +X axis points down-slope |
| AlignMaxAngle | `float` | The maximum angle in degrees that foliage instances will be adjusted away from the vertical |
| RandomYaw | `uint32` | If selected, foliage instances will have a random yaw rotation around their vertical axis applied |
| RandomPitchAngle | `float` | A random pitch adjustment can be applied to each instance, up to the specified angle in degrees, from the original vertical |
| GroundSlopeAngle | [FFloatInterval](../../cppstruct/F/FF/FFloatInterval.md) | Foliage instances will only be placed on surfaces sloping in the specified angle range from the horizontal |
| Height | [FFloatInterval](../../cppstruct/F/FF/FFloatInterval.md) | The valid altitude range where foliage instances will be placed, specified using minimum and maximum world coordinate Z values |
| LandscapeLayers | `TArray < FName >` | If a layer name is specified, painting on landscape will limit the foliage to areas of landscape with the specified layer painted |
| LandscapeLayer_DEPRECATED | `FName` |  |
| CollisionWithWorld | `uint32` | If checked, an overlap test with existing world geometry is performed before each instance is placed |
| CollisionScale | [FVector](../../cppstruct/F/FV/FVector.md) | The foliage instance's collision bounding box will be scaled by the specified amount before performing the overlap check |
| MinimumLayerWeight | `float` | Specifies the minimum value above which the landscape layer weight value must be, in order for foliage instances to be placed in a specific area |
| MeshBounds | [FBoxSphereBounds](../../cppstruct/F/FB/FBoxSphereBounds.md) |  |
| LowBoundOriginRadius | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| Mobility | `TEnumAsByte < EComponentMobility :: Type >` | Mobility property to apply to foliage components |
| CullDistance | [FInt32Interval](../../cppstruct/F/FI/FInt32Interval.md) | The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables.<br>	  When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all. |
| NearCullDistance | `int32` |  |
| bIsFlyType | `bool` |  |
| bEnableStaticLighting_DEPRECATED | `uint32` | Deprecated. Now use the Mobility setting to control staticdynamic lighting |
| CastShadow | `uint32` | Controls whether the foliage should cast a shadow or not. |
| bAffectDynamicIndirectLighting | `uint32` | Controls whether the foliage should inject light into the Light Propagation Volume.  This flag is only used if CastShadow is true. |
| bAffectDistanceFieldLighting | `uint32` | Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. |
| bCastDynamicShadow | `uint32` | Controls whether the foliage should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. |
| bCastStaticShadow | `uint32` | Whether the foliage should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true. |
| bGenerateSurfaceSample | `uint32` |  |
| bOccludeLightingRay | `uint32` |  |
| bCastShadowAsTwoSided | `uint32` | Whether this foliage should cast dynamic shadows as if it were a two sided material. |
| bReceivesDecals | `uint32` | Whether the foliage receives decals. |
| bOverrideLightMapRes | `uint32` | Whether to override the lightmap resolution defined in the static mesh. |
| OverriddenLightMapRes | `int32` | Overrides the lightmap resolution defined in the static mesh |
| LightmapType | [ELightmapType](../../cppenum/E/EL/ELightmapType.md) | Controls the type of lightmap used for this component. |
| FakeSkyLightAOIntensity | `float` | Controls the intensity of FakeSkyLightAO. 0 = no fake AO (full bright), 1 = full effect (default). |
| bUseAsOccluder | `uint32` | If enabled, foliage will render a pre-pass which allows it to occlude other primitives, and also allows<br>	  it to correctly receive DBuffer decals. Enabling this setting may have a negative performance impact. |
| BodyInstance | [FBodyInstance](../../cppstruct/F/FB/FBodyInstance.md) | Custom collision for foliage |
| CustomNavigableGeometry | `TEnumAsByte < EHasCustomNavigableGeometry :: Type >` | Force navmesh |
| LightingChannels | [FLightingChannels](../../cppstruct/F/FL/FLightingChannels.md) | Lighting channels that placed foliage will be assigned. Lights with matching channels will affect the foliage.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| bRenderCustomDepth | `uint32` | If true, the foliage will be rendered in the CustomDepth pass (usually used for outlines) |
| CustomDepthStencilValue | `int32` | Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3) |
| CollisionRadius | `float` | The CollisionRadius determines when two instances overlap. When two instances overlap a winner will be picked based on rules and priority. |
| ShadeRadius | `float` | The ShadeRadius determines when two instances overlap. If an instance can grow in the shade this radius is ignored. |
| NumSteps | `int32` | The number of times we age the species and spread its seeds. |
| InitialSeedDensity | `float` | Specifies the number of seeds to populate along 10 meters. The number is implicitly squared to cover a 10m x 10m area |
| AverageSpreadDistance | `float` | The average distance between the spreading instance and its seeds. For example, a tree with an AverageSpreadDistance 10 will ensure the average distance between the tree and its seeds is 10cm |
| SpreadVariance | `float` | Specifies how much seed distance varies from the average. For example, a tree with an AverageSpreadDistance 10 and a SpreadVariance 1 will produce seeds with an average distance of 10cm plus or minus 1cm |
| SeedsPerStep | `int32` | The number of seeds an instance will spread in a single step of the simulation. |
| DistributionSeed | `int32` | The seed that determines placement of initial seeds. |
| MaxInitialSeedOffset | `float` | The seed that determines placement of initial seeds. |
| bCanGrowInShade | `bool` | If true, seeds of this type will ignore shade radius during overlap tests with other types. |
| bSpawnsInShade | `bool` | Whether new seeds are spawned exclusively in shade. Occurs in a second pass after all types that do not spawn in shade have been simulated.<br>	  Only valid when CanGrowInShade is true. |
| MaxInitialAge | `float` | Allows a new seed to be older than 0 when created. New seeds will be randomly assigned an age in the range [0,MaxInitialAge] |
| MaxAge | `float` | Specifies the oldest a seed can be. After reaching this age the instance will still spread seeds, but will not get any older |
| OverlapPriority | `float` | When two instances overlap we must determine which instance to remove.<br>	  The instance with a lower OverlapPriority will be removed.<br>	  In the case where OverlapPriority is the same regular simulation rules apply. |
| ProceduralScale | [FFloatInterval](../../cppstruct/F/FF/FFloatInterval.md) | The scale range of this type when being procedurally generated. Configured with the Scale Curve. |
| ScaleCurve | [FRuntimeFloatCurve](../../cppstruct/F/FR/FRuntimeFloatCurve.md) | Instance scale factor as a function of normalized age (i.e. Current Age  Max Age).<br>	  X = 0 corresponds to Age = 0, X = 1 corresponds to Age = Max Age.<br>	  Y = 0 corresponds to Min Scale, Y = 1 corresponds to Max Scale. |
| ChangeCount | `int32` |  |
| ReapplyDensity | `uint32` | If checked, the density of foliage instances already placed will be adjusted by the density adjustment factor. |
| ReapplyRadius | `uint32` | If checked, foliage instances not meeting the new Radius constraint will be removed |
| ReapplyAlignToNormal | `uint32` | If checked, foliage instances will have their normal alignment adjusted by the Reapply tool |
| ReapplyRandomYaw | `uint32` | If checked, foliage instances will have their yaw adjusted by the Reapply tool |
| ReapplyScaling | `uint32` | If checked, foliage instances will have their scale adjusted to fit the specified scaling behavior by the Reapply tool |
| ReapplyScaleX | `uint32` | If checked, foliage instances will have their X scale adjusted by the Reapply tool |
| ReapplyScaleY | `uint32` | If checked, foliage instances will have their Y scale adjusted by the Reapply tool |
| ReapplyScaleZ | `uint32` | If checked, foliage instances will have their Z scale adjusted by the Reapply tool |
| ReapplyRandomPitchAngle | `uint32` | If checked, foliage instances will have their pitch adjusted by the Reapply tool |
| ReapplyGroundSlope | `uint32` | If checked, foliage instances not meeting the ground slope condition will be removed by the Reapply too |
| ReapplyHeight | `uint32` | If checked, foliage instances not meeting the valid Z height condition will be removed by the Reapply tool |
| ReapplyLandscapeLayers | `uint32` | If checked, foliage instances painted on areas that do not have the appropriate landscape layer painted will be removed by the Reapply tool |
| ReapplyZOffset | `uint32` | If checked, foliage instances will have their Z offset adjusted by the Reapply tool |
| ReapplyCollisionWithWorld | `uint32` | If checked, foliage instances will have an overlap test with the world reapplied, and overlapping instances will be removed by the Reapply tool |
| ReapplyVertexColorMask | `uint32` | If checked, foliage instances no longer matching the vertex color constraint will be removed by the Reapply too |
| bEnableDensityScaling | `uint32` | Whether this foliage type should be affected by the Engine Scalability system's Foliage scalability setting.<br>	  Enable for detail meshes that don't really affect the game. Disable for anything important.<br>	  Typically, this will be enabled for small meshes without collision (e.g. grass) and disabled for large meshes with collision (e.g. trees) |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
