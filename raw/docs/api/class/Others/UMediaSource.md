# UMediaSource

Abstract base class for media sources.

  Media sources describe the location andor settings of media objects that can
  be played in a media player, such as a video file on disk, a video stream on
  the internet, or a web cam attached to or built into the target device. The
  location is encoded as a media URL string, whose URI scheme and optional file
  extension will be used to locate a suitable media player.

## Parents

- [UObject](./UObject.md)
- IMediaOptions

## Variables

_None_

## Functions

### GetUrl

Get the media source's URL string (must be implemented in child classes).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Validate

Validate the media source settings (must be implemented in child classes).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp
