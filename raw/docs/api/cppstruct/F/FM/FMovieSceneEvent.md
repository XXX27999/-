# FMovieSceneEvent

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Ptrs | [FMovieSceneEventPtrs](./FMovieSceneEventPtrs.md) | The function that should be called to invoke this event.<br>	 Functions must have either no parameters, or a single, pass-by-value objectinterface parameter, with no return parameter. |
| PayloadVariables | `TMap < FName , FMovieSceneEventPayloadVariable >` | Array of payload variables to be added to the generated function |
| CompiledFunctionName | `FName` |  |
| BoundObjectPinName | `FName` |  |
| WeakEndpoint | `TWeakObjectPtr < UObject >` | Serialized weak pointer to the function entry (UK2Node_FunctionEntry) or custom event node (UK2Node_CustomEvent) within the blueprint graph for this event. Stored as an editor-only UObject so UHT can parse it when building for non-editor. |
| GraphGuid_DEPRECATED | [FGuid](../FG/FGuid.md) | (deprecated) The UEdGraph::GraphGuid property that relates the graph within which our endpoint lives. |
| NodeGuid_DEPRECATED | [FGuid](../FG/FGuid.md) | (deprecated) When valid, relates to the The UEdGraphNode::NodeGuid for a custom event node that defines our event endpoint. When invalid, we must be bound to a UBlueprint::FunctionGraphs graph. |
| FunctionEntry_DEPRECATED | `TWeakObjectPtr < UObject >` | Deprecated weak pointer to the function entry to call - no longer serialized but cached on load. Predates GraphGuid and NodeGuid |
