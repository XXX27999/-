# UEngine

Abstract base class of all Engine classes, responsible for management of systems critical to editor or game systems.
  Also defines default classes for certain engine systems.

## Parents

- [UObject](./UObject.md)
- FExec

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TinyFont | `UFont *` |  |
| TinyFontName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| SmallFont | `UFont *` | @todo document |
| SmallFontName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| MediumFont | `UFont *` | @todo document |
| MediumFontName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| LargeFont | `UFont *` | @todo document |
| LargeFontName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| SubtitleFont | `UFont *` | @todo document |
| SubtitleFontName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| AdditionalFonts | `TArray < UFont * >` | Any additional fonts that script may use without hard-referencing the font. |
| AdditionalFontNames | `TArray < FString >` | @todo document |
| ConsoleClass | `TSubclassOf < UConsole >` | The class to use for the game console. |
| ConsoleClassName | `FSoftClassPath` | @todo document |
| GameViewportClientClass | `TSubclassOf < UGameViewportClient >` | The class to use for the game viewport client. |
| GameViewportClientClassName | `FSoftClassPath` | @todo document |
| LocalPlayerClass | `TSubclassOf < ULocalPlayer >` | The class to use for local players. |
| LocalPlayerClassName | `FSoftClassPath` | @todo document |
| WorldSettingsClass | `TSubclassOf < AWorldSettings >` | The class for WorldSettings |
| WorldSettingsClassName | `FSoftClassPath` | @todo document |
| NavigationSystemClassName | `FSoftClassPath` | @todo document |
| NavigationSystemClass | `TSubclassOf < UNavigationSystem >` | The class for NavigationSystem |
| AvoidanceManagerClassName | `FSoftClassPath` | Name of behavior tree manager class |
| AvoidanceManagerClass | `TSubclassOf < UAvoidanceManager >` | The class for behavior tree manager |
| PhysicsCollisionHandlerClass | `TSubclassOf < UPhysicsCollisionHandler >` | PhysicsCollisionHandler class we should use by default |
| PhysicsCollisionHandlerClassName | `FSoftClassPath` | Name of PhysicsCollisionHandler class we should use by default. |
| GameUserSettingsClassName | `FSoftClassPath` |  |
| GameUserSettingsClass | `TSubclassOf < UGameUserSettings >` |  |
| AIControllerClassName | `FSoftClassPath` | name of Controller class to be used as default AIController class for pawns |
| GameUserSettings | `UGameUserSettings *` | Global instance of the user game settings |
| LevelScriptActorClass | `TSubclassOf < ALevelScriptActor >` | @todo document |
| LevelScriptActorClassName | `FSoftClassPath` | @todo document |
| DefaultBlueprintBaseClassName | `FSoftClassPath` | Name of the base class to use for new blueprints, configurable on a per-game basis |
| GameSingletonClassName | `FSoftClassPath` | Name of a singleton class to create at startup time, configurable per game |
| GameSingleton | `UObject *` | A UObject spawned at initialization time to handle game-specific data |
| AssetManagerClassName | `FSoftClassPath` | Name of a singleton class to spawn as the AssetManager, configurable per game. If empty, it will not spawn one |
| AssetManager | `UAssetManager *` | A UObject spawned at initialization time to handle game-specific data |
| DefaultTexture | `UTexture2D *` | A global default texture. |
| DefaultTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| DefaultDiffuseTexture | `UTexture *` | A global default diffuse texture. |
| DefaultDiffuseTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| DefaultTextureArray | `UTexture2DArray *` | A global default texture array. |
| DefaultBSPVertexTexture | `UTexture2D *` | @todo document |
| DefaultBSPVertexTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| HighFrequencyNoiseTexture | `UTexture2D *` | Texture used to get random image grain values for post processing |
| HighFrequencyNoiseTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| DefaultBokehTexture | `UTexture2D *` | Texture used to blur out of focus content, mimics the Bokeh shape of actual cameras |
| DefaultBokehTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| DefaultBloomKernelTexture | `UTexture2D *` | Texture used to bloom when using FFT, mimics characteristic bloom produced in a camera from a signle bright source |
| DefaultBloomKernelTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| WireframeMaterial | `UMaterial *` | The material used to render wireframe meshes. |
| WireframeMaterialName | `FString` | @todo document |
| DebugMeshMaterial | `UMaterial *` | A material used to render debug meshes. |
| DebugMeshMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| LevelColorationLitMaterial | `UMaterial *` | Material used for visualizing level membership in lit view port modes. |
| LevelColorationLitMaterialName | `FString` | @todo document |
| LevelColorationUnlitMaterial | `UMaterial *` | Material used for visualizing level membership in unlit view port modes. |
| LevelColorationUnlitMaterialName | `FString` | @todo document |
| LightingTexelDensityMaterial | `UMaterial *` | Material used for visualizing lighting only w lightmap texel density. |
| LightingTexelDensityName | `FString` | @todo document |
| ShadedLevelColorationLitMaterial | `UMaterial *` | Material used for visualizing level membership in lit view port modes. Uses shading to show axis directions. |
| ShadedLevelColorationLitMaterialName | `FString` | @todo document |
| ShadedLevelColorationUnlitMaterial | `UMaterial *` | Material used for visualizing level membership in unlit view port modes.  Uses shading to show axis directions. |
| ShadedLevelColorationUnlitMaterialName | `FString` | @todo document |
| NewShadedLevelColorationUnlitMaterial | `UMaterial *` | Material used for visualizing level membership in unlit view port modes.  Uses shading to show axis directions. |
| NewShadedLevelColorationUnlitMaterialName | `FString` | @todo document |
| RemoveSurfaceMaterial | `UMaterial *` | Material used to indicate that the associated BSP surface should be removed. |
| RemoveSurfaceMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| VertexColorMaterial | `UMaterial *` | Material that renders vertex color as emmissive. |
| VertexColorMaterialName | `FString` | @todo document |
| VertexColorViewModeMaterial_ColorOnly | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (color only, no alpha) |
| VertexColorViewModeMaterialName_ColorOnly | `FString` | @todo document |
| VertexColorViewModeMaterial_AlphaAsColor | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (alpha channel as color) |
| VertexColorViewModeMaterialName_AlphaAsColor | `FString` | @todo document |
| VertexColorViewModeMaterial_RedOnly | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (red only) |
| VertexColorViewModeMaterialName_RedOnly | `FString` | @todo document |
| VertexColorViewModeMaterial_GreenOnly | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (green only) |
| VertexColorViewModeMaterialName_GreenOnly | `FString` | @todo document |
| VertexColorViewModeMaterial_BlueOnly | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (blue only) |
| VertexColorViewModeMaterialName_BlueOnly | `FString` | @todo document |
| DebugEditorMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | A material used to render debug opaque material. Used in various animation editor viewport features. |
| ConstraintLimitMaterial | `UMaterial *` | Material used to render constraint limits |
| ConstraintLimitMaterialX | `UMaterialInstanceDynamic *` |  |
| ConstraintLimitMaterialXAxis | `UMaterialInstanceDynamic *` |  |
| ConstraintLimitMaterialY | `UMaterialInstanceDynamic *` |  |
| ConstraintLimitMaterialYAxis | `UMaterialInstanceDynamic *` |  |
| ConstraintLimitMaterialZ | `UMaterialInstanceDynamic *` |  |
| ConstraintLimitMaterialZAxis | `UMaterialInstanceDynamic *` |  |
| ConstraintLimitMaterialPrismatic | `UMaterialInstanceDynamic *` |  |
| InvalidLightmapSettingsMaterial | `UMaterial *` | Material that renders a message about lightmap settings being invalid. |
| InvalidLightmapSettingsMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| PreviewShadowsIndicatorMaterial | `UMaterial *` | Material that renders a message about preview shadows being used. |
| PreviewShadowsIndicatorMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| ArrowMaterial | `UMaterial *` | Material that 'fakes' lighting, used for arrows, widgets. |
| ArrowMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| OutlineMaterial | `UMaterial *` | Material IdeaOutline. |
| OutlineMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| OutlineMaskedMaterial | `UMaterial *` |  |
| OutlineMaskedMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| OutlineMaterialNewOpaque | `UMaterial *` |  |
| OutlineMaterialNewOpaqueName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| OutlineMaterialNewTranslucent | `UMaterial *` |  |
| OutlineMaterialNewTranslucentName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| OutlineMaskedMaterialNewOpaque | `UMaterial *` |  |
| OutlineMaskedMaterialNewOpaqueName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| OutlineMaskedMaterialNewTranslucent | `UMaterial *` |  |
| OutlineMaskedMaterialNewTranslucentName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| HighlightMaterial | `UMaterial *` |  |
| HighlightMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| SmaaAreaTexName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | SMAA AreaTex name |
| SmaaSearchTexName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | SMAA SearchTex name |
| SmaaAreaTex | `UTexture2D *` | SMAA AreaTex |
| SmaaSearchTex | `UTexture2D *` | SMAA SearchTex |
| DyeingColorMaterial | `UMaterial *` | Material IdeaOutline. |
| DyeingColorMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| LightingOnlyBrightness | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | @todo document |
| ShaderComplexityColors | `TArray < FLinearColor >` | The colors used to render shader complexity. |
| QuadComplexityColors | `TArray < FLinearColor >` | The colors used to render quad complexity. |
| LightComplexityColors | `TArray < FLinearColor >` | The colors used to render light complexity. |
| StationaryLightOverlapColors | `TArray < FLinearColor >` | The colors used to render stationary light overlap. |
| LODColorationColors | `TArray < FLinearColor >` | The colors used to render LOD coloration. |
| HLODColorationColors | `TArray < FLinearColor >` | The colors used to render LOD coloration. |
| LightmapColorationColors | `TArray < FLinearColor >` | The colors used to render Lightmap type coloration. |
| StreamingAccuracyColors | `TArray < FLinearColor >` | The colors used for texture streaming accuracy debug view modes. |
| TextureStreamingBudgetColors | `TArray < FLinearColor >` |  |
| DesiredTexelDensity | `int32` |  |
| TexelDensityTextureSuffixList | `TArray < FString >` |  |
| TexelDensityAccuracyColors | `TArray < FLinearColor >` |  |
| MaxPixelShaderAdditiveComplexityCount | `float` | Complexity limits for the various complexity view mode combinations.<br>	 These limits are used to map instruction counts to ShaderComplexityColors. |
| MaxES2PixelShaderAdditiveComplexityCount | `float` |  |
| MinLightMapDensity | `float` | Range for the lightmap density view mode.<br>	 Minimum lightmap density value for coloring. |
| IdealLightMapDensity | `float` | Ideal lightmap density value for coloring. |
| MaxLightMapDensity | `float` | Maximum lightmap density value for coloring. |
| bRenderLightMapDensityGrayscale | `uint32` | If true, then render gray scale density. |
| RenderLightMapDensityGrayscaleScale | `float` | The scale factor when rendering gray scale density. |
| RenderLightMapDensityColorScale | `float` | The scale factor when rendering color density. |
| LightMapDensityVertexMappedColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color to render vertex mapped objects in for LightMap Density view mode. |
| LightMapDensitySelectedColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color to render selected objects in for LightMap Density view mode. |
| StatColorMappings | `TArray < FStatColorMapping >` | @todo document |
| DefaultPhysMaterial | `UPhysicalMaterial *` | PhysicalMaterial to use if none is defined for a particular object. |
| DefaultPhysMaterialName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| ActiveGameNameRedirects | `TArray < FGameNameRedirect >` |  |
| ActiveClassRedirects | `TArray < FClassRedirect >` |  |
| ActivePluginRedirects | `TArray < FPluginRedirect >` |  |
| ActiveStructRedirects | `TArray < FStructRedirect >` |  |
| PreIntegratedSkinBRDFTexture | `UTexture2D *` | Texture used for pre-integrated skin shading |
| PreIntegratedSkinBRDFTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| MiniFontTexture | `UTexture2D *` | Texture used to do font rendering in shaders |
| MiniFontTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| WeightMapPlaceholderTexture | `UTexture *` | Texture used as a placeholder for terrain weight-maps to give the material the correct texture format. |
| WeightMapPlaceholderTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| LightMapDensityTexture | `UTexture2D *` | Texture used to display LightMapDensity |
| LightMapDensityTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | @todo document |
| GameViewport | `UGameViewportClient *` | The view port representing the current game instance. Can be 0 so don't use without checking. |
| DeferredCommands | `TArray < FString >` | Array of deferred command strings execs that get executed at the end of the frame |
| TickCycles | `int32` | @todo document |
| GameCycles | `int32` | @todo document |
| ClientCycles | `int32` | @todo document |
| NearClipPlane | `float` | The distance of the camera's near clipping plane. |
| bHardwareSurveyEnabled_DEPRECATED | `uint32` | DEPRECATED - Can a runtime gameapplication report anonymous hardware survey statistics (such as display resolution and GPU model) back to Epic? |
| bSubtitlesEnabled | `uint32` | Flag for completely disabling subtitles for localized sounds. |
| bSubtitlesForcedOff | `uint32` | Flag for forcibly disabling subtitles even if you try to turn them back on they will be off |
| MaximumLoopIterationCount | `int32` | Script maximum loop iteration count used as a threshold to warn users about script execution runaway |
| bCanBlueprintsTickByDefault | `uint32` |  |
| bOptimizeAnimBlueprintMemberVariableAccess | `uint32` | Controls whether anim blueprint nodes that access member variables of their class directly should use the optimized path that avoids a thunk to the Blueprint VM. This will force all anim blueprints to be recompiled. |
| bAllowMultiThreadedAnimationUpdate | `uint32` | Controls whether by default we allow anim blueprint graph updates to be performed on non-game threads. This enables some extra checks in the anim blueprint compiler that will warn when unsafe operations are being attempted. This will force all anim blueprints to be recompiled. |
| bEnableEditorPSysRealtimeLOD | `uint32` | @todo document |
| bSmoothFrameRate | `uint32` | Whether to enable framerate smoothing. |
| bUseFixedFrameRate | `uint32` | Whether to use a fixed framerate. |
| FixedFrameRate | `float` | The fixed framerate to use. |
| SmoothedFrameRateRange | [FFloatRange](../../cppstruct/F/FF/FFloatRange.md) | Range of framerates in which smoothing will kick in |
| bCheckForMultiplePawnsSpawnedInAFrame | `uint32` | Whether we should check for more than N pawns spawning in a single frame.<br>	  Basically, spawning pawns and all of their attachments can be slow.  And on consoles it<br>	  can be really slow.  If this bool is true we will display a |
| NumPawnsAllowedToBeSpawnedInAFrame | `int32` | If bCheckForMultiplePawnsSpawnedInAFrame==true, then we will check to see that no more than this number of pawns are spawned in a frame. |
| bShouldGenerateLowQualityLightmaps_DEPRECATED | `uint32` | Whether or not the LQ lightmaps should be generated during lighting rebuilds.  This has been moved to r.SupportLowQualityLightmaps. |
| C_WorldBox | [FColor](../../cppstruct/F/FC/FColor.md) |  |
| C_BrushWire | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_AddWire | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_SubtractWire | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_SemiSolidWire | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_NonSolidWire | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_WireBackground | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_ScaleBoxHi | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_VolumeCollision | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_BSPCollision | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_OrthoBackground | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_Volume | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| C_BrushShape | [FColor](../../cppstruct/F/FC/FColor.md) | @todo document |
| StreamingDistanceFactor | `float` | Fudge factor for tweaking the distance based miplevel determination |
| GameScreenshotSaveDirectory | [FDirectoryPath](../../cppstruct/F/FD/FDirectoryPath.md) | The save directory for newly created screenshots |
| TransitionType | `TEnumAsByte < enum ETransitionType >` | The current transition type. |
| TransitionDescription | `FString` | The current transition description text. |
| TransitionGameMode | `FString` | The gamemode for the destination map |
| MeshLODRange | `float` | Level of detail range control for meshes |
| bAllowMatureLanguage | `uint32` | whether mature language is allowed |
| CameraRotationThreshold | `float` | camera rotation (deg) beyond which occlusion queries are ignored from previous frame (because they are likely not valid) |
| CameraTranslationThreshold | `float` | camera movement beyond which occlusion queries are ignored from previous frame (because they are likely not valid) |
| PrimitiveProbablyVisibleTime | `float` | The amount of time a primitive is considered to be probably visible after it was last actually visible. |
| MaxOcclusionPixelsFraction | `float` | Max screen pixel fraction where retesting when unoccluded is worth the GPU time. |
| bPauseOnLossOfFocus | `uint32` | Whether to pause the game if focus is lost. |
| MaxParticleResize | `int32` | The maximum allowed size to a ParticleEmitterInstance::Resize call.<br>	 	If larger, the function will return without resizing. |
| MaxParticleResizeWarn | `int32` | If the resize request is larger than this, spew out a warning to the log |
| PendingDroppedNotes | `TArray < FDropNoteInfo >` | @todo document |
| PhysicErrorCorrection | [FRigidBodyErrorCorrection](../../cppstruct/F/FR/FRigidBodyErrorCorrection.md) | Error correction data for replicating simulated physics (rigid bodies) |
| NetClientTicksPerSecond | `float` | Number of times to tick each client per second |
| DisplayGamma | `float` | Current display gamma setting |
| MinDesiredFrameRate | `float` | Minimum desired framerate setting |
| ShaderPrecompileProgress | `int32` |  |
| DefaultSelectedMaterialColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Default color of selected objects in the level viewport (additive) |
| SelectedMaterialColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color of selected objects in the level viewport (additive) |
| SelectionOutlineColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color of the selection outline color.  Generally the same as selected material color unless the selection material color is being overridden |
| SubduedSelectionOutlineColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Subdued version of the selection outline color. Used for indicating sub-selection of components vs actors |
| SelectedMaterialColorOverride | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | An override to use in some cases instead of the selected material color |
| bIsOverridingSelectedColor | `bool` | Whether or not selection color is being overridden |
| bEnableOnScreenDebugMessages | `uint32` | If true, then disable OnScreenDebug messages. Can be toggled in real-time. |
| bEnableOnScreenDebugMessagesDisplay | `uint32` | If true, then disable the display of OnScreenDebug messages (used when running) |
| bSuppressMapWarnings | `uint32` | If true, then skip drawing map warnings on screen even in non (UE_BUILD_SHIPPING \|\| UE_BUILD_TEST) builds |
| bDisableAILogging | `uint32` | determines whether AI logging should be processed or not |
| bEnableVisualLogRecordingOnStart | `uint32` |  |
| BlueNoiseScalarTexture | `UTexture2D *` | Tiled blue-noise texture |
| BlueNoiseVec2Texture | `UTexture2D *` | Spatial-temporal blue noise texture with two channel output |
| BlueNoiseScalarTextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | Path of the tiled blue-noise texture |
| BlueNoiseVec2TextureName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | Path of the tiled blue-noise texture |
| ScreenSaverInhibitorSemaphore | `int32` | Semaphore to control screen saver inhibitor thread access. |
| bLockReadOnlyLevels | `uint32` | true if the the user cannot modify levels that are read only. |
| ParticleEventManagerClassPath | `FString` | Particle event manager |
| SelectionHighlightIntensity | `float` | Used to alter the intensity level of the selection highlight on selected objects |
| SelectionMeshSectionHighlightIntensity | `float` | Used to alter the intensity level of the selection highlight on selected mesh sections in mesh editors |
| BSPSelectionHighlightIntensity | `float` | Used to alter the intensity level of the selection highlight on selected BSP surfaces |
| HoverHighlightIntensity | `float` | Used to alter the intensity level of the selection highlight on hovered objects |
| SelectionHighlightIntensityBillboards | `float` | Used to alter the intensity level of the selection highlight on selected billboard objects |
| NetDriverDefinitions | `TArray < FNetDriverDefinition >` | A list of named UNetDriver definitions |
| ServerActors | `TArray < FString >` | A configurable list of actors that are automatically spawned upon server startup (just prior to InitGame) |
| RuntimeServerActors | `TArray < FString >` | Runtime-modified list of server actors, allowing plugins to use serveractors, without permanently adding them to config files |
| bStartedLoadMapMovie | `uint32` | true if the loading movie was started during LoadMap(). |
| NextWorldContextHandle | `int32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
