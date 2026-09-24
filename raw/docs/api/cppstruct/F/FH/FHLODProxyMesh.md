# FHLODProxyMesh

A mesh proxy entry

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LODActor | `TLazyObjectPtr < ALODActor >` | The ALODActor that we were generated from |
| StaticMesh | `UStaticMesh *` | The mesh used to display this proxy |
| Key | `FName` | The key generated from an ALODActor. If this differs from that generated from the ALODActor, then the mesh needs regenerating. |
