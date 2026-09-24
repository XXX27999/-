# FAIDamageEvent

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Amount | `float` | Damage taken by DamagedActor.<br>	 	@Note 0-damage events do not get ignored |
| Location | [FVector](../FV/FVector.md) | Event's "Location", or what will be later treated as the perceived location for this sense.<br>	 	If not set, HitLocation will be used, if that is unset too DamagedActor's location |
| HitLocation | [FVector](../FV/FVector.md) | Event's additional spatial information<br>	 	@TODO document |
| DamagedActor | `AActor *` | Damaged actor |
| Instigator | `AActor *` | Actor that instigated damage. Can be None |
