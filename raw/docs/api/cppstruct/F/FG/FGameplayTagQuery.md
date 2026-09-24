# FGameplayTagQuery

Queries are internally represented as a byte stream that is memory-efficient and can be evaluated quickly at runtime.
  Note: these have an extensive details and graph pin customization for editing, so there is no need to expose the internals to Blueprints.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TokenStreamVersion | `int32` | Versioning for future token stream protocol changes. See EGameplayTagQueryStreamVersion. |
| TagDictionary | `TArray < FGameplayTag >` | List of tags referenced by this entire query. Token stream stored indices into this list. |
| QueryTokenStream | `TArray < uint8 >` | Stream representation of the actual hierarchical query |
| UserDescription | `FString` | User-provided string describing the query |
| AutoDescription | `FString` | Auto-generated string describing the query |
