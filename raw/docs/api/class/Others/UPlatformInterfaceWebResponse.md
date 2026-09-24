# UPlatformInterfaceWebResponse

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OriginalURL | `FString` | This holds the original requested URL |
| ResponseCode | `int32` | Result code from the response (200=OK, 404=Not Found, etc) |
| Tag | `int32` | A user-specified tag specified with the request |
| StringResponse | `FString` | For string results, this is the response |
| BinaryResponse | `TArray < uint8 >` | For non-string results, this is the response |

## Functions

### GetNumHeaders

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetHeader

Retrieve the header and value for the given index of headervalue pair

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HeaderIndex | `int32` |  |
| Header | `FString &` |  |
| Value | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetHeaderValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HeaderName | `FString &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
