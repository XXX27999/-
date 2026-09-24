# FCollisionResponseTemplate

Structure for collision response templates.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Name | `FName` |  |
| CollisionEnabled | `TEnumAsByte < ECollisionEnabled :: Type >` |  |
| ObjectTypeName | `FName` |  |
| CustomResponses | `TArray < FResponseChannel >` | Types of objects that this physics objects will collide with. |
| HelpMessage | `FString` | Help message for collision profile |
| bCanModify | `bool` | Help message for collision profile |
