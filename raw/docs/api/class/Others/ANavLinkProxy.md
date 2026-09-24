# ANavLinkProxy

## Parents

- [AActor](./AActor.md)
- INavLinkHostInterface
- INavRelevantInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PointLinks | `TArray < FNavigationLink >` | Navigation links (point to point) added to navigation data |
| SegmentLinks | `TArray < FNavigationSegmentLink >` | Navigation links (segment to segment) added to navigation data<br>		@todo hidden from use until we fix segment links. Not really working now |
| SmartLinkComp | `UNavLinkCustomComponent *` | Smart link: can affect path following |
| bSmartLinkIsRelevant | `bool` | Smart link: toggle relevancy |
| EdRenderComp | `UNavLinkRenderingComponent *` | Editor Preview |
| SpriteComponent | `UBillboardComponent *` |  |

## Functions

### ReceiveSmartLinkReached

called when agent reaches smart link during path following, use ResumePathFollowing() to give control back

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Agent | `AActor *` |  |
| Destination | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### ResumePathFollowing

resume normal path following

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Agent | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### IsSmartLinkEnabled

check if smart link is enabled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSmartLinkEnabled

change state of smart link

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### HasMovingAgents

check if any agent is moving through smart link right now

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnSmartLinkReached |  |  |

## Language

cpp
