# UKismetStringLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### Conv_FloatToString

Converts a float value to a string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFloat | `float` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntToString

Converts an integer value to a string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Conv_Int64ToString

Converts an integer64 value to a string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt64 | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Conv_UInt64ToString

Converts an uinteger64 value to a string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InUInt64 | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ByteToString

Converts a byte value to a string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InByte | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Conv_BoolToString

Converts a boolean value to a string, either 'true' or 'false'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBool | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToString

Converts a vector value to a string, in the form 'X= Y= Z='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntVectorToString

Converts an IntVector value to a string, in the form 'X= Y= Z='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIntVec | [FIntVector](../../cppstruct/F/FI/FIntVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_Vector2dToString

Converts a vector2d value to a string, in the form 'X= Y='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_RotatorToString

Converts a rotator value to a string, in the form 'P= Y= R='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_TransformToString

Converts a transform value to a string, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTrans | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ObjectToString

Converts a UObject value to a string by calling the object's GetName method

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObj | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ColorToString

Converts a linear color value to a string, in the form '(R=,G=,B=,A=)'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_DateTimeToString

Converts a date time value to a string, in the form '%Y.%m.%d-%H.%M.%S'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDateTime | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### Conv_NameToString

Converts a name value to a string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToName

Converts a string to a name value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToInt

Converts a string to a int value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToInt64

Converts a string to a int64 value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToFloat

Converts a string to a float value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToVector

Convert String Back To Vector. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |
| OutConvertedVector | `FVector &` |  |
| OutIsValid | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToVector2D

Convert String Back To Vector2D. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |
| OutConvertedVector2D | `FVector2D &` |  |
| OutIsValid | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToRotator

Convert String Back To Rotator. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |
| OutConvertedRotator | `FRotator &` |  |
| OutIsValid | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_StringToColor

Convert String Back To Color. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |
| OutConvertedColor | `FLinearColor &` |  |
| OutIsValid | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### BuildString_Float

Converts a float->string, create a new string in the form AppendTo+Prefix+InFloat+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InFloat | `float` | - The float value to convert |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Int

Converts a int->string, creating a new string in the form AppendTo+Prefix+InInt+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InInt | `int32` | - The int value to convert |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Int64

Converts a int->string, creating a new string in the form AppendTo+Prefix+InInt+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InInt64 | `int64` |  |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Bool

Converts a boolean->string, creating a new string in the form AppendTo+Prefix+InBool+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InBool | `bool` | - The bool value to convert. Will add "true" or "false" to the conversion string |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Vector

Converts a vector->string, creating a new string in the form AppendTo+Prefix+InVector+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InVector | `FVector` | - The vector value to convert. Uses the standard FVector::ToString conversion |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_IntVector

Converts an IntVector->string, creating a new string in the form AppendTo+Prefix+InIntVector+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InIntVector | `FIntVector` | - The intVector value to convert. Uses the standard FVector::ToString conversion |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Vector2d

Converts a vector2d->string, creating a new string in the form AppendTo+Prefix+InVector2d+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InVector2d | `FVector2D` | - The vector2d value to convert. Uses the standard FVector2D::ToString conversion |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Rotator

Converts a rotator->string, creating a new string in the form AppendTo+Prefix+InRot+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InRot | `FRotator` | - The rotator value to convert. Uses the standard ToString conversion |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Object

Converts a object->string, creating a new string in the form AppendTo+Prefix+object name+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InObj | `UObject *` | - The object to convert. Will insert the name of the object into the conversion string |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Color

Converts a color->string, creating a new string in the form AppendTo+Prefix+InColor+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InColor | `FLinearColor` | - The linear color value to convert. Uses the standard ToString conversion |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### BuildString_Name

Converts a color->string, creating a new string in the form AppendTo+Prefix+InName+Suffix

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AppendTo | `FString &` | - An existing string to use as the start of the conversion string |
| Prefix | `FString &` | - A string to use as a prefix, after the AppendTo string |
| InName | `FName` | - The name value to convert |
| Suffix | `FString &` | - A suffix to append to the end of the conversion string |

**Return**

- Type: 
- Description: _None_

### Concat_StrStr

Concatenates two strings together to make a new string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FString &` | - The original string |
| B | `FString &` | - The string to append to A |

**Return**

- Type: 
- Description: _None_

### EqualEqual_StrStr

Test if the input strings are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FString &` | - The string to compare against |
| B | `FString &` | - The string to compare |

**Return**

- Type: 
- Description: _None_

### EqualEqual_StriStri

Test if the input strings are equal (A == B), ignoring case

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FString &` | - The string to compare against |
| B | `FString &` | - The string to compare |

**Return**

- Type: 
- Description: _None_

### NotEqual_StrStr

Test if the input string are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FString &` | - The string to compare against |
| B | `FString &` | - The string to compare |

**Return**

- Type: 
- Description: _None_

### NotEqual_StriStri

Test if the input string are not equal (A != B), ignoring case differences

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FString &` | - The string to compare against |
| B | `FString &` | - The string to compare |

**Return**

- Type: 
- Description: _None_

### Len

Returns the number of characters in the string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| S | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetSubstring

Returns a substring from the string starting at the specified position

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | - The string to get the substring from |
| StartIndex | `int32` | - The location in SourceString to use as the start of the substring |
| Length | `int32` | The length of the requested substring |

**Return**

- Type: 
- Description: _None_

### FindSubstring

Finds the starting index of a substring in the a specified string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SearchIn | `FString &` | The string to search within |
| Substring | `FString &` | The string to look for in the SearchIn string |
| bUseCase | `bool` | Whether or not to be case-sensitive |
| bSearchFromEnd | `bool` | Whether or not to start the search from the end of the string instead of the beginning |
| StartPosition | `int32` | The position to start the search from |

**Return**

- Type: 
- Description: _None_

### Contains

Returns whether this string contains the specified substring.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SearchIn | `FString &` |  |
| Substring | `FString &` |  |
| bUseCase | `bool` |  |
| bSearchFromEnd | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetCharacterAsNumber

Gets a single character from the string (as an integer)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | - The string to convert |
| Index | `int32` | - Location of the character whose value is required |

**Return**

- Type: 
- Description: _None_

### ParseIntoArray

Gets an array of strings from a source string divided up by a separator and empty strings can optionally be culled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | - The string to chop up |
| Delimiter | `FString &` | - The string to delimit on |
| CullEmptyStrings | `bool` | = true - Cull (true) empty strings or add them to the array (false) |

**Return**

- Type: 
- Description: _None_

### JoinStringArray

Concatenates an array of strings into a single string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceArray | `TArray < FString > &` | - The array of strings to concatenate. |
| Separator | `FString &` | - The string used to separate each element. |

**Return**

- Type: 
- Description: _None_

### GetCharacterArrayFromString

Returns an array that contains one entry for each character in SourceString

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | The string to break apart into characters |

**Return**

- Type: 
- Description: _None_

### ToUpper

Returns a string converted to Upper case

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | The string to convert |

**Return**

- Type: 
- Description: _None_

### ToLower

Returns a string converted to Lower case

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | The string to convert |

**Return**

- Type: 
- Description: _None_

### LeftPad

Pad the left of this string for a specified number of characters

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | The string to pad |
| ChCount | `int32` | Amount of padding required |

**Return**

- Type: 
- Description: _None_

### RightPad

Pad the right of this string for a specified number of characters

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | The string to pad |
| ChCount | `int32` | Amount of padding required |

**Return**

- Type: 
- Description: _None_

### IsNumeric

Checks if a string contains only numeric characters

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` | The string to check |

**Return**

- Type: 
- Description: _None_

### StartsWith

Test whether this string starts with given string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| InPrefix | `FString &` |  |
| SearchCase | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Return**

- Type: 
- Description: _None_

### EndsWith

Test whether this string ends with given string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| InSuffix | `FString &` |  |
| SearchCase | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Return**

- Type: 
- Description: _None_

### MatchesWildcard

Searches this string for a given wild card

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| Wildcard | `FString &` | ?-type wildcard |
| SearchCase | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Return**

- Type: 
- Description: _None_

### Trim

Removes whitespace characters from the front of this string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### TrimTrailing

Removes trailing whitespace characters

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### CullArray

Takes an array of strings and removes any zero length entries.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| InArray | `TArray < FString > &` | The array to cull |

**Return**

- Type: 
- Description: _None_

### Reverse

Returns a copy of this string, with the characters in reverse order

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### Replace

Replace all occurrences of a substring in this string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| From | `FString &` | substring to replace |
| To | `FString &` | substring to replace From with |
| SearchCase | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Return**

- Type: 
- Description: _None_

### ReplaceInline

Replace all occurrences of SearchText with ReplacementText in this string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| SearchText | `FString &` | the text that should be removed from this string |
| ReplacementText | `FString &` | the text to insert in its place |
| SearchCase | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Return**

- Type: 
- Description: _None_

### Split

Splits this string at given string position case sensitive.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| InStr | `FString &` | The string to search and split at |
| LeftS | `FString &` | out the string to the left of InStr, not updated if return is false |
| RightS | `FString &` | out the string to the right of InStr, not updated if return is false |
| SearchCase | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |
| SearchDir | `ESearchDir :: Type` | Indicates whether the search starts at the begining or at the end ( defaults to ESearchDir::FromStart ) |

**Return**

- Type: 
- Description: _None_

### Left

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| Count | `int32` |  |

**Return**

- Type: 
- Description: _None_

### LeftChop

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| Count | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Right

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| Count | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RightChop

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| Count | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Mid

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceString | `FString &` |  |
| Start | `int32` |  |
| Count | `int32` |  |

**Return**

- Type: 
- Description: _None_

### TimeSecondsToString

Convert a number of seconds into minutes:seconds.milliseconds format string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### TimeSecondsToStringSec

Convert a number of seconds into minutes:seconds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
