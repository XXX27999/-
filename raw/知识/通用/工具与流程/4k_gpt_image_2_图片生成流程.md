# 4k/gpt-image-2 图片生成流程与规范

> 类型：工具与流程规范
> 主题：4k/gpt-image-2 图片生成模型调用、解码与保存流程
> 适用范围：全局通用；通过模型生成、替换或定制图片素材（如 UI 背景、格子图标、角色素材）的场景
> 证据状态：实测已证实（2026-09-15 两轮独立验证，见来源记录）；其中「接口路由」「尺寸矩阵」「参数白名单」「耗时基线」为本轮新增实测，「Codex 本地代理 57321 + OpenAI SDK」为既有实测
> 来源：[2026-09-15 4k/gpt-image-2 接口路由与尺寸实测](../来源记录/2026-09-15_4k_gpt_image_2接口路由与尺寸实测.md)
> 更新时间：2026-09-15
> 关联主题：[资源导入与路径规范](../配置与数据/资源导入与路径规范.md), [调试备份存放](./调试备份存放.md)
> 排除范围：非 4k/gpt-image-2 之外的传统本地或远端离线图片生成工具，以及直接用 Python 在编辑器 runtime 修改 `.uasset` 贴图的方案（这类情况应当使用资源导入规范与 MCP 贴图绑定流程）
> 官方依据：OpenAI Images API 协议；网关 `https://apihub.veletis.com/v1` 2026-09-15 实测响应；本地 Codex 运行环境 `config.toml` custom provider 及 port `57321` API 接口协议

## 核心结论

在进行《和平精英》绿洲起源项目或 UI 原型制作时，若需要高质量、高精度的图片素材（例如 UI 背景图、格子物品、角色头像或装备图标），可以且应当使用 **4k/gpt-image-2** 图片生成模型进行生成。

该模型**不是对话模型**，只有图像端点可用。成功流程的最小闭环是：

1. **选对端点**：必须 `POST /v1/images/generations`，`/v1/chat/completions` 恒失败。
2. **只传四个参数**：`model` / `prompt` / `n` / `size`。
3. **取 `b64_json` 并 `base64.b64decode`** 解码为二进制 PNG 流。
4. **写入指定交付目录**（如 `outputs/`），并核验 PNG 头宽高。
5. **按 [资源导入与路径规范](../配置与数据/资源导入与路径规范.md) 导入编辑器或生成高保真预览**。

## 接口路由（关键，2026-09-15 实测）

网关：`https://apihub.veletis.com/v1`（WorkBuddy 自定义模型 `custom-local:4k/gpt-image-2` 的 `url` 字段）。`/v1/models` 中确认存在 `4k/gpt-image-2`，另有 `4k/gpt-image-2.5-flare`、`4k/gpt-image-2.5-sunburst`。

| 端点 | 结果 | 证据 |
| --- | --- | --- |
| `POST /v1/models` | ✅ 200，列出 `4k/gpt-image-2` | 模型已注册 |
| `POST /v1/images/generations` | ✅ 200，返回 `data[0].b64_json`（PNG） | 唯一可用出图路径 |
| `POST /v1/chat/completions` | ❌ 502 `upstream_server_error` | 中/英文、长/短提示各试一次，共 3 次全失败 |

**结论**：把 `4k/gpt-image-2` 当对话模型在客户端里直接选用会报上游错误；必须走图像端点。同一密钥调 `deepseek-v4-flash` 秒回正常，说明密钥与网关本身无故障，问题只在该图像模型链路。

## 尺寸矩阵（2026-09-15 实测）

| `size` | 结果 | 备注 |
| --- | --- | --- |
| `1024x1024` | ✅ 200 | 约 56s，1.45 MB PNG |
| `1024x1536` | ✅ 200 | 竖版可用；实测 1024x1536，1.80 MB PNG，耗时 133.9s，`output_tokens` 158（人物立绘场景） |
| `2048x2048` | ✅ 200 | 约 346s，6.1 MB PNG；**当前实测上限** |
| `auto` | ✅ 200 | 实测返回 1254x1254（非标准值，需回读宽高确认） |
| `1536x1024` | ❌ 503 `upstream_configuration_error` | 横版该尺寸上游未配好 |
| `4096x4096` | ❌ 400 `invalid_parameter_value` | 名称含 4k 但不支持 4096 |
| `4096x2160` | ❌ 400 `invalid_parameter_value` | 同上 |
| `"2K"` / `"4K"` 字符串 | ❌ 400 `invalid_parameter_value` | 只接受 `宽x高` 数值格式 |

**名称里的 “4k” 名不副实**：实测上限只到 2048×2048，4096 级别被明确拒绝。需要更大图时用 [调试备份存放](./调试备份存放.md) 中的放大方案或改用其他模型，不要反复试 4096。

## 耗时基线（2026-09-15 实测）

