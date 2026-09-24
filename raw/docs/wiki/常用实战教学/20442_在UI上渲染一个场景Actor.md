# 在UI上渲染一个场景Actor

本文档介绍如何使用 SceneCaptureComponent2D（场景捕获2D组件），将场景中的 3D Actor 实时渲染到 UI 图片控件上，可通过该功能实现角色展示、装备预览等效果。

## 创建Actor对象

创建一个Actor，在这个Actor上，添加静态网格组件，作为被渲染的背景。

![image.png](../_assets/images/c2fbd391_R3IRWimage.png)

创建一个SkeletalMesh组件，作为被渲染的对象，并设置该对象的位置、朝向及动画。

![image.png](../_assets/images/e19a4e86_DbHcSimage.png)

创建一个SceneCaptureComponent2D（场景捕获2D组件）组件。

![image.png](../_assets/images/80b4f4b9_j1QW4image.png)

选择一个渲染目标资产，用于接收当前渲染的结果（若没有须在选择列表中点击新建渲染目标资产）。

![image.png](../_assets/images/a55175cd_4BXupimage.png)

将Actor拖入场景，放入z=-1000的位置。

![image.png](../_assets/images/f024e999_TUiO7image.png)

## 设置渲染效果

在Actor的SceneCaptureComponent2D（场景捕获2D组件）组件中，从属性组【Scene Capture】设置渲染效果，相关配置及说明如下：

![image.png](../_assets/images/e2b284a9_5YnyKimage.png)

|属性名称|说明|
|:-:|-|
|纹理目标|指定捕获画面输出的目标资产。捕获到的画面将实时渲染并存储在该纹理上|
|捕获源|决定捕获的画面数据来源及通道|
|合成模式|控制捕获画面与最终输出的合成方式：<br>• 覆盖 (Overwrite)：直接用捕获结果覆盖目标纹理<br>• 叠加 (Additive)：将捕获结果叠加到目标纹理上<br>• 复合节点 (Compositing)：允许使用材质进行自定义混合|
|基元渲染模式|控制场景中哪些几何体参与渲染：<br>• 传统场景捕捉：渲染整个场景（受隐藏/仅显示列表影响）<br>• 渲染场景基元：仅渲染指定的基元<br>• 使用仅显示列表：仅渲染【仅显示actor】列表中的物体（常用于小地图或专属视角）。|
|隐藏的Actor|场景捕获中隐藏的Actor列表，列表中的Actor将不会出现在最终的渲染目标中|
|Show Attached Actor|勾选后，即使某个Actor被附加（Attach）到了隐藏的Actor下，该Actor依然会正常显示在捕获画面中（防止子组件被误隐藏）|
|仅显示actor|场景捕获中仅显示的actor列表，仅在【基元渲染模式】选择“使用仅显示列表”时生效|
|捕获每帧|是否每帧更新捕获的内容。如禁用，组件只在加载时渲染一次，然后只在移动时再次渲染|
|移动时捕获|是否更新运动中的捕获内容。如果要手动从蓝图进行捕获，则将其禁用|
|固定坚持渲染状态|是否坚持渲染状态，即使bCaptureEveryFrame为false也同样如此。这可计算动态模糊和临时抗锯齿的速度|
|最大视图距离重载|如大于0，则设置最大渲染距离重载。如发射平面处于一个封闭区域(如走廊或房间)中，则可用于剔除反射的远景物体|
|捕获排序优先级|帧中的捕获优先级，对GPU上的场景捕获进行排序，解决多个捕获组件之间的相互依赖性。优先级最高则最先进行|

创建一个材质实例，母材质选择“场景抓取”，MainTexture选择对应的渲染目标资产，不透明度设置1。

![image.png](../_assets/images/a5460a2f_qALkLimage.png)

## 创建并挂接UI

打开UI编辑器，以“用户控件模板”为模板创建一个UI组件，在组件中添加一个图片控件。

![image.png](../_assets/images/40a30f39_7znBKimage.png)

将图片控件的锚点设置为全屏，并将材质实例赋值给图片控件。

![image.png](../_assets/images/62b99d5c_PsQh5image.png)

最后根据自身需求挂接上UI。

![Scene.gif](../_assets/images/696f4087_1AcRDScene.gif)

## 示例：实现透明背景的渲染效果

首先直接在场景下方放置一个需要被渲染的Actor对象。

![image.png](../_assets/images/42bd3c21_RG0buimage.png)

在场景中拖入SceneCapture2D的Actor后，【捕获源】选择“RGB场景颜色（HDR），A中的场景深度”，【合成模式】选择“覆盖”，【基元渲染模式】选择“使用仅显示列表”，并在【仅显示actor】中选择被渲染的对象，并调整其坐标位置。

![image.png](../_assets/images/7c9dd23b_rrTg7image.png)

取消勾选【通用显示标志】的【Fog】。

![image.png](../_assets/images/557be35a_ZswFQimage.png)

此时得到的渲染目标资产就是一个背景为黑色的纹理。

![image.png](../_assets/images/3a9f833d_mcSWdimage.png)

将渲染目标资产放入材质实例，不透明度设置为0，此时将会隐藏黑色背景

![image.png](../_assets/images/1655d942_IbJWwimage.png)

最后根据自身需求创建并挂接上UI。

![image.png](../_assets/images/430cea50_RIuC3image.png)
