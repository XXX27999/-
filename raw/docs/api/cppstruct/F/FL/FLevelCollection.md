# FLevelCollection

Contains a group of levels of a particular ELevelCollectionType within a UWorld
  and the context required to properly tickupdate those levels. This object is move-only.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| GameState | `AGameStateBase *` | The GameState associated with this collection. This may be different than the UWorld's GameState<br>	  since the source collection and the duplicated collection will have their own instances. |
| NetDriver | `UNetDriver *` | The network driver associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| DemoNetDriver | `UDemoNetDriver *` | The demo network driver associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| MDNetDriverServer | `UNetDriver *` | The md network driver associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| MDNetDriverClient | `UNetDriver *` |  |
| PersistentLevel | `ULevel *` | The persistent level associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| Levels | `TSet < ULevel * >` | All the levels in this collection. |
