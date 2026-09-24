# AGameNetworkManager

Handles game-specific networking management (cheat detection, bandwidth management, etc.).

## Parents

- [AInfo](./AInfo.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AdjustedNetSpeed | `int32` | Current adjusted net speed - Used for dynamically managing netspeed for listen servers |
| LastNetSpeedUpdateTime | `float` | Last time netspeed was updated for server (by client entering or leaving) |
| TotalNetBandwidth | `int32` | Total available bandwidth for listen server, split dynamically across net connections |
| MinDynamicBandwidth | `int32` | Minimum bandwidth dynamically set per connection |
| MaxDynamicBandwidth | `int32` | Maximum bandwidth dynamically set per connection |
| bIsStandbyCheckingEnabled | `uint32` | Used to determine if checking for standby cheats should occur |
| bHasStandbyCheatTriggered | `uint32` | Used to determine whether we've already caught a cheat or not |
| StandbyRxCheatTime | `float` | The amount of time without packets before triggering the cheat code |
| StandbyTxCheatTime | `float` | The amount of time without packets before triggering the cheat code |
| BadPingThreshold | `int32` | The point we determine the server is either delaying packets or has bad upstream |
| PercentMissingForRxStandby | `float` | The percentage of clients missing RX data before triggering the standby code |
| PercentMissingForTxStandby | `float` | The percentage of clients missing TX data before triggering the standby code |
| PercentForBadPing | `float` | The percentage of clients with bad ping before triggering the standby code |
| JoinInProgressStandbyWaitTime | `float` | The amount of time to wait before checking a connection for standby issues |
| MoveRepSize | `float` | Average size of replicated move packet (ServerMove() packet size) from player |
| MAXPOSITIONERRORSQUARED | `float` | MAXPOSITIONERRORSQUARED is the square of the max position error that is accepted (not corrected) in net play |
| MAXNEARZEROVELOCITYSQUARED | `float` | MAXNEARZEROVELOCITYSQUARED is the square of the max velocity that is considered zero (not corrected) in net play |
| CLIENTADJUSTUPDATECOST | `float` | CLIENTADJUSTUPDATECOST is the bandwidth cost in bytes of sending a client adjustment update. 180 is greater than the actual cost, but represents a tweaked value reserving enough bandwidth for<br>	other updates sent to the client.  Increase this value to reduce client adjustment update frequency, or if the amount of data sent in the clientadjustment() call increases |
| MAXCLIENTUPDATEINTERVAL | `float` | MAXCLIENTUPDATEINTERVAL is the maximum time between movement updates from the client before the server forces an update. |
| MaxMoveDeltaTime | `float` | MaxMoveDeltaTime is the default maximum time delta of CharacterMovement ServerMoves. Should be less than or equal to MAXCLIENTUPDATEINTERVAL, otherwise server will interfere by forcing position updates. |
| ClientNetSendMoveDeltaTime | `float` | ClientNetSendMoveDeltaTime is the default minimum time delta of CharacterMovement client moves to the server. When updates occur more frequently, they may be combined to save bandwidth.<br>	  This value is not used when player count is over ClientNetSendMoveThrottleOverPlayerCount or player net speed is <= ClientNetSendMoveThrottleAtNetSpeed (see ClientNetSendMoveDeltaTimeThrottled). |
| ClientNetSendMoveDeltaTimeThrottled | `float` | ClientNetSendMoveDeltaTimeThrottled is used in place of ClientNetSendMoveDeltaTime when player count is high or net speed is low. See ClientNetSendMoveDeltaTime for more info. |
| ClientNetSendMoveDeltaTimeStationary | `float` | ClientNetSendMoveDeltaTimeStationary is used when players are determined to not be moving or changing their view. See ClientNetSendMoveDeltaTime for more info. |
| ClientNetSendMoveThrottleAtNetSpeed | `int32` | When player net speed (CurrentNetSpeed, based on ConfiguredInternetSpeed or ConfiguredLanSpeed) is less than or equal to this amount, ClientNetSendMoveDeltaTimeThrottled is used instead of ClientNetSendMoveDeltaTime. |
| ClientNetSendMoveThrottleOverPlayerCount | `int32` | When player count is greater than this amount, ClientNetSendMoveDeltaTimeThrottled is used instead of ClientNetSendMoveDeltaTime. |
| ClientAuthorativePosition | `bool` | If client update is within MAXPOSITIONERRORSQUARED then he is authorative on his final position |
| ClientErrorUpdateRateLimit | `float` | Minimum delay between the server sending error corrections to a client, in seconds. |
| bMovementTimeDiscrepancyDetection | `bool` | Whether movement time discrepancy detection is enabled. |
| bMovementTimeDiscrepancyResolution | `bool` | Whether movement time discrepancy resolution is enabled (when detected, make client movement "pay back" excessive time discrepancies) |
| MovementTimeDiscrepancyMaxTimeMargin | `float` | Maximum time client can be ahead before triggering movement time discrepancy detectionresolution (if enabled). |
| MovementTimeDiscrepancyMinTimeMargin | `float` | Maximum time client can be behind. |
| MovementTimeDiscrepancyResolutionRate | `float` | During time discrepancy resolution, we "pay back" the time discrepancy at this rate for future moves until total error is zero.<br>	  1.0 = 100% resolution rate, meaning the next X ServerMoves from the client are fully paying back the time,<br>	  0.5 = 50% resolution rate, meaning future ServerMoves will spend 50% of tick continuing to move the character and 50% paying back.<br>	  Lowering from 100% could be used to produce less severenoticeable corrections, although typically we would want to correct<br>	  the client as quickly as possible. |
| MovementTimeDiscrepancyDriftAllowance | `float` | Accepted drift in clocks between client and server as a percent per second allowed.<br><br>	  0.0 is "no forgiveness" and all logic would run on raw values, no tampering on the server side.<br>	  0.02 would be a 2% per second difference "forgiven" - if the time discrepancy in a given second was less than 2%,<br>	  the error handlingdetection code effectively ignores it.<br><br>	  Increasing this value above 0% lessens the chance of false positives on time discrepancy (burst packet loss, performance<br>	  hitches), but also means anyone tampering with their client time below that percent will not be detected and no resolution<br>	  action will be taken, and anyone above that threshold will still gain the advantage of this % of time boost (if running at<br>	  10% speed-up and this value is 0.05 or 5% allowance, they would only be resolved down to a 5% speed boost).<br><br>	  Time discrepancy detection code DOES keep track of LifetimeRawTimeDiscrepancy, which is unaffected by this drift allowance,<br>	  so cheating below DriftAllowance percent could be tracked and acted on outside of an individual game. For example, if DriftAllowance<br>	  was 0.05 (meaning we're not going to actively prevent any cheating below 5% boosts to ensure less false positives for normal players),<br>	  we could still post-process analytics of the game showing that Player X regularly runs at 4% speed boost and take action. |
| bMovementTimeDiscrepancyForceCorrectionsDuringResolution | `bool` | Whether client moves should be force corrected during time discrepancy resolution, useful for projects that have lenient<br>	  move error toleranceClientAuthorativePosition enabled. |
| bUseDistanceBasedRelevancy | `bool` | If true, actor network relevancy is constrained by whether they are within their NetCullDistanceSquared from the client's view point. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
