# UMaterialExpressionDeviceLevelSwitch

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Default | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Default input (must be connected). Same as Low. Used when DEVICE_LEVEL_HIGH is 0. |
| Low | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Low device input (optional). If connected, overrides Default. Used when DEVICE_LEVEL_HIGH is 0. |
| High | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | High device input (optional). Used when DEVICE_LEVEL_HIGH is 1. Connecting this enables DeviceLevel shader variants. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
