# UI 页面切换与 Widget 生命周期

> 来源：`raw/docs/ai/2026-06-24_UI_Switch_Pattern.md`、`raw/docs/ai/2026-06-30_仓库3D预览模型双创建修复.md`  
> 官方依据：`raw/docs/api/class/和平全局接口/UI 界面/UGCWidgetManagerSystem.md`、`raw/docs/wiki/进阶内容/UI系统`

---

## 一、标准切换流程（5 步）

页面间跳转并销毁当前页：

1. 获取本地玩家控制器：`STExtraGameplayStatics.GetFirstPlayerController(self)`，判空。
2. 拼完整资源路径：`UGCGameSystem.GetUGCResourcesFullPath('Asset/Blueprint/Prefabs/.../蓝图名.蓝图名_C')`。
3. 加载类并创建实例：`UE.LoadClass(fullPath)` → `UserWidget.NewWidgetObjectBP(PC, UClass)`，两步都判空。
4. 显示：`AddToViewport(ZOrder)`。
5. 关闭当前页：先 `UGCWidgetManagerSystem.HideWidget(self)`，再 `UGCWidgetManagerSystem.DestroyWidget(self)`。

**销毁顺序不可颠倒**：先隐藏再销毁，否则可能出现视觉残留或报错。

---

## 二、四种切换语义

| 场景 | 处理 |
| --- | --- |
| 页面间跳转 | 创建目标页 → 销毁当前页 |
| 子 UI 叠加弹出 | 只创建子 UI（更高 ZOrder），当前页保留 |
| 关闭当前页 | 销毁并恢复默认布局 `SetWidgetLayout` |
| 点击当前页自身标签 | 忽略跳转，不重复创建 |

主界面布局通过 `UGCWidgetManagerSystem.SetWidgetLayout(LayoutPath)` 切换，关闭时需恢复默认布局。

---

## 三、ZOrder 约定

| ZOrder | 用途 |
| --- | --- |
| 500 | 主页面（同级分页互跳） |
| 501 | 叠加在主页上的弹窗类子 UI |

---

## 四、涉及 API（均为客户端）

| API | 说明 |
| --- | --- |
| `STExtraGameplayStatics.GetFirstPlayerController` | 获取本地控制器 |
| `UGCGameSystem.GetUGCResourcesFullPath` | 资源完整路径 |
| `UE.LoadClass` | 加载蓝图类 |
| `UserWidget.NewWidgetObjectBP` | 创建 Widget 实例 |
| `UUserWidget:AddToViewport(ZOrder)` | 加入视口 |
| `UGCWidgetManagerSystem.HideWidget` / `DestroyWidget` | 隐藏 / 销毁 |
| `UGCWidgetManagerSystem.SetWidgetLayout` | 设置主界面布局 |

---

## 五、`_G` 隔离陷阱

仓库 3D 预览曾出现「一个模型可旋转、一个不可旋转」：

- PIE 是单进程，服务端与客户端**共享 `_G`**，问题不复现。
- 生产环境双进程各自独立 `_G`，服务端创建的模型与客户端创建的模型互不可见。
- 旋转函数直接通过 `_G["_Pet3DDisplayManager"]` 查表，只能在模型所在进程工作。

修复方式：把创建路径统一到客户端 `_G`（经 `ClientUpdateUI3D` → `SetModelName`），并在 `Destruct` 与关闭点分别清理双端模型。

推论：凡是依赖 `_G` 的跨端逻辑，PIE 通过不代表生产正确，见 [PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)。

---

## 六、UMG 布局注意

打工区实战中，UMG 绝对坐标导致文本偏移，最终改为水平中心锚点 + 文本居中 + AutoSize。UMG 结构改动须通过 UGCAskQ MCP 落盘，见 [蓝图与 MCP 写入流程](../工具与流程/蓝图与MCP写入流程.md)。UI 尺寸与坐标不应硬编码，见 [配置表驱动开发](../配置与数据/配置表驱动开发.md)。

---

## 七、官方挂点（AddToSlot）必须成对摘除

- 用 `UGCWidgetManagerSystem.AddToSlot(Widget, SlotName, ZOrder)` 或 `UGCWidgetUtility.AddToSlot` 挂到 `UI.UISlot.*` 的控件，关闭时**只 `HideWidget` + `DestroyWidget` 不够**，必须在销毁前调用 `RemoveFromSlot(Widget)`。
  - 官方依据：`raw/docs/api/class/和平全局接口/UI 界面/UGCWidgetManagerSystem.md`（`RemoveFromSlot` 从 UI 挂点槽位移除控件；`IsWidgetAddedToSlot` 判断是否已挂载）；`raw/docs/wiki/进阶内容/UI系统/20097_和平控件锚点.md` 定义 `UI.UISlot.MainUISlot_Low` = 和平主界面**低层级**锚点。
- 不摘的后果：挂点上残留已销毁控件；同 `ZOrder` 下新实例与残留控件的排序不确定，新实例可能被压在残留控件之下 → **界面打开了却点不动**（不是报错，是没反应）。
- 正确顺序：`RemoveFromSlot` → 清业务缓存（如 `UIUtils.LoadedUIWidgets[name]`）→ `HideWidget` → `DestroyWidget`。
- `Destruct` 可能因蓝图事件未绑定而**不触发**，清理逻辑不能只写在 `Destruct`，主动关闭路径必须自己清。
- 反向风险（防重复打开）：缓存命中的"复用现有实例"分支必须校验实例是否 `UE.IsValid`；**不能**用"调用某接口不报错"当有效性判定——UGC 侧对已销毁 UObject 常只写一条 `LuaException` 日志、`pcall` 仍返回 true，于是复用失效实例并静默失败。

---

## 八、相关页面

- [3D UI 挂载方案](../程序与网络/3DUI挂载方案.md)
- [MCP UI 编辑与高保真还原知识库](MCP-UI编辑与高保真还原知识库.md)
- [模型渲染与缩放问题](模型渲染与缩放问题.md)
- [配置表驱动开发](../配置与数据/配置表驱动开发.md)
- 来源：[2026-08-26 raw 资料入库总结](../来源记录/2026-08-26_raw资料入库总结.md)
