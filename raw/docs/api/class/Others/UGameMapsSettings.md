# UGameMapsSettings

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EditorStartupMap | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | If set, this map will be loaded when the Editor starts up. |
| LocalMapOptions | `FString` | The default options that will be appended to a map being loaded. |
| TransitionMap | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | The map loaded when transition from one map to another. |
| bUseSplitscreen | `bool` | Whether the screen should be split or not when multiple local players are present |
| TwoPlayerSplitscreenLayout | `TEnumAsByte < ETwoPlayerSplitScreenType :: Type >` | The viewport layout to use if the screen should be split and there are two local players |
| ThreePlayerSplitscreenLayout | `TEnumAsByte < EThreePlayerSplitScreenType :: Type >` | The viewport layout to use if the screen should be split and there are three local players |
| bOffsetPlayerGamepadIds | `bool` | If enabled, this will make so that gamepads start being assigned to the second controller ID in local multiplayer games.<br>	 In PIE sessions with multiple windows, this has the same effect as enabling "Route 1st Gamepad to 2nd Client" |
| GameInstanceClass | `FSoftClassPath` | The class to use when instantiating the transient GameInstance class |
| GameDefaultMap | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | The map that will be loaded by default when no other map is loaded. |
| HSCDefaultMap | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| UGCMDefaultMap | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) |  |
| ServerDefaultMap | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | The map that will be loaded by default when no other map is loaded (DEDICATED SERVER). |
| GlobalDefaultGameMode | `FSoftClassPath` | GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL). |
| GlobalDefaultServerGameMode | `FSoftClassPath` | GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL) (DEDICATED SERVERS)<br>	  If not set, the GlobalDefaultGameMode value will be used. |
| GameModeMapPrefixes | `TArray < FGameModeName >` | Overrides the GameMode to use when loading a map that starts with a specific prefix |
| GameModeClassAliases | `TArray < FGameModeName >` | List of GameModes to load when game= is specified in the URL (e.g. "DM" could be an alias for "MyProject.MyGameModeMP_DM") |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
