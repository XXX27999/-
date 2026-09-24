# UGameplayTagsSettings

Class for importing GameplayTags directly from a config file.
 	FGameplayTagsEditorModule::StartupModule adds this class to the Project Settings menu to be edited.
 	Editing this in Project Settings will output changes to ConfigDefaultGameplayTags.ini.

 	Primary advantages of this approach are:
 	-Adding new tags doesn't require checking out external and editing file (CSV or xls) then reimporting.
 	-New tags are mergeable since .ini are text and non exclusive checkout.

 	To do:
 	-Better support could be added for adding new tags. We could match existing tags and autocomplete subtags as
 	the user types (e.g, autocomplete 'Damage.Physical' as the user is adding a 'Damage.Physical.Slash' tag).

## Parents

- [UGameplayTagsList](./UGameplayTagsList.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ImportTagsFromConfig | `bool` | If true, will import tags from ini files in the configtags folder |
| WarnOnInvalidTags | `bool` | If true, will give load warnings when reading invalid tags off disk |
| InvalidTagCharacters | `FString` | These characters cannot be used in gameplay tags, in addition to special ones like newline |
| CategoryRemapping | `TArray < FGameplayTagCategoryRemap >` |  |
| FastReplication | `bool` | If true, will replicate gameplay tags by index instead of name. For this to work, tags must be identical on client and server |
| GameplayTagTableList | `TArray < FSoftObjectPath >` | List of data tables to load tags from |
| GameplayTagRedirects | `TArray < FGameplayTagRedirect >` | List of active tag redirects |
| CommonlyReplicatedTags | `TArray < FName >` | List of tags most frequently replicated |
| NumBitsForContainerSize | `int32` | Numbers of bits to use for replicating container size, set this based on how large your containers tend to be |
| NetIndexFirstBitSegment | `int32` | The length in bits of the first segment when net serializing tags. We will serialize NetIndexFirstBitSegment + 1 bit to indicate "more", which is slower to replicate |
| GameplayTagDontNeedFastReplicationList | `TArray < FName >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
