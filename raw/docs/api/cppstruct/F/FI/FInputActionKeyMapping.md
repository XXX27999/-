# FInputActionKeyMapping

Defines a mapping between an action and key

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ActionName | `FName` | Friendly name of action, e.g "jump" |
| Key | `FKey` | Key to bind it to. |
| bShift | `uint8` | true if one of the Shift keys must be down when the KeyEvent is received to be acknowledged |
| bCtrl | `uint8` | true if one of the Ctrl keys must be down when the KeyEvent is received to be acknowledged |
| bAlt | `uint8` | true if one of the Alt keys must be down when the KeyEvent is received to be acknowledged |
| bCmd | `uint8` | true if one of the Cmd keys must be down when the KeyEvent is received to be acknowledged |
| KeySeq | `uint8` | key sequence number: 0 for Primary key, 1 for Backup key |
