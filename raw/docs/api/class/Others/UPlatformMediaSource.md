# UPlatformMediaSource

A media source that selects other media sources based on target platform.

  Use this asset to override media sources on a per-platform basis.

## Parents

- [UMediaSource](./UMediaSource.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MediaSource | `UMediaSource *` | Default media source.<br><br>	  This media source will be used if no source was specified for a target platform. |
| PlatformMediaSources | `TMap < FString , UMediaSource * >` | Media sources per platform. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