| 尺寸 | 场景 | 耗时 |
| --- | --- | --- |
| `1024x1024` | 写实风景/静物 | 约 56s |
| `1024x1536` | 人物立绘（竖版，细节多） | 约 134s |
| `2048x2048` | 写实风景 | 约 346s |

结论：耗时随像素量与主体复杂度上升，**1024x1536 与 2048x2048 都超过常见 120s 默认超时**，必须显式放大超时。

## 参数白名单（2026-09-15 实测）

仅接受 `model`、`prompt`、`n`、`size` 四个字段。以下字段一律返回 400 `unsupported_parameter`：

- `quality`（`low` / `medium` / `high`）
- `output_format`（`png` / `jpeg` / `webp`）
- `background`（`opaque` / `transparent`）

响应体自报的字段为服务端回显、不可控：`background: opaque`、`output_format: png`、`quality: low`，并带 `usage`（文本入 token / 图像出 token，2048 图约 48 入 / 892 出）。

## 成功流程 A：直连网关（零脚本，推荐）

无需 Python 脚本，全程 `curl` + 一次性解码，不产生工程内残留文件。

```bash
# 0) 本机 Git Bash 的 shim 会丢 PATH，先补回
export PATH="/usr/bin:/bin:/usr/local/bin:$PATH"

# 1) 从本地配置读取密钥（不要把密钥写进脚本或提交到知识库）
CFG="C:/Users/Administrator/.workbuddy/cache/acc-product-config-v3.json"
KEY=$(grep -o '"apiKey":"sk-alh[^"]*"' "$CFG" | head -1 | cut -d'"' -f4)

# 2) 出图（1024 约 60s，2048 约 350s，务必放大超时）
curl -s -m 500 "https://apihub.veletis.com/v1/images/generations" \
  -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d '{"model":"4k/gpt-image-2","prompt":"<提示词>","n":1,"size":"1024x1024"}' \
  -o result.json -w "http=%{http_code} time=%{time_total}s size=%{size_download}\n"

# 3) 解码并回读真实宽高（PNG 头第 16-24 字节）
python -c "import json,base64,struct;d=json.load(open('result.json',encoding='utf-8'));raw=base64.b64decode(d['data'][0]['b64_json']);print('dims',struct.unpack('>II',raw[16:24]));open('out.png','wb').write(raw)"
```

验证判据：`http=200` 且 `result.json` 顶层含 `data[0].b64_json`；解码后宽高与请求 `size` 一致；PNG 文件可被正常打开。

## 成功流程 B：Codex 本地代理 57321 + OpenAI SDK

在本地 Codex 环境中，该模型集成于 custom provider，通过 `http://127.0.0.1:57321/v1` 的 OpenAI Images API 调用，返回同样是 base64（`b64_json`）。

### 1. 准备环境与依赖
确保当前 Python 环境已安装 `openai` SDK：
```bash
python -c "import openai"
```

### 2. Python 脚本模板
使用此模型生成图片时，必须在项目的 `work/` 目录下编写并执行形如以下的 Python 脚本。
> 注意：**不要将临时 Python 脚本遗留在 UGC 工程中**（如 IslandAuctionKing 根目录），以免 PIE 校验文件名特殊字符失败导致编译中断。

```python
import os
import base64
from openai import OpenAI

def generate_and_save_asset():
    print("Initializing image generation via 4k/gpt-image-2...")
    
    # 1. 初始化客户端，指向本地代理端口
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="http://127.0.0.1:57321/v1"
    )
    
    # 2. 构造提示词与生成参数
    prompt = "A beautiful and detailed digital art of a golden mechanical clockwork dragon, white background, cinematic lighting, concept art, highly detailed"
    output_path = r"C:\Users\Administrator\Documents\Codex\2026-09-15\4k-gpt-image-2-x20\outputs\clockwork_dragon.png"
    
    try:
        # 3. 发送请求
        response = client.images.generate(
            model="4k/gpt-image-2",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        
        # 4. 验证响应并进行 Base64 解码保存
        if response.data and response.data[0].b64_json:
            b64_data = response.data[0].b64_json
            img_bytes = base64.b64decode(b64_data)
            
            # 自动创建目标目录
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # 5. 二进制写入本地文件
            with open(output_path, "wb") as f:
                f.write(img_bytes)
            print(f"Success! Image saved to: {output_path}")
        else:
            print("Error: No b64_json returned in response.")
            
    except Exception as e:
        print(f"Image generation failed: {e}")

if __name__ == "__main__":
    generate_and_save_asset()
```

### 3. 解码并保存至交付资产
- 生成的图片应当写入到项目的交付资产中，优先路径为绝对路径形式（例如：`C:\Users\Administrator\Documents\Codex\<YYYY-MM-DD>\<Project>\outputs\<文件名>.png`）。
- 使用 `view_image` 工具或 Markdown 绝对路径引用对其进行渲染预览和质量审计。

