# FMemberReference

## Fields

| Name | Type | Description |
| --- | --- | --- |
| MemberParent | `UObject *` | Most often the Class that this member is defined in. Could be a UPackage<br>	  if it is a native delegate signature function (declared globally). Should<br>	  be NULL if bSelfContext is true. |
| MemberScope | `FString` |  |
| MemberName | `FName` | Name of variable |
| MemberGuid | [FGuid](../FG/FGuid.md) | The Guid of the variable |
| bSelfContext | `bool` | Whether or not this should be a "self" context |
| bWasDeprecated | `bool` | Whether or not this property has been deprecated |
