# UKismetSystemLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### StackTrace

Prints a stack trace to the log, so you can see how a blueprint got to this node

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsValid

对象是否可用

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsRecycled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsValidClass

类型是否可用

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Class | `UClass *` |  |

**Return**

- Type: 
- Description: _None_

### GetObjectName

获取对象名称

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetPathName

获取对象路径

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetDisplayName

获取对象展示名称

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetClassDisplayName

获取类展示名称

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Class | `UClass *` |  |

**Return**

- Type: 
- Description: _None_

### StripObjectClass

If there is an object class, strips it off.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PathName | `FString &` |  |
| bAssertOnBadPath | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetEngineVersion

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGameName

Get the name of the current game

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGameBundleId

Retrieves the game's platform-specific bundle identifier or package name of the game

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlatformUserName

Get the current user name from the OS

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DoesImplementInterface

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TestObject | `UObject *` |  |
| Interface | `TSubclassOf < UInterface >` |  |

**Return**

- Type: 
- Description: _None_

### GetGameTimeInSeconds

Get the current game time, in seconds. This stops when the game is paused and is affected by slomo.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | World context |

**Return**

- Type: 
- Description: _None_

### IsServer

Returns whether the world this object is in is the host or not

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsDedicatedServer

Returns whether this is running on a dedicated server

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsStandalone

Returns whether this game instance is stand alone (no networking).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsPackagedForDistribution

Returns whether this is a build that is packaged for distribution

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUniqueDeviceId

Returns the platform specific unique device id

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDeviceId

Returns the platform specific unique device id

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Conv_InterfaceToObject

Converts an interfance into an object

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Interface | `FScriptInterface &` |  |

**Return**

- Type: 
- Description: _None_

### MakeSoftObjectPath

将路径字符串转换为SoftObjectPath

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PathString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### BreakSoftObjectPath

