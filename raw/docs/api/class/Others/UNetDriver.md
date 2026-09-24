# UNetDriver

## Parents

- [UObject](./UObject.md)
- FExec

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NetConnectionClassName | `FString` | Used to specify the class to use for connections |
| MaxDownloadSize | `int32` | @todo document |
| bClampListenServerTickRate | `uint32` | @todo document |
| NetServerMaxTickRate | `int32` | @todo document |
| MaxInternetClientRate | `int32` | @todo document |
| MaxClientRate | `int32` | @todo document |
| ServerTravelPause | `float` | Amount of time a server will wait before traveling to next map, gives clients time to receive final RPCs on existing level @see NextSwitchCountdown |
| SpawnPrioritySeconds | `float` | @todo document |
| RelevantTimeout | `float` | @todo document |
| KeepAliveTime | `float` | @todo document |
| InitialConnectTimeout | `float` | Amount of time to wait for a new net connection to be established before destroying the connection |
| IgnoreNetReadyReplicateActorCount | `int32` | Number of prioritized actors which should ignore IsNetReady when gets replicated |
| ConnectionTimeout | `float` | Amount of time to wait before considering an established connection timed out.<br>	  Typically shorter than the time to wait on a new connection because this connection<br>	  should already have been setup and any interruption should be trapped quicker. |
| TimeoutMultiplierForUnoptimizedBuilds | `float` | A multiplier that is applied to the above values when we are running with unoptimized builds (debug)<br>	 or data (uncooked). This allows us to retain normal timeout behavior while debugging without resorting<br>	 to the nuclear 'notimeouts' option or bumping the values above. If ==0 multiplier = 1 |
| bNoTimeouts | `bool` | If true, ignore timeouts completely.  Should be used only in development |
| SimpleRepClassConfig | `TArray < FString >` |  |
| ServerConnection | `UNetConnection *` | Connection to the server (this net driver is a client) |
| ClientConnections | `TArray < UNetConnection * >` | Array of connections to clients (this net driver is a host) |
| World | `UWorld *` | World this net driver is associated with |
| NetConnectionClass | `UClass *` | The loaded UClass of the net connection type to use |
| RoleProperty | `UProperty *` | @todo document |
| RemoteRoleProperty | `UProperty *` | @todo document |
| NetDriverName | `FName` | Used to specify the net driver to filter actors with (NAME_None \|\| NAME_GameNetDriver is the default net driver) |
| Time | `float` | Accumulated time for the net driver, updated by Tick |
| bOpenClientClampDriverDeltaTime | `bool` |  |
| ClientClampDriverDeltaTimeMin | `float` |  |
| ClientClampDriverDeltaTimeMax | `float` |  |
| NeedResendSubObjectCreateOrRemoveInfoClassConfiges | `TArray < FString >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
