# FEditorImportExportTestDefinition

Holds settings for the asset import  export automation test

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ImportFilePath | [FFilePath](../FF/FFilePath.md) | The file to import<br>	UPROPERTY(config, EditAnywhere, Category = Automation, meta = (FilePathFilter = "")) |
| ExportFileExtension | `FString` | The file extension to use when exporting |
| bSkipExport | `bool` | If true, the export step will be skipped |
| FactorySettings | `TArray < FImportFactorySettingValues >` | Settings for the import factory |
