# FAnimNode_CurveSource

Supply curves from some external source (e.g. audio)

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SourcePose | `FPoseLink` |  |
| SourceBinding | `FName` | The binding of the curve source we want to bind to.<br>	  We will bind to an object that implements ICurveSourceInterface. First we check<br>	  the actor that owns this (if any), then we check each of its components to see if we should<br>	  bind to the source that matches this name. |
| Alpha | `float` | How much we wan to blend the curve in by |
| CurveSource | `TScriptInterface < ICurveSourceInterface >` | Our bound source |
