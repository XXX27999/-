# FLightmassDebugOptions

Debug options for Lightmass

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bStatsEnabled | `uint32` | If true, all participating Lightmass agents will report back detailed stats to the log. |
| bGatherBSPSurfacesAcrossComponents | `uint32` | If true, BSP surfaces split across model components are joined into 1 mapping |
| CoplanarTolerance | `float` | The tolerance level used when gathering BSP surfaces. |
| bDebugMode | `uint32` | If false, UnrealLightmass.exe is launched automatically (default)<br>	 	If true, it must be launched manually (e.g. through a debugger) with the -debug command line parameter. |
| bUseImmediateImport | `uint32` | If true, Lightmass will import mappings immediately as they complete.<br>	 	It will not process them, however. |
| bImmediateProcessMappings | `uint32` | If true, Lightmass will process appropriate mappings as they are imported.<br>	 	NOTE: Requires ImmediateMode be enabled to actually work. |
| bSortMappings | `uint32` | If true, Lightmass will sort mappings by texel cost. |
| bDumpBinaryFiles | `uint32` | If true, the generate coefficients will be dumped to binary files. |
| bDebugMaterials | `uint32` | If true, Lightmass will write out BMPs for each generated material property<br>	 	sample to <GAME>\ScreenShots\Materials. |
| bPadMappings | `uint32` | If true, Lightmass will pad the calculated mappings to reduceeliminate seams. |
| bDebugPaddings | `uint32` | If true, will fill padding of mappings with a color rather than the sampled edges.<br>	 	Means nothing if bPadMappings is not enabled... |
| bOnlyCalcDebugTexelMappings | `uint32` | If true, only the mapping containing a debug texel will be calculated, all others<br>	  will be set to white |
| bUseRandomColors | `uint32` | If true, color lightmaps a random color |
| bColorBordersGreen | `uint32` | If true, a green border will be placed around the edges of mappings |
| bColorByExecutionTime | `uint32` | If true, Lightmass will overwrite lightmap data with a shade of red relating to<br>	  how long it took to calculate the mapping (Red = Time  ExecutionTimeDivisor) |
| ExecutionTimeDivisor | `float` | The amount of time that will be count as full red when bColorByExecutionTime is enabled |
