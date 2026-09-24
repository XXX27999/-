# USoundNodeRandom

Selects sounds from a random set

## Parents

- [USoundNode](./USoundNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Weights | `TArray < float >` |  |
| PreselectAtLevelLoad | `int32` | If greater than 0, then upon each level load such a number of inputs will be randomly selected<br>	   and the rest will be removed. This can be used to cut down the memory usage of large randomizing<br>	   cues. |
| bRandomizeWithoutReplacement | `uint32` | Determines whether or not this SoundNodeRandom should randomize with or without<br>	  replacement.<br><br>	  WithoutReplacement means that only nodes left will be valid for<br>	  selection.  So with that, you are guarenteed to have only one occurrence of the<br>	  sound played until all of the other sounds in the set have all been played.<br><br>	  WithReplacement means that a node will be chosen and then placed back into the set.<br>	  So one could play the same sound over and over if the probabilities don't go your way :-) |
| HasBeenUsed | `TArray < bool >` | Internal state of which sounds have been played.  This is only used at runtime<br>	  to keep track of which sounds have been played |
| NumRandomUsed | `int32` | Counter var so we don't have to count all of the used sounds each time we choose a sound |
| PIEHiddenNodes | `TArray < int32 >` | Editor only list of nodes hidden to duplicate behavior of PreselectAtLevelLoad |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
