# FHardwareCursorReference

## Fields

| Name | Type | Description |
| --- | --- | --- |
| CursorPath | `FName` | Specify the partial game content path to the hardware cursor.  For example,<br>	    DO:   SlateDefaultPointer<br>	    DONT: SlateDefaultPointer.cur<br><br>	  NOTE: Having a 'Slate' directory in your game content folder will always be cooked, if<br>	        you're trying to decide where to locate these cursor files.<br><br>	  The hardware cursor system will search for platform specific formats first if you want to<br>	  take advantage of those capabilities.<br><br>	  Windows:<br>	    .ani -> .cur -> .png<br><br>	  Mac:<br>	    .tiff -> .png<br><br>	  Linux:<br>	    .png<br><br>	  Multi-Resolution Png Fallback<br>	   Because there's not a universal multi-resolution format for cursors there's a pattern we look for<br>	   on all platforms where pngs are all that is found instead of curanitiff.<br><br>	     Pointer.png<br>	     Pointer@1.25x.png<br>	     Pointer@1.5x.png<br>	     Pointer@1.75x.png<br>	     Pointer@2x.png<br>	     ...etc |
| HotSpot | [FVector2D](../FV/FVector2D.md) | HotSpot needs to be in normalized (0..1) coordinates since it may apply to different resolution images.<br>	  NOTE: This HotSpot is only used on formats that do not provide their own hotspot, e.g. Tiff, PNG. |
