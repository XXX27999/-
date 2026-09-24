# FGameMagnitudeWrapper

数值Wrapper

## Fields

| Name | Type | Description |
| --- | --- | --- |
| CalculatorType | [EPESkillValueCalculatorType](../../../cppenum/E/EP/EPESkillValueCalculatorType.md) | 数值计算方式 |
| Value | `float` | 数值 |
| GameAttribute | `FGameAttributeContainer` | 要使用的属性名<br><br>	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (DisplayName = "数值=AX+B")) |
| ValueA | `FFloatGetter` | 公式参数A |
| ValueB | `FFloatGetter` | 公式参数B |
