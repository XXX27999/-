# FSoundGroup

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SoundGroup | `TEnumAsByte < ESoundGroup >` |  |
| DisplayName | `FString` |  |
| bAlwaysDecompressOnLoad | `uint32` |  |
| DecompressedDuration | `float` | Sound duration in seconds below which sounds are entirely expanded to PCM at load time<br>	  Disregarded if bAlwaysDecompressOnLoad is true |