将SoftObjectPath转换为路径字符串

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSoftObjectPath | [FSoftObjectPath](../../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| PathString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### BreakSoftClassPath

将SoftClassPath转换为路径字符串

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSoftClassPath | `FSoftClassPath` |  |
| PathString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### IsValidSoftObjectReference

SoftObjectPath是否有效

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftObjectReference | `TSoftObjectPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_SoftObjectReferenceToString

Converts a Soft Object Reference to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftObjectReference | `TSoftObjectPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_SoftObjectReference

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSoftObjectPtr < UObject > &` |  |
| B | `TSoftObjectPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_SoftObjectReference

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSoftObjectPtr < UObject > &` |  |
| B | `TSoftObjectPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### IsValidSoftClassReference

Returns true if the Soft Class Reference is not null

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftClassReference | `TSoftClassPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_SoftClassReferenceToString

Converts a Soft Class Reference to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftClassReference | `TSoftClassPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_SoftClassReference

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSoftClassPtr < UObject > &` |  |
| B | `TSoftClassPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_SoftClassReference

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSoftClassPtr < UObject > &` |  |
| B | `TSoftClassPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_SoftObjectReferenceToObject

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftObject | `TSoftObjectPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_SoftClassReferenceToClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftClass | `TSoftClassPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ObjectToSoftObjectReference

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### Conv_ClassToSoftClassReference

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Class | `TSubclassOf < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### LoadAsset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Asset | `TSoftObjectPtr < UObject >` |  |
| OnLoaded | `FOnAssetLoaded` |  |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) |  |

**Return**

- Type: 
- Description: _None_

### LoadAssetClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| AssetClass | `TSoftClassPtr < UObject >` |  |
| OnLoaded | `FOnAssetClassLoaded` |  |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) |  |

**Return**

- Type: 
- Description: _None_

### MakeLiteralInt

Creates a literal integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` | value to set the integer to |

**Return**

- Type: 
- Description: _None_

### MakeLiteralInt64

Creates a literal integer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int64` | value to set the integer to |

**Return**

- Type: 
- Description: _None_

### MakeLiteralFloat

Creates a literal float

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` | value to set the float to |

**Return**

- Type: 
- Description: _None_

### MakeLiteralBool

Creates a literal bool

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `bool` | value to set the bool to |

**Return**

- Type: 
- Description: _None_

### MakeLiteralName

Creates a literal name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `FName` | value to set the name to |

**Return**

- Type: 
- Description: _None_

### MakeLiteralByte

Creates a literal byte

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `uint8` | value to set the byte to |

**Return**

- Type: 
- Description: _None_

### MakeLiteralString

Creates a literal string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `FString &` | value to set the string to |

**Return**

- Type: 
- Description: _None_

### MakeLiteralText

Creates a literal FText

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `FText` | value to set the FText to |

**Return**

- Type: 
- Description: _None_

### PrintString

Prints a string to the log, and optionally, to the screen
	  If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InString | `FString &` | The string to log out |
| bPrintToScreen | `bool` | Whether or not to print the output to the screen |
| bPrintToLog | `bool` | Whether or not to print the output to the log |
| TextColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | Whether or not to print the output to the console |
| Duration | `float` | The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config. |

**Return**

- Type: 
- Description: _None_

### PrintText

Prints text to the log, and optionally, to the screen
	  If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InText | `FText` | The text to log out |
| bPrintToScreen | `bool` | Whether or not to print the output to the screen |
| bPrintToLog | `bool` | Whether or not to print the output to the log |
| TextColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | Whether or not to print the output to the console |
| Duration | `float` | The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config. |

**Return**

- Type: 
- Description: _None_

### PrintWarning

Prints a warning string to the log and the screen. Meant to be used as a way to inform the user that they misused the node.

	  WARNING!! Don't change the signature of this function without fixing up all nodes using it in the compiler

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` | The string to log out |

**Return**

- Type: 
- Description: _None_

### SetWindowTitle

Sets the game window title

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Title | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### ExecuteConsoleCommand

Executes a console command, optionally on a specific controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Command | `FString &` | Command to send to the console |
| SpecificPlayer | `APlayerController *` | If specified, the console command will be routed through the specified player |
| bDisableCheck | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ExecuteConsoleCommandDisableCheck

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Command | `FString &` |  |
| SpecificPlayer | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### GetConsoleVariableFloatValue

Attempts to retrieve the value of the specified float console variable, if it exists.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| VariableName | `FString &` | Name of the console variable to find. |

**Return**

- Type: 
- Description: _None_

### GetConsoleVariableIntValue

Attempts to retrieve the value of the specified integer console variable, if it exists.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| VariableName | `FString &` | Name of the console variable to find. |

**Return**

- Type: 
- Description: _None_

### GetConsoleVariableBoolValue

Evaluates, if it exists, whether the specified integer console variable has a non-zero value (true) or not (false).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| VariableName | `FString &` | Name of the console variable to find. |

**Return**

- Type: 
- Description: _None_

### QuitGame

Exit the current game

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| SpecificPlayer | `APlayerController *` | The specific player to quit the game. If not specified, player 0 will quit. |
| QuitPreference | `TEnumAsByte < EQuitPreference :: Type >` |  |

**Return**

- Type: 
- Description: _None_

### Delay

Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Duration | `float` | length of delay (in seconds). |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) | The latent action. |

**Return**

- Type: 
- Description: _None_

### DelayUntilNextTick

Perform a latent action with a delay of one tick.  Calling again while it is counting down will be ignored.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) | The latent action. |

**Return**

- Type: 
- Description: _None_

### DelayReplacePreDuration

Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Duration | `float` | length of delay (in seconds). |
| IsReplacePreDuration | `bool` | replace previous action Duration |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) | The latent action. |

**Return**

- Type: 
- Description: _None_

### RetriggerableDelay

Perform a latent action with a retriggerable delay (specified in seconds).  Calling again while it is counting down will reset the countdown to Duration.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Duration | `float` | length of delay (in seconds). |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) | The latent action. |

**Return**

- Type: 
- Description: _None_

### MoveComponentTo

Interpolate a component to the specified relative location and rotation over the course of OverTime seconds.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `USceneComponent *` | Component to interpolate |
| TargetRelativeLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | Relative target location |
| TargetRelativeRotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Relative target rotation |
| bEaseOut | `bool` | if true we will ease out (ie end slowly) during interpolation |
| bEaseIn | `bool` | if true we will ease in (ie start slowly) during interpolation |
| OverTime | `float` | duration of interpolation |
| bForceShortestRotationPath | `bool` | if true we will always use the shortest path for rotation |
| MoveAction | `TEnumAsByte < EMoveComponentAction :: Type >` | required movement behavior @see EMoveComponentAction |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) | The latent action |

**Return**

- Type: 
- Description: _None_

### K2_SetTimerDelegate

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |
| Time | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| bLooping | `bool` | True to keep executing the delegate every Time seconds, false to execute delegate only once. |

**Return**

- Type: 
- Description: _None_

### K2_SetTimerForNextTickDelegate

Set a timer to execute a delegate next tick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_SetTimerTickDelegate

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicParamDelegate` |  |
| Time | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| InExeFirst | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_SetTimerDelegateForLua

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| Time | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| bLooping | `bool` | True to keep executing the delegate every Time seconds, false to execute delegate only once. |

**Return**

- Type: 
- Description: _None_

### K2_ClearTimerDelegate

Clears a set timer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_PauseTimerDelegate

Pauses a set timer at its current elapsed time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_UnPauseTimerDelegate

Resumes a paused timer from its current elapsed time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_IsTimerActiveDelegate

Returns true if a timer exists and is active for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_IsTimerPausedDelegate

Returns true if a timer exists and is paused for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_TimerExistsDelegate

Returns true is a timer for the given delegate exists, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetTimerElapsedTimeDelegate

Returns elapsed time for the given delegate (time since current countdown iteration began).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetTimerRemainingTimeDelegate

Returns time until the timer will next execute its delegate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `FTimerDynamicDelegate` |  |

**Return**

- Type: 
- Description: _None_

### K2_IsValidTimerHandle

Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to check validity of. |

**Return**

- Type: 
- Description: _None_

### K2_InvalidateTimerHandle

Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | [FTimerHandle &](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to check validity of. |

**Return**

- Type: 
- Description: _None_

### K2_ClearTimerHandle

Clears a set timer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to clear. |

**Return**

- Type: 
- Description: _None_

### K2_ClearAndInvalidateTimerHandle

Clears a set timer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle &](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to clear. |

**Return**

- Type: 
- Description: _None_

### K2_PauseTimerHandle

Pauses a set timer at its current elapsed time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to pause. |

**Return**

- Type: 
- Description: _None_

### K2_UnPauseTimerHandle

Resumes a paused timer from its current elapsed time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to unpause. |

**Return**

- Type: 
- Description: _None_

### K2_IsTimerActiveHandle

Returns true if a timer exists and is active for the given handle, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to check whether it is active. |

**Return**

- Type: 
- Description: _None_

### K2_IsTimerPausedHandle

Returns true if a timer exists and is paused for the given handle, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to check whether it is paused. |

**Return**

- Type: 
- Description: _None_

### K2_TimerExistsHandle

Returns true is a timer for the given handle exists, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle to check whether it exists. |

**Return**

- Type: 
- Description: _None_

### K2_GetTimerElapsedTimeHandle

Returns elapsed time for the given handle (time since current countdown iteration began).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to get the elapsed time of. |

**Return**

- Type: 
- Description: _None_

### K2_GetTimerRemainingTimeHandle

Returns time until the timer will next execute its handle.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Handle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | The handle of the timer to time remaining of. |

**Return**

- Type: 
- Description: _None_

### K2_SetTimer

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |
| Time | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| bLooping | `bool` | true to keep executing the delegate every Time seconds, false to execute delegate only once. |

**Return**

- Type: 
- Description: _None_

### K2_SetTimerForNextTick

Set a timer to execute a delegate on the next tick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_ClearTimer

Clears a set timer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_PauseTimer

Pauses a set timer at its current elapsed time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_UnPauseTimer

Resumes a paused timer from its current elapsed time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_IsTimerActive

Returns true if a timer exists and is active for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_IsTimerPaused

Returns true if a timer exists and is paused for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_TimerExists

Returns true is a timer for the given delegate exists, false otherwise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_GetTimerElapsedTime

Returns elapsed time for the given delegate (time since current countdown iteration began).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### K2_GetTimerRemainingTime

Returns time until the timer will next execute its delegate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| FunctionName | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Return**

- Type: 
- Description: _None_

### SetIntPropertyByName

Set an int32 property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetInt64PropertyByName

Set an int64 property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `int64` |  |

**Return**

- Type: 
- Description: _None_

### SetUInt64PropertyByName

Set an uint64 property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `uint64` |  |

**Return**

- Type: 
- Description: _None_

### SetBytePropertyByName

Set an uint8 or enum property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### SetFloatPropertyByName

Set a float property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBoolPropertyByName

Set a bool property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetObjectPropertyByName

Set an OBJECT property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SetClassPropertyByName

Set a CLASS property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `TSubclassOf < UObject >` |  |

**Return**

- Type: 
- Description: _None_

### SetInterfacePropertyByName

Set an INTERFACE property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `FScriptInterface &` |  |

**Return**

- Type: 
- Description: _None_

### SetNamePropertyByName

Set a NAME property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### SetSoftObjectPropertyByName

Set a SOFTOBJECT property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `TSoftObjectPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### SetSoftClassPropertyByName

Set a SOFTCLASS property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `TSoftClassPtr < UObject > &` |  |

**Return**

- Type: 
- Description: _None_

### SetStringPropertyByName

Set a STRING property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### SetTextPropertyByName

Set a TEXT property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### SetVectorPropertyByName

Set a VECTOR property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetRotatorPropertyByName

Set a ROTATOR property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | [FRotator &](../../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### SetLinearColorPropertyByName

Set a LINEAR COLOR property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | [FLinearColor &](../../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetTransformPropertyByName

Set a TRANSFORM property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | [FTransform &](../../../cppstruct/F/FT/FTransform.md) |  |

**Return**

- Type: 
- Description: _None_

### SetCollisionProfileNameProperty

Set a CollisionProfileName property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | [FCollisionProfileName &](../../../cppstruct/F/FC/FCollisionProfileName.md) |  |

**Return**

- Type: 
- Description: _None_

### SetStructurePropertyByName

Set a custom structure property by name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | [FGenericStruct &](../../../cppstruct/F/FG/FGenericStruct.md) |  |

**Return**

- Type: 
- Description: _None_

### SphereOverlapActors

返回一组跟指定球体范围发生重叠的Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| SpherePos | [FVector](../../../cppstruct/F/FV/FVector.md) | 球心位置 |
| SphereRadius | `float` | 球体半径 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ActorClassFilter | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutActors | `TArray < AActor * > &` | 输出的产生碰撞的Actor列表 |

**Return**

- Type: 
- Description: _None_

### SphereOverlapComponents

返回一组跟指定球体范围发生重叠的Component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| SpherePos | [FVector](../../../cppstruct/F/FV/FVector.md) | 球心位置 |
| SphereRadius | `float` | 球体半径 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ComponentClassFilter | `UClass *` | 组件类型过滤，只检测指定类型的组件 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutComponents | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Return**

- Type: 
- Description: _None_

### BoxOverlapAnyTest

检测指定Box范围是否发生重叠

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| BoxPos | [FVector](../../../cppstruct/F/FV/FVector.md) | Box中心位置 |
| Rotator | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box旋转量 |
| BoxExtent | [FVector](../../../cppstruct/F/FV/FVector.md) | Box范围 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ActorClassFilter | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |

**Return**

- Type: 
- Description: _None_

### BoxOverlapActors

返回一组跟指定Box范围发生重叠的Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| BoxPos | [FVector](../../../cppstruct/F/FV/FVector.md) | Box中心位置 |
| BoxRotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) |  |
| BoxExtent | [FVector](../../../cppstruct/F/FV/FVector.md) | Box范围 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ActorClassFilter | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutActors | `TArray < AActor * > &` | 输出的产生碰撞的Actor列表 |

**Return**

- Type: 
- Description: _None_

### BoxOverlapComponents

返回一组跟指定Box范围发生重叠的Component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| BoxPos | [FVector](../../../cppstruct/F/FV/FVector.md) | Box中心位置 |
| BoxRotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) |  |
| Extent | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ComponentClassFilter | `UClass *` |  |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutComponents | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Return**

- Type: 
- Description: _None_

### BoxOverlapOBBActors

Returns an array of actors that overlap the given axis-aligned box.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| BoxPos | [FVector &](../../../cppstruct/F/FV/FVector.md) | Center of box. |
| BoxRot | [FRotator &](../../../cppstruct/F/FR/FRotator.md) | Rotator of box. |
| BoxExtent | [FVector &](../../../cppstruct/F/FV/FVector.md) | Extents of box. |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` |  |
| ActorClassFilter | `UClass *` |  |
| ActorsToIgnore | `TArray < AActor * > &` | Ignore these actors in the list |
| OutActors | `TArray < AActor * > &` | Returned array of actors. Unsorted. |

**Return**

- Type: 
- Description: _None_

### BoxOverlapOBBComponents

Returns an array of components that overlap the given axis-aligned box.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| BoxPos | [FVector &](../../../cppstruct/F/FV/FVector.md) | Center of box. |
| BoxRot | [FRotator &](../../../cppstruct/F/FR/FRotator.md) | Rotator of box. |
| Extent | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` |  |
| ComponentClassFilter | `UClass *` |  |
| ActorsToIgnore | `TArray < AActor * > &` | Ignore these actors in the list |
| OutComponents | `TArray < UPrimitiveComponent * > &` |  |

**Return**

- Type: 
- Description: _None_

### CapsuleOverlapActors

返回一组跟指定胶囊体范围发生重叠的Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| CapsulePos | [FVector](../../../cppstruct/F/FV/FVector.md) | 胶囊体中心位置 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半高 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ActorClassFilter | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutActors | `TArray < AActor * > &` | Returned array of actors. Unsorted. |

**Return**

- Type: 
- Description: _None_

### CapsuleOverlapComponents

返回一组跟指定胶囊体范围发生重叠的Component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| CapsulePos | [FVector](../../../cppstruct/F/FV/FVector.md) | 胶囊体中心位置 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半高 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ComponentClassFilter | `UClass *` |  |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutComponents | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Return**

- Type: 
- Description: _None_

### ComponentOverlapActors

返回一组跟指定Component发生重叠的Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UPrimitiveComponent *` | Component对象 |
| ComponentTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) | Component的Transform |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ActorClassFilter | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutActors | `TArray < AActor * > &` | 输出的产生碰撞的Actor列表 |

**Return**

- Type: 
- Description: _None_

### ComponentOverlapComponents

返回一组跟指定Component发生重叠的Component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UPrimitiveComponent *` | Component对象 |
| ComponentTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) | Component的Transform |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| ComponentClassFilter | `UClass *` |  |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| OutComponents | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Return**

- Type: 
- Description: _None_

### LineTraceSingle

返回第一个跟射线碰撞的物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### LineTraceSingleByCollisionChannel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| CollisionChannel | `ECollisionChannel` |  |
| bTraceComplex | `bool` |  |
| ActorsToIgnore | `TArray < AActor * > &` |  |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) |  |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### LineTraceMulti

返回所有跟射线碰撞的物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### SphereTraceSingle

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 球体半径 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### SphereTraceMulti

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 球体半径 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### BoxTraceSingle

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | Box边的半长尺寸 |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box的朝向 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### BoxTraceMulti

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | Box边的半长尺寸 |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box的朝向 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### CapsuleTraceSingle

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半长高度 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### CapsuleTraceMulti

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半长高度 |
| TraceChannel | `ETraceTypeQuery` | 轨迹检测通道 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### LineTraceSingleForObjects

返回第一个跟射线碰撞的物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### LineTraceSingleByObjectType

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| ObjectTypes | `TArray < TEnumAsByte < ECollisionChannel > > &` |  |
| bTraceComplex | `bool` |  |
| ActorsToIgnore | `TArray < AActor * > &` |  |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) |  |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### LineTraceMultiForObjects

返回所有跟射线碰撞的物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### SphereTraceSingleForObjects

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 球体半径 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### SphereTraceMultiForObjects

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 球体半径 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### BoxTraceSingleForObjects

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | Box边的半长尺寸 |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box的朝向 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### BoxTraceMultiForObjects

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | Box边的半长尺寸 |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box的朝向 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### CapsuleTraceSingleForObjects

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半长高度 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### CapsuleTraceMultiForObjects

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半长高度 |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### LineTraceSingleByProfile

返回第一个跟射线碰撞的物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### LineTraceMultiByProfile

返回所有跟射线碰撞的物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### SphereTraceSingleByProfile

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 球体半径 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### SphereTraceMultiByProfile

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 球体半径 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### BoxTraceSingleByProfile

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | Box边的半长尺寸 |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box的朝向 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### BoxTraceMultiByProfile

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | Box边的半长尺寸 |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box的朝向 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### CapsuleTraceSingleByProfile

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半长高度 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### CapsuleTraceMultiByProfile

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `float` | 胶囊体半径 |
| HalfHeight | `float` | 胶囊体半长高度 |
| ProfileName | `FName` | 预设名称 |
| bTraceComplex | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| DrawDebugType | `EDrawDebugTrace :: Type` |  |
| OutHits | `TArray < FHitResult > &` | 输出的HitResult列表 |
| bIgnoreSelf | `bool` |  |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetActorListFromComponentList

Returns an array of unique actors represented by the given list of components.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ComponentList | `TArray < UPrimitiveComponent * > &` | List of components. |
| ActorClassFilter | `UClass *` |  |
| OutActorList | `TArray < AActor * > &` | Start of line segment. |

**Return**

- Type: 
- Description: _None_

### PrintToScreen

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |
| TextColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| TextScale | [FVector2D](../../../cppstruct/F/FV/FVector2D.md) |  |
| Duration | `float` |  |
| bIsUGC | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FlushOnScreenDebugMessages

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DrawDebugLine

Draw a debug line

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| LineStart | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| LineEnd | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugCircle

Draw a debug circle!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Radius | `float` |  |
| NumSegments | `int32` |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |
| YAxis | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| ZAxis | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| bDrawAxis | `bool` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugPoint

Draw a debug point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Position | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Size | `float` |  |
| PointColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugArrow

Draw directional arrow, pointing from LineStart to LineEnd.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| LineStart | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| LineEnd | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| ArrowSize | `float` |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugBox

Draw a debug box

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Extent | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugCoordinateSystem

Draw a debug coordinate system.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| AxisLoc | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| AxisRot | [FRotator](../../../cppstruct/F/FR/FRotator.md) |  |
| Scale | `float` |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugSphere

Draw a debug sphere

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Radius | `float` |  |
| Segments | `int32` |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugCylinder

Draw a debug cylinder

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Radius | `float` |  |
| Segments | `int32` |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugCone

Draw a debug cone

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Origin | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Direction | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Length | `float` |  |
| AngleWidth | `float` |  |
| AngleHeight | `float` |  |
| NumSides | `int32` |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugConeInDegrees

Draw a debug cone
	  Angles are specified in degrees

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Origin | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Direction | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Length | `float` |  |
| AngleWidth | `float` |  |
| AngleHeight | `float` |  |
| NumSides | `int32` |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugCapsule

Draw a debug capsule

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Center | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| HalfHeight | `float` |  |
| Radius | `float` |  |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) |  |
| LineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugString

Draw a debug string at a 3d world location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| TextLocation | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Text | `FString &` |  |
| TestBaseActor | `AActor *` |  |
| TextColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |

**Return**

- Type: 
- Description: _None_

### FlushDebugStrings

Removes all debug strings.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugPlane

Draws a debug plane.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PlaneCoordinates | [FPlane &](../../../cppstruct/F/FP/FPlane.md) |  |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Size | `float` |  |
| PlaneColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |

**Return**

- Type: 
- Description: _None_

### FlushPersistentDebugLines

Flush all persistent debug lines and shapes.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugFrustum

Draws a debug frustum.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| FrustumTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) |  |
| FrustumColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugCamera

Draw a debug camera shape.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CameraActor | `ACameraActor *` |  |
| CameraColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugFloatHistoryTransform

Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawTransform for the position in the world.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| FloatHistory | `FDebugFloatHistory &` |  |
| DrawTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) |  |
| DrawSize | [FVector2D](../../../cppstruct/F/FV/FVector2D.md) |  |
| DrawColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugFloatHistoryLocation

Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawLocation for the location in the world, rotation will face camera of first player.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| FloatHistory | `FDebugFloatHistory &` |  |
| DrawLocation | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| DrawSize | [FVector2D](../../../cppstruct/F/FV/FVector2D.md) |  |
| DrawColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |

**Return**

- Type: 
- Description: _None_

### AddFloatHistorySample

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| FloatHistory | `FDebugFloatHistory &` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugActorName

绘制Actor名称

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| Offset | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| LinearColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugActorMoveTrack

绘制Actor运动轨迹

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| LinearColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugDistance

绘制Self到Tartget的连线与距离

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Self | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Target | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| LinearColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugTargetAimedAt

绘制准心瞄准物体名称

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Length | `float` |  |
| DrawTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugActorCollision

绘制碰撞盒

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| LinearColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### DrawDebugActorBounds

绘制Actor的包围盒

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| LinearColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) |  |
| Duration | `float` |  |
| Thickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### CreateCopyForUndoBuffer

Mark as modified.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectToModify | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetComponentBounds

Get bounds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `USceneComponent *` |  |
| Origin | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |
| BoxExtent | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |
| SphereRadius | `float &` |  |

**Return**

- Type: 
- Description: _None_

### GetActorBounds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| Origin | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |
| BoxExtent | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GetRenderingDetailMode

Get the clamped state of r.DetailMode, see console variable help (allows for scalability, cannot be used in construction scripts)
	  0: low, show only object with DetailMode low or higher
	  1: medium, show all object with DetailMode medium or higher
	  2: high, show all objects

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRenderingMaterialQualityLevel

Get the clamped state of r.MaterialQualityLevel, see console variable help (allows for scalability, cannot be used in construction scripts)
	  0: low
	  1: high
	  2: medium
	  3: ultimatehigh

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSupportedFullscreenResolutions

Gets the list of support fullscreen resolutions.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Resolutions | `TArray < FIntPoint > &` |  |

**Return**

- Type: 
- Description: _None_

### GetConvenientWindowedResolutions

Gets the list of windowed resolutions which are convenient for the current primary display size.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Resolutions | `TArray < FIntPoint > &` |  |

**Return**

- Type: 
- Description: _None_

### GetMinYResolutionForUI

Gets the smallest Y resolution we want to support in the UI, clamped within reasons

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMinYResolutionFor3DView

Gets the smallest Y resolution we want to support in the 3D view, clamped within reasons

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LaunchURL

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| URL | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### CanLaunchURL

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| URL | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### CollectGarbage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bFullPurge | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetTimeSinceLastPendingKillPurge

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ShowAdBanner

Will show an ad banner (iAd on iOS, or AdMob on Android) on the top or bottom of screen, on top of the GL view (doesn't resize the view)
	  (iOS and Android only)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AdIdIndex | `int32` | The index of the ID to select for the ad to show |
| bShowOnBottomOfScreen | `bool` | If true, the iAd will be shown at the bottom of the screen, top otherwise |

**Return**

- Type: 
- Description: _None_

### GetAdIDCount

Retrieves the total number of Ad IDs that can be selected between

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HideAdBanner

Hides the ad banner (iAd on iOS, or AdMob on Android). Will force close the ad if it's open
	  (iOS and Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ForceCloseAdBanner

Forces closed any displayed ad. Can lead to loss of revenue
	  (iOS and Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LoadInterstitialAd

Will load a fullscreen interstitial AdMob ad. Call this before using ShowInterstitialAd
	 (Android only)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AdIdIndex | `int32` | The index of the ID to select for the ad to show |

**Return**

- Type: 
- Description: _None_

### IsInterstitialAdAvailable

Returns true if the requested interstitial ad is loaded and ready
	 (Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsInterstitialAdRequested

Returns true if the requested interstitial ad has been successfully requested (false if load request fails)
	 (Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ShowInterstitialAd

Shows the loaded interstitial ad (loaded with LoadInterstitialAd)
	 (Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ShowPlatformSpecificLeaderboardScreen

Displays the built-in leaderboard GUI (iOS and Android only; this function may be renamed or moved in a future release)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CategoryName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### ShowPlatformSpecificAchievementsScreen

Displays the built-in achievements GUI (iOS and Android only; this function may be renamed or moved in a future release)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SpecificPlayer | `APlayerController *` | Specific player's achievements to show. May not be supported on all platforms. If null, defaults to the player with ControllerId 0 |

**Return**

- Type: 
- Description: _None_

### IsLoggedIn

Returns whether the player is logged in to the currently active online subsystem.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SpecificPlayer | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### ControlScreensaver

Allows or inhibits screensaver

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bAllowScreenSaver | `bool` | If false, don't allow screensaver if possible, otherwise allow default behavior |

**Return**

- Type: 
- Description: _None_

### SetVolumeButtonsHandledBySystem

Allows or inhibits system default handling of volume up and volume down buttons (Android only)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` | If true, allow Android to handle volume up and down events |

**Return**

- Type: 
- Description: _None_

### GetVolumeButtonsHandledBySystem

Returns true if system default handling of volume up and volume down buttons enabled (Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetGamepadAssignments

Resets the gamepad to player controller id assignments (Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetGamepadAssignmentToController

Resets the gamepad assignment to player controller id (Android only)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ControllerId | `int32` |  |

**Return**

- Type: 
- Description: _None_

### IsControllerAssignedToGamepad

Returns true if controller id assigned to a gamepad (Android only)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ControllerId | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetSuppressViewportTransitionMessage

Sets the state of the transition message rendered by the viewport. (The blue text displayed when the game is paused and so forth.)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | World context |
| bState | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetPreferredLanguages

Returns an array of the user's preferred languages in order of preference

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDefaultLanguage

Get the default language (for localization) used by this platform

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDefaultLocale

Get the default locale (for internationalization) used by this platform

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalCurrencyCode

Returns the currency code associated with the device's locale

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalCurrencySymbol

Returns the currency symbol associated with the device's locale

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RegisterForRemoteNotifications

Requests permission to send remote notifications to the user's device.
	  (Android and iOS only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UnregisterForRemoteNotifications

Requests Requests unregistering from receiving remote notifications to the user's device.
	 (Android only)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetUserActivity

Tells the engine what the user is doing for debug, analytics, etc.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UserActivity | [FUserActivity &](../../../cppstruct/F/FU/FUserActivity.md) |  |

**Return**

- Type: 
- Description: _None_

### GetCommandLine

Returns the command line that the process was launched with.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetObjectFromPrimaryAssetId

Returns the Object associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### GetClassFromPrimaryAssetId

Returns the Blueprint Class associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### GetSoftObjectReferenceFromPrimaryAssetId

Returns the Object Id associated with a Primary Asset Id, this works even if the asset is not loaded

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### GetSoftClassReferenceFromPrimaryAssetId

Returns the Blueprint Class Id associated with a Primary Asset Id, this works even if the asset is not loaded

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### GetPrimaryAssetIdFromObject

Returns the Primary Asset Id for an Object, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetPrimaryAssetIdFromClass

Returns the Primary Asset Id for a Class, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Class | `TSubclassOf < UObject >` |  |

**Return**

- Type: 
- Description: _None_

### GetPrimaryAssetIdFromSoftObjectReference

Returns the Primary Asset Id for a Soft Object Reference, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftObjectReference | `TSoftObjectPtr < UObject >` |  |

**Return**

- Type: 
- Description: _None_

### GetPrimaryAssetIdFromSoftClassReference

Returns the Primary Asset Id for a Soft Class Reference, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SoftClassReference | `TSoftClassPtr < UObject >` |  |

**Return**

- Type: 
- Description: _None_

### GetPrimaryAssetIdList

Returns list of PrimaryAssetIds for a PrimaryAssetType

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetType | [FPrimaryAssetType](../../../cppstruct/F/FP/FPrimaryAssetType.md) |  |
| OutPrimaryAssetIdList | `TArray < FPrimaryAssetId > &` |  |

**Return**

- Type: 
- Description: _None_

### IsValidPrimaryAssetId

Returns true if the Primary Asset Id is valid

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_PrimaryAssetIdToString

Converts a Primary Asset Id to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_PrimaryAssetId

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |
| B | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_PrimaryAssetId

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |
| B | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### IsValidPrimaryAssetType

Returns list of Primary Asset Ids for a PrimaryAssetType

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetType | [FPrimaryAssetType](../../../cppstruct/F/FP/FPrimaryAssetType.md) |  |

**Return**

- Type: 
- Description: _None_

### Conv_PrimaryAssetTypeToString

Converts a Primary Asset Type to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetType | [FPrimaryAssetType](../../../cppstruct/F/FP/FPrimaryAssetType.md) |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_PrimaryAssetType

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FPrimaryAssetType](../../../cppstruct/F/FP/FPrimaryAssetType.md) |  |
| B | [FPrimaryAssetType](../../../cppstruct/F/FP/FPrimaryAssetType.md) |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_PrimaryAssetType

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | [FPrimaryAssetType](../../../cppstruct/F/FP/FPrimaryAssetType.md) |  |
| B | [FPrimaryAssetType](../../../cppstruct/F/FP/FPrimaryAssetType.md) |  |

**Return**

- Type: 
- Description: _None_

### UnloadPrimaryAsset

Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |

**Return**

- Type: 
- Description: _None_

### UnloadPrimaryAssetList

Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetIdList | `TArray < FPrimaryAssetId > &` |  |

**Return**

- Type: 
- Description: _None_

### GetCurrentBundleState

Returns the list of loaded bundles for a given Primary Asset. This will return false if the asset is not loaded at all.
	  If ForceCurrentState is true it will return the current state even if a load is in process

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetId | [FPrimaryAssetId](../../../cppstruct/F/FP/FPrimaryAssetId.md) |  |
| bForceCurrentState | `bool` |  |
| OutBundles | `TArray < FName > &` |  |

**Return**

- Type: 
- Description: _None_

### GetPrimaryAssetsWithBundleState

Returns the list of assets that are in a given bundle state. Required Bundles must be specified
	  If ExcludedBundles is not empty, it will not return any assets in those bundle states
	  If ValidTypes is not empty, it will only return assets of those types
	  If ForceCurrentState is true it will use the current state even if a load is in process

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RequiredBundles | `TArray < FName > &` |  |
| ExcludedBundles | `TArray < FName > &` |  |
| ValidTypes | `TArray < FPrimaryAssetType > &` |  |
| bForceCurrentState | `bool` |  |
| OutPrimaryAssetIdList | `TArray < FPrimaryAssetId > &` |  |

**Return**

- Type: 
- Description: _None_

### AddResMapping

Functions for Asset Redirect

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPackageNameRemap | `TMap < FName , FName > &` |  |

**Return**

- Type: 
- Description: _None_

### AddResPathMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPackagePathRemap | `TMap < FString , FString > &` |  |

**Return**

- Type: 
- Description: _None_

### AddResARMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InARPaths | `TSet < FString > &` |  |

**Return**

- Type: 
- Description: _None_

### IterateAddResARMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InARRoot | `FString &` |  |
| InARPaths | `TSet < FString > &` |  |

**Return**

- Type: 
- Description: _None_

### IterateRemoveResARMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InARRoot | `FString &` |  |
| InARPaths | `TSet < FString > &` |  |

**Return**

- Type: 
- Description: _None_

### IsResARMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InARPath | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### RemoveResMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PathKeys | `TArray < FString > &` |  |

**Return**

- Type: 
- Description: _None_

### EmptyResMapping

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddBlackResMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPackageNames | `TSet < FName > &` |  |

**Return**

- Type: 
- Description: _None_

### RemoveBlackResMapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPackageNames | `TSet < FName > &` |  |

**Return**

- Type: 
- Description: _None_

### EmptyBlackResMapping

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BindPackageNameResolver

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UnBindPackageNameResolver

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPackageNameResolverBinded

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsARPathActivated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InARPath | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetOriginalPath

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Path | `FName &` |  |
| OriginalPath | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetDelegateResolvedPackagePath

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSourcePackagePath | `FString &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
