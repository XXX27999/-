# UBlueprintGameplayTagLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### MatchesTag

Determine if TagOne matches against TagTwo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagOne | `FGameplayTag` | Tag to check for match |
| TagTwo | `FGameplayTag` | Tag to check match against |
| bExactMatch | `bool` | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |

**Return**

- Type: 
- Description: _None_

### MatchesAnyTags

Determine if TagOne matches against any tag in OtherContainer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagOne | `FGameplayTag` | Tag to check for match |
| OtherContainer | `FGameplayTagContainer &` | Container to check against. |
| bExactMatch | `bool` | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |

**Return**

- Type: 
- Description: _None_

### EqualEqual_GameplayTag

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGameplayTag` |  |
| B | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_GameplayTag

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGameplayTag` |  |
| B | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) |  |

**Return**

- Type: 
- Description: _None_

### IsGameplayTagValid

Returns true if the passed in gameplay tag is non-null

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GameplayTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) |  |

**Return**

- Type: 
- Description: _None_

### GetTagName

Returns FName of this tag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GameplayTag | `FGameplayTag &` |  |

**Return**

- Type: 
- Description: _None_

### MakeLiteralGameplayTag

Creates a literal FGameplayTag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) |  |

**Return**

- Type: 
- Description: _None_

### GetNumGameplayTagsInContainer

Get the number of gameplay tags in the specified container

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` | Tag container to get the number of tags from |

**Return**

- Type: 
- Description: _None_

### HasTag

Check if the tag container has the specified tag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` | Container to check for the tag |
| Tag | `FGameplayTag` | Tag to check for in the container |
| bExactMatch | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Return**

- Type: 
- Description: _None_

### HasAnyTags

Check if the specified tag container has ANY of the tags in the other container

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` | Container to check if it matches any of the tags in the other container |
| OtherContainer | `FGameplayTagContainer &` | Container to check against. |
| bExactMatch | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Return**

- Type: 
- Description: _None_

### HasAllTags

Check if the specified tag container has ALL of the tags in the other container

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` | Container to check if it matches all of the tags in the other container |
| OtherContainer | `FGameplayTagContainer &` | Container to check against. If this is empty, the check will succeed |
| bExactMatch | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Return**

- Type: 
- Description: _None_

### DoesContainerMatchTagQuery

Check if the specified tag container matches the given Tag Query

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` | Container to check if it matches all of the tags in the other container |
| TagQuery | `FGameplayTagQuery &` | Query to match against |

**Return**

- Type: 
- Description: _None_

### GetAllActorsOfClassMatchingTagQuery

Get an array of all actors of a specific class (or subclass of that class) which match the specified gameplay tag query.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ActorClass | `TSubclassOf < AActor >` | Class of actors to fetch |
| GameplayTagQuery | `FGameplayTagQuery &` | Query to match against |
| OutActors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### AddGameplayTag

Adds a single tag to the passed in tag container

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` |  |
| Tag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | The tag to add to the container |

**Return**

- Type: 
- Description: _None_

### RemoveGameplayTag

Remove a single tag from the passed in tag container, returns true if found

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` |  |
| Tag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | The tag to add to the container |

**Return**

- Type: 
- Description: _None_

### AppendGameplayTagContainers

Appends all tags in the InTagContainer to InOutTagContainer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOutTagContainer | `FGameplayTagContainer &` | The container that will be appended too. |
| InTagContainer | `FGameplayTagContainer &` | The container to append. |

**Return**

- Type: 
- Description: _None_

### EqualEqual_GameplayTagContainer

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGameplayTagContainer &` |  |
| B | `FGameplayTagContainer &` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_GameplayTagContainer

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGameplayTagContainer &` |  |
| B | `FGameplayTagContainer &` |  |

**Return**

- Type: 
- Description: _None_

### MakeLiteralGameplayTagContainer

Creates a literal FGameplayTagContainer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [FGameplayTagContainer](../../cppstruct/F/FG/FGameplayTagContainer.md) |  |

**Return**

- Type: 
- Description: _None_

### MakeGameplayTagContainerFromArray

Creates a FGameplayTagContainer from the array of passed in tags

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GameplayTags | `TArray < FGameplayTag > &` |  |

**Return**

- Type: 
- Description: _None_

### MakeGameplayTagContainerFromTag

Creates a FGameplayTagContainer containing a single tag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SingleTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) |  |

**Return**

- Type: 
- Description: _None_

### BreakGameplayTagContainer

Breaks tag container into explicit array of tags

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GameplayTagContainer | `FGameplayTagContainer &` |  |
| GameplayTags | `TArray < FGameplayTag > &` |  |

**Return**

- Type: 
- Description: _None_

### MakeGameplayTagQuery

Creates a literal FGameplayTagQuery

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagQuery | [FGameplayTagQuery](../../cppstruct/F/FG/FGameplayTagQuery.md) | value to set the FGameplayTagQuery to |

**Return**

- Type: 
- Description: _None_

### HasAllMatchingGameplayTags

Check Gameplay tags in the interface has all of the specified tags in the tag container (expands to include parents of asset tags)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainerInterface | `TScriptInterface < IGameplayTagAssetInterface >` | An Interface to a tag container |
| OtherContainer | `FGameplayTagContainer &` | A Tag Container |

**Return**

- Type: 
- Description: _None_

### DoesTagAssetInterfaceHaveTag

Check if the specified tag container has the specified tag, using the specified tag matching types

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainerInterface | `TScriptInterface < IGameplayTagAssetInterface >` | An Interface to a tag container |
| Tag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | Tag to check for in the container |

**Return**

- Type: 
- Description: _None_

### NotEqual_TagTag

Checks if a gameplay tag's name and a string are not equal to one another

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGameplayTag` |  |
| B | `FString` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_TagContainerTagContainer

Checks if a gameplay tag containers's name and a string are not equal to one another

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGameplayTagContainer` |  |
| B | `FString` |  |

**Return**

- Type: 
- Description: _None_

### GetDebugStringFromGameplayTagContainer

Returns an FString listing all of the gameplay tags in the tag container for debugging purposes.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TagContainer | `FGameplayTagContainer &` | The tag container to get the debug string from. |

**Return**

- Type: 
- Description: _None_

### GetDebugStringFromGameplayTag

Returns an FString representation of a gameplay tag for debugging purposes.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GameplayTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | The tag to get the debug string from. |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
