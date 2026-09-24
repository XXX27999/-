# UMaterialInstance

## Parents

- [UMaterialInterface](./UMaterialInterface.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MeshLogicType | `int32` | 材质实例的功能分类：1:挂件 |
| PhysMaterial | `UPhysicalMaterial *` | Physical material to use for this graphics material. Used for sounds, effects etc. |
| Parent | `UMaterialInterface *` | Parent material. |
| bOverride_IncludeShaderCode | `uint32` |  |
| bIncludeShaderCode | `uint32` |  |
| bHasStaticPermutationResource | `uint32` | Indicates whether the instance has static permutation resources (which are required when static parameters are present)<br>	  Read directly from the rendering thread, can only be modified with the use of a FMaterialUpdateContext.<br>	  When true, StaticPermutationMaterialResources will always be valid and non-null. |
| bOverrideSubsurfaceProfile | `uint32` | Defines if SubsurfaceProfile from this instance is used or it uses the parent one. |
| FontParameterValues | `TArray < FFontParameterValue >` | Font parameters. |
| ScalarParameterValues | `TArray < FScalarParameterValue >` | Scalar parameters. |
| TextureParameterValues | `TArray < FTextureParameterValue >` | Texture parameters. |
| VectorParameterValues | `TArray < FVectorParameterValue >` | Vector parameters. |
| CustomParameterValues | `TArray < FCustomParameterValue >` | 项目自定义参数值数组。<br>	  承载 Atlas  Clipmap 等原先寄生在 ScalarParameterValues  TextureParameterValues 上的扩展数据。<br>	  仅当 IsScalarParameterUsedAsAtlasPosition  IsTextureParameterUsedAsClipmap  GetClipmapParameterValue 等编辑期或预处理逻辑读取，<br>	  渲染线程所需的数值仍然仅依赖 ScalarParameterValues  TextureParameterValues。<br><br>	  注意：不标 BlueprintReadOnly —— FCustomParameterValue 含 TSoftObjectPtr  ECustomParameterKind 等<br>	  非蓝图兼容字段，UHT 会报 "Type 'TArray<FCustomParameterValue>' is not supported by blueprint"。<br>	  这个数组原本就不是蓝图 API 面（蓝图继续通过 ScalarTexture Parameter 接口读写）。 |
| DynamicInstancingParameters | `TMap < FString , FVector4 >` | Dynamic instancing parameters. |
| bOverrideBaseProperties_DEPRECATED | `bool` |  |
| BasePropertyOverrides | [FMaterialInstanceBasePropertyOverrides](../../cppstruct/F/FM/FMaterialInstanceBasePropertyOverrides.md) |  |
| PermutationTextureReferences | `TArray < UTexture * >` | Cached texture references from all expressions in the material (including nested functions).<br>	 This is used to link uniform texture expressions which were stored in the DDC with the UTextures that they reference. |
| bEnableTexture2DArrayShaderVariant | `uint32` |  |
| ReferencedTextureGuids | `TArray < FGuid >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
