# UActorChannel

A channel for exchanging actor and its subobject's properties and RPCs.

  ActorChannel manages the creation and lifetime of a replicated actor. Actual replication of properties and RPCs
  actually happens in FObjectReplicator now (see DataReplication.h).

  An ActorChannel bunch looks like this:

 		|----------------------|---------------------------------------------------------------------------|
 		| SpawnInfo		       | (Spawn Info) Initial bunch only                                           |
 		|  -Actor Class        |	-Created by ActorChannel	                                           |
 		|  -Spawn LocRot      |                                                                           |
       | NetGUID assigns      |                                                                           |
 		|  -Actor NetGUID      |                                                                           |
 		|  -Component NetGUIDs |                                                                           |
 		|----------------------|---------------------------------------------------------------------------|
 		|                      |                                                                           |
 		|----------------------|---------------------------------------------------------------------------|
 		| NetGUID ObjRef       | (Content chunks) x number of replicating objects (Actor + any components) |
  		|                      |		-Each chunk created by its own FObjectReplicator instance.         |
  		|----------------------|---------------------------------------------------------------------------|
       |                      |		                                                                   |
 		| Properties...        |                                                                           |
 		|                      |	                                                                       |
 		| RPCs...              |                                                                           |
       |                      |                                                                           |
       |----------------------|---------------------------------------------------------------------------|
 		| <End Tag>           |                                                                           |
 		|----------------------|---------------------------------------------------------------------------|

## Parents

- [UChannel](./UChannel.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| ActorName | `FName` |  |
| ActorStaticTag | `uint64` |  |
| bPausedUntilSubObjectReliableACK | `bool` |  |
| ServerScondsSinceWhenPauseReplicateForSubObjectAddOrRemove | `float` |  |
| ServerScondsFirstReplicateSinceWhenPauseReplicateForSubObjectAddOrRemove | `float` |  |
| LastWarningTimeForPauseTooLong_SinceWhenPauseReplicateForSubObjectAddOrRemove | `float` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
