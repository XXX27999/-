# FHitResult

Structure containing information about one hit of a trace, such as point of impact and surface normal at that point.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bStartPenetrating | `uint32` | Whether the trace started in penetration, i.e. with an initial blocking overlap.<br>	  In the case of penetration, if PenetrationDepth > 0.f, then it will represent the distance along the Normal vector that will result in<br>	  minimal contact between the swept shape and the object that was hit. In this case, ImpactNormal will be the normal opposed to movement at that location<br>	  (ie, Normal may not equal ImpactNormal). ImpactPoint will be the same as Location, since there is no single impact point to report. |
| bBlockingHit | `uint32` | Indicates if this hit was a result of blocking collision. If false, there was no hit or it was an overlaptouch instead. |
| ImpactPoint | `FVector_NetQuantize` | Location in world space of the actual contact of the trace shape (box, sphere, ray, etc) with the impacted object.<br>	  Example: for a sphere trace test, this is the point where the surface of the sphere touches the other object.<br>	  @note: In the case of initial overlap (bStartPenetrating=true), ImpactPoint will be the same as Location because there is no meaningful single impact point to report. |
| Time | `float` | 'Time' of impact along trace direction (ranging from 0.0 to 1.0) if there is a hit, indicating time between TraceStart and TraceEnd.<br>	  For swept movement (but not queries) this may be pulled back slightly from the actual time of impact, to prevent precision problems with adjacent geometry. |
| Distance | `float` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| Location | `FVector_NetQuantize` | The location in world space where the moving shape would end up against the impacted object, if there is a hit. Equal to the point of impact for line tests.<br>	  Example: for a sphere trace test, this is the point where the center of the sphere would be located when it touched the other object.<br>	  For swept movement (but not queries) this may not equal the final location of the shape since hits are pulled back slightly to prevent precision issues from overlapping another surface. |
| Normal | `FVector_NetQuantizeNormal` | Normal of the hit in world space, for the object that was swept. Equal to ImpactNormal for line tests.<br>	  This is computed for capsules and spheres, otherwise it will be the same as ImpactNormal.<br>	  Example: for a sphere trace test, this is a normalized vector pointing in towards the center of the sphere at the point of impact. |
| ImpactNormal | `FVector_NetQuantizeNormal` | Normal of the hit in world space, for the object that was hit by the sweep, if any.<br>	  For example if a box hits a flat plane, this is a normalized vector pointing out from the plane.<br>	  In the case of impact with a corner or edge of a surface, usually the "most opposing" normal (opposed to the query direction) is chosen. |
| TraceStart | `FVector_NetQuantize` | Start location of the trace.<br>	  For example if a sphere is swept against the world, this is the starting location of the center of the sphere. |
| TraceEnd | `FVector_NetQuantize` | End location of the trace; this is NOT where the impact occurred (if any), but the furthest point in the attempted sweep.<br>	  For example if a sphere is swept against the world, this would be the center of the sphere if there was no blocking hit. |
| PenetrationDepth | `float` | If this test started in penetration (bStartPenetrating is true) and a depenetration vector can be computed,<br>	   this value is the distance along Normal that will result in moving out of penetration.<br>	   If the distance cannot be computed, this distance will be zero. |
| Item | `int32` | Extra data about item that was hit (hit primitive specific). |
| PhysMaterial | `TWeakObjectPtr < UPhysicalMaterial >` | Physical material that was hit.<br>	  @note Must set bReturnPhysicalMaterial on the swept PrimitiveComponent or in the query params for this to be returned. |
| Actor | `TWeakObjectPtr < AActor >` | Actor hit by the trace. |
| Component | `TWeakObjectPtr < UPrimitiveComponent >` | PrimitiveComponent hit by the trace. |
| BoneName | `FName` | Name of bone we hit (for skeletal meshes). |
| FaceIndex | `int32` | Face index we hit (for complex hits with triangle meshes). |
