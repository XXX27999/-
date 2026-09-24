# FNetViewer

stores information on a viewer that actors need to be checked against for relevancy

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Connection | `UNetConnection *` |  |
| InViewer | `AActor *` | The "controlling net object" associated with this view (typically player controller) |
| ViewTarget | `AActor *` | The actor that is being directly viewed, usually a pawn.  Could also be the net actor of consequence |
| ViewLocation | [FVector](../FV/FVector.md) | Where the viewer is looking from |
| ViewDir | [FVector](../FV/FVector.md) | Direction the viewer is looking |
