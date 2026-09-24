# FKeyBind

Struct containing mappings for legacy method of binding keys to exec commands.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` | The key to be bound to the command |
| Command | `FString` | The command to execute when the key is pressedreleased |
| Control | `uint8` | Whether the control key needs to be held when the key event occurs |
| Shift | `uint8` | Whether the shift key needs to be held when the key event occurs |
| Alt | `uint8` | Whether the alt key needs to be held when the key event occurs |
| Cmd | `uint8` | Whether the command key needs to be held when the key event occurs |
| bIgnoreCtrl | `uint8` | Whether the control key must not be held when the key event occurs |
| bIgnoreShift | `uint8` | Whether the shift key must not be held when the key event occurs |
| bIgnoreAlt | `uint8` | Whether the alt key must not be held when the key event occurs |
| bIgnoreCmd | `uint8` | Whether the command key must not be held when the key event occurs |
| bDisabled | `uint8` |  |
