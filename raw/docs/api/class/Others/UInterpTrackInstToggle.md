# UInterpTrackInstToggle

## Parents

- UInterpTrackInst

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Action | `TEnumAsByte < enum ETrackToggleAction >` |  |
| LastUpdatePosition | `float` | Position we were in last time we evaluated.<br>	 	During UpdateTrack, toggles between this time and the current time will be processed. |
| bSavedActiveState | `uint32` | Cached 'active' state for the toggleable actor before we possessed it; restored when Matinee exits |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
