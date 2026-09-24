# UTwitterIntegrationBase

## Parents

- [UPlatformInterfaceBase](./UPlatformInterfaceBase.md)

## Variables

_None_

## Functions

### Init

Perform any needed initialization

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CanShowTweetUI

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ShowTweetUI

Kicks off a tweet, using the platform to show the UI. If this returns false, or you are on a platform that doesn't support the UI,
	  you can use the TwitterRequest method to perform a manual tweet using the Twitter API

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InitialMessage | `FString &` | [optional] Initial message to show |
| URL | `FString &` | [optional] URL to attach to the tweet |
| Picture | `FString &` | [optional] Name of a picture (stored locally, platform subclass will do the searching for it) to add to the tweet |

**Return**

- Type: 
- Description: _None_

### AuthorizeAccounts

Starts the process of authorizing the local user(s). When TID_AuthorizeComplete is called, then GetNumAccounts()
	  will return a valid number of accounts

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetNumAccounts

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAccountName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AccountIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### TwitterRequest

Kicks off a generic twitter request

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| URL | `FString &` | The URL for the twitter request |
| ParamKeysAndValues | `TArray < FString > &` |  |
| RequestMethod | `ETwitterRequestMethod` |  |
| AccountIndex | `int32` | A user index if an account is needed, or -1 if an account isn't needed for the request |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
