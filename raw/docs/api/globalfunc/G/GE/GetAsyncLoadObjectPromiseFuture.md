# GetAsyncLoadObjectPromiseFuture

使用 PromiseFuture 异步加载资源并创建对象实例
用法：GetAsyncLoadObjectPromiseFuture(PlayerController, ObjectPath):Then(function (PromiseFuture) local Obj = PromiseFuture:Get() end):AutoResume()
生效范围：服务器&客户端

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| Outer | [UObject](../../../class/Others/UObject.md) | Outer 对象，一般为 PlayerController |
| FullPath | `string` | 资源路径 |

## Return

- Type: 
- Description: _None_
