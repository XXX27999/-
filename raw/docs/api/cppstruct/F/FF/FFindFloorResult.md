# FFindFloorResult

Data about the floor for walking movement, used by CharacterMovementComponent.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bBlockingHit | `uint32` | True if there was a blocking hit in the floor test that was NOT in initial penetration.<br>	 The HitResult can give more info about other circumstances. |
| bWalkableFloor | `uint32` | True if the hit found a valid walkable floor. |
| bLineTrace | `uint32` | True if the hit found a valid walkable floor using a line trace (rather than a sweep test, which happens when the sweep test fails to yield a walkable surface). |
| FloorDist | `float` | The distance to the floor, computed from the swept capsule trace. |
| LineDist | `float` | The distance to the floor, computed from the trace. Only valid if bLineTrace is true. |
| HitResult | [FHitResult](../FH/FHitResult.md) | Hit result of the test that found a floor. Includes more specific data about the point of impact and surface normal at that point. |
