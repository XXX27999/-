# UGameNetworkManagerSettings

Holds the settings for the AGameNetworkManager class.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MinDynamicBandwidth | `int32` | Minimum bandwidth dynamically set per connection. |
| MaxDynamicBandwidth | `int32` | Maximum bandwidth dynamically set per connection. |
| TotalNetBandwidth | `int32` | Total available bandwidth for listen server, split dynamically across net connections. |
| BadPingThreshold | `int32` | The point we determine the server is either delaying packets or has bad upstream. |
| bIsStandbyCheckingEnabled | `uint32` | Used to determine if checking for standby cheats should occur. |
| StandbyRxCheatTime | `float` | The amount of time without packets before triggering the cheat code. |
| StandbyTxCheatTime | `float` | The amount of time without packets before triggering the cheat code. |
| PercentMissingForRxStandby | `float` | The percentage of clients missing RX data before triggering the standby code. |
| PercentMissingForTxStandby | `float` | The percentage of clients missing TX data before triggering the standby code. |
| PercentForBadPing | `float` | The percentage of clients with bad ping before triggering the standby code. |
| JoinInProgressStandbyWaitTime | `float` | The amount of time to wait before checking a connection for standby issues. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
