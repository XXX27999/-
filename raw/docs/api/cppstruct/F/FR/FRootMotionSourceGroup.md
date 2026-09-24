# FRootMotionSourceGroup

Group of Root Motion Sources that are applied

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bHasAdditiveSources | `bool` | Whether this group has additive root motion sources |
| bHasOverrideSources | `bool` | Whether this group has override root motion sources |
| LastPreAdditiveVelocity | `FVector_NetQuantize10` | Saved off pre-additive-applied Velocity, used for being able to reliably addremove additive<br>	   velocity from currently computed Velocity (otherwise we would be removing additive velocity<br>	   that no longer exists, like if you run into a wall and your Velocity becomes 0 - subtracting<br>	   the velocity that we added heading into the wall last tick would make you go backwards. With<br>	   this method we override that resulting Velocity due to obstructions |
| bIsAdditiveVelocityApplied | `bool` | True when we had additive velocity applied last tick, checked to know if we should restore<br>	   LastPreAdditiveVelocity before a Velocity computation |
| LastAccumulatedSettings | [FRootMotionSourceSettings](./FRootMotionSourceSettings.md) | Aggregate Settings of the last group of accumulated sources |
