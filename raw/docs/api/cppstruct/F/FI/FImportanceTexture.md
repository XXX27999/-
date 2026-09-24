# FImportanceTexture

Texture processed for importance sampling
 Holds marginal PDF of the rows, as well as the PDF of each row

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Size | [FIntPoint](./FIntPoint.md) |  |
| NumMips | `int` |  |
| MarginalCDF | `TArray < float >` |  |
| ConditionalCDF | `TArray < float >` |  |
| TextureData | `TArray < FColor >` |  |
| Texture | `TWeakObjectPtr < UTexture2D >` |  |
| Weighting | `TEnumAsByte < EImportanceWeight :: Type >` |  |
