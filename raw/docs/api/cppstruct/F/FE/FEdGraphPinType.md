# FEdGraphPinType

Struct used to define the type of information carried on this pin

## Fields

| Name | Type | Description |
| --- | --- | --- |
| PinCategory | `FString` | Category of pin type |
| PinSubCategory | `FString` | Sub-category of pin type |
| PinSubCategoryObject | `TWeakObjectPtr < UObject >` | Sub-category object |
| PinSubCategoryMemberReference | [FSimpleMemberReference](../FS/FSimpleMemberReference.md) | Sub-category member reference |
| PinValueType | [FEdGraphTerminalType](./FEdGraphTerminalType.md) | Data used to determine value types when bIsMap is true |
| ContainerType | [EPinContainerType](../../../cppenum/E/EP/EPinContainerType.md) |  |
| bIsArray_DEPRECATED | `uint8` | DEPRECATED(4.17) Whether or not this pin represents an array of values |
| bIsReference | `uint8` | Whether or not this pin is a value passed by reference or not |
| bIsConst | `uint8` | Whether or not this pin is a immutable const value |
| bIsWeakPointer | `uint8` | Whether or not this is a weak reference |
