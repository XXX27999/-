# UAutomationTestSettings

Implements the Editor's user settings.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EngineTestModules | `TArray < FString >` | Modules to load that have engine tests |
| EditorTestModules | `TArray < FString >` | Modules to load that have editor tests |
| AutomationTestmap | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | The automation test map to be used for several of the automation tests. |
| EditorPerformanceTestMaps | `TArray < FEditorMapPerformanceTestDefinition >` | The map to be used for the editor performance capture tool. |
| AssetsToOpen | `TArray < FSoftObjectPath >` | Asset to test for open in automation process |
| BuildPromotionTest | [FBuildPromotionTestSettings](../../cppstruct/F/FB/FBuildPromotionTestSettings.md) | Editor build promotion test settings |
| MaterialEditorPromotionTest | [FMaterialEditorPromotionSettings](../../cppstruct/F/FM/FMaterialEditorPromotionSettings.md) | Material editor promotion test settings |
| ParticleEditorPromotionTest | [FParticleEditorPromotionSettings](../../cppstruct/F/FP/FParticleEditorPromotionSettings.md) | Particle editor promotion test settings |
| BlueprintEditorPromotionTest | [FBlueprintEditorPromotionSettings](../../cppstruct/F/FB/FBlueprintEditorPromotionSettings.md) | Blueprint editor promotion test settings |
| TestLevelFolders | `TArray < FString >` | Folders containing levels to exclude from automated tests |
| ExternalTools | `TArray < FExternalToolDefinition >` | External executables and scripts to run as part of automation. |
| ImportExportTestDefinitions | `TArray < FEditorImportExportTestDefinition >` | Asset import  Export test settings |
| LaunchOnSettings | `TArray < FLaunchOnTestSettings >` | The map and device type to be used for the editor Launch On With Map Iterations test. |
| DefaultScreenshotResolution | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) | The default resolution to take all automation screenshots at. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
