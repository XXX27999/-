# FModulatorContinuousParams

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` | The name of the sound instance parameter that specifies the current value. |
| Default | `float` | The default value to be used if the parameter is not found. |
| MinInput | `float` | The minimum input value. Values will be clamped to the [MinInput, MaxInput] range. |
| MaxInput | `float` | The maximum input value. Values will be clamped to the [MinInput, MaxInput] range. |
| MinOutput | `float` | The minimum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput] |
| MaxOutput | `float` | The maximum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput] |
| ParamMode | `TEnumAsByte < enum ModulationParamMode >` | The mode with which to treat the input value |
