# FExternalToolDefinition

Structure for defining an external tool

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ToolName | `FString` | The name of the tool  test. |
| ExecutablePath | [FFilePath](../FF/FFilePath.md) | The executable to run.<br>	UPROPERTY(config, EditAnywhere, Category=ExternalTools, meta=(FilePathFilter = "")) |
| CommandLineOptions | `FString` | The command line options to pass to the executable. |
| WorkingDirectory | [FDirectoryPath](../FD/FDirectoryPath.md) | The working directory for the new process. |
| ScriptExtension | `FString` | If set, look for scripts with this extension. |
| ScriptDirectory | [FDirectoryPath](../FD/FDirectoryPath.md) | If the ScriptExtension is set, look here for the script files. |
