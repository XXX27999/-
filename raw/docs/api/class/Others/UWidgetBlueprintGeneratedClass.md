# UWidgetBlueprintGeneratedClass

The widget blueprint generated class allows us to create blueprint-able widgets for UMG at runtime.
  All WBPGC's are of UUserWidget classes, and they perform special post initialization using this class
  to give themselves many of the same capabilities as AActor blueprints, like dynamic delegate binding for
  widgets.

## Parents

- UBlueprintGeneratedClass

## Variables

| Name | Type | Description |
| --- | --- | --- |
| WidgetTree | `UWidgetTree *` | A tree of the widget templates to be created |
| WidgetTreePath | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| bAutoReleaseWidgetTree | `uint8` |  |
| bAllowTemplate | `uint8` |  |
| bValidTemplate | `uint8` |  |
| bTemplateInitialized | `uint8` |  |
| bCookedTemplate | `uint8` |  |
| Bindings | `TArray < FDelegateRuntimeBinding >` |  |
| Animations | `TArray < UWidgetAnimation * >` |  |
| NamedSlots | `TArray < FName >` |  |
| TemplateAsset | `TSoftObjectPtr < UUserWidget >` |  |
| Template | `UUserWidget *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