### 4. 导入编辑器中（参考 [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)）
- 依据 Wiki 277_资源导入.md 规范，将图片通过拖入或通过 `ue.import_asset` 工具导入到绿洲编辑器指定文件夹，并设置相应的 Texture 属性（UI 材质等）。

## 两条路径的关系（避免误读）

| 路径 | 端点 | 证据状态 | 适用环境 |
| --- | --- | --- | --- |
| A 直连网关 | `https://apihub.veletis.com/v1` | 2026-09-15 实测（WorkBuddy） | WorkBuddy / 任何可出网环境 |
| B 本地代理 | `http://127.0.0.1:57321/v1` | 2026-09-15 实测（Codex） | Codex custom provider 已启动时 |

两者是同一模型的**两条接入路径**，不是互相否定的结论：B 的本地端口是 Codex 侧的 custom provider 代理，A 是直连上游网关。任一路径失败时先换另一条验证，再判定为模型故障。

## 常见错误与排除

- **❌ 错误 1: 直接使用 `scripts/image_gen.py` 进行 `4k/gpt-image-2` 传参调用**
  - **原因**: 默认的 `image_gen.py` 在 `_validate_model` 中对模型名有 `gpt-image-` 这一前缀过滤。
  - **纠正**: 使用上述 `work/generate_and_save.py` 自定义脚本或临时修剪前缀校验，直接通过原生 OpenAI SDK 的 images.generate 接口进行调用。
- **❌ 错误 2: 响应提示 API 鉴权失败**
  - **原因**: 本地没有设置环境变量 `OPENAI_API_KEY`（路径 B）。
  - **纠正**: 确认 `OPENAI_API_KEY` 已经正确导入系统环境中；路径 A 改为从本地配置读取网关密钥。
- **❌ 错误 3: 临时脚本残留于编辑器项目内**
  - **原因**: 直接在 UGC 项目根目录下创建或留存 `__pycache__` 或 `*.py`。
  - **纠正**: 一次性生成脚本仅允许存放在 `D:\知识库\和平精英绿洲起源\备份\` 或工作区的 `work/` 路径下，用完即删；优先用流程 A 的零脚本 `curl` 方案。
- **❌ 错误 4: 502 `upstream_server_error`（2026-09-15 新增）**
  - **原因**: 把该模型当对话模型调了 `/v1/chat/completions`。
  - **纠正**: 改调 `/v1/images/generations`。中英文、长短提示均无法绕过。
- **❌ 错误 5: 400 `invalid_parameter_value` / `unsupported_parameter`（2026-09-15 新增）**
  - **原因**: 传了不支持的 `size`（4096 系列、`2K`/`4K` 字符串）或多余字段（`quality`、`output_format`、`background`）。
  - **纠正**: 只保留 `model`/`prompt`/`n`/`size`，尺寸从 `1024x1024`、`1024x1536`、`2048x2048`、`auto` 中选。
- **❌ 错误 6: 503 `upstream_configuration_error`（2026-09-15 新增）**
  - **原因**: 请求了 `1536x1024` 等上游未配置的尺寸。
  - **纠正**: 换用尺寸矩阵中已验证可用的组合；该错误与 502 不同，属于上游配置缺失而非模型整体不可用。
- **❌ 错误 7: 请求被工具默认超时掐断（2026-09-15 新增）**
  - **原因**: 2048 出图实测 346s，超过常见 120s 默认超时，进程被 SIGTERM。
  - **纠正**: 显式放大超时（如 `-m 500` / 工具 `timeout` 参数），或改后台执行后轮询。
- **❌ 错误 8: 本机 Git Bash 报 `dirname: command not found` / `ls: command not found`**
  - **原因**: WorkBuddy 的 shell shim 未带起 PATH。
  - **纠正**: 每条命令前先 `export PATH="/usr/bin:/bin:/usr/local/bin:$PATH"`。

## 待查证

- `1536x1024`（以及其他横版组合如 `2048x1536`、`1536x2048`）返回 503 是长期配置缺失还是当日上游波动，未复测。
- `auto` 返回 1254x1254 的取值规则（是否由提示词或内容决定）未验证。
- 名称中的 “4k” 是否对应某个未开放的上游档位（如需要额外参数或白名单）未查证。
- 路径 B 的 `57321` 端口代理与 `apihub.veletis.com` 是否为同一上游，未经官方确认（属推断）。

## 相关页面

- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [调试备份存放](./调试备份存放.md)
- [2026-09-15 4k/gpt-image-2 接口路由与尺寸实测](../来源记录/2026-09-15_4k_gpt_image_2接口路由与尺寸实测.md)
- [2026-09-14 主界面底图导入与拖拽导入受阻查证](../来源记录/2026-09-14_主界面底图导入与拖拽导入受阻查证.md)
