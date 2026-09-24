# FComponentReference

Struct that allows for different ways to reference a component.
 	If just an Actor is specified, will return RootComponent of that Actor.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` | Pointer to a different Actor that owns the Component. |
| ComponentProperty | `FName` | Name of component property to use |
