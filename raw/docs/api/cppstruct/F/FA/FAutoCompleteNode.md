# FAutoCompleteNode

Node for storing an auto-complete tree based on each char in the command.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| IndexChar | `int32` | Char for node in the tree |
| AutoCompleteListIndices | `TArray < int32 >` | Indices into AutoCompleteList for commands that match to this level |
