# FPacketSimulationSettings

Holds the packet simulation settings in one place

## Fields

| Name | Type | Description |
| --- | --- | --- |
| PktLoss | `int32` | When set, will cause calls to FlushNet to drop packets.<br>	  Value is treated as % of packets dropped (i.e. 0 = None, 100 = All).<br>	  No general pattern  ordering is guaranteed.<br>	  Clamped between 0 and 100.<br><br>	  Works with all other settings. |
| PktOrder | `int32` | When set, will cause calls to FlushNet to change ordering of packets at random.<br>	  Value is treated as a bool (i.e. 0 = False, anything else = True).<br>	  This works by randomly selecting packets to be delayed until a subsequent call to FlushNet.<br><br>	  Takes precedence over PktDup and PktLag. |
| PktLag | `int32` | When set, will cause calls to FlushNet to delay packets.<br>	  Value is treated as millisecond lag.<br><br>	  Cannot be used with PktOrder. |
| PktDup | `int32` | When set, will cause calls to FlushNet to duplicate packets.<br>	  Value is treated as % of packets duplicated (i.e. 0 = None, 100 = All).<br>	  No general pattern  ordering is guaranteed.<br>	  Clamped between 0 and 100.<br><br>	  Cannot be used with PktOrder or PktLag. |
| PktLagVariance | `int32` | When set, will cause PktLag to use variable lag instead of constant.<br>	  Value is treated as millisecond lag range (e.g. -GivenVariance <= 0 <= GivenVariance).<br>	  Clamped between 0 and 100.<br><br>	  Can only be used when PktLag is enabled. |
| PktIncomingLoss | `int32` | The ratio of incoming packets that will be dropped<br>	  to simulate packet loss |
