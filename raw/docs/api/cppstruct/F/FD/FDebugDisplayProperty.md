# FDebugDisplayProperty

Debug property display functionality to interact with this, use "display", "displayall", "displayclear"

  @see UGameViewportClient
  @see FDebugDisplayProperty
  @see DrawStatsHUD

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Obj | `UObject *` | the object whose property to display. If this is a class, all objects of that class are drawn. |
| WithinClass | `TSubclassOf < UObject >` | if Obj is a class and WithinClass is not nullptr, further limit the display to objects that have an Outer of WithinClass |
