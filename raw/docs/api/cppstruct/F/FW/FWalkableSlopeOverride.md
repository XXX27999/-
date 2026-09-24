# FWalkableSlopeOverride

Struct allowing control over "walkable" normals, by allowing a restriction or relaxation of what steepness is normally walkable.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| WalkableSlopeBehavior | `TEnumAsByte < EWalkableSlopeBehavior >` | Behavior of this surface (whether we affect the walkable slope).<br>	  @see GetWalkableSlopeBehavior(), SetWalkableSlopeBehavior() |
| WalkableSlopeAngle | `float` | Override walkable slope angle (in degrees), applying the rules of the Walkable Slope Behavior.<br>	  @see GetWalkableSlopeAngle(), SetWalkableSlopeAngle() |
