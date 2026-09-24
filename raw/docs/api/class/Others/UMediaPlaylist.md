# UMediaPlaylist

Implements a media play list.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Loop | `uint32` | Whether the play list should loop (default = true). |
| Items | `TArray < UMediaSource * >` | List of media sources to play. |

## Functions

### Add

Add a media source to the play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MediaSource | `UMediaSource *` | The media source to append. |

**Return**

- Type: 
- Description: _None_

### AddFile

Add a media file path to the play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FilePath | `FString &` | The file path to add. |

**Return**

- Type: 
- Description: _None_

### AddUrl

Add a media URL to the play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Url | `FString &` | The URL to add. |

**Return**

- Type: 
- Description: _None_

### Get

Get the media source at the specified index.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | The index of the media source to get. |

**Return**

- Type: 
- Description: _None_

### GetNext

Get the next media source in the play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOutIndex | `int32 &` | Index of the current media source (will contain the new index). |

**Return**

- Type: 
- Description: _None_

### GetPrevious

Get the previous media source in the play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOutIndex | `int32 &` | Index of the current media source (will contain the new index). |

**Return**

- Type: 
- Description: _None_

### GetRandom

Get a random media source in the play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutIndex | `int32 &` | Will contain the index of the returned media source. |

**Return**

- Type: 
- Description: _None_

### Insert

Insert a media source into the play list at the given position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MediaSource | `UMediaSource *` | The media source to insert. |
| Index | `int32` | The index to insert into. |

**Return**

- Type: 
- Description: _None_

### Num

Get the number of media sources in the play list.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Remove

Remove all occurrences of the given media source in the play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MediaSource | `UMediaSource *` | The media source to remove. |

**Return**

- Type: 
- Description: _None_

### RemoveAt

Remove the media source at the specified position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | The index of the media source to remove. |

**Return**

- Type: 
- Description: _None_

### Replace

Replace the media source at the specified position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | The index of the media source to replace. |
| Replacement | `UMediaSource *` | The replacement media source. |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
