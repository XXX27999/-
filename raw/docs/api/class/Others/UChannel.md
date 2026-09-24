# UChannel

Base class of communication channels.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Connection | `UNetConnection *` |  |
| OpenAcked | `uint32` |  |
| Closing | `uint32` |  |
| Dormant | `uint32` |  |
| bIsReplicationPaused | `uint32` |  |
| OpenTemporary | `uint32` |  |
| Broken | `uint32` |  |
| bTornOff | `uint32` |  |
| bPendingDormancy | `uint32` |  |
| bPausedUntilReliableACK | `uint32` |  |
| ChIndex | `int32` |  |
| OpenedLocally | `int32` |  |
| OpenPacketId | `FPacketIdRange` |  |
| ChType | `EChannelType` |  |
| NumInRec | `int32` |  |
| NumOutRec | `int32` |  |
| InRec | `FInBunch *` |  |
| OutRec | `FOutBunch *` |  |
| InPartialBunch | `FInBunch *` |  |
| bEnableSendBunchOpt | `bool` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
