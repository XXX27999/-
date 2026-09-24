# FOverlapResult

Structure containing information about one hit of an overlap test

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Actor | `TWeakObjectPtr < AActor >` | Actor that the check hit. |
| Component | `TWeakObjectPtr < UPrimitiveComponent >` | PrimitiveComponent that the check hit. |
| bBlockingHit | `uint32` | Indicates if this hit was requesting a block - if false, was requesting a touch instead |
