# UMediaPlayer

Implements a media player asset that can play movies and other media sources.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CacheAhead | `FTimespan` | Duration of samples to cache ahead of the play head.<br><br>	  @see CacheBehind, CacheBehindGame |
| CacheBehind | `FTimespan` | Duration of samples to cache behind the play head (when not running as game).<br><br>	  @see CacheAhead, CacheBehindGame |
| CacheBehindGame | `FTimespan` | Duration of samples to cache behind the play head (when running as game).<br><br>	  @see CacheAhead, CacheBehind |
| NativeAudioOut | `bool` | Output any audio via the operating system's sound mixer instead of a Sound Wave asset.<br><br>	  If enabled, the assigned Sound Wave asset will be ignored. The SetNativeVolume<br>	  function can then be used to change the audio output volume at runtime. Note that<br>	  not all media player plug-ins may support native audio output on all platforms.<br><br>	  @see SetNativeVolume |
| PlayOnOpen | `bool` | Automatically start playback after media opened successfully.<br><br>	  If disabled, listen to the OnMediaOpened Blueprint event to detect when<br>	  the media finished opening, and then start playback using the Play function.<br><br>	  @see OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Play |
| Shuffle | `uint32` | Whether playback should shuffle media sources in the play list.<br><br>	  @see OpenPlaylist, OpenPlaylistIndex |
| Loop | `uint32` | Whether the player should loop when media playback reaches the end.<br><br>	  Use the SetLooping function to change this value at runtime.<br><br>	  @see IsLooping, SetLooping |
| Playlist | `UMediaPlaylist *` | The play list to use, if any.<br><br>	  Use the OpenPlaylist or OpenPlaylistIndex function to change this value at runtime.<br><br>	  @see OpenPlaylist, OpenPlaylistIndex |
| PlaylistIndex | `int32` | The current index of the source in the play list being played.<br><br>	  Use the Previous and Next methods to change this value at runtime.<br><br>	  @see Next, Previous |
| HorizontalFieldOfView | `float` | The initial horizontal field of view (in Euler degrees; default = 90).<br><br>	  This setting is used only for 360 videos. It determines the portion of the<br>	  video that is visible at a time. To modify the field of view at runtime in<br>	  Blueprints, use the SetHorizontalFieldOfView function.<br><br>	  @see GetHorizontalFieldOfView, SetHorizontalFieldOfView, VerticalFieldOfView, ViewRotation |
| VerticalFieldOfView | `float` | The initial vertical field of view (in Euler degrees; default = 60).<br><br>	  This setting is used only for 360 videos. It determines the portion of the<br>	  video that is visible at a time. To modify the field of view at runtime in<br>	  Blueprints, use the SetHorizontalFieldOfView function.<br><br>	  Please note that some 360 video players may be able to change only the<br>	  horizontal field of view, and this setting may be ignored.<br><br>	  @see GetVerticalFieldOfView, SetVerticalFieldOfView, HorizontalFieldOfView, ViewRotation |
| ViewRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | The initial view rotation.<br><br>	  This setting is used only for 360 videos. It determines the rotation of<br>	  the video's view. To modify the view orientation at runtime in Blueprints,<br>	  use the GetViewRotation and SetViewRotation functions.<br><br>	  Please note that not all players may support video view rotations.<br><br>	  @see GetViewRotation, SetViewRotation, HorizontalFieldOfView, VerticalFieldOfView |
| PlayerGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) | The player's globally unique identifier. |

## Functions

### CanPause

Check whether media playback can be paused right now.

	  Playback can be paused if the media supports pausing and if it is currently playing.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CanPlaySource

Check whether the specified media source can be played by this player.

	  If a desired player name is set for this player, it will only check
	  whether that particular player type can play the specified source.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MediaSource | `UMediaSource *` | The media source to check. |

**Return**

- Type: 
- Description: _None_

### CanPlayUrl

Check whether the specified URL can be played by this player.

	  If a desired player name is set for this player, it will only check
	  whether that particular player type can play the specified URL.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Url | `FString &` | The URL to check. |

**Return**

- Type: 
- Description: _None_

### Close

Close the currently open media, if any.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAudioTrackChannels

Get the number of channels in the specified audio track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | Index of the audio track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetAudioTrackSampleRate

Get the sample rate of the specified audio track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | Index of the audio track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetAudioTrackType

Get the type of the specified audio track format.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetDesiredPlayerName

