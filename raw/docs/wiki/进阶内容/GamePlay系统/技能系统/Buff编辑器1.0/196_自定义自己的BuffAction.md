#  自定义自己的BuffAction

### 使用Lua脚本Action

- 在BuffActions中添加新的Action,类型选择Lua脚本Action
- 在LuaFile中填入路径

![企业微信截图_16867095152247.png](../../../../_assets/images/31f7d6b3_企业微信截图_16867095152247.png)

- 对应的脚本路径

![企业微信截图_16867095284718.png](../../../../_assets/images/6b8ad21e_企业微信截图_16867095284718.png)

- 脚本对应实现如下

```lua
local myBuffAction = {};

function myBuffAction:LuaDoAction()
    print("myBuffAction:LuaDoAction")
    return true
end

function myBuffAction:LuaUndoAction()
    print("myBuffAction:LuaUndoAction")
    return true
end

function myBuffAction:LuaResetAction()
    print("myBuffAction:LuaResetAction")
    return true
end

function myBuffAction:LuaUpdateAction(DeltaSeconds)
    print("myBuffAction:LuaUpdateAction:"..DeltaSeconds)
    return true
end

return myBuffAction;
```
