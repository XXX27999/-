# FWorldContext

FWorldContext
 	A context for dealing with UWorlds at the engine level. As the engine brings up and destroys world, we need a way to keep straight
 	what world belongs to what.

 	WorldContexts can be thought of as a track. By default we have 1 track that we load and unload levels on. Adding a second context is adding
 	a second track; another track of progression for worlds to live on.

 	For the GameEngine, there will be one WorldContext until we decide to support multiple simultaneous worlds.
 	For the EditorEngine, there may be one WorldContext for the EditorWorld and one for the PIE World.

 	FWorldContext provides both a way to manage 'the current PIE UWorld' as well as state that goes along with connectingtravelling to
   new worlds.

 	FWorldContext should remain internal to the UEngine classes. Outside code should not keep pointers or try to manage FWorldContexts directly.
 	Outside code can steal deal with UWorld, and pass UWorlds into Engine level functions. The Engine code can look up the relevant context
 	for a given UWorld.

   For convenience, FWorldContext can maintain outside pointers to UWorlds. For example, PIE can tie UWorld UEditorEngine::PlayWorld to the PIE
 	world context. If the PIE UWorld changes, the UEditorEngine::PlayWorld pointer will be automatically updated. This is done with AddRef() and
   SetCurrentWorld().

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LastURL | `FURL` | URL the last time we traveled |
| LastRemoteURL | `FURL` | last server we connected to (for "reconnect" command) |
| PendingNetGame | `UPendingNetGame *` |  |
| PackagesToFullyLoad | `TArray < FFullyLoadedPackagesInfo >` | A list of tagarray pairs that is used at LoadMap time to fully load packages that may be needed for the mapgame with DLC, but we can't use DynamicLoadObject to load from the packages |
| LoadedLevelsForPendingMapChange | `TArray < ULevel * >` | Array of already loaded levels. The ordering is arbitrary and depends on what is already loaded and such. |
| ObjectReferencers | `TArray < UObjectReferencer * >` | Handles to object references; used by the engine to e.g. the prevent objects from being garbage collected. |
| PendingLevelStreamingStatusUpdates | `TArray < FLevelStreamingStatus >` |  |
| GameViewport | `UGameViewportClient *` |  |
| OwningGameInstance | `UGameInstance *` |  |
| ActiveNetDrivers | `TArray < FNamedNetDriver >` | A list of active net drivers |
