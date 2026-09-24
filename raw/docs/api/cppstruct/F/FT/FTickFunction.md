# FTickFunction

Abstract Base class for all tick functions.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TickGroup | `TEnumAsByte < enum ETickingGroup >` | Defines the minimum tick group for this tick function. These groups determine the relative order of when objects tick during a frame update.<br>	  Given prerequisites, the tick may be delayed.<br><br>	  @see ETickingGroup<br>	  @see FTickFunction::AddPrerequisite() |
| EndTickGroup | `TEnumAsByte < enum ETickingGroup >` | Defines the tick group that this tick function must finish in. These groups determine the relative order of when objects tick during a frame update.<br><br>	  @see ETickingGroup |
| bTickEvenWhenPaused | `uint8` | Bool indicating that this function should execute even if the game is paused. Pause ticks are very limited in capabilities. |
| bCanEverTick | `uint8` | If false, this tick function will never be registered and will never tick. Only settable in defaults. |
| bStartWithTickEnabled | `uint8` | If true, this tick function will start enabled, but can be disabled later on. |
| bAllowTickOnDedicatedServer | `uint8` | If we allow this tick to run on a dedicated server |
| bPureLogicTick | `uint8` | Pure logic tick group that is actually tick in game thread,  don't need to queue tick and task graph system |
| bAllowDynamicSchedule | `uint8` | Whether dynamic scheduling is allowed for this tick function |
| TickInterval | `float` | The frequency in seconds at which this tick function will be executed.  If less than or equal to 0 then it will tick every frame |
| TickIntervalStartTime | `float` | TickInterval Start Time Offset |
