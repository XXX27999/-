# FBPInterfaceDescription

Struct containing information about what interfaces are implemented in this blueprint

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Interface | `TSubclassOf < UInterface >` | Reference to the interface class we're adding to this blueprint |
| Graphs | `TArray < UEdGraph * >` | References to the graphs associated with the required functions for this interface |
