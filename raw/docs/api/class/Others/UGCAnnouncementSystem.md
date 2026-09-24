# UGCAnnouncementSystem

UGC公告系统

## Parents

_None_

## Variables

_None_

## Functions

### GetLatestAnnouncements

发起异步请求获取最新的公告列表（最新的5个公告）
参考用法：
```lua
local PF = UGCAnnouncementSystem.GetLatestAnnouncements()
PF:Then(function (PromiseFuture) local Announcements = PromiseFuture:Get() end)
PF:Else(function (PromiseFuture) print("[UGCAnnouncementSystem.GetLatestAnnouncements] Failed, timeout") end)
```
Announcements结构为Lua数组
```
Announcements = {{Title:string, Content:string, EffectiveTime:number, bTop:boolean}, ...}
```
生效范围：服务器

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

lua
