# UMaterial

A Material is an asset which can be applied to a mesh to control the visual look of the scene.
  When light from the scene hits the surface, the shading model of the material is used to calculate how that light interacts with the surface.

  Warning: Creating new materials directly increases shader compile times!  Consider creating a Material Instance off of an existing material instead.

## Parents

- [UMaterialInterface](./UMaterialInterface.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PhysMaterial | `UPhysicalMaterial *` | Physical material to use for this graphics material. Used for sounds, effects etc. |
| DiffuseColor_DEPRECATED | [FColorMaterialInput](../../cppstruct/F/FC/FColorMaterialInput.md) |  |
| SpecularColor_DEPRECATED | [FColorMaterialInput](../../cppstruct/F/FC/FColorMaterialInput.md) |  |
| BaseColor | [FColorMaterialInput](../../cppstruct/F/FC/FColorMaterialInput.md) |  |
| Metallic | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| Specular | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| Roughness | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| Normal | [FVectorMaterialInput](../../cppstruct/F/FV/FVectorMaterialInput.md) |  |
| EmissiveColor | [FColorMaterialInput](../../cppstruct/F/FC/FColorMaterialInput.md) |  |
| Opacity | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| OpacityMask | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| ReplaceMaterial | `UMaterialInterface *` |  |
| MaterialDomain | `TEnumAsByte < enum EMaterialDomain >` | The domain that the material's attributes will be evaluated in.<br>	  Certain pieces of material functionality are only valid in certain domains, for example vertex normal is only valid on a surface. |
| BlendMode | `TEnumAsByte < enum EBlendMode >` | Determines how the material's color is blended with background colors. |
| DecalBlendMode | `TEnumAsByte < enum EDecalBlendMode >` | Defines how the GBuffer chanels are getting manipulated by a decal material pass. (only with MaterialDomain == MD_DeferredDecal) |
| MaterialDecalResponse | `TEnumAsByte < enum EMaterialDecalResponse >` | Defines how the material reacts on DBuffer decals (Affects look, performance and texturesample usage).<br>	  Non DBuffer Decals can be disabled on the primitive (e.g. static mesh) |
| ShadingModel | `TEnumAsByte < enum EMaterialShadingModel >` | Determines how inputs are combined to create the material's final color. |
| bIncludeShaderCode | `uint32` |  |
| OpacityMaskClipValue | `float` | If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue. |
| bTranslucentVelocityRendering | `uint32` |  |
| TranslucentVelocityClipValue | `float` |  |
| VertexOffsetAlongNormal | `float` | pixels offset along vertex normal, for outline drawing. |
| bCastDynamicShadowAsMasked | `uint32` | If true, translucent materials will cast dynamic shadows according to their opacity.<br>	 OpacityMaskClipValue is used as the threshold value. |
| bCastDynamicShadowAsUnlit | `uint32` |  |
| OITBlendMode | `TEnumAsByte < enum EOITBlendMode >` |  |
| WorldPositionOffset | [FVectorMaterialInput](../../cppstruct/F/FV/FVectorMaterialInput.md) | Adds to world position in the vertex shader. |
| WorldDisplacement | [FVectorMaterialInput](../../cppstruct/F/FV/FVectorMaterialInput.md) | Offset in world space applied to tessellated vertices. |
| TessellationMultiplier | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) | Multiplies the tessellation factors applied when a tessellation mode is set. |
| SubsurfaceColor | [FColorMaterialInput](../../cppstruct/F/FC/FColorMaterialInput.md) | Inner material color, only used for ShadingModel=Subsurface |
| ClearCoat | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| ClearCoatRoughness | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| AmbientOcclusion | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) | output ambient occlusion to the GBuffer |
| Refraction | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) | output refraction index for translucent rendering<br>	  Air:1.0 Water:1.333 Ice:1.3 Glass:~1.6 Diamond:2.42 |
| CustomizedUVs | [FVector2MaterialInput](../../cppstruct/F/FV/FVector2MaterialInput.md) | These inputs are evaluated in the vertex shader and allow artists to do arbitrary vertex shader operations and access them in the pixel shader.<br>	  When unconnected or hidden they default to passing through the vertex UVs. |
| MaterialAttributes | [FMaterialAttributesInput](../../cppstruct/F/FM/FMaterialAttributesInput.md) |  |
| PixelDepthOffset | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| CustomizedVertexColor | [FVector4MaterialInput](../../cppstruct/F/FV/FVector4MaterialInput.md) |  |
| PlanarReflectionOffsetScale | [FVector4MaterialInput](../../cppstruct/F/FV/FVector4MaterialInput.md) |  |
| VertexDepthOffset | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| PixelDepthOffsetNegative | [FScalarMaterialInput](../../cppstruct/F/FS/FScalarMaterialInput.md) |  |
| bAllowGCCluster | `uint32` |  |
| bEnableSeparateTranslucency | `uint32` | Indicates that the material should be rendered in the SeparateTranslucency Pass (not affected by DOF, requires bAllowSeparateTranslucency to be set in .ini). |
| bTranslucencyRenderAfterSS | `uint32` | Indicates that the material should be rendered after post process and super sampling, dedicate for reticle materials |
| bEnableMobileSeparateTranslucency | `uint32` | Indicates that the translucent material should not be affected by bloom or DOF. (Note: Depth testing is not available) |
| bEnableMobileDownsampleSeparateTranslucency | `uint32` | Indicates that the translucent material can be rendered on an off-screen render target at a low resolution) |
| bEnableResponsiveAA | `uint32` | Indicates that the material should be rendered using responsive anti-aliasing. Improves sharpness of small moving particles such as sparks.<br>	  Only use for small moving features because it will cause aliasing of the background. |
| bScreenSpaceReflections | `uint32` | SSR on translucency |
| TwoSided | `uint32` | Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces. |
| DitheredLODTransition | `uint32` | Whether meshes rendered with the material should support dithered LOD transitions. |
| ForceOpaqueLevelPointIndirectLighting | `uint32` |  |
| DitherOpacityMask | `uint32` | Dither opacity mask. When combined with Temporal AA this can be used as a form of limited translucency which supports all lighting features. |
| bAllowNegativeEmissiveColor | `uint32` | Whether the material should allow outputting negative emissive color values.  Only allowed on unlit materials. |
| NumCustomizedUVs | `int32` | Number of customized UV inputs to display.  Unconnected customized UV inputs will just pass through the vertex UVs. |
| TranslucencyLightingMode | `TEnumAsByte < enum ETranslucencyLightingMode >` | Sets the lighting mode that will be used on this material if it is translucent. |
| TranslucencyDirectionalLightingIntensity | `float` | Useful for artificially increasing the influence of the normal on the lighting result for translucency.<br>	  A value larger than 1 increases the influence of the normal, a value smaller than 1 makes the lighting more ambient. |
| AllowTranslucentCustomDepthWrites | `uint32` | Allows a translucenct material to be used with custom depth writing by compiling additional shaders. |
| TranslucentShadowDensityScale | `float` | Scale used to make translucent shadows more or less opaque than the material's actual opacity. |
| TranslucentSelfShadowDensityScale | `float` | Scale used to make translucent self-shadowing more or less opaque than the material's shadow on other objects.<br>	  This is only used when the object is casting a volumetric translucent shadow. |
| TranslucentSelfShadowSecondDensityScale | `float` | Used to make a second self shadow gradient, to add interesting shading in the shadow of the first. |
| TranslucentSelfShadowSecondOpacity | `float` | Controls the strength of the second self shadow gradient. |
| TranslucentBackscatteringExponent | `float` | Controls how diffuse the material's backscattering is when using the MSM_Subsurface shading model.<br>	  Larger exponents give a less diffuse look (smaller, brighter backscattering highlight).<br>	  This is only used when the object is casting a volumetric translucent shadow from a directional light. |
| TranslucentMultipleScatteringExtinction | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Colored extinction factor used to approximate multiple scattering in dense volumes.<br>	  This is only used when the object is casting a volumetric translucent shadow. |
| TranslucentShadowStartOffset | `float` | Local space distance to bias the translucent shadow.  Positive values move the shadow away from the light. |
| bDisableDepthTest | `uint32` | Whether to draw on top of opaque pixels even if behind them. This only has meaning for translucency. |
| bGenerateSphericalParticleNormals | `uint32` | Whether to generate spherical normals for particles that use this material. |
| bTangentSpaceNormal | `uint32` | Whether the material takes a tangent space normal or a world space normal as input.<br>	  (TangentSpace requires extra instructions but is often more convenient). |
| bUseEmissiveForDynamicAreaLighting | `uint32` | If enabled, the material's emissive colour is injected into the LightPropagationVolume |
| bBlockGI | `uint32` | If enabled, the material's opacity defines how much GI is blocked when using the LightPropagationVolume feature |
| bUseSimpleGI | `uint32` | If enabled, the material uses simplified and inaccurate GI color for efficiency |
| bUsedAsSpecialEngineMaterial | `uint32` | This is a special usage flag that allows a material to be assignable to any primitive type.<br>	  This is useful for materials used by code to implement certain viewmodes, for example the default material or lighting only material.<br>	  The cost is that nearly 20x more shaders will be compiled for the material than the average material, which will greatly increase shader compile time and memory usage.<br>	  This flag should only be enabled when absolutely necessary, and is purposefully not exposed to the UI to prevent abuse. |
| bUsedWithSkeletalMesh | `uint32` | Indicates that the material and its instances can be use with skeletal meshes.<br>	  This will result in the shaders required to support skeletal meshes being compiled which will increase shader compile time and memory usage. |
| bUsedWithGFur | `uint32` | Indicates that the material and its instances can be use with GFur.<br>	 This will result in the shaders required to support skeletal meshes being compiled which will increase shader compile time and memory usage. |
| bUsedWithEditorCompositing | `uint32` | Indicates that the material and its instances can be use with editor compositing<br>	  This will result in the shaders required to support editor compositing being compiled which will increase shader compile time and memory usage. |
| bUsedWithParticleSprites | `uint32` | Indicates that the material and its instances can be use with particle sprites<br>	  This will result in the shaders required to support particle sprites being compiled which will increase shader compile time and memory usage. |
| bForceDisableSubUVCalculate | `uint32` |  |
| bUsedWithBeamTrails | `uint32` | Indicates that the material and its instances can be use with beam trails<br>	  This will result in the shaders required to support beam trails being compiled which will increase shader compile time and memory usage. |
| bUsedWithMeshParticles | `uint32` | Indicates that the material and its instances can be use with mesh particles<br>	  This will result in the shaders required to support mesh particles being compiled which will increase shader compile time and memory usage. |
| bUsedWithParticleBigWorldPrecision | `uint32` |  |
| bUsedWithNiagaraSprites | `uint32` | Indicates that the material and its instances can be use with Niagara sprites (meshes and ribbons, respectively)<br>	 This will result in the shaders required to support Niagara sprites being compiled which will increase shader compile time and memory usage. |
| bUsedWithNiagaraRibbons | `uint32` |  |
| bUsedWithNiagaraMeshParticles | `uint32` |  |
| bUsedWithIBL | `uint32` | Indicates that the material and its instances can be use with reflection cube<br>	  This will result in the shaders required to support IBL being compiled which will increase shader compile time and memory usage. |
| bUsedWithStaticLighting | `uint32` | Indicates that the material and its instances can be use with static lighting<br>	  This will result in the shaders required to support static lighting being compiled which will increase shader compile time and memory usage. |
| bUsedWithMorphTargets | `uint32` | Indicates that the material and its instances can be use with morph targets<br>	  This will result in the shaders required to support morph targets being compiled which will increase shader compile time and memory usage. |
| bUsedWithSplineMeshes | `uint32` | Indicates that the material and its instances can be use with spline meshes<br>	  This will result in the shaders required to support spline meshes being compiled which will increase shader compile time and memory usage. |
| bUsedWithQuantizedMeshes | `uint32` |  |
| bUsedWithInstancedStaticMeshes | `uint32` | Indicates that the material and its instances can be use with instanced static meshes<br>	  This will result in the shaders required to support instanced static meshes being compiled which will increase shader compile time and memory usage. |
| bUsedWithCustomInstancedStaticMeshes | `uint32` | Indicates that the material and its instances can be use with custom instanced static meshes<br>	  This will result in the shaders required to support instanced static meshes being compiled which will increase shader compile time and memory usage. |
| bUsedWithInstancedWidget | `uint32` |  |
| bUsedWithInstancedPDSurface | `uint32` |  |
| bUsesDistortion | `uint32` | Indicates that the material and its instances can be use with distortion<br>	  This will result in the shaders required to support distortion being compiled which will increase shader compile time and memory usage. |
| bUsedWithClothing | `uint32` | Indicates that the material and its instances can be use with clothing<br>	  This will result in the shaders required to support clothing being compiled which will increase shader compile time and memory usage. |
| bUsedWithUI_DEPRECATED | `uint32` | Indicates that the material and its instances can be use with Slate UI and UMG<br>	  This will result in the shaders required to support UI materials being compiled which will increase shader compile time and memory usage. |
| bUsedWithPPRBackgroud | `uint32` | Indicates that the material would use for ppr background in deferred rendering. |
| bUsedWithSurfelInjectColor | `uint32` | Indicates that the material and its instances can be use with SurfelGI inject color<br>	  This will result in the shaders required to support SurfelGI inject color being compiled which will increase shader compile time and memory usage.<br>	  HACK by huiwenjiang. |
| bUsedWithTranslucentGI | `uint32` | [SurfelGI - brainfkli ADD]<br>	  Indicates that the material and its instances can be affected by GI in translucent blend mode. |
| bUsedWithAtmosphericSkyBox | `uint32` | Indicates that the material and its instances can be use with AtmosphericSkyBox<br>	  This will result in the shaders required to support AtmosphericSkyBox being compiled which will increase shader compile time and memory usage. |
| bAutomaticallySetUsageInEditor | `uint32` | Whether to automatically set usage flags based on what the material is applied to in the editor.<br>	  It can be useful to disable this on a base material with many instances, where adding another usage flag accidentally (eg bUsedWithSkeletalMeshes) can add a lot of shader permutations. |
| bFullyRough | `uint32` | Forces the material to be completely rough. Saves a number of instructions and one sampler. Note: Overrided by Lite Rough. |
| bUsedWithLandscapeDeform | `uint32` | Indicates that the material and its instances can be use with Landscape Deform<br>	  This will result in the shaders required to support LandscapeDeform being compiled which will increase shader compile time and memory usage. |
| bUseFullPrecision | `uint32` | Forces this material to use full (highp) precision in the pixel shader.<br>	 	This is slower than the default (mediump) but can be used to work around precision-related rendering errors.<br>	 	This setting has no effect on older mobile devices that do not support high precision.<br>	   Note: Overrided by Lite Rough. |
| bForceMaterialFloat | `uint32` | Forces this material's temporary variables to use full precision float in the pixel shader.<br>	  Keeps uniforms to use default precision. HACK by huiwen. |
| bUseLightmapDirectionality | `uint32` | Use lightmap directionality and per pixel normals. If disabled, lighting from lightmaps will be flat but cheaper. |
| bUsedWithDynamicInstancing | `uint32` | Indicates that the each material instance(of this material) can be dynamic instanced. |
| bDynamicInstancingByUBO | `uint32` |  |
| bUsedWithRuntimeStaticBatchMultiParams | `uint32` |  |
| bNeedInstanceTransform | `uint32` |  |
| bUseSimplestShader | `uint32` |  |
| bBypassSystemMaterialQuality | `uint32` |  |
| bBypassMobilePointLight | `uint32` |  |
| bUseAsEarlyZ | `uint32` |  |
| bForceOutputLinearSpace | `uint32` |  |
| bUseAsDrawToRenderTarget | `uint32` |  |
| bRenderInTwoPass | `uint32` |  |
| bShadowUseTentFilter | `uint32` |  |
| bUseLightmap | `uint32` |  |
| bUseGPUVolumetricLightMap | `uint32` |  |
| bUsedGPUVLMVertexLighting | `uint32` |  |
| bUseVolumeProbeGIMobile | `uint32` |  |
| bUseVolumeProbeGIMobileWithAO | `uint32` |  |
| bShouldReceiveGridShadow | `uint32` |  |
| bEnableMicroShadow | `uint32` |  |
| MicroShadowIntensity | `float` |  |
| bUseIndirectLighting | `uint32` |  |
| bShadowOnEmissiveColor | `uint32` |  |
| bUsedGrassInstnaceColor | `uint32` |  |
| bUsedVertexPointLight | `uint32` |  |
| bUsedWithLandscapeShadow | `uint32` |  |
| bUseLandscapeMultiLayer | `uint32` |  |
| bUsedWithPhotonShadow | `uint32` | #if WITH_PHOTON_SHADOW |
| bUsedWithPhotonShadowPCSS | `uint32` |  |
| bUsedDynamicObjectVertexLighting | `uint32` |  |
| bUsedWithDynamicBatching | `uint32` | Indicates that the material instance shared with same base mat can be batched |
| bUsedWithDynamicMergeSkeletalMesh | `uint32` |  |
| bUsedWithDynamicInstancingES2Fixup | `uint32` |  |
| bUsedWithMatIDLandscape | `uint32` |  |
| ShadowOverride | `TEnumAsByte < enum EMaterialShadowOverride >` |  |
| SimpleVertexNormalSituation | `TEnumAsByte < enum ESimpleVertexNormalSituation >` |  |
| bZForceFar | `uint32` |  |
| bWettable | `uint32` |  |
| bUseLegacySpecular | `uint32` | use Phong instead of GGX |
| bCorrectBlendingColorInHDR | `uint32` |  |
| bGPUSkinForceUseBonesUniformBuffer | `uint32` |  |
| bUseAsTranslucentEarlyZ | `uint32` |  |
| bLiteRough | `uint32` | Override: Fully Rough On、UseFullPrecision Off |
| bUseSimpleSkyLight | `uint32` |  |
| bACESOff | `uint32` |  |
| bEmissionOff | `uint32` |  |
| bInstL2WOnlyTranslation | `uint32` | Instancing only uses translation of LocalToWorld, exclusive of rotation and scale. |
| bUseLiteFog | `uint32` |  |
| bUseChromaticAberration | `uint32` |  |
| bUsedWithFirstPerson | `uint32` |  |
| bUsedWithScope | `uint32` |  |
| bUsedWithMaterialDistFade | `uint32` |  |
| bUseHQForwardReflections | `uint32` | Forward renderer: enables multiple parallax-corrected reflection captures that blend together.<br>	  Mobile renderer: blend between nearest 3 reflection captures, but reduces the number of samplers available to the material as two more samplers will be used for reflection cubemaps. |
| bUsePlanarForwardReflections | `uint32` | Enables planar reflection when using the forward renderer or mobile. Enabling this setting reduces the number of samplers available to the material as one more sampler will be used for the planar reflection. |
| bApplyVertexFog | `uint32` | When false, materials are not fogged in forward shading or mobile. Defaults to true. |
| bNormalCurvatureToRoughness | `uint32` | Reduce roughness based on screen space normal changes. |
| D3D11TessellationMode | `TEnumAsByte < enum EMaterialTessellationMode >` | The type of tessellation to apply to this object.  Note D3D11 required for anything except MTM_NoTessellation. |
| bEnableCrackFreeDisplacement | `uint32` | Prevents cracks in the surface of the mesh when using tessellation. |
| bEnableAdaptiveTessellation | `uint32` | Enables adaptive tessellation, which tries to maintain a uniform number of pixels per triangle. |
| bUsedWithTexture2DArrayShaderVariant | `uint32` | ENABLE_TEXTURE2D_ARRAY_SHADER_VARIANT<br>	 Enable Dynamic MaterialInstance use Texture 2D Array shader variant with Texture 2D material expression graph |
| bSkipRSH | `uint32` | Skip Runtime Static Batching (RSH) |
| bSkipDynamicSwitchOp | `uint32` |  |
| bUsesDeviceLevelSwitch | `uint32` | 缓存标记：材质是否使用了DeviceLevelSwitch节点且High输入已连接，在PostEditChangeProperty中自动更新 |
| bForceUsesDeviceLevelSwitch | `uint32` | 强制开启DeviceLevelSwitch：勾选后bUsesDeviceLevelSwitch将被强制设为true，即使材质中没有DeviceLevelSwitch节点 |
| bCanChangeQualitySeparately | `uint32` | 勾选后，该材质将使用独立的场景材质质量等级（r.SceneMaterialQualityLevel），而非全局 r.MaterialQualityLevel |
| bDisableShadowWPO | `uint32` |  |
| bEnableGrassShadowScale | `uint32` |  |
| bForceDisableVertexNormal | `uint32` |  |
| MaxDisplacement | `float` |  |
| Wireframe | `uint32` | Enables a wireframe view of the mesh the material is applied to. |
| bOutputVelocityOnBasePass | `uint32` | Skips outputting velocity during the base pass. |
| bUnlitOutputAllMTOnBasePass | `uint32` | Force unlit material output all MT during the base pass. |
| ShadingRate | `TEnumAsByte < EMaterialShadingRate >` | Select what shading rate to apply for platforms that have variable rate shading |
| EditorX | `int32` |  |
| EditorY | `int32` |  |
| EditorPitch | `int32` |  |
| EditorYaw | `int32` |  |
| Expressions | `TArray < UMaterialExpression * >` | Array of material expressions, excluding Comments.  Used by the material editor. |
| MaterialFunctionInfos | `TArray < FMaterialFunctionInfo >` | Array of all functions this material depends on. |
| MaterialParameterCollectionInfos | `TArray < FMaterialParameterCollectionInfo >` | Array of all parameter collections this material depends on. |
| bCanMaskedBeAssumedOpaque | `uint32` | true if this Material can be assumed Opaque when set to masked. |
| bIsMasked_DEPRECATED | `uint32` | true if Material is masked and uses custom opacity |
| bIsPreviewMaterial | `uint32` | true if Material is the preview material used in the material editor. |
| bUseMaterialAttributes | `uint32` | when true, the material attributes pin is used instead of the regular pins. |
| bComputeFogPerPixel | `uint32` | When true, translucent materials have fog computed for every pixel, which costs more but fixes artifacts due to low tessellation. |
| bDisableDirectionalLighting | `uint32` | When true, the directional lighting will be disabled |
| bAllowDevelopmentShaderCompile | `uint32` | If true the compilation environment will be changed to remove the global COMPILE_SHADERS_FOR_DEVELOPMENT flag. |
| bIsMaterialEditorStatsMaterial | `uint32` | true if this is a special material used for stats by the material editor. |
| bUseLandscapeVertexAO | `uint32` |  |
| bAllowLandscapeVertexMorph | `uint32` |  |
| bUseLandscapeVertexHole | `uint32` |  |
| UsageFlagWarnings | `uint32` | true if we have printed a warning about material usage for a given usage flag. |
| BlendableLocation | `TEnumAsByte < enum EBlendableLocation >` | Where the node is inserted in the (post processing) graph, only used if domain is PostProcess |
| BlendablePriority | `int32` | If multiple nodes with the same  type are inserted at the same point, this defined order and if they get combined, only used if domain is PostProcess |
| BlendableOutputAlpha | `bool` | If this is enabled, the blendable will output alpha |
| RefractionMode | `TEnumAsByte < enum ERefractionMode >` | Controls how the Refraction input is interpreted and how the refraction offset into scene color is computed for this material. |
| RefractionDepthBias | `float` | This is the refraction depth bias, larger values offset distortion to prevent closer objects from rendering into the distorted surface at acute viewing angles but increases the disconnect between surface and where the refraction starts. |
| bOceanFoam | `uint32` |  |
| bEnableMeshClip | `uint32` |  |
| bEnableMeshDiscard | `uint32` |  |
| bEnableMeshArcPlaneClip | `uint32` |  |
| bIsEnhancedUImage | `uint32` |  |
| bSimplePointLight | `uint32` | Enable this so the material will not calculate spot light shadows |
| StateId | [FGuid](../../cppstruct/F/FG/FGuid.md) | Guid that uniquely identifies this material.<br>	  Any changes to the state of the material that do not appear separately in the shadermap DDC keys must cause this guid to be regenerated!<br>	  For example, a modification to the Expressions array.<br>	  Code changes that cause the guid to be regenerated on load should be avoided, as that requires a resave of the content to stop recompiling every load. |
| ExpressionTextureReferences | `TArray < UTexture * >` | Cached texture references from all expressions in the material (including nested functions).<br>	  This is used to link uniform texture expressions which were stored in the DDC with the UTextures that they reference. |
| EditorComments | `TArray < UMaterialExpressionComment * >` | Array of comments associated with this material; viewed in the material editor. |
| ParameterGroupData | `TArray < FParameterGroupData >` | Controls where this parameter group is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list. |
| ReferencedTextureGuids | `TArray < FGuid >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
