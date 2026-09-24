# UKismetMathLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### RandomBool

Returns a uniformly distributed random bool

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RandomBoolWithWeight

Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
	 		Weight = .6 return value = True 60% of the time

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Weight | `float` |  |

**Return**

- Type: 
- Description: _None_

### RandomBoolWithWeightFromStream

Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
			Weight = .6 return value = True 60% of the time

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Weight | `float` |  |
| RandomStream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### Not_PreBool

Returns the logical complement of the Boolean value (NOT A)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_BoolBool

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |
| B | `bool` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_BoolBool

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |
| B | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BooleanAND

Returns the logical AND of two values (A AND B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |
| B | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BooleanNAND

Returns the logical NAND of two values (A AND B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |
| B | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BooleanOR

Returns the logical OR of two values (A OR B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |
| B | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BooleanXOR

Returns the logical eXclusive OR of two values (A XOR B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |
| B | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BooleanNOR

Returns the logical Not OR of two values (A NOR B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `bool` |  |
| B | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_ByteByte

Multiplication (A  B)
	UFUNCTION(BlueprintPure, meta=(DisplayName = "Byte  Byte", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Byte")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Divide_ByteByte

Division (A  B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Percent_ByteByte

Modulo (A % B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Add_ByteByte

Addition (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_ByteByte

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### BMin

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### BMax

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Less_ByteByte

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Greater_ByteByte

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### LessEqual_ByteByte

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### GreaterEqual_ByteByte

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_ByteByte

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_ByteByte

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint8` |  |
| B | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_IntInt

Multiplication (A  B)
	UFUNCTION(BlueprintPure, meta=(DisplayName = "integer  integer", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Integer")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Divide_IntInt

Division (A  B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Percent_IntInt

Modulo (A % B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Add_IntInt

Addition (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_IntInt

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Less_IntInt

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Greater_IntInt

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### LessEqual_IntInt

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GreaterEqual_IntInt

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_IntInt

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_IntInt

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### InRange_IntInt

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |
| Min | `int32` |  |
| Max | `int32` |  |
| InclusiveMin | `bool` |  |
| InclusiveMax | `bool` |  |

**Return**

- Type: 
- Description: _None_

### And_IntInt

Bitwise AND (A & B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Xor_IntInt

Bitwise XOR (A ^ B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Or_IntInt

Bitwise OR (A | B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Not_Int

Bitwise NOT (~A)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |

**Return**

- Type: 
- Description: _None_

### LeftShift_Int

Bitwise LeftShift (A << N)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| N | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RightShift_Int

Bitwise RightShift (A >> N)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| N | `int32` |  |

**Return**

- Type: 
- Description: _None_

### LeftShift_Int64

Bitwise LeftShift (A << N)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| N | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RightShift_Int64

Bitwise RightShift (A >> N)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| N | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SignOfInteger

Sign (integer, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RandomInteger

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RandomIntegerInRange

Return a random integer between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `int32` |  |
| Max | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Min

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Max

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Clamp

Returns Value clamped to be between A and B (inclusive)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | `int32` |  |
| A | `int32` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Abs_Int

Returns the absolute (positive) value of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_Int64Int64

Multiplication (A  B)
	UFUNCTION(BlueprintPure, meta=(DisplayName = "integer64  integer64", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Integer64")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Divide_Int64Int64

Division (A  B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Add_Int64Int64

Addition (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_Int64Int64

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Less_Int64Int64

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Greater_Int64Int64

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### LessEqual_Int64Int64

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### GreaterEqual_Int64Int64

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_Int64Int64

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_Int64Int64

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### InRange_Int64Int64

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int64` |  |
| Min | `int64` |  |
| Max | `int64` |  |
| InclusiveMin | `bool` |  |
| InclusiveMax | `bool` |  |

**Return**

- Type: 
- Description: _None_

### And_Int64Int64

Bitwise AND (A & B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Xor_Int64Int64

Bitwise XOR (A ^ B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Or_Int64Int64

Bitwise OR (A | B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Not_Int64

Bitwise NOT (~A)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |

**Return**

- Type: 
- Description: _None_

### SignOfInteger64

Sign (integer64, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |

**Return**

- Type: 
- Description: _None_

### RandomInteger64

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |

**Return**

- Type: 
- Description: _None_

### RandomInteger64InRange

Return a random integer64 between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `int64` |  |
| Max | `int64` |  |

**Return**

- Type: 
- Description: _None_

### MinInt64

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### MaxInt64

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### ClampInt64

Returns Value clamped to be between A and B (inclusive)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | `int64` |  |
| A | `int64` |  |
| B | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Abs_Int64

Returns the absolute (positive) value of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_UInt64UInt64

Multiplication (A  B)
	UFUNCTION(BlueprintPure, meta = (DisplayName = "uinteger64  uinteger64", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category = "Math|Integer64")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Divide_UInt64UInt64

Division (A  B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Add_UInt64UInt64

Addition (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_UInt64UInt64

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Less_UInt64UInt64

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Greater_UInt64UInt64

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### LessEqual_UInt64UInt64

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### GreaterEqual_UInt64UInt64

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_UInt64UInt64

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_UInt64UInt64

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### InRange_UInt64UInt64

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `uint64` |  |
| Min | `uint64` |  |
| Max | `uint64` |  |
| InclusiveMin | `bool` |  |
| InclusiveMax | `bool` |  |

**Return**

- Type: 
- Description: _None_

### And_UInt64UInt64

Bitwise AND (A & B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Xor_UInt64UInt64

Bitwise XOR (A ^ B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Or_UInt64UInt64

Bitwise OR (A | B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### Not_UInt64

Bitwise NOT (~A)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### RandomUInteger64

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### RandomUInteger64InRange

Return a random integer64 between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `uint64` |  |
| Max | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### MinUInt64

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### MaxUInt64

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### ClampUInt64

Returns Value clamped to be between A and B (inclusive)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | `uint64` |  |
| A | `uint64` |  |
| B | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### MultiplyMultiply_FloatFloat

Power (Base to the Exp-th power)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Base | `float` |  |
| Exp | `float` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_FloatFloat

Multiplication (A  B)
	UFUNCTION(BlueprintPure, meta=(DisplayName = "float  float", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Float")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_IntFloat

Multiplication (A  B)
	UFUNCTION(BlueprintPure, meta=(DisplayName = "int  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Float")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Divide_FloatFloat

Division (A  B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Percent_FloatFloat

Modulo (A % B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Fraction

Returns the fractional part of a float.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Add_FloatFloat

Addition (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_FloatFloat

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Less_FloatFloat

Returns true if A is Less than B (A < B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Greater_FloatFloat

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### LessEqual_FloatFloat

Returns true if A is Less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### GreaterEqual_FloatFloat

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_FloatFloat

Returns true if A is exactly equal to B (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### NearlyEqual_FloatFloat

Returns true if A is nearly equal to B (|A - B| < ErrorTolerance)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |
| ErrorTolerance | `float` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_FloatFloat

Returns true if A does not equal B (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### InRange_FloatFloat

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| Min | `float` |  |
| Max | `float` |  |
| InclusiveMin | `bool` |  |
| InclusiveMax | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Hypotenuse

Returns the hypotenuse of a right-angled triangle given the width and height.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Width | `float` |  |
| Height | `float` |  |

**Return**

- Type: 
- Description: _None_

### GridSnap_Float

Snaps a value to the nearest grid multiple. E.g.,
	 		Location = 5.1, GridSize = 10.0 : return value = 10.0
	  If GridSize is 0 Location is returned
	  if GridSize is very small precision issues may occur.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Location | `float` |  |
| GridSize | `float` |  |

**Return**

- Type: 
- Description: _None_

### Abs

Returns the absolute (positive) value of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Sin

Returns the sine of A (expects Radians)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Asin

Returns the inverse sine (arcsin) of A (result is in Radians)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Cos

Returns the cosine of A (expects Radians)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Acos

Returns the inverse cosine (arccos) of A (result is in Radians)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Tan

Returns the tan of A (expects Radians)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Atan

Returns the inverse tan (atan) (result is in Radians)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Atan2

Returns the inverse tan (atan2) of AB (result is in Radians)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Exp

Returns exponential(e) to the power A (e^A)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Log

Returns log of A base B (if B^R == A, returns R)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| Base | `float` |  |

**Return**

- Type: 
- Description: _None_

### Loge

Returns natural log of A (if e^R == A, returns R)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Sqrt

Returns square root of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### Square

Returns square of A (AA)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### RandomFloat

Returns a random float between 0 and 1

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RandomFloatInRange

Generate a random number between Min and Max

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `float` |  |
| Max | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetPI

Returns the value of PI

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTAU

Returns the value of TAU (= 2  PI)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DegreesToRadians

Returns radians value based on the input degrees

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### RadiansToDegrees

Returns degrees value based on the input radians

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### DegSin

Returns the sin of A (expects Degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### DegAsin

Returns the inverse sin (arcsin) of A (result is in Degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### DegCos

Returns the cos of A (expects Degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### DegAcos

Returns the inverse cos (arccos) of A (result is in Degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### DegTan

Returns the tan of A (expects Degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### DegAtan

Returns the inverse tan (atan) (result is in Degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### DegAtan2

Returns the inverse tan (atan2) of AB (result is in Degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClampAngle

Clamps an arbitrary angle to be between the given angles.  Will clamp to nearest boundary.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AngleDegrees | `float` |  |
| MinAngleDegrees | `float` | "from" angle that defines the beginning of the range of valid angles (sweeping clockwise) |
| MaxAngleDegrees | `float` | "to" angle that defines the end of the range of valid angles |

**Return**

- Type: 
- Description: _None_

### FMin

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### FMax

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### FClamp

Returns Value clamped between A and B (inclusive)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | `float` |  |
| A | `float` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### MaxOfIntArray

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IntArray | `TArray < int32 > &` |  |
| IndexOfMaxValue | `int32 &` |  |
| MaxValue | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### MinOfIntArray

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IntArray | `TArray < int32 > &` |  |
| IndexOfMinValue | `int32 &` |  |
| MinValue | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### MaxOfFloatArray

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FloatArray | `TArray < float > &` |  |
| IndexOfMaxValue | `int32 &` |  |
| MaxValue | `float &` |  |

**Return**

- Type: 
- Description: _None_

### MinOfFloatArray

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FloatArray | `TArray < float > &` |  |
| IndexOfMinValue | `int32 &` |  |
| MinValue | `float &` |  |

**Return**

- Type: 
- Description: _None_

### MaxOfByteArray

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ByteArray | `TArray < uint8 > &` |  |
| IndexOfMaxValue | `int32 &` |  |
| MaxValue | `uint8 &` |  |

**Return**

- Type: 
- Description: _None_

### MinOfByteArray

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ByteArray | `TArray < uint8 > &` |  |
| IndexOfMinValue | `int32 &` |  |
| MinValue | `uint8 &` |  |

**Return**

- Type: 
- Description: _None_

### Lerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |
| V | `float` |  |

**Return**

- Type: 
- Description: _None_

### InverseLerp

Returns the fraction (alpha) of the range B-A that corresponds to Value, e.g.,
		inputs A = 0, B = 8, Value = 3 : outputs Return Value = 38, indicating Value is 38 from A to B
		inputs A = 8, B = 0, Value = 3 : outputs Return Value = 58, indicating Value is 58 from A to B
	 Named InverseLerp because Lerp( A, B, InverseLerp(A, B, Value) ) == Value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` | The "from" value this float could be, usually but not necessarily a minimum. Returned as 0. |
| B | `float` | The "to" value this float could be, usually but not necessarily a maximum. Returned as 1. |
| Value | `float` | A value intended to be normalized relative to B-A |

**Return**

- Type: 
- Description: _None_

### Ease

Easeing  between A and B using a specified easing function

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |
| Alpha | `float` |  |
| EasingFunc | `TEnumAsByte < EEasingFunc :: Type >` |  |
| BlendExp | `float` |  |
| Steps | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Round

Rounds A to the nearest integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### FFloor

Rounds A to the largest previous integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### FTrunc

Rounds A to an integer with truncation towards zero.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### FTruncVector

Rounds A to an integer with truncation towards zero for each element in a vector.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVector | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### FCeil

Rounds A to the smallest following integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### FMod

Returns the number of times Divisor will go into Dividend (i.e., Dividend divided by Divisor), as well as the remainder

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Dividend | `float` |  |
| Divisor | `float` |  |
| Remainder | `float &` |  |

**Return**

- Type: 
- Description: _None_

### SignOfFloat

Sign (float, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### NormalizeToRange

Returns Value normalized to the given range.  (e.g. 20 normalized to the range 10->50 would result in 0.25)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| RangeMin | `float` |  |
| RangeMax | `float` |  |

**Return**

- Type: 
- Description: _None_

### MapRangeUnclamped

Returns Value mapped from one range into another.  (e.g. 20 normalized from the range 10->50 to 20->40 would result in 25)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| InRangeA | `float` |  |
| InRangeB | `float` |  |
| OutRangeA | `float` |  |
| OutRangeB | `float` |  |

**Return**

- Type: 
- Description: _None_

### MapRangeClamped

Returns Value mapped from one range into another where the Value is clamped to the Input Range.  (e.g. 0.5 normalized from the range 0->1 to 0->50 would result in 25)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| InRangeA | `float` |  |
| InRangeB | `float` |  |
| OutRangeA | `float` |  |
| OutRangeB | `float` |  |

**Return**

- Type: 
- Description: _None_

### MultiplyByPi

Multiplies the input value by pi.
	UFUNCTION(BlueprintPure, meta=(Keywords = " multiply"), Category="Math|Float")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### FInterpEaseInOut

Interpolate between A and B, applying an ease inout function.  Exp controls the degree of the curve.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |
| Alpha | `float` |  |
| Exponent | `float` |  |

**Return**

- Type: 
- Description: _None_

### MakePulsatingValue

Simple function to create a pulsating scalar value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCurrentTime | `float` | Current absolute time |
| InPulsesPerSecond | `float` | How many full pulses per second? |
| InPhase | `float` | Optional phase amount, between 0.0 and 1.0 (to synchronize pulses) |

**Return**

- Type: 
- Description: _None_

### FixedTurn

Returns a new rotation component value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCurrent | `float` | is the current rotation value |
| InDesired | `float` | is the desired rotation value |
| InDeltaRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_VectorFloat

Scales Vector A by B
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_VectorInt

Scales Vector A by B
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  int", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_VectorVector

UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  vector", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Vector")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Divide_VectorFloat

Vector divide by a float

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Divide_VectorInt

Vector divide by an integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Divide_VectorVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Add_VectorVector

Vector addition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Add_VectorFloat

Adds a float to each component of a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Add_VectorInt

Adds an integer to each component of a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_VectorVector

Vector subtraction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Subtract_VectorFloat

Subtracts a float from each component of a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_VectorInt

Subtracts an integer from each component of a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### LessLess_VectorRotator

Returns result of vector A rotated by the inverse of Rotator B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### GreaterGreater_VectorRotator

Returns result of vector A rotated by Rotator B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### RotateAngleAxis

Returns result of vector A rotated by AngleDeg around Axis

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVect | `FVector` |  |
| AngleDeg | `float` |  |
| Axis | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_VectorVector

Returns true if vector A is equal to vector B (A == B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `FVector` |  |
| ErrorTolerance | `float` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_VectorVector

Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `FVector` |  |
| ErrorTolerance | `float` |  |

**Return**

- Type: 
- Description: _None_

### Dot_VectorVector

Returns the dot product of two 3d vectors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Cross_VectorVector

Returns the cross product of two 3d vectors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### DotProduct2D

Returns the dot product of two 2d vectors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### CrossProduct2D

Returns the cross product of two 2d vectors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### VSize

Returns the length of the FVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### VSize2D

Returns the length of a 2d FVector.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### VSizeSquared

Returns the squared length of the FVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### VSize2DSquared

Returns the squared length of a 2d FVector.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### Normal

Returns a unit normal version of the FVector A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Normal2D

Returns a unit normal version of the vector2d A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### VLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `FVector` |  |
| V | `float` |  |

**Return**

- Type: 
- Description: _None_

### VEase

Easeing  between A and B using a specified easing function

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `FVector` |  |
| Alpha | `float` |  |
| EasingFunc | `TEnumAsByte < EEasingFunc :: Type >` |  |
| BlendExp | `float` |  |
| Steps | `int32` |  |

**Return**

- Type: 
- Description: _None_

### VContainsNan

Returns true if the vector contains NAN

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### RandomUnitVector

Returns a random vector with length of 1

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RandomPointInBoundingBox

Returns a random point within the specified bounding box

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | `FVector &` |  |
| BoxExtent | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInConeInRadians

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector` | The base "center" direction of the cone. |
| ConeHalfAngleInRadians | `float` | The half-angle of the cone (from ConeDir to edge), in radians. |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInConeInDegrees

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector` | The base "center" direction of the cone. |
| ConeHalfAngleInDegrees | `float` | The half-angle of the cone (from ConeDir to edge), in degrees. |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInEllipticalConeInRadians

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector` |  |
| MaxYawInRadians | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in radians. |
| MaxPitchInRadians | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in radians. |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInEllipticalConeInDegrees

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector` |  |
| MaxYawInDegrees | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in degrees. |
| MaxPitchInDegrees | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in degrees. |

**Return**

- Type: 
- Description: _None_

### MirrorVectorByNormal

Mirrors a vector by a normal

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### ProjectVectorOnToVector

Projects one vector (V) onto another (Target) and returns the projected vector.
	 If Target is nearly zero in length, returns the zero vector.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | `FVector` | Vector to project. |
| Target | [FVector](../../cppstruct/F/FV/FVector.md) | Vector on which we are projecting. |

**Return**

- Type: 
- Description: _None_

### GetReflectionVector

Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
	  Produces a result like shining a laser at a mirror!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Direction | `FVector` | Direction vector the ray is coming from. |
| SurfaceNormal | [FVector](../../cppstruct/F/FV/FVector.md) | A normal of the surface the ray should be reflected on. |

**Return**

- Type: 
- Description: _None_

### FindNearestPointsOnLineSegments

Find closest points between 2 segments.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Segment1Start | `FVector` | Start of the 1st segment. |
| Segment1End | `FVector` | End of the 1st segment. |
| Segment2Start | `FVector` | Start of the 2nd segment. |
| Segment2End | `FVector` | End of the 2nd segment. |
| Segment1Point | `FVector &` | Closest point on segment 1 to segment 2. |
| Segment2Point | `FVector &` | Closest point on segment 2 to segment 1. |

**Return**

- Type: 
- Description: _None_

### FindClosestPointOnSegment

Find the closest point on a segment to a given point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point for which we find the closest point on the segment. |
| SegmentStart | `FVector` | Start of the segment. |
| SegmentEnd | [FVector](../../cppstruct/F/FV/FVector.md) | End of the segment. |

**Return**

- Type: 
- Description: _None_

### FindClosestPointOnLine

Find the closest point on an infinite line to a given point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point for which we find the closest point on the line. |
| LineOrigin | `FVector` | Point of reference on the line. |
| LineDirection | [FVector](../../cppstruct/F/FV/FVector.md) | Direction of the line. Not required to be normalized. |

**Return**

- Type: 
- Description: _None_

### GetPointDistanceToSegment

Find the distance from a point to the closest point on a segment.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point for which we find the distance to the closest point on the segment. |
| SegmentStart | `FVector` | Start of the segment. |
| SegmentEnd | [FVector](../../cppstruct/F/FV/FVector.md) | End of the segment. |

**Return**

- Type: 
- Description: _None_

### GetPointDistanceToLine

Find the distance from a point to the closest point on an infinite line.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point for which we find the distance to the closest point on the line. |
| LineOrigin | `FVector` | Point of reference on the line. |
| LineDirection | [FVector](../../cppstruct/F/FV/FVector.md) | Direction of the line. Not required to be normalized. |

**Return**

- Type: 
- Description: _None_

### ProjectPointOnToPlane

Projects a point onto a plane defined by a point on the plane and a plane normal.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point to project onto the plane. |
| PlaneBase | `FVector` | A point on the plane. |
| PlaneNormal | [FVector](../../cppstruct/F/FV/FVector.md) | Normal of the plane. |

**Return**

- Type: 
- Description: _None_

### ProjectVectorOnToPlane

Projects a vector onto a plane defined by a normalized vector (PlaneNormal).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| V | `FVector` | Vector to project onto the plane. |
| PlaneNormal | [FVector](../../cppstruct/F/FV/FVector.md) | Normal of the plane. |

**Return**

- Type: 
- Description: _None_

### NegateVector

Negate a vector.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### ClampVectorSize

Clamp the vector size between a min and max length

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| Min | `float` |  |
| Max | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetMinElement

Find the minimum element (X, Y or Z) of a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GetMaxElement

Find the maximum element (X, Y or Z) of a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GetVectorArrayAverage

Find the average of an array of vectors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vectors | `TArray < FVector > &` |  |

**Return**

- Type: 
- Description: _None_

### GetDirectionUnitVector

Find the unit direction vector from one position to another.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| From | `FVector` |  |
| To | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_RotatorRotator

Returns true if rotator A is equal to rotator B (A == B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | `FRotator` |  |
| ErrorTolerance | `float` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_RotatorRotator

Returns true if rotator A is not equal to rotator B (A != B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | `FRotator` |  |
| ErrorTolerance | `float` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_RotatorFloat

Returns rotator representing rotator A scaled by B
	UFUNCTION(BlueprintPure, meta=(DisplayName = "ScaleRotator", CompactNodeTitle = "", Keywords = " multiply rotate rotation"), Category="Math|Rotator")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_RotatorInt

Returns rotator representing rotator A scaled by B
	UFUNCTION(BlueprintPure, meta=(DisplayName = "ScaleRotator (int)", CompactNodeTitle = "", Keywords = " multiply rotate rotation"), Category="Math|Rotator")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ComposeRotators

Combine 2 rotations to give you the resulting rotation of first applying A, then B.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### NegateRotator

Negate a rotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### NormalRotator

Negate a rotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### GetAxes

Get the reference frame direction vectors (axes) described by this rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| X | `FVector &` |  |
| Y | `FVector &` |  |
| Z | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### RandomRotator

Generates a random rotation, with optional random roll.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bRoll | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | `FRotator` |  |
| Alpha | `float` |  |
| bShortestPath | `bool` |  |

**Return**

- Type: 
- Description: _None_

### REase

Easeing  between A and B using a specified easing function

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | `FRotator` |  |
| Alpha | `float` |  |
| bShortestPath | `bool` |  |
| EasingFunc | `TEnumAsByte < EEasingFunc :: Type >` |  |
| BlendExp | `float` |  |
| Steps | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RContainsNan

Returns true if the rotation contains NAN

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### NormalizedDeltaRotator

Normalized A-B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### RotatorFromAxisAndAngle

Create a rotation from an axis and and angle (in degrees)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Axis | `FVector` |  |
| Angle | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClampAxis

Clamps an angle to the range of [0, 360].

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Angle | `float` | The angle to clamp. |

**Return**

- Type: 
- Description: _None_

### NormalizeAxis

Clamps an angle to the range of [-180, 180].

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Angle | `float` | The Angle to clamp. |

**Return**

- Type: 
- Description: _None_

### LinearColorLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FLinearColor` |  |
| B | `FLinearColor` |  |
| Alpha | `float` |  |

**Return**

- Type: 
- Description: _None_

### LinearColorLerpUsingHSV

Linearly interpolates between two colors by the specified Alpha amount (100% of A when Alpha=0 and 100% of B when Alpha=1).  The interpolation is performed in HSV color space taking the shortest path to the new color's hue.  This can give better results than a normal lerp, but is much more expensive.  The incoming colors are in RGB space, and the output color will be RGB.  The alpha value will also be interpolated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FLinearColor` | The color and alpha to interpolate from as linear RGBA |
| B | `FLinearColor` | The color and alpha to interpolate to as linear RGBA |
| Alpha | `float` | Scalar interpolation amount (usually between 0.0 and 1.0 inclusive) |

**Return**

- Type: 
- Description: _None_

### Multiply_LinearColorLinearColor

Element-wise multiplication of two linear colors (RR, GG, BB, AA)
	UFUNCTION(BlueprintPure, meta=(DisplayName = "LinearColor  (LinearColor)", CompactNodeTitle = ""), Category="Math|Color")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FLinearColor` |  |
| B | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### Multiply_LinearColorFloat

Element-wise multiplication of a linear color by a float (FR, FG, FB, FA)
	UFUNCTION(BlueprintPure, meta=(DisplayName = "LinearColor  Float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Color")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FLinearColor` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### MakePlaneFromPointAndNormal

Creates a plane with a facing direction of Normal at the given Point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | A point on the plane |
| Normal | [FVector](../../cppstruct/F/FV/FVector.md) | The Normal of the plane at Point |

**Return**

- Type: 
- Description: _None_

### MakeDateTime

Makes a DateTime struct

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Year | `int32` |  |
| Month | `int32` |  |
| Day | `int32` |  |
| Hour | `int32` |  |
| Minute | `int32` |  |
| Second | `int32` |  |
| Millisecond | `int32` |  |

**Return**

- Type: 
- Description: _None_

### MakeDateTimeFromString

Makes a DateTime struct

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### BreakDateTime

Breaks a DateTime into its components

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDateTime | `FDateTime` |  |
| Year | `int32 &` |  |
| Month | `int32 &` |  |
| Day | `int32 &` |  |
| Hour | `int32 &` |  |
| Minute | `int32 &` |  |
| Second | `int32 &` |  |
| Millisecond | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### Add_DateTimeTimespan

Addition (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_DateTimeTimespan

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_DateTimeDateTime

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_DateTimeDateTime

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_DateTimeDateTime

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### Greater_DateTimeDateTime

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GreaterEqual_DateTimeDateTime

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### Less_DateTimeDateTime

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### LessEqual_DateTimeDateTime

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |
| B | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetDate

Returns the date component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetDay

Returns the day component of A (1 to 31)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetDayOfYear

Returns the day of year of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetHour

Returns the hour component of A (24h format)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetHour12

Returns the hour component of A (12h format)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetMillisecond

Returns the millisecond component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetMinute

Returns the minute component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetMonth

Returns the month component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetSecond

Returns the second component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetTimeOfDay

Returns the time elapsed since midnight of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### GetYear

Returns the year component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### IsAfternoon

Returns whether A's time is in the afternoon

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### IsMorning

Returns whether A's time is in the morning

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FDateTime` |  |

**Return**

- Type: 
- Description: _None_

### DaysInMonth

Returns the number of days in the given year and month

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Year | `int32` |  |
| Month | `int32` |  |

**Return**

- Type: 
- Description: _None_

### DaysInYear

Returns the number of days in the given year

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Year | `int32` |  |

**Return**

- Type: 
- Description: _None_

### IsLeapYear

Returns whether given year is a leap year

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Year | `int32` |  |

**Return**

- Type: 
- Description: _None_

### DateTimeMaxValue

Returns the maximum date and time value

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DateTimeMinValue

Returns the minimum date and time value

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Now

Returns the local date and time on this computer

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Today

Returns the local date on this computer

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UtcNow

Returns the UTC date and time on this computer

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DateTimeFromIsoString

Converts a date string in ISO-8601 format to a DateTime object

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsoString | `FString` |  |
| Result | `FDateTime &` |  |

**Return**

- Type: 
- Description: _None_

### DateTimeFromString

Converts a date string to a DateTime object

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DateTimeString | `FString` |  |
| Result | `FDateTime &` |  |

**Return**

- Type: 
- Description: _None_

### MakeTimespan

Makes a Timespan struct

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Days | `int32` |  |
| Hours | `int32` |  |
| Minutes | `int32` |  |
| Seconds | `int32` |  |
| Milliseconds | `int32` |  |

**Return**

- Type: 
- Description: _None_

### MakeTimespan2

Makes a Timespan struct

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Days | `int32` |  |
| Hours | `int32` |  |
| Minutes | `int32` |  |
| Seconds | `int32` |  |
| FractionNano | `int32` |  |

**Return**

- Type: 
- Description: _None_

### BreakTimespan

Breaks a Timespan into its components

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTimespan | `FTimespan` |  |
| Days | `int32 &` |  |
| Hours | `int32 &` |  |
| Minutes | `int32 &` |  |
| Seconds | `int32 &` |  |
| Milliseconds | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### BreakTimespan2

Breaks a Timespan into its components

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTimespan | `FTimespan` |  |
| Days | `int32 &` |  |
| Hours | `int32 &` |  |
| Minutes | `int32 &` |  |
| Seconds | `int32 &` |  |
| FractionNano | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### Add_TimespanTimespan

Addition (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_TimespanTimespan

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_TimespanFloat

Scalar multiplication (A  s)
	UFUNCTION(BlueprintPure, meta=(DisplayName="Timespan  float", CompactNodeTitle="", Keywords=" multiply"), Category="Math|Timespan")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| Scalar | `float` |  |

**Return**

- Type: 
- Description: _None_

### Divide_TimespanFloat

Scalar division (A  s)
	UFUNCTION(BlueprintPure, meta=(DisplayName="Timespan  float", CompactNodeTitle="", Keywords=" divide"), Category="Math|Timespan")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| Scalar | `float` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_TimespanTimespan

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_TimespanTimespan

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### Greater_TimespanTimespan

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GreaterEqual_TimespanTimespan

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### Less_TimespanTimespan

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### LessEqual_TimespanTimespan

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetDays

Returns the days component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetDuration

Returns the absolute value of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetHours

Returns the hours component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetMilliseconds

Returns the milliseconds component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetMinutes

Returns the minutes component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetSeconds

Returns the seconds component of A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetTotalDays

Returns the total number of days in A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetTotalHours

Returns the total number of hours in A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetTotalMilliseconds

Returns the total number of milliseconds in A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetTotalMinutes

Returns the total number of minutes in A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### GetTotalSeconds

Returns the total number of seconds in A

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### FromDays

Returns a time span that represents the specified number of days

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Days | `float` |  |

**Return**

- Type: 
- Description: _None_

### FromHours

Returns a time span that represents the specified number of hours

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hours | `float` |  |

**Return**

- Type: 
- Description: _None_

### FromMilliseconds

Returns a time span that represents the specified number of milliseconds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Milliseconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### FromMinutes

Returns a time span that represents the specified number of minutes

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Minutes | `float` |  |

**Return**

- Type: 
- Description: _None_

### FromSeconds

Returns a time span that represents the specified number of seconds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Seconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### TimespanMaxValue

Returns the maximum time span value

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TimespanMinValue

Returns the minimum time span value

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TimespanRatio

Returns the ratio between two time spans (A  B), handles zero values

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTimespan` |  |
| B | `FTimespan` |  |

**Return**

- Type: 
- Description: _None_

### TimespanZeroValue

Returns a zero time span value

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TimespanFromString

Converts a time span string to a Timespan object

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimespanString | `FString` |  |
| Result | `FTimespan &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ByteToFloat

Converts a byte to a float

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InByte | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntToFloat

Converts an integer to a float

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntToInt64

Converts an integer to a 64 bit integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Conv_Int64ToInt

Converts an 64 bit integer to a 32 bit integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt | `int64` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntToByte

Converts an integer to a byte (if the integer is too large, returns the low 8 bits)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntToIntVector

Converts an integer to an IntVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntToBool

Converts a int to a bool

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInt | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Conv_BoolToInt

Converts a bool to an int

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBool | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Conv_BoolToFloat

Converts a bool to a float (0.0f or 1.0f)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBool | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Conv_BoolToByte

Converts a bool to a byte

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBool | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ByteToInt

Converts a byte to an integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InByte | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToLinearColor

Converts a vector to LinearColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_LinearColorToVector

Converts a LinearColor to a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLinearColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_ColorToLinearColor

Converts a color to LinearColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | [FColor](../../cppstruct/F/FC/FColor.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_LinearColorToColor

Converts a LinearColor to a color

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLinearColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToTransform

Convert a vector to a transform. Uses vector as location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTranslation | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToVector2D

Convert a Vector to a Vector2D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_Vector2DToVector

Convert a Vector2D to a Vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec2D | `FVector2D` |  |
| Z | `float` |  |

**Return**

- Type: 
- Description: _None_

### Conv_IntVectorToVector

Convert an IntVector to a vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIntVector | `FIntVector &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_FloatToVector

Convert a float into a vector, where each element is that float

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFloat | `float` |  |

**Return**

- Type: 
- Description: _None_

### Conv_FloatToLinearColor

Convert a float into a LinearColor, where each element is that float

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFloat | `float` |  |

**Return**

- Type: 
- Description: _None_

### MakeBox

Makes an FBox from Min and Max and sets IsValid to true

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `FVector` |  |
| Max | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### MakeBox2D

Makes an FBox2D from Min and Max and sets IsValid to true

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `FVector2D` |  |
| Max | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### MakeVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `float` |  |
| Y | `float` |  |
| Z | `float` |  |

**Return**

- Type: 
- Description: _None_

### BreakVector

Breaks a vector apart into X, Y, Z

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | `FVector` |  |
| X | `float &` |  |
| Y | `float &` |  |
| Z | `float &` |  |

**Return**

- Type: 
- Description: _None_

### MakeVector2D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `float` |  |
| Y | `float` |  |

**Return**

- Type: 
- Description: _None_

### BreakVector2D

Breaks a 2D vector apart into X, Y.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | `FVector2D` |  |
| X | `float &` |  |
| Y | `float &` |  |

**Return**

- Type: 
- Description: _None_

### GetForwardVector

Rotate the world forward vector by the given rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### GetRightVector

Rotate the world right vector by the given rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### GetUpVector

Rotate the world up vector by the given rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### CreateVectorFromYawPitch

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Yaw | `float` |  |
| Pitch | `float` |  |
| Length | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetYawPitchFromVector

Breaks a vector apart into Yaw, Pitch rotation values given in degrees. (non-clamped)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | `FVector` |  |
| Yaw | `float &` |  |
| Pitch | `float &` |  |

**Return**

- Type: 
- Description: _None_

### GetAzimuthAndElevation

Breaks a direction vector apart into Azimuth (Yaw) and Elevation (Pitch) rotation values given in degrees. (non-clamped)
	 Relative to the provided reference frame (an Actor's WorldTransform for example)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDirection | `FVector` |  |
| ReferenceFrame | `FTransform &` |  |
| Azimuth | `float &` |  |
| Elevation | `float &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Roll | `float` |  |
| Pitch | `float` |  |
| Yaw | `float` |  |

**Return**

- Type: 
- Description: _None_

### FindLookAtRotation

Find a rotation for an object at Start location to point at Target location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | `FVector &` |  |
| Target | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromX

Builds a rotator given only a XAxis. Y and Z are unspecified but will be orthonormal. XAxis need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromY

Builds a rotation matrix given only a YAxis. X and Z are unspecified but will be orthonormal. YAxis need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Y | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromZ

Builds a rotation matrix given only a ZAxis. X and Y are unspecified but will be orthonormal. ZAxis need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Z | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromXY

Builds a matrix with given X and Y axes. X will remain fixed, Y may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `FVector &` |  |
| Y | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromXZ

Builds a matrix with given X and Z axes. X will remain fixed, Z may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `FVector &` |  |
| Z | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromYX

Builds a matrix with given Y and X axes. Y will remain fixed, X may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Y | `FVector &` |  |
| X | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromYZ

Builds a matrix with given Y and Z axes. Y will remain fixed, Z may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Y | `FVector &` |  |
| Z | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromZX

Builds a matrix with given Z and X axes. Z will remain fixed, X may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Z | `FVector &` |  |
| X | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotFromZY

Builds a matrix with given Z and Y axes. Z will remain fixed, Y may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Z | `FVector &` |  |
| Y | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### BreakRotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | `FRotator` |  |
| Roll | `float &` |  |
| Pitch | `float &` |  |
| Yaw | `float &` |  |

**Return**

- Type: 
- Description: _None_

### BreakRotIntoAxes

Breaks apart a rotator into its component axes

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | `FRotator &` |  |
| X | `FVector &` |  |
| Y | `FVector &` |  |
| Z | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeTransform

Make a transform from location, rotation and scale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Translation | `FVector` |  |
| Rotation | `FRotator` |  |
| Scale | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### BreakTransform

Breaks apart a transform into location, rotation and scale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTransform | `FTransform &` |  |
| Translation | `FVector &` |  |
| Rotation | `FRotator &` |  |
| Scale | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### MakeRandomStream

Makes a SRand-based random number generator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InitialSeed | `int32` |  |

**Return**

- Type: 
- Description: _None_

### BreakRandomStream

Breaks apart a random number generator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRandomStream | `FRandomStream &` |  |
| InitialSeed | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### MakeColor

Make a color from individual color components (RGB space)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| R | `float` |  |
| G | `float` |  |
| B | `float` |  |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### BreakColor

Breaks apart a color into individual RGB components (as well as alpha)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | `FLinearColor` |  |
| R | `float &` |  |
| G | `float &` |  |
| B | `float &` |  |
| A | `float &` |  |

**Return**

- Type: 
- Description: _None_

### HSVToRGB

Make a color from individual color components (HSV space)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| H | `float` |  |
| S | `float` |  |
| V | `float` |  |
| A | `float` |  |

**Return**

- Type: 
- Description: _None_

### RGBToHSV

Breaks apart a color into individual HSV components (as well as alpha)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | `FLinearColor` |  |
| H | `float &` |  |
| S | `float &` |  |
| V | `float &` |  |
| A | `float &` |  |

**Return**

- Type: 
- Description: _None_

### HSVToRGB_Vector

Converts a HSV linear color (where H is in R, S is in G, and V is in B) to RGB

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HSV | `FLinearColor` |  |
| RGB | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### RGBToHSV_Vector

Converts a RGB linear color to HSV (where H is in R, S is in G, and V is in B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RGB | `FLinearColor` |  |
| HSV | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### HexToRGB_Vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HexString | `FString` |  |
| bSRGB | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RGB_VectorToHex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RGB | `FLinearColor` |  |
| bSRGB | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectString

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FString &` |  |
| B | `FString &` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectInt

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `int32` |  |
| B | `int32` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectFloat

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `float` |  |
| B | `float` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectVector

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector` |  |
| B | `FVector` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectRotator

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FRotator` |  |
| B | `FRotator` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectColor

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FLinearColor` |  |
| B | `FLinearColor` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectTransform

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTransform &` |  |
| B | `FTransform &` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectObject

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `UObject *` |  |
| B | `UObject *` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SelectClass

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `UClass *` |  |
| B | `UClass *` |  |
| bSelectA | `bool` |  |

**Return**

- Type: 
- Description: _None_

### MakeRotationFromAxes

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Forward | `FVector` |  |
| Right | `FVector` |  |
| Up | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_VectorToRotator

Create a rotator which orients X along the supplied direction vector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVec | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_RotatorToVector

Get the X direction vector after this rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_ObjectObject

Returns true if A and B are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `UObject *` |  |
| B | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_ObjectObject

Returns true if A and B are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `UObject *` |  |
| B | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_ClassClass

Returns true if A and B are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `UClass *` |  |
| B | `UClass *` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_ClassClass

Returns true if A and B are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `UClass *` |  |
| B | `UClass *` |  |

**Return**

- Type: 
- Description: _None_

### ClassIsChildOf

Determine if a class is a child of another class.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TestClass | `TSubclassOf < UObject >` |  |
| ParentClass | `TSubclassOf < UObject >` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_NameName

Returns true if A and B are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FName` |  |
| B | `FName` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_NameName

Returns true if A and B are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FName` |  |
| B | `FName` |  |

**Return**

- Type: 
- Description: _None_

### TransformLocation

Transform a position by the supplied transform.
	 	For example, if T was an object's transform, this would transform a position from local space to world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | `FTransform &` |  |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### TransformDirection

Transform a direction vector by the supplied transform - will not change its length.
	 	For example, if T was an object's transform, this would transform a direction from local space to world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | `FTransform &` |  |
| Direction | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### TransformRotation

Transform a rotator by the supplied transform.
	 	For example, if T was an object's transform, this would transform a rotation from local space to world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | `FTransform &` |  |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### InverseTransformLocation

Transform a position by the inverse of the supplied transform.
	 	For example, if T was an object's transform, this would transform a position from world space to local space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | `FTransform &` |  |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### InverseTransformDirection

Transform a direction vector by the inverse of the supplied transform - will not change its length.
	 	For example, if T was an object's transform, this would transform a direction from world space to local space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | `FTransform &` |  |
| Direction | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### InverseTransformRotation

Transform a rotator by the inverse of the supplied transform.
	 	For example, if T was an object's transform, this would transform a rotation from world space to local space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | `FTransform &` |  |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### ComposeTransforms

Compose two transforms in order: A  B.

	  Order matters when composing transforms:
	  A  B will yield a transform that logically first applies A then B to any subsequent transformation.

	  Example: LocalToWorld = ComposeTransforms(DeltaRotation, LocalToWorld) will change rotation in local space by DeltaRotation.
	  Example: LocalToWorld = ComposeTransforms(LocalToWorld, DeltaRotation) will change rotation in world space by DeltaRotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTransform &` |  |
| B | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### ConvertTransformToRelative

Returns the given transform, converted to be relative to the given ParentTransform.

	  Example: AToB = ConvertTransformToRelative(AToWorld, BToWorld) to compute A relative to B.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Transform | `FTransform &` | The transform you wish to convert |
| ParentTransform | `FTransform &` | The transform the conversion is relative to (in the same space as Transform) |

**Return**

- Type: 
- Description: _None_

### InvertTransform

Returns the inverse of the given transform T.

	  Example: Given a LocalToWorld transform, WorldToLocal will be returned.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| T | `FTransform &` | The transform you wish to invert |

**Return**

- Type: 
- Description: _None_

### TLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTransform &` |  |
| B | `FTransform &` |  |
| Alpha | `float` |  |
| InterpMode | `TEnumAsByte < ELerpInterpolationMode :: Type >` |  |

**Return**

- Type: 
- Description: _None_

### TEase

Ease between A and B using a specified easing function.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTransform &` |  |
| B | `FTransform &` |  |
| Alpha | `float` |  |
| EasingFunc | `TEnumAsByte < EEasingFunc :: Type >` |  |
| BlendExp | `float` |  |
| Steps | `int32` |  |

**Return**

- Type: 
- Description: _None_

### TInterpTo

Tries to reach a target transform.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FTransform &` |  |
| Target | `FTransform &` |  |
| DeltaTime | `float` |  |
| InterpSpeed | `float` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_TransformTransform

Returns true if transform A is equal to transform B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTransform &` |  |
| B | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### NearlyEqual_TransformTransform

Returns true if transform A is nearly equal to B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FTransform &` |  |
| B | `FTransform &` |  |
| LocationTolerance | `float` | How close position of transforms need to be to be considered equal |
| RotationTolerance | `float` | How close rotations of transforms need to be to be considered equal |
| Scale3DTolerance | `float` | How close scale of transforms need to be to be considered equal |

**Return**

- Type: 
- Description: _None_

### Add_Vector2DVector2D

Returns addition of Vector A and Vector B (A + B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### Subtract_Vector2DVector2D

Returns subtraction of Vector B from Vector A (A - B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### Multiply_Vector2DFloat

Returns Vector A scaled by B
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector2d  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector2D")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Multiply_Vector2DVector2D

UFUNCTION(BlueprintPure, meta = (DisplayName = "vector2d  vector2d", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category = "Math|Vector2D")

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### Divide_Vector2DFloat

Returns Vector A divided by B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Divide_Vector2DVector2D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### Add_Vector2DFloat

Returns Vector A added by B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### Subtract_Vector2DFloat

Returns Vector A subtracted by B

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | `float` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_Vector2DVector2D

Returns true if vector2D A is equal to vector2D B (A == B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | `FVector2D` |  |
| ErrorTolerance | `float` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_Vector2DVector2D

Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FVector2D` |  |
| B | `FVector2D` |  |
| ErrorTolerance | `float` |  |

**Return**

- Type: 
- Description: _None_

### FInterpTo

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `float` | Actual position |
| Target | `float` | Target position |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### FInterpTo_Constant

Tries to reach Target at a constant rate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `float` | Actual position |
| Target | `float` | Target position |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### VInterpTo

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FVector` | Actual position |
| Target | `FVector` | Target position |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### VInterpTo_Constant

Tries to reach Target at a constant rate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FVector` | Actual position |
| Target | `FVector` | Target position |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### Vector2DInterpTo

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FVector2D` | Actual position |
| Target | `FVector2D` | Target position |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### Vector2DInterpTo_Constant

Tries to reach Target at a constant rate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FVector2D` | Actual position |
| Target | `FVector2D` | Target position |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### RInterpTo

Tries to reach Target rotation based on Current rotation, giving a nice smooth feeling when rotating to Target rotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FRotator` | Actual rotation |
| Target | `FRotator` | Target rotation |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### RInterpTo_Constant

Tries to reach Target rotation at a constant rate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FRotator` | Actual rotation |
| Target | `FRotator` | Target rotation |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### CInterpTo

Interpolates towards a varying target color smoothly.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FLinearColor` | Current Color |
| Target | `FLinearColor` | Target Color |
| DeltaTime | `float` | Time since last tick |
| InterpSpeed | `float` | Interpolation speed |

**Return**

- Type: 
- Description: _None_

### FloatSpringInterp

Uses a simple spring model to interpolate a float from Current to Target.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `float` | Current value |
| Target | `float` | Target value |
| SpringState | `FFloatSpringState &` | Data related to spring model (velocity, error, etc..) - Create a unique variable per spring |
| Stiffness | `float` | How stiff the spring model is (more stiffness means more oscillation around the target value) |
| CriticalDampingFactor | `float` | How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation) |
| DeltaTime | `float` |  |
| Mass | `float` | Multiplier that acts like mass on a spring |

**Return**

- Type: 
- Description: _None_

### VectorSpringInterp

Uses a simple spring model to interpolate a vector from Current to Target.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Current | `FVector` | Current value |
| Target | `FVector` | Target value |
| SpringState | `FVectorSpringState &` | Data related to spring model (velocity, error, etc..) - Create a unique variable per spring |
| Stiffness | `float` | How stiff the spring model is (more stiffness means more oscillation around the target value) |
| CriticalDampingFactor | `float` | How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation) |
| DeltaTime | `float` |  |
| Mass | `float` | Multiplier that acts like mass on a spring |

**Return**

- Type: 
- Description: _None_

### ResetFloatSpringState

Resets the state of a given spring

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SpringState | `FFloatSpringState &` |  |

**Return**

- Type: 
- Description: _None_

### ResetVectorSpringState

Resets the state of a given spring

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SpringState | `FVectorSpringState &` |  |

**Return**

- Type: 
- Description: _None_

### RandomIntegerFromStream

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Max | `int32` |  |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### RandomIntegerInRangeFromStream

Return a random integer between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `int32` |  |
| Max | `int32` |  |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### RandomBoolFromStream

Returns a random bool

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### RandomFloatFromStream

Returns a random float between 0 and 1

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### RandomFloatInRangeFromStream

Generate a random number between Min and Max

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `float` |  |
| Max | `float` |  |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorFromStream

Returns a random vector with length of 1.0

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### RandomRotatorFromStream

Create a random rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bRoll | `bool` |  |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### ResetRandomStream

Reset a random stream

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### SeedRandomStream

Create a new random seed for a random stream

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Stream | `FRandomStream &` |  |

**Return**

- Type: 
- Description: _None_

### SetRandomStreamSeed

Set the seed of a random stream to a specific number

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Stream | `FRandomStream &` |  |
| NewSeed | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInConeInRadiansFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector &` | The base "center" direction of the cone. |
| ConeHalfAngleInRadians | `float` | The half-angle of the cone (from ConeDir to edge), in radians. |
| Stream | `FRandomStream &` | The random stream from which to obtain the vector. |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInConeInDegreesFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector &` | The base "center" direction of the cone. |
| ConeHalfAngleInDegrees | `float` | The half-angle of the cone (from ConeDir to edge), in degrees. |
| Stream | `FRandomStream &` | The random stream from which to obtain the vector. |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInEllipticalConeInRadiansFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector &` |  |
| MaxYawInRadians | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in radians. |
| MaxPitchInRadians | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in radians. |
| Stream | `FRandomStream &` | The random stream from which to obtain the vector. |

**Return**

- Type: 
- Description: _None_

### RandomUnitVectorInEllipticalConeInDegreesFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConeDir | `FVector &` |  |
| MaxYawInDegrees | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in degrees. |
| MaxPitchInDegrees | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in degrees. |
| Stream | `FRandomStream &` | The random stream from which to obtain the vector. |

**Return**

- Type: 
- Description: _None_

### MinimumAreaRectangle

Finds the minimum area rectangle that encloses all of the points in InVerts

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InVerts | `TArray < FVector > &` | - Points to enclose in the rectangle |
| SampleSurfaceNormal | `FVector &` |  |
| OutRectCenter | `FVector &` |  |
| OutRectRotation | `FRotator &` |  |
| OutSideLengthX | `float &` |  |
| OutSideLengthY | `float &` |  |
| bDebugDraw | `bool` |  |

**Return**

- Type: 
- Description: _None_

### PointsAreCoplanar

Determines whether a given set of points are coplanar, with a tolerance. Any three points or less are always coplanar.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Points | `TArray < FVector > &` | - The set of points to determine coplanarity for. |
| Tolerance | `float` | - Larger numbers means more variance is allowed. |

**Return**

- Type: 
- Description: _None_

### IsPointInBox

Determines whether the given point is in a box. Includes points on the box.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point to test |
| BoxOrigin | `FVector` | Origin of the box |
| BoxExtent | [FVector](../../cppstruct/F/FV/FVector.md) | Extents of the box (distance in each axis from origin) |

**Return**

- Type: 
- Description: _None_

### IsPointInBoxWithTransform

Determines whether a given point is in a box with a given transform. Includes points on the box.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point to test |
| BoxWorldTransform | `FTransform &` | Component-to-World transform of the box. |
| BoxExtent | [FVector](../../cppstruct/F/FV/FVector.md) | Extents of the box (distance in each axis from origin), in component space. |

**Return**

- Type: 
- Description: _None_

### LinePlaneIntersection

Computes the intersection point between a line and a plane.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LineStart | `FVector &` |  |
| LineEnd | `FVector &` |  |
| APlane | `FPlane &` |  |
| T | `float &` | - The t of the intersection between the line and the plane |
| Intersection | `FVector &` | - The point of intersection between the line and the plane |

**Return**

- Type: 
- Description: _None_

### LinePlaneIntersection_OriginNormal

Computes the intersection point between a line and a plane.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LineStart | `FVector &` |  |
| LineEnd | `FVector &` |  |
| PlaneOrigin | `FVector` |  |
| PlaneNormal | `FVector` |  |
| T | `float &` | - The t of the intersection between the line and the plane |
| Intersection | `FVector &` | - The point of intersection between the line and the plane |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
