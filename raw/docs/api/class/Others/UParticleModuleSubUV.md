# UParticleModuleSubUV

## Parents

- UParticleModuleSubUVBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Animation | `USubUVAnimation *` | SubUV animation asset to use.<br>	  When specified, optimal bounding geometry for each SubUV frame will be used when rendering the sprites for this emitter instead of full quads.<br>	  This reduction in overdraw can reduce the GPU cost of rendering the emitter by 2x or 3x, depending on how much unused space was in the texture.<br>	  The bounding geometry is generated off of the texture alpha setup in the SubUV Animation asset, so that has to match what the material is using for opacity, or clipping will occur.<br>	  When specified, SubImages_Horizontal and SubImages_Vertical will come from the asset instead of the Required Module. |
| SubImageIndex | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The index of the sub-image that should be used for the particle.<br>	 	The value is retrieved using the RelativeTime of the particles. |
| bUseRealTime | `uint32` | If true, use real time when updating the image index.<br>	 	The movie will update regardless of the slomo settings of the game. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
