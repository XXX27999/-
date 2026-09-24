# FInputAxisKeyMapping

Defines a mapping between an axis and key

## Fields

| Name | Type | Description |
| --- | --- | --- |
| AxisName | `FName` | Friendly name of axis, e.g "MoveForward" |
| Key | `FKey` | Key to bind it to. |
| Scale | `float` | Multiplier to use for the mapping when accumulating the axis value |
| KeySeq | `uint8` | key sequence number: 0 for Primary key, 1 for Backup key |
