# FAdditionalRescanRootEntry

One entry of UWorldComposition extra scan roots.
  Allows a persistent map to pull in tiles from directories outside its own folder
  (e.g. shared tile libraries), with per-root include  exclude filtering.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| RootPath | `FString` | Long Package Path (must be a registered content mount), e.g. "GameCommonSharedTiles".<br>	  Leading and trailing slashes are normalized automatically. |
| IncludeTiles | `TArray < FString >` | If non-empty, ONLY tiles produced by RootPath whose long package name matches one of these<br>	  patterns are kept. Pattern syntax:<br>	    "Forest"                              -> folder prefix relative to RootPath<br>	    "ForestTile_X1_Y1"                    -> exact tile, relative to RootPath<br>	    "GameCommonSharedTilesForest"     -> absolute folder prefix<br>	    "GameCommonSharedTilesForestTile_X1_Y1" -> absolute exact tile<br>	  Folder patterns must end with ''. |
| ExcludeTiles | `TArray < FString >` | Same syntax as IncludeTiles. Tiles matching any pattern here are dropped.<br>	  Applied AFTER IncludeTiles, so a tile must (pass include) AND (not match exclude) to survive. |
