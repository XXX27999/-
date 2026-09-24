# UEnvQueryTest

## Parents

- [UEnvQueryNode](./UEnvQueryNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TestOrder | `int32` | Number of test as defined in data asset |
| TestPurpose | `TEnumAsByte < EEnvTestPurpose :: Type >` | The purpose of this test.  Should it be used for filtering possible results, scoring them, or both? |
| TestComment | `FString` | Optional comment or explanation about what this test is for.  Useful when the purpose of tests may not be clear,<br>	   especially when there are multiple tests of the same type. |
| MultipleContextFilterOp | `TEnumAsByte < EEnvTestFilterOperator :: Type >` | Determines filtering operator when context returns multiple items |
| MultipleContextScoreOp | `TEnumAsByte < EEnvTestScoreOperator :: Type >` | Determines scoring operator when context returns multiple items |
| FilterType | `TEnumAsByte < EEnvTestFilterType :: Type >` | Does this test filter out results that are below a lower limit, above an upper limit, or both?  Or does it just look for a matching value? |
| BoolValue | [FAIDataProviderBoolValue](../../cppstruct/F/FA/FAIDataProviderBoolValue.md) | Desired boolean value of the test for scoring to occur or filtering test to pass. |
| FloatValueMin | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Minimum limit (inclusive) of valid values for the raw test value. Lower values will be discarded as invalid. |
| FloatValueMax | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Maximum limit (inclusive) of valid values for the raw test value. Higher values will be discarded as invalid. |
| ScoringEquation | `TEnumAsByte < EEnvTestScoreEquation :: Type >` | The shape of the curve equation to apply to the normalized score before multiplying by factor. |
| ClampMinType | `TEnumAsByte < EEnvQueryTestClamping :: Type >` | How should the lower bound for normalization of the raw test value before applying the scoring formula be determined?<br>	    Should it use the lowest value found (tested), the lower threshold for filtering, or a separate specified normalization minimum? |
| ClampMaxType | `TEnumAsByte < EEnvQueryTestClamping :: Type >` | How should the upper bound for normalization of the raw test value before applying the scoring formula be determined?<br>	    Should it use the highest value found (tested), the upper threshold for filtering, or a separate specified normalization maximum? |
| NormalizationType | [EEQSNormalizationType](../../cppenum/E/EE/EEQSNormalizationType.md) | Specifies how to determine value span used to normalize scores |
| ScoreClampMin | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Minimum value to use to normalize the raw test value before applying scoring formula. |
| ScoreClampMax | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Maximum value to use to normalize the raw test value before applying scoring formula. |
| ScoringFactor | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | The weight (factor) by which to multiply the normalized score after the scoring equation is applied. |
| ReferenceValue | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | When specified gets used to normalize test's results in such a way that the closer a value is to ReferenceValue<br>	 	the higher normalized result it will produce. Value farthest from ReferenceValue will be normalized<br>	 	to 0, and all the other values in between will get normalized linearly with the distance to ReferenceValue. |
| bDefineReferenceValue | `bool` | When set to true enables usage of ReferenceValue. It's false by default |
| bWorkOnFloatValues | `uint32` | When set, test operates on float values (e.g. distance, with AtLeast, UpTo conditions),<br>	   otherwise it will accept bool values (e.g. visibility, with Equals condition) |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