Get the name of the current desired native player.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDuration

Get the media's duration.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetHorizontalFieldOfView

Get the current horizontal field of view (only for 360 videos).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMediaName

Get the human readable name of the currently loaded media source.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetNumTracks

Get the number of tracks of the given type.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | [EMediaPlayerTrack](../../cppenum/E/EM/EMediaPlayerTrack.md) | The type of media tracks. |

**Return**

- Type: 
- Description: _None_

### GetNumTrackFormats

Get the number of formats of the specified track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | `EMediaPlayerTrack` | The type of media tracks. |
| TrackIndex | `int32` | The index of the track. |

**Return**

- Type: 
- Description: _None_

### GetPlayerName

Get the name of the current native media player.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlaylist

Get the current play list.

	  Media players always have a valid play list. In C++ code you can use
	  the GetPlaylistRef to get a reference instead of a pointer to it.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlaylistIndex

Get the current play list index.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRate

Get the media's current playback rate.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSelectedTrack

Get the index of the currently selected track of the given type.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | [EMediaPlayerTrack](../../cppenum/E/EM/EMediaPlayerTrack.md) | The type of track to get. |

**Return**

- Type: 
- Description: _None_

### GetSupportedRates

Get the supported playback rates.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutRates | `TArray < FFloatRange > &` |  |
| Unthinned | `bool` | Whether the rates are for unthinned playback. |

**Return**

- Type: 
- Description: _None_

### GetTime

Get the media's current playback time.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTrackDisplayName

Get the human readable name of the specified track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | `EMediaPlayerTrack` | The type of track. |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetTrackFormat

Get the index of the active format of the specified track type.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | `EMediaPlayerTrack` | The type of track. |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetTrackLanguage

Get the language tag of the specified track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | `EMediaPlayerTrack` | The type of track. |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetUrl

Get the URL of the currently loaded media, if any.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVerticalFieldOfView

Get the current vertical field of view (only for 360 videos).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVideoTrackAspectRatio

Get the aspect ratio of the specified video track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | Index of the video track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetVideoTrackDimensions

Get the current dimensions of the specified video track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetVideoTrackFrameRate

Get the frame rate of the specified video track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetVideoTrackFrameRates

Get the supported range of frame rates of the specified video track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetVideoTrackType

Get the type of the specified video track format.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Return**

- Type: 
- Description: _None_

### GetViewRotation

Get the current view rotation (only for 360 videos).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasError

Check whether the player is in an error state.

	  When the player is in an error state, no further operations are possible.
	  The current media must be closed, and a new media source must be opened
	  before the player can be used again. Errors are usually caused by faulty
	  media files or interrupted network connections.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsBuffering

Check whether playback is buffering data.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsConnecting

Check whether the player is currently connecting to a media source.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsLooping

Check whether playback is looping.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPaused

Check whether playback is currently paused.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlaying

Check whether playback has started.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPreparing

Check whether the media is currently opening or buffering.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsReady

Check whether media is ready for playback.

	  A player is ready for playback if it has a media source opened that
	  finished preparing and is not in an error state.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Next

Open the next item in the current play list.

	  The player will start playing the new media source if it was playing
	  something previously, otherwise it will only open the media source.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OpenFile

Opens the specified media file path.

	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FilePath | `FString &` | The file path to open. |

**Return**

- Type: 
- Description: _None_

### OpenPlaylist

Open the first media source in the specified play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPlaylist | `UMediaPlaylist *` | The play list to open. |

**Return**

- Type: 
- Description: _None_

### OpenPlaylistIndex

Open a particular media source in the specified play list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPlaylist | `UMediaPlaylist *` | The play list to open. |
| Index | `int32` | The index of the source to open. |

**Return**

- Type: 
- Description: _None_

### OpenSource

Open the specified media source.

	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MediaSource | `UMediaSource *` | The media source to open. |

**Return**

- Type: 
- Description: _None_

### OpenUrl

Opens the specified media URL.

	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Url | `FString &` | The URL to open. |

**Return**

- Type: 
- Description: _None_

### Pause

Pauses media playback.

	  This is the same as setting the playback rate to 0.0.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Play

Starts media playback.

	  This is the same as setting the playback rate to 1.0.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Previous

Open the previous item in the current play list.

	  The player will start playing the new media source if it was playing
	  something previously, otherwise it will only open the media source.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Reopen

