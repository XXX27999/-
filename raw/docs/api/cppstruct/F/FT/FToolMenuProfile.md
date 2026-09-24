# FToolMenuProfile

A menu profile is a way for systems to modify instances of a menu by showinghiding specific items. You can have multiple profiles active on
  a single menu at the same time.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Name | `FName` |  |
| Entries | `TMap < FName , FCustomizedToolMenuEntry >` |  |
| Sections | `TMap < FName , FCustomizedToolMenuSection >` |  |
| SuppressExtenders | `TArray < FName >` |  |
