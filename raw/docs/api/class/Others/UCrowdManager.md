# UCrowdManager

## Parents

- UCrowdManagerBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MyNavData | `ANavigationData *` |  |
| AvoidanceConfig | `TArray < FCrowdAvoidanceConfig >` | obstacle avoidance params |
| SamplingPatterns | `TArray < FCrowdAvoidanceSamplingPattern >` | obstacle avoidance params |
| MaxAgents | `int32` | max number of agents supported by crowd |
| MaxAgentRadius | `float` | max radius of agent that can be added to crowd |
| MaxAvoidedAgents | `int32` | max number of neighbor agents for velocity avoidance |
| MaxAvoidedWalls | `int32` | max number of wall segments for velocity avoidance |
| NavmeshCheckInterval | `float` | how often should agents check their position after moving off navmesh? |
| PathOptimizationInterval | `float` | how often should agents try to optimize their paths? |
| SeparationDirClamp | `float` | clamp separation force to leftright when neighbor is behind (dot between forward and dirToNei, -1 = disabled) |
| PathOffsetRadiusMultiplier | `float` | agent radius multiplier for offsetting path around corners |
| bResolveCollisions | `uint32` | should crowd simulation resolve collisions between agents? if not, this will be handled by their movement components |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
