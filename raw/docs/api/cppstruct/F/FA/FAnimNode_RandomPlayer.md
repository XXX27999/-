# FAnimNode_RandomPlayer

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bShuffleMode | `bool` | When shuffle mode is active we will never loop a sequence beyond MaxLoopCount<br>	   without visiting each sequence in turn (no repeats). Enabling this will ignore<br>	   ChanceToPlay for each entry |
| Entries | `TArray < FRandomPlayerSequenceEntry >` | List of sequences to randomly step through |