Reopens the currently opened media or play list.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Rewind

Rewinds the media to the beginning.

	  This is the same as seeking to zero time.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Seek

Seeks to the specified playback time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `FTimespan &` | The playback time to set. |

**Return**

- Type: 
- Description: _None_

### SelectTrack

Select the active track of the given type.

	  The selected track will use its currently active format. Active formats will
	  be remembered on a per track basis. The first available format is active by
	  default. To switch the track format, use SetTrackFormat instead.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | `EMediaPlayerTrack` | The type of track to select. |
| TrackIndex | `int32` | The index of the track to select, or INDEX_NONE to deselect. |

**Return**

- Type: 
- Description: _None_

### SetDesiredPlayerName

Set the name of the desired native player.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerName | `FName` | The name of the player to set. |

**Return**

- Type: 
- Description: _None_

### SetLooping

Enables or disables playback looping.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Looping | `bool` | Whether playback should be looped. |

**Return**

- Type: 
- Description: _None_

### SetRate

Changes the media's playback rate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rate | `float` | The playback rate to set. |

**Return**

- Type: 
- Description: _None_

### SetNativeVolume

Set the volume on the native player if not mixing with Sound Wave asset.

	  The SetNativeVolume can be used to change the audio output volume at runtime. Note that
	  not all media player plug-ins may support native audio output on all platforms.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Volume | `float` | The volume to set. |

**Return**

- Type: 
- Description: _None_

### SetTrackFormat

Set the format on the specified track.

	  Selecting the format will not switch to the specified track. To switch
	  tracks, use SelectTrack instead. If the track is already selected, the
	  format change will be applied immediately.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackType | `EMediaPlayerTrack` | The type of track to update. |
| TrackIndex | `int32` | The index of the track to update. |
| FormatIndex | `int32` | The index of the format to select (must be valid). |

**Return**

- Type: 
- Description: _None_

### SetVideoTrackFrameRate

Set the frame rate of the specified video track.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TrackIndex | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| FormatIndex | `int32` | Index of the track format, or INDEX_NONE for the selected one. |
| FrameRate | `float` | The frame rate to set (must be in range of format's supported frame rates). |

**Return**

- Type: 
- Description: _None_

### SetViewField

Set the field of view (only for 360 videos).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Horizontal | `float` | Horizontal field of view (in Euler degrees). |
| Vertical | `float` | Vertical field of view (in Euler degrees). |
| Absolute | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetViewRotation

Set the view's rotation (only for 360 videos).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rotation | `FRotator &` | The desired view rotation. |
| Absolute | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SupportsRate

Check whether the specified playback rate is supported.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rate | `float` | The playback rate to check. |
| Unthinned | `bool` | Whether no frames should be dropped at the given rate. |

**Return**

- Type: 
- Description: _None_

### SupportsScrubbing

Check whether the currently loaded media supports scrubbing.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SupportsSeeking

Check whether the currently loaded media can jump to a certain position.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAudioDeviceGUID

Sets the audio device for the media player; currently only effective on PC platforms.
	  add by watsonxie

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeviceGUID | `FString &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnEndReached |  | A delegate that is invoked when playback has reached the end of the media. |
| OnMediaClosed |  | A delegate that is invoked when a media source has been closed. |
| OnMediaOpened |  | A delegate that is invoked when a media source has been opened.<br><br>	  Depending on whether the underlying player implementation opens the media<br>	  synchronously or asynchronously, this event may be executed before or<br>	  after the call to OpenSource  OpenUrl returns. |
| OnMediaOpenFailed |  | A delegate that is invoked when a media source has failed to open.<br><br>	  This delegate is only executed if OpenSource  OpenUrl returned true and<br>	  the media failed to open asynchronously later. It is not executed if<br>	  OpenSource  OpenUrl returned false, indicating an immediate failure. |
| OnPlaybackResumed |  | A delegate that is invoked when media playback has been resumed. |
| OnPlaybackSuspended |  | A delegate that is invoked when media playback has been suspended. |
| OnSeekCompleted |  | A delegate that is invoked when a seek operation completed successfully.<br><br>	  Depending on whether the underlying player implementation performs seeks<br>	  synchronously or asynchronously, this event may be executed before or<br>	  after the call to Seek returns. |
| OnTracksChanged |  | A delegate that is invoked when the media track collection changed. |
| OnMediaPlayFirstFrame |  |  |

## Language

cpp
