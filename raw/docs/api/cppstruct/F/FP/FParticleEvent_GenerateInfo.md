# FParticleEvent_GenerateInfo

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Type | `TEnumAsByte < EParticleEventType >` | The type of event. |
| Frequency | `int32` | How often to trigger the event (<= 1 means EVERY time). |
| ParticleFrequency | `int32` | Only fire the first time (collision only). |
| FirstTimeOnly | `uint32` | Only fire the first time (collision only). |
| LastTimeOnly | `uint32` | Only fire the last time (collision only). |
| UseReflectedImpactVector | `uint32` | Use the impact FVector not the hit normal (collision only). |
| bUseOrbitOffset | `uint32` | Use the orbit offset when computing the position at which the event occurred. |
| CustomName | `FName` | Should the event tag with a custom name? Leave blank for the default. |
| ParticleModuleEventsToSendToGame | `TArray < UParticleModuleEventSendToGame * >` | The events we want to fire off when this event has been generated |
