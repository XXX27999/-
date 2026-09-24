# UKismetTextLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### Conv_VectorToText

Converts a vector value to localized formatted text, in the form 'X= Y= Z='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_Vector2dToText

Converts a vector2d value to localized formatted text, in the form 'X= Y='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_RotatorToText

Converts a rotator value to localized formatted text, in the form 'P= Y= R='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_TransformToText

Converts a transform value to localized formatted text, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTrans | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ObjectToText

Converts a UObject value to culture invariant text by calling the object's GetName method

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObj | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ColorToText

Converts a linear color value to localized formatted text, in the form '(R=,G=,B=,A=)'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_TextToString

Converts localizable text to the string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToText

Converts string to culture invariant text. Use Format or Make Literal Text to create localizable text

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_NameToText

Converts Name to culture invariant text

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### TextIsEmpty

Returns true if text is empty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextIsTransient

Returns true if text is transient.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextIsCultureInvariant

Returns true if text is culture invariant.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextToLower

Transforms the text to lowercase in a culture correct way.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextToUpper

Transforms the text to uppercase in a culture correct way.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextTrimPreceding

Removes whitespace characters from the front of the text.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextTrimTrailing

Removes trailing whitespace characters.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextTrimPrecedingAndTrailing

Removes whitespace characters from the front and end of the text.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### GetEmptyText

Returns an empty piece of text.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FindTextInLocalizationTable

Attempts to find existing Text using the representation found in the loc tables for the specified namespace and key.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Namespace | `FString &` |  |
| Key | `FString &` |  |
| OutText | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_TextText

Returns true if A and B are linguistically equal (A == B).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FText &` |  |
| B | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_IgnoreCase_TextText

Returns true if A and B are linguistically equal (A == B), ignoring case.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FText &` |  |
| B | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_TextText

Returns true if A and B are linguistically not equal (A != B).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FText &` |  |
| B | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_IgnoreCase_TextText

Returns true if A and B are linguistically not equal (A != B), ignoring case.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FText &` |  |
| B | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_BoolToText

Converts a boolean value to formatted text, either 'true' or 'false'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBool | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ByteToText

Converts a byte value to formatted text

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntToText

Converts a passed in integer to text based on formatting options

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |
| bUseGrouping | `bool` |  |
| MinimumIntegralDigits | `int32` |  |
| MaximumIntegralDigits | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Conv_FloatToText

Converts a passed in float to text based on formatting options

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| RoundingMode | `TEnumAsByte < ERoundingMode >` |  |
| bUseGrouping | `bool` |  |
| MinimumIntegralDigits | `int32` |  |
| MaximumIntegralDigits | `int32` |  |
| MinimumFractionalDigits | `int32` |  |
| MaximumFractionalDigits | `int32` |  |

**Return**

- Type: 
- Description: _None_

### AsCurrencyBase

Generate an FText that represents the passed number as currency in the current culture.
	  BaseVal is specified in the smallest fractional value of the currency and will be converted for formatting according to the selected culture.
	  Keep in mind the CurrencyCode is completely independent of the culture it's displayed in (and they do not imply one another).
	  For example: FText::AsCurrencyBase(650, TEXT("EUR")); would return an FText of "<EUR>6.50" in most English cultures (en_USen_UK) and "6,50<EUR>" in Spanish (es_ES) (where <EUR> is U+20AC)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BaseValue | `int32` |  |
| CurrencyCode | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### AsCurrency_Integer

Converts a passed in integer to a text formatted as a currency

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |
| RoundingMode | `TEnumAsByte < ERoundingMode >` |  |
| bUseGrouping | `bool` |  |
| MinimumIntegralDigits | `int32` |  |
| MaximumIntegralDigits | `int32` |  |
| MinimumFractionalDigits | `int32` |  |
| MaximumFractionalDigits | `int32` |  |
| CurrencyCode | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### AsCurrency_Float

Converts a passed in float to a text formatted as a currency

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| RoundingMode | `TEnumAsByte < ERoundingMode >` |  |
| bUseGrouping | `bool` |  |
| MinimumIntegralDigits | `int32` |  |
| MaximumIntegralDigits | `int32` |  |
| MinimumFractionalDigits | `int32` |  |
| MaximumFractionalDigits | `int32` |  |
| CurrencyCode | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### AsPercent_Float

Converts a passed in float to a text, formatted as a percent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| RoundingMode | `TEnumAsByte < ERoundingMode >` |  |
| bUseGrouping | `bool` |  |
| MinimumIntegralDigits | `int32` |  |
| MaximumIntegralDigits | `int32` |  |
| MinimumFractionalDigits | `int32` |  |
| MaximumFractionalDigits | `int32` |  |

**Return**

- Type: 
- Description: _None_

### AsDate_DateTime

Converts a passed in date & time to a text, formatted as a date using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDateTime | `FDateTime &` |  |

**Return**

- Type: 
- Description: _None_

### AsTimeZoneDate_DateTime

Converts a passed in date & time to a text, formatted as a date using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDateTime | `FDateTime &` |  |
| InTimeZone | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### AsDateTime_DateTime

Converts a passed in date & time to a text, formatted as a date & time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| In | `FDateTime &` |  |

**Return**

- Type: 
- Description: _None_

### AsTimeZoneDateTime_DateTime

Converts a passed in date & time to a text, formatted as a date & time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDateTime | `FDateTime &` |  |
| InTimeZone | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### AsTime_DateTime

Converts a passed in date & time to a text, formatted as a time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| In | `FDateTime &` |  |

**Return**

- Type: 
- Description: _None_

### AsTimeZoneTime_DateTime

Converts a passed in date & time to a text, formatted as a time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDateTime | `FDateTime &` |  |
| InTimeZone | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### AsTimespan_Timespan

Converts a passed in time span to a text, formatted as a time span

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTimespan | `FTimespan &` |  |

**Return**

- Type: 
- Description: _None_

### Format

Used for formatting text using the FText::Format function and utilized by the UK2Node_FormatText

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPattern | `FText` |  |
| InArgs | `TArray < FFormatArgumentData >` |  |

**Return**

- Type: 
- Description: _None_

### TextIsFromStringTable

Returns true if the given text is referencing a string table.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### TextFromStringTable

Attempts to create a text instance from a string table ID and key.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |
| Key | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### StringTableIdAndKeyFromText

Attempts to find the String Table ID and key used by the given text.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText` |  |
| OutTableId | `FName &` |  |
| OutKey | `FString &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
