# -*- coding: utf-8 -*-
"""
绿洲启元 地图数据采样器（ADB 截屏 + OCR）
================================================
用途：采集《和平精英》绿洲启元玩法大厅列表页上的 地图名 / 热度 / 评分 / 评论数。

合规边界（重要，勿越过）：
  * 只读截屏，不修改游戏客户端、不注入进程、不需要 root。
  * 不使用任何抓包 / 证书绑定绕过 / 私有协议逆向手段。
  * 「自动上滑」通过 adb shell input swipe 模拟用户滑动，默认关闭，请自行评估使用场景。

三种输入源：
  1) ADB 实时截屏（需本机有 adb.exe，工具可手动指定路径）
  2) 导入本地图片 / 文件夹（另一台设备拍照、系统截图后传入）
  3) 剪贴板粘贴（PrintScreen 后直接粘）

运行（必须用带 tkinter 的解释器）：
  D:\\知识库\\和平精英绿洲起源\\工具\\OasisOcrSampler\\.venv\\Scripts\\python.exe OasisOcrSampler.py
"""

import os
import re
import csv
import json
import time
import queue
import threading
import subprocess
import datetime
import shutil
from decimal import Decimal
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

try:
    from PIL import Image, ImageTk, ImageGrab, ImageOps, ImageEnhance, ImageFilter
except Exception:
    raise SystemExit("缺少 Pillow，请先安装：pip install pillow")

APP_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(APP_DIR, "sampler_config.json")
SHOTS_DIR = os.path.join(APP_DIR, "shots")
CROPS_DIR = os.path.join(APP_DIR, "crops")
OUT_DIR = os.path.join(APP_DIR, "out")
for _d in (SHOTS_DIR, CROPS_DIR, OUT_DIR):
    os.makedirs(_d, exist_ok=True)

# 采样字段（前 3 个是核心指标，后 2 个为图内可见的辅助信息）
FIELDS = ["地图名", "热度", "评分", "评论数", "标签", "入口按钮"]
# 数值字段：需要做「万 / 亿」单位换算
NUMERIC_FIELDS = {"热度", "评分", "评论数"}
FIELD_COLORS = {"地图名": "#e8453c", "热度": "#f5a623", "评分": "#2f9e44",
                "评论数": "#1c7ed6", "标签": "#ae3ec9", "入口按钮": "#0ca678"}

# ---------------------------------------------------------------- 大厅布局常量（2026-09-18 按真机截图标定）
# 视觉坐标基准：用户提供的 1920x864 大厅截图 === 1078x468 视图
VIEW_W, VIEW_H = 1078.0, 468.0

# 几何版本号：每次修改 LOBBY 几何（卡片顶/行距/卡高/字段偏移）都必须 +1。
# 程序启动时若存档里的 geom_version 与当前不一致，会丢弃存档中的旧几何并回到默认值，
# 防止历史错误标定被旧配置静默复活。
GEOM_VERSION = 4    # v2 = 首行顶 91 / 行距 170 / 两行共用一套字段偏移
                    # v3 = 卡片网格明确为「一页 2 行 × 3 列」，列数改为两种模式共用，
                    #      新增列距(495)，自选框选改为按行×列复制。
                    #      v2 存档里的 rects/ncol/card_count/card_step 语义已变（列数曾被设成 2、
                    #      手工框在大厅模式下不生效），一律丢弃回到按图实测的默认值。
                    # v4 = 评分框左边界右移到 71 视觉（原 62.9）。2026-09-20 真机 2400x1080
                    #      实测：星标墨迹占「相对卡左」约 137..165 真机px，评分数字占 165..200；
                    #      旧框换算后是 140..250，把星标右半（140..165）整块圈进来 →
                    #      星标右弧被 OCR 读成 '7'，产出 '74.3' / '?2.9'。右移后只留约 7px 星标尾。

# ---------------------------------------------------------------- 大厅布局常量
# 全部由 1920x864 真机截图逐像素测量得出，坐标一律用「1078x468 视图」表示，
# 运行时按 帧宽/1078、帧高/468 换算成真机像素。
#
# 实测依据（真机 px，2026-09-18 两轮复测修正）：
#   三列卡片边界 = (109,590) (603,1085) (1098,1580)   -> 列宽 481，列距 494
#   第一行卡片顶 y=168（三列一致，行方差在 y=168 出现单像素尖峰 = 卡片上边框）
#   第一行卡片底 y=481                              -> 卡高 313 真机 = 169.5 视觉
#   第二行卡片顶 y=482                              -> 行距 314 真机 = 170.1 视觉
#   列表视口上沿（筛选条下沿）真机 y≈167 -> 视觉 90.5
#
#   字段相对「卡片顶」的实测框（真机 px，两行完全一致 —— 这是本次修正的关键）：
#     热度      框 ( 10,  -4, 102,  40)   '77.0万' / '51.2万' …
#     评分      框 (112,  -8, 200,  48)   '4.1' / '2.4'（只取星标右侧的数字，见 ③）
#     地图名    框 (  4, 226, 312, 263)   '从实习生到CEO' …
#     标签      框 (  4, 266, 300, 292)   '射击 | 冒险闯关 | 肉鸽' …
#     入口按钮  框 (342, 252, 480, 297)   '下载' / '维护中'
#
#   ⚠ 四处曾标错，务必不要再犯：
#     ① 早前把第一行卡片顶当成 y=103（那其实是筛选条下沿），据此把两行拆成
#        fields_row0 / fields_rowN 两套偏移，还把 row_step 记成 231 —— 三处都错。
#        修正后两行共用同一套偏移，find_cards 用统一行距即可。
#     ② 字段框高度必须给足：热度要 44px 才带得上单位「万」，按钮要 45px 才读全
#        「下载」；收窄会把相邻字切掉，且失败是静默的（只少一个字符，不报错）。
#     ③ 评分框「不要」把星标并进来（2026-09-20 用两个分辨率复测后收紧）。
#        星标墨迹与评分数字是**紧贴**的（中间没有空隙），所以任何「含全部数字」的框
#        都必然带进一点星标；能做的是把带入量压到最小。
#        实测（用 RapidOCR 直接读整条信息带，取 token 墨迹 x 区间，均为「相对卡左」真机px）：
#          1920x864  基准图：数字 '4.1' 在 135..155；星标墨迹约止于 132
#          2400x1080 真机：  数字 '4.4/4.3/3.6' 在 165..200；星标墨迹约 137..165
#        两者除以各自 sx 都落在视觉 x≈74..76 —— 即「数字起点」在两种分辨率下是一致的，
#        等比换算成立。旧框视觉 62.9 换算到 2400 是 140，等于把星标右半（140..165）整块
#        圈进来，星标右弧被读成 '7' → 产出 '74.3'、'?2.9'。现固定左边界视觉 71（= 真机
#        158@2400 / 126@1920），只留约 6~7px 星标尾，且两种分辨率下数字都完整在框内。
#        结论：评分宁可少读左边一点点，也不能让它和星标连成一块。

# 卡片网格（视觉坐标）。列表区固定在「筛选行」之下，页脚「房间」按钮之上。
LOBBY = {
    # 三列卡片的左右边界（x0, x1）—— 取自像素测量的列边界
    "col_x": [(61, 331), (339, 609), (617, 887)],
    # 卡片高度与行间距（视觉坐标）。真机 313 / 314 px 换算而来
    "card_h": 170,
    "row_step": 170,
    # 第一行卡片顶部 y（= 可滚动视口内第一张卡片的实际上沿，真机 y=168 -> 视觉 91.0）
    "first_row_y": 91,
    # 行间缝隙与封面可见高度（2026-09-21 三张真机截图逐行实测 @1920x864 基准图）：
    #   封面可见 302px（168..469），**亮色缝隙 12px**（470..481），下一行卡顶 482。
    #   这条缝隙是「对齐网格」的唯一可靠锚点：封面内部再怎么有横向结构，
    #   也很难三列在同一行同时对齐，而缝隙是三列同时「亮 + 平」的。
    #   用户的三张截图实测：图1（标定基准）顶行卡顶=168 → 对齐；
    #   图2（4012b2f7）顶行卡顶=177 → 偏下 9px（就是「没对准红线」的状态）。
    "cover_h": 163.6,   # 302 / 1.8462 视觉：封面可见高度（不含缝隙）
    "gap_h": 6.5,       # 12 / 1.8462 视觉：行间亮缝高度
    "clip_y": 90.5,     # 列表视口上沿 = 筛选条下沿（真机 167@864），缝隙判定从这个 y 起扫
    # 可滚动列表区 / 排除区：这些矩形内不可能有卡片（顶部筛选行、右侧推荐侧栏、页脚按钮条）
    "list_area": (55, 88, 892, 452),
    "exclude": [(0, 0, 900, 88), (890, 88, 1078, 452), (0, 448, 900, 468)],
    # 字段框（相对「卡片左上角」，视觉坐标）。两行共用同一套偏移。
    # 数值由真机像素实测换算（÷1.7811 / ÷1.8462），并用三列 × 两行共 6 张卡片交叉验证。
    # 每个框的高度都是「给足」的 —— 实测发现收窄会切掉相邻字：
    #   热度框真机高 44px 才读得到单位「万」，收到 40px 只回数字（77.0 而非 77.0万）→ 值差 1e4；
    #   按钮框真机高 45px 才读得到「下载/维护中」，收到 30px 只剩「载」「力」。
    "fields": {
        "热度":   (5.6, -2.2, 57.3, 21.7),   # 真机 ( 10,-4,102,40)  火苗图标右侧的数字+单位
        "评分":   (71.0, -5.0, 115.0, 26.0),  # 真机 (126,-9,205,48)@1920 星标「右侧」的数字，勿并入星标
        "地图名": (2.2, 122.4, 175.2, 142.5),  # 真机 (4,226,312,263)  标题大字
        "标签":   (2.2, 144.1, 168.4, 158.2),  # 真机 (4,266,300,292)  标签小字（竖线分隔）
        "入口按钮": (192.0, 136.5, 269.5, 160.9),  # 真机 (342,252,480,297) 下载/维护中
    },
    # 本页不可用字段（两行一致）：该位置没有可 OCR 的文本，识别时直接留空。
    # 实测依据：本页列表卡片上只有 热度 与 评分 两个数字；「评论数」在本页不出现
    # （截图逐像素核查过顶部信息带，只有火苗+热度、星星+评分两组），
    # 故标记为不可用，而不是给个错位框去读无关文字。
    "fields_unavailable": ["评论数"],
}

# 一页卡片网格的默认值（真机 px，与上面 LOBBY 同一张截图的实测值）：
#   列距 495 = 三列卡左边界 604-109 与 1099-604；行距 314 = 第二行卡顶 482 - 第一行卡顶 168。
#   一页 2 行 × 3 列 = 6 张卡（第三行卡顶会落到 y>864，超出屏幕）。
# 这几个值是「自选框选」模式的默认步长，也让界面上的默认数字与真机对齐。
INT_COL_STEP = 495
INT_ROW_STEP = 314
INT_ROW_COUNT = 2

# 字段级 OCR 预处理模式（依据见 preprocess 的说明）。
# 注意：热度必须留空 —— 实测加预处理会把 '111万' 读成 '川1万'，值差 100 倍。
FIELD_PREP = {"评分": "sharp"}

# 数值合理区间：解析结果落在此区间外时，判定为「读错」——
# 原始文本照常保留（可人工复核），但 *不要* 写入数值列，避免把错数当数据用。
# 评分实测会把小数点读丢（'4.5' -> '★45'、'4.1' -> '41'），这类值会落在此区间外而被拦下。
FIELD_VALID_RANGE = {"评分": (0.0, 10.0)}

# 本页不可用的字段：识别时按「无框可用」处理，直接留空而不是给一个错位的框去读无关文字。
FIELD_PAGE_UNAVAILABLE = set(LOBBY.get("fields_unavailable", []))

# 卡片状态表（图内可判断的状态）
CARD_STATE = {
    "normal": "可进入",
    "maintain": "维护中",
    "downloading": "下载中",
    "downloaded": "已下载",
}

# ---------------------------------------------------------------- 导出列
# 导出专用的最终列顺序（与界面表格列不同）。必须定义在类体之前 —— 类里 `COLS = EXPORT_COLS`
# 是在**类加载时**求值的，放到文件末尾会 NameError（2026-09-20 实测踩到）。
EXPORT_COLS = ["时间", "来源", "列", "行", "地图名", "热度", "热度_值", "评分", "评分_值",
               "评论数", "评论数_值", "标签", "入口按钮", "卡片状态"]
# 需要按「数字」写进 Excel 的列：这些是换算后的数值，写成文本就没法排序/计算
EXPORT_NUM_COLS = ("热度_值", "评分_值", "评论数_值")

UNIT_MAP = {"万": 1e4, "亿": 1e8, "w": 1e4, "W": 1e4, "k": 1e3, "K": 1e3}

# OCR 常把字段名一起读进来，按字段剥掉（长的在前，避免「评论数」被「评论」吃掉后半）
# 星级符号 / 火苗图标被误读出来的常见形态也一并剥掉。
LABELS = {
    "热度": ["热度", "热力", "人气", "HOT", "hot", "★", "☆", "🔥", "△", "▲"],
    "评分": ["评分", "星级", "分数", "分", "SCORE", "★", "☆", "🔥", "△", "▲"],
    "评论数": ["评论数", "讨论数", "评价数", "评论", "讨论", "评价", "留言"],
}


def strip_label(text, field):
    """剥掉字段名与图标误读字符，只留数值部分"""
    s = text
    for lb in LABELS.get(field, []):
        s = s.replace(lb, "")
    return s.strip() or text


# ---------------------------------------------------------------- 数值解析
def parse_number(text):
    """从 OCR 文本中提取数值，支持 1128万 / 2.2亿 / 83条 / 4.4 分 / 1,234 等写法。
    返回 (float|None, 原始匹配串|None)"""
    if not text:
        return None, None
    s = str(text).replace(",", "").replace("，", "").strip()
    # 优先匹配「数字 + 单位」。用 Decimal 避免 2.2亿 算成 220000000.00000003
    m = re.search(r"(\d+(?:\.\d+)?)\s*([万亿wWkK])", s)
    if m:
        val = Decimal(m.group(1)) * Decimal(int(UNIT_MAP[m.group(2)]))
        return float(val), m.group(0)
    # 其次匹配纯数字（评分 4.4、评论 83 条）
    m = re.search(r"(\d+(?:\.\d+)?)", s)
    if m:
        return float(m.group(1)), m.group(0)
    return None, None


# 评分形态：「一位整数 . 一位小数」。findall 会给出全部匹配，取最后一个（真值在星标右侧）。
SCORE_RE = re.compile(r"(\d)\.(\d)")


def parse_score(text):
    """评分专用解析。返回 (float|None, 匹配串|None)。

    评分是「个位.一位小数、取值 0~10」的定长格式。星标与数字紧贴（中间无空隙），
    所以 OCR 必然会把一点星标带进来；带进来的星标会被读成各种字符：
      '★4.3' / '74.3'（星标右弧读成 7）/ '?2.9'（星标读成 ?）/ '3.67'（尾数误粘）
    通用 parse_number 遇到这些会取到错的数字（74.3、或去掉小数点后的 367），
    越界拦截只能拦「粗错」，拦不住落在 (0,10) 内的 '2' 这类假值。

    这里改按**形态**匹配：取所有「一位整数 . 一位小数」中**最后**那个匹配。
    「取最后一个」是关键 —— 真值在星标右侧，误读字符粘在它左边。
    实测（2026-09-20 真机 2400x1080，6 张卡）：
      '★4.3'->4.3   '74.3'->4.3   '?2.9'->2.9   '3.67'->3.6   '4.5'->4.5
      'A2'->None    '36'->None（小数点丢失，宁可不取值也不猜）
    已知边界：满分 10.0 会被误取成 0.0（见下方 10.0 的特判）。
    """
    if not text:
        return None, None
    s = str(text)
    # 满分特判：'10.0' 是唯一可能出现两位整数的合法分值
    if "10.0" in s:
        return 10.0, "10.0"
    hits = SCORE_RE.findall(s)
    if not hits:
        return None, None
    a, b = hits[-1]
    hit = "%s.%s" % (a, b)
    return float(hit), hit


# 字段级解析器覆盖：默认走 parse_number，评分走 parse_score（形态匹配，抗星标污染）
FIELD_PARSERS = {"评分": parse_score}


def clean_text(s):
    """OCR 文本清洗：去空白与常见干扰符号"""
    if not s:
        return ""
    s = str(s).strip()
    s = re.sub(r"\s+", "", s)
    return s


def overlay_cover_mode(img):
    """封面主色是蓝紫/纯色块时判为「封面未渲染完」。
    规则（可调）：整图饱和度低 + 亮度集中 + 颜色通道几乎一致。
    回传 (是否未加载, 指标说明)"""
    try:
        small = img.convert("RGB").resize((24, 24))
        px = list(small.getdata())
        if not px:
            return False, "采样失败"
        n = float(len(px))
        r = sum(p[0] for p in px) / n
        g = sum(p[1] for p in px) / n
        b = sum(p[2] for p in px) / n
        spread = max(r, g, b) - min(r, g, b)
        lum = (r + g + b) / 3.0
        blank = spread < 12 and 60 < lum < 210
        return blank, "通道差=%.1f 亮度=%.1f" % (spread, lum)
    except Exception as e:
        return False, "判定异常: %s" % e


def card_top_v(geom, row):
    """卡片顶部的视觉 y（row 从 0 起）。统一行距，两行无差异。"""
    return geom["first_row_y"] + row * geom["row_step"]


def find_cards(img, geom=None, ocr_texts=None):
    """在整帧里定位卡片。
    策略（由强到弱）：① 几何表给出的固定网格里，用「排除区 + 亮度阈值」判断每格是否有卡片；
    ② 对存活格子做封面未加载检测，标记状态。
    回传 [{"col":c,"row":r,"box":(x0,y0,x1,y1),"state":...}, ...]（真机像素坐标）"""
    geom = geom or LOBBY
    sx = img.size[0] / VIEW_W
    sy = img.size[1] / VIEW_H
    out = []
    ncols = len(geom["col_x"])
    area = geom["list_area"]
    first_y = geom["first_row_y"]
    card_h = geom["card_h"]
    row_step = geom["row_step"]
    # 行数由列表区高度 + 行距推出来（保证末行不漏）
    max_rows = int((area[3] - first_y) / row_step) + 1
    for r in range(max(1, max_rows)):
        y0v = card_top_v(geom, r)
        y1v = y0v + card_h
        for c in range(ncols):
            x0v, x1v = geom["col_x"][c]
            # 视觉 -> 真机像素一律用 round：int() 是截断，会把 108.6 变成 108，
            # 实测这 1px 偏移足以让顶部淡字整块读不出来（2026-09-18 踩过）。
            box = (int(round(x0v * sx)), int(round(y0v * sy)),
                   int(round(x1v * sx)), int(round(y1v * sy)))
            if box[3] > img.size[1] or box[2] > img.size[0] or box[1] >= img.size[1]:
                continue
            crop = img.crop(box)
            blank, _why = overlay_cover_mode(crop)
            out.append({"col": c, "row": r, "box": box,
                        "state": "loading" if blank else "normal"})
    return out


def detect_page_state(img):
    """判定当前帧是「正常列表 / 空列表 / 加载失败 / 黑屏 / 禁止截屏」。
    只做能给出证据的判断，判不出来就回 'unknown' 并交给调用方记日志，不猜。"""
    if img is None:
        return "invalid", "图像为空"
    if is_blank(img):
        return "blank", "整帧纯色/黑屏（屏幕熄灭或界面禁截屏，见日志中的成因判定）"
    w, h = img.size
    # 列表区中段取一条横带：若整带亮度极低（深色大底板）通常是空态/加载态遮罩
    y0 = int(h * 0.25)
    y1 = int(h * 0.60)
    x0 = int(w * 0.05)
    x1 = int(w * 0.55)
    band = img.crop((x0, y0, x1, y1)).convert("L")
    lo, hi = band.getextrema()
    avg = sum(band.getdata()) / float(max(band.size[0] * band.size[1], 1))
    if hi - lo < 20 and avg < 70:
        return "empty_or_loading", "列表区近乎纯暗（avg=%.1f 极差=%d）" % (avg, hi - lo)
    return "list", "列表区有内容（avg=%.1f 极差=%d）" % (avg, hi - lo)


def detect_row_bounds(img, geom=None):
    """检测列表视口里「卡片行上边界」的 y（原图像素，升序）—— 顶行对齐红线用。

    依据（2026-09-21 三张真机截图逐行实测，基准图 ec1ab78a @1920x864）：
    行与行之间有约 12px 的**亮色缝隙**（封面可见 302px + 缝隙 12px = 行距 314），
    缝隙行在**三列上同时**表现为「亮 + 平」（横梯度中位数 <3.5 且亮占比 >85%）。
    封面内部的横向结构很难三列同一行同时对齐 —— 这就是缝隙与封面内容边缘的区别。
    实测：图1 顶行卡顶 168（=目标位，对齐）；图2 顶行卡顶 177（偏下 9px，未对齐）。

    返回 (边界y列表|None, 说明dict)。列表首元素 = 视口内第一张**完整**卡片的顶边，
    它与目标位（first_row_y 换算）之差就是「还要往下滚多少像素」。
    判定分三种状态（都能推出同一个结论：还要滚 drift = 首边界 - 目标位）：
      top_in_gap  视口顶部正好落在**一条真正的行缝**里（缝高≈gap_h 且下条缝在行距外）
      aligned     顶部封面基本完整（可见高度 ≥ 封面高 - 容差）→ 已对齐，drift≈0
      cut         顶部封面被视口上沿裁掉 → 第一张完整卡在第一条缝隙之后
    ⚠ 2026-09-22 纠错：列表上沿之上还有一条**页面背景空档**，它也是「亮 + 平」，
    会被亮缝检测当成行缝。旧代码只判「亮平区是否贴着视口上沿」就下 top_in_gap 结论，
    于是「首行已滚出视口」被读成「只差几 px」—— 用户报的「顶部都滑上去超屏了还报已对齐」
    就是这个。现在必须**缝高对得上 gap_h 且缝距对得上行距**才算真行缝，否则判 cut。
    """
    try:
        import numpy as np
    except Exception:
        return None, {"why": "缺少 numpy"}
    geom = geom or LOBBY
    w, h = img.size
    sx, sy = w / float(VIEW_W), h / float(VIEW_H)
    R = geom["row_step"] * sy
    T = geom["first_row_y"] * sy
    cover_h = geom.get("cover_h", 163.6) * sy
    y0 = int(round(geom.get("clip_y", 90.5) * sy)) + 1     # 视口第一行
    y1 = min(h - 2, int(round(geom["list_area"][3] * sy)))
    if y1 - y0 < int(1.6 * R):
        return None, {"why": "列表视口太矮，扫不出一行半（%d..%d）" % (y0, y1)}
    spans = []
    for x0v, x1v in geom["col_x"]:
        a, b = int(round(x0v * sx)) + 8, int(round(x1v * sx)) - 8
        if b - a < 40:
            return None, {"why": "卡片列宽异常（%d..%d）" % (a, b)}
        spans.append((a, b))
    g = np.asarray(img.convert("L"), dtype=np.float32)
    # 逐行统计：flat = 三列横向梯度中位数的**最大值**（缝隙行三列都要平），
    #           brightmin = 三列亮占比的**最小值**（缝隙行三列都要亮）。
    # 用 max/min 而不是均值：只要有一列还是封面（暗/有纹理），这一行就不是缝隙。
    flat = np.full(y1 - y0 + 1, -1.0)
    brightmin = np.full(y1 - y0 + 1, 1.0)
    for a, b in spans:
        band = g[y0:y1 + 1, a:b]
        flat = np.maximum(flat, np.median(np.abs(np.diff(band, axis=1)), axis=1))
        brightmin = np.minimum(brightmin, (band >= 90).mean(axis=1))
    is_gap = (flat < 3.5) & (brightmin > 0.85)
    min_gap = max(4, int(round(geom.get("gap_h", 6.5) * sy * 0.5)))
    gaps, i, n = [], 0, len(is_gap)
    while i < n:
        if is_gap[i]:
            j = i
            while j + 1 < n and is_gap[j + 1]:
                j += 1
            if j - i + 1 >= min_gap:
                gaps.append((y0 + i, y0 + j))
            i = j + 1
        else:
            i += 1
    if not gaps:
        return None, {"why": "视口内找不到行间亮缝（可能已滚到列表末尾，或封面盖住了缝隙）",
                      "y0": y0, "R": round(R)}
    gap_h_dev = geom.get("gap_h", 6.5) * sy
    # 防御 1：整片视口都是「亮 + 平」（空态 / 纯色 / 封面未加载）→ 没有行结构，
    #         绝不能把「没东西」当成「顶行在某个位置」编出一个偏差来。
    if len(gaps) == 1 and gaps[0][0] <= y0 + 2 and gaps[0][1] >= y1 - 2:
        return None, {"why": "视口内整片亮平（空态/纯色/未加载），无行结构可对齐", "y0": y0}
    # 防御 2：视口顶部的「缝隙」比正常行缝宽得多 → 不是行缝（可能是空态边界），
    #         这时候定位不到卡顶，宁可不给值。
    if gaps[0][0] <= y0 + 2 and (gaps[0][1] - gaps[0][0] + 1) > 2.5 * gap_h_dev:
        return None, {"why": "视口顶部亮区过宽（%dpx > 行缝 %.1fpx），不是行间缝隙"
                      % (gaps[0][1] - gaps[0][0] + 1, gap_h_dev), "y0": y0}
    tol = max(5.0, 0.02 * cover_h)
    g0, g1 = gaps[0]
    gap_h_new = gaps[0][1] - gaps[0][0] + 1
    # ── 2026-09-22 用户实测纠错：区分「页面背景空档」与「真行缝」────────────────────
    # 用户原话：「有时候滑动到红线识别也不准，地图顶部都滑上去超出屏幕了，还报顶行已对齐红线。
    #          按照滑动到图片中每张地图位于红框情况。」
    #
    # 逐像素实测（shots\shot_20260922_140417_001.png @2400×1080，141129_002 同形）：
    #   左卡片列 (x=70..340) 纵向剖面：
    #     y=192..208  mean≈190 flat≈2.0   ← 页面背景空档（亮+平）
    #     y=209..211  mean= 85 flat=0.0   ← **3px 暗色分隔线**（「全部」筛选行与卡片列表之间）
    #     y=212..219  mean≈190 flat≈2.0   ← 紧贴其下的又一段亮平空档（8px）
    #     y=220       flat 58 → 封面开始
    #     y=221+      flat≈117            ← **真实卡片封面顶部 = 221**
    #   亮缝检测把 y=210..220（暗分隔线夹在两段亮平区之间）合并成一个 11px 的「缝」，
    #   于是 gaps[0]=(210,220)，g1+1=221 恰好等于**真实卡顶**。
    #
    # 关键：此处第一行卡片**根本没有滑出视口**，它就是视口内第一张完整卡，
    # 只是因为缝里混了分隔线，「缝下沿+1」正好等于卡顶，被旧代码误读成「顶部在缝里」。
    # 真实偏差 = 卡顶 221 - 红线 210 = +11px（卡片整体在红线**下方** 11px，需再向下微滚）。
    #
    # ⚠ 2026-09-22 二次纠错（重要）：「回退一行距反推首行卡顶」这个思路**整体作废**。
    # 我曾据此新增过一个 scrolled_past（首行已整行滑出）状态并让它返回负 drift、触发反向回滚。
    # 全量真机帧重跑 + 放大目视核验后证明该状态**不存在**：
    #   · shot_20260922_141831_002：gaps[0]=(300,325) 落在**卡片封面内部的浅色平坦区**
    #     （封面天空/云雾），根本不是行缝；放大后首行「异兽吞噬进化」的封面、标题、
    #     标签、下载按钮全部完整可见 → 首行没被裁，drift 应为**正**值。
    #   · shot_20260920_143617_003 / shot_20260921_121936_002 同理（h_vis=124/181，
    #     首行残留可见 181~303px）→ 都是 cut，正 drift，应继续**向下**滚。
    #   · 合成帧回归（test_pipeline N2）也直接打脸反推法：S=157 时 g1+1-R = 11.2
    #     落进「视口上方」区间 → 被误判成 drift=-157，而正解是 +157。
    # 根因：单凭「缝在哪」无法区分「顶上是一条被裁的卡」与「顶上没有卡」，
    # 反推会凭空造出负偏差，方向整个反过来 —— 这正是用户报的缺陷更严重的一种形态。
    # 故最终只保留两条可证判据，且**只产出非负 drift**：
    #   ① g0 贴视口上沿 → 缝下沿+1 即首行卡顶（真机实测 221），state=top_in_gap；
    #   ② g0 在视口内部 → 首行被裁（cut），"缝下沿+1" 是下一行卡顶，继续向下滚补齐。
    # 两种情况的正解都是「向下滚」，绝不会出现需要反向回滚的场景。
    if g0 <= y0 + 2:
        first, state = g1 + 1, "top_in_gap"      # 缝下沿之后即首行卡顶（真机实测 221）
    elif (g0 - y0) >= cover_h - tol:
        first, state = y0, "aligned"
    else:
        first, state = g1 + 1, "cut"
    bounds = sorted({first} | {b + 1 for a, b in gaps if b + 1 > first})
    # 校验：相邻边界间距应 ≈ 行距（±8%）。间距乱了说明缝隙误判，宁可不给出
    spacing_ok = all(abs((bounds[k + 1] - bounds[k]) - R) <= 0.08 * R
                     for k in range(len(bounds) - 1))
    return bounds, {"state": state, "T": round(T), "R": round(R), "y0": y0,
                    "gaps": gaps[:5], "spacing_ok": spacing_ok,
                    "gap_h": round(gap_h_new, 1),
                    "h_vis": (gaps[0][0] - y0) if state != "top_in_gap" else 0}


def grid_drift(img, geom=None):
    """顶行相对「红线」（first_row_y）还差多少像素：正 = 要再往下滚，0 = 已贴住红线。

    返回 (drift|None, 说明dict)。这是 align_to_grid 的纯计算部分，便于单测。

    历史与三次纠错（务必按顺序读，前两版都是错的）：
      ① 最初 `max(0, drift)` 把负值夹成 0 —— 错，会让「越滑越偏」被读成「已到位」。
      ② 于是放宽为「如实回传负值」，并新增 scrolled_past（首行已整行滑出视口）状态
         触发反向回滚 —— 同样错，见下。
      ③ **当前版：drift 恒 ≥ 0**，不再有反向回滚。理由：全量真机帧 + 放大目视核验
         证明「首行整行滑出视口」这一状态在本页不存在；被误当成它的帧
         （shot_20260922_141831_002 等）其实是**亮缝检测把卡片封面内部的浅色平坦区
         当成了行缝**，此时首行封面/标题/按钮全部完整可见，正解是继续**向下**滚。
         合成帧回归（test_pipeline N2）也证实「回退一行距反推」会凭空造出负偏差。

    状态与 drift 的对应（均由 detect_row_bounds 判定，本题不做二次推断）：
      · aligned    —— first_top = 视口上沿，drift ≈ 0（首行封面完整贴红线）；
      · top_in_gap —— first_top = 缝下沿+1（= 首行卡顶），drift = 卡顶-红线，**小正值**；
      · cut        —— first_top = 缝下沿+1（= 第二行卡顶），drift = 下一行卡顶-红线，**正大值**。

    ⚠ 2026-09-22 二次纠错：曾有一个 `scrolled_past`（首行已整行滑出视口）状态在这里
    返回负 drift 以触发反向回滚 —— **该状态已证伪并删除**。全量真机帧 + 放大目视核验
    + 合成帧回归三重验证表明：视口内首行从未「整行滑出」，那些看似如此的情况
    （gaps 落在封面内部浅色平坦区）其实是 `cut`，正解是**继续向下滚**。
    因此本函数现在只产出 ≥0 的 drift，调用方不再有「反向回滚」分支。
    """
    bounds, info = detect_row_bounds(img, geom)
    if not bounds:
        return None, info
    T = info["T"]
    drift = int(round(bounds[0] - T))
    info["first_top"] = bounds[0]
    info["drift"] = drift
    return drift, info



# ---------------------------------------------------------------- OCR 引擎
def preprocess(img, mode):
    """字段级预处理。顶部 热度/评分 是半透明彩字叠在封面图上，原样识别常整块丢掉。
    实测（2026-09-18 本页截图 6 卡交叉验证）：
      * 热度：**不要预处理**！原样 6/6 正确；加自动对比度反而把 '111万' 读成 '川1万'（差 100 倍）。
      * 评分：用 'sharp'（自动对比度 + 锐化）最好，能救回小数点（'4.1'/'2.4'）。
    mode: None 原样 / 'auto' 自动对比度+提对比 / 'sharp' 自动对比度+锐化。"""
    if not mode:
        return img
    try:
        if mode in ("auto", "sharp"):
            c = ImageOps.autocontrast(img.convert("RGB"), cutoff=1)
            if mode == "sharp":
                return c.filter(ImageFilter.UnsharpMask(radius=2, percent=180, threshold=2))
            return ImageEnhance.Contrast(c).enhance(2.0)
    except Exception:
        return img
    return img


def parse_field_value(field, txt):
    """把某字段的 OCR 文本转成 (清洗后文本, 数值|None)，并对数值做区间校验。
    区间校验的意义：评分会把小数点读丢（'4.5' -> '★45'），若直接采信就会把 45 当评分；
    这类越界值一律不写数值列，只保留原始文本供人工复核。"""
    if field not in NUMERIC_FIELDS:
        return txt, None
    txt = strip_label(txt, field)
    # 评分用形态匹配（抗星标污染），其余字段用通用 parse_number
    parser = FIELD_PARSERS.get(field, parse_number)
    v, _m = parser(txt)
    if v is not None:
        lo_hi = FIELD_VALID_RANGE.get(field)
        if lo_hi:
            lo, hi = lo_hi
            if (lo is not None and v < lo) or (hi is not None and v > hi):
                return txt, None
    return txt, v


def _pick_consensus(readings):
    """从多次读取结果里挑一个最可信的 (文本, 值)。
    规则：① 有带单位（万/亿）的读法优先，取其中出现次数最多的；
         ② 其次在有效值里取众数，票数相同时优先「带小数点」的读法（信息更完整，
            实测 评分 会抖动出 '4.4' 与 'A2'，带小数点的更像真读法）；
         ③ 全无有效值则返回最长的文本 + None。"""
    unit = [(t, v) for t, v in readings if v is not None and m_has_unit(t)]
    if unit:
        return _vote(unit)
    vals = [(t, v) for t, v in readings if v is not None]
    if vals:
        return _vote(vals)
    best = max(readings, key=lambda r: len(r[0])) if readings else ("", None)
    return best[0], None


def _vote(pairs):
    """在 (文本, 值) 列表里按值投票；票数相同时优先带小数点的文本。"""
    tally = {}
    for t, v in pairs:
        tally.setdefault(v, []).append(t)
    best_v = max(tally, key=lambda k: (len(tally[k]), any("." in t for t in tally[k])))
    texts = tally[best_v]
    best_t = next((t for t in texts if "." in t), texts[0])
    return best_t, best_v


def read_field(engine, crop, field, base_scale):
    """读一个字段。
    数值字段会在一个小阶梯的放大倍数上各读一次，再按多数票挑结果：
      ① 优先「带单位」的读法（热度 '111万' 优于 '111'，前者才不会被漏掉 1e4 倍）；
      ② 其次在有效值里取众数；
      ③ 都没有则数值列留空（原始文本照留，供人工复核）。
    为什么必须多读几次（2026-09-18 实测）：RapidOCR 对同一张裁切图**跨进程结果会抖动**，
    顶部那行淡字尤其明显（c3r2 热度同框在不同次运行里读出 '111万门' / '万'；
    c1r1 评分读出 '4.4' / 'A2'）。单次读取会把抖动当成结论，多档读取投票才稳。"""
    if field not in NUMERIC_FIELDS and field not in FIELD_PREP:
        raw = engine.recognize(crop, scale=base_scale, prep=FIELD_PREP.get(field))
        return parse_field_value(field, clean_text(raw))

    # 数值字段（或需预处理的字段）：在小阶梯上多读几档再投票
    ladder = []
    for s in (base_scale, max(base_scale - 1, 2), base_scale + 1, base_scale + 2):
        if s not in ladder and s >= 1:
            ladder.append(s)

    readings = []
    for s in ladder:
        raw = engine.recognize(crop, scale=s, prep=FIELD_PREP.get(field))
        readings.append(parse_field_value(field, clean_text(raw)))
    return _pick_consensus(readings)


def m_has_unit(text):
    """文本里是否带 万/亿/千/百/w/k 之类的量级单位。"""
    return bool(re.search(r"[万亿千百wWkK]", text or ""))


# ---------------------------------------------------------------- 顶部彩字字段的多配方读取
# 2026-09-22 真机（2400×1080）+ 基准图（1920×864）双通路取证（12 张卡 × 6 配方 × 4 档 ≈ 600 次 OCR）：
# 「热度/评分」是**彩色小字压在封面或亮条上**的字段，单配方单裁切读不稳。实测三类失败：
#   ① **前导数字丢失**（真机 r2c1 '116万' → '16万'/'1万'，值差 10 倍；r2c2 '101万' → '0万'）
#      —— 静默错值，最危险；
#   ② 尾部粘连（'73.3万' → '73.3万福'、'21.1万' → '21.1万2'，读进来的是封面杂字）；
#   ③ 亮条上的淡字整块丢掉（基准图 r2c3 '111万' 原样读只剩 '万'）。
# 实测有效的三个配方维度（**都不含二值掩膜** —— 二值会把细笔画与小数点吃掉：
# 实测 '4.3'→'43'、'73.3万'→'733万'，反而制造错值）：
#   * 原样（无预处理）：基准图上的淡字最好；
#   * **颜色增强灰** color_gray（灰度 = clip((R−B)×k)）：真机红/珊瑚彩字显著提对比，
#     但基准图（旧截图、字更淡）上更差 —— 所以只当**投票成员**，不当唯一配方；
#   * **跳火苗框**（左边界 5.6 → 18.0 视图）：避免火苗被读成前导数字。
# ⚠ 反向教训（已实测）：把框**加宽**（0..62）会让火苗被读成前导数字
#   （'13.1万'→'0113.1万'、'202万'→'2202万'），所以左边界只能右移、绝不能左扩。
PIX_K = 2.2                     # 颜色增强灰的增益
# 两个候选框：左右边界分「原框 / 跳火苗框」，上下边界**统一用信息带高度（-7..32.5 视图）**。
# ⚠ 别复用 LOBBY["fields"] 的字段框高度（-2.2..21.7）：那是「窄框读法」的最小可用高度，
#   用在多配方读法上会把彩字上沿切掉，实测读数直接退化（真机 r2c1 又变回 '16万' 的假值）。
HOT_BOXES_V = ((5.6, -7.0, 57.3, 32.5),     # 原框左右边界 + 信息带上下边界
               (18.0, -7.0, 57.3, 32.5))    # 跳火苗框（左边界右移）
COLOR_SCALES = (3, 4, 6, 8)     # 多档尺度：RapidOCR 跨进程会抖动，单档取值不可信


def color_gray(img, k=PIX_K):
    """红/珊瑚彩字增强：灰度 = clip((R − B) × k)。

    红字在蓝底/浅色条上 R−B 很大，封面杂色极少是纯红 —— 等价于「按颜色挑字」，
    又不像二值掩膜那样把细笔画的抗锯齿边缘一起吃掉（实测二值掩膜把 '101万' 读成 '0方'）。"""
    try:
        import numpy as np
        a = np.asarray(img.convert("RGB")).astype(np.float32)
        g = (a[:, :, 0] - a[:, :, 2]) * float(k)
        return Image.fromarray(np.clip(g, 0, 255).astype(np.uint8)).convert("RGB")
    except Exception:
        return img


def heat_value(text):
    """热度读数 → 数值|None。要求「带单位」且**数字部分不以 0 开头**。

    丢前导 '1' 会造出 '0万' 这类假值（实测真机 r2c2 给出过 '0万' → 0），而热度真值
    不会以 0 开头；加宽左边界时火苗被读成前导数字则会造出 '0113.1万' —— 两者都判无效。
    宁可留空让人工复核，也不写入一个假数值。"""
    if not m_has_unit(text):
        return None
    m = re.search(r"(\d+(?:\.\d+)?)", (text or "").replace(",", "").replace("，", ""))
    if not m or m.group(1).startswith("0"):
        return None
    v, _hit = parse_number(text)
    return v


def digits_len(text):
    """文本里的数字个数 —— 判定「位数最多优先」用。"""
    return len(re.findall(r"\d", text or ""))


def _modal_reading(readings):
    """一组读数 [(文本, 值)] → (代表文本, 值, 票数, 有效票数)。

    按**值**聚类：同一值的不同文本（'73.3万' / '73.3万福'）算同一票；
    代表文本取「票数最多、其次最短」的那条（尾部粘连时更短的才是干净读法）。"""
    tally = {}
    for t, v in readings:
        if v is None:
            continue
        tally.setdefault(v, []).append(t)
    if not tally:
        return "", None, 0, 0
    v, texts = max(tally.items(), key=lambda kv: (len(kv[1]), -min(len(x) for x in kv[1])))
    rep = sorted(texts, key=len)[0]
    return rep, v, len(texts), sum(len(x) for x in tally.values())


def decide_readings(modals):
    """多配方读数 → (文本, 值, 判定说明)。纯函数，便于单测。

    `modals` = [(配方名, 代表文本, 值, 票数)]，值 None 表示该配方没读出有效值。
    判定优先级（按 12 张卡实测校准，文件头有取证）：
      1) 只有一个不同的有效值 → 采纳；
      2) 多个 → **数字位数最多**的那个（OCR 丢字远比凭空多字常见，前导丢失已实测两次）；
         位数打平 → 票数最多的；再打平 → 弃权（错值比空值更糟）；
      3) 一个有效值都没有 → 交给上层用 sharp 复核。
    """
    valid = [(n, t, v, c) for n, t, v, c in modals if v is not None]
    if not valid:
        return "", None, "no_value"
    by_val = {}
    for n, t, v, c in valid:
        by_val.setdefault(v, {"texts": [], "votes": 0, "recipes": []})
        by_val[v]["texts"].append(t)
        by_val[v]["votes"] += c
        by_val[v]["recipes"].append(n)
    if len(by_val) == 1:
        v = list(by_val)[0]
        return sorted(by_val[v]["texts"], key=len)[0], v, "single"
    top_digits = max(digits_len(t) for v, d in by_val.items() for t in d["texts"])
    cand = {v: d for v, d in by_val.items()
            if max(digits_len(t) for t in d["texts"]) == top_digits}
    best_votes = max(d["votes"] for d in cand.values())
    winners = [v for v, d in cand.items() if d["votes"] == best_votes]
    if len(winners) > 1:
        return "", None, "conflict(%s)" % "/".join(str(w) for w in sorted(winners))
    v = winners[0]
    return sorted(cand[v]["texts"], key=len)[0], v, "most_digits"


def read_heat(engine, img, box, scales=COLOR_SCALES):
    """热度：多配方（原样 / 颜色增强灰 × 原框 / 跳火苗框）多档尺度读取，按规则定值。

    返回 (文本, 值|None, detail)。detail 含每个配方的读数与判定说明 `why`，
    便于日志与人工复核。这是「热度」的专用读法：它压在封面亮条上、左侧还有火苗图标，
    单配方最容易丢**前导数字**（实测 '116万' → '16万'，值差 10 倍）。
    """
    sx = img.size[0] / float(VIEW_W)
    sy = img.size[1] / float(VIEW_H)
    modals = []
    detail = {}
    for i, vb in enumerate(HOT_BOXES_V):
        rect = (box[0] + int(round(vb[0] * sx)), box[1] + int(round(vb[1] * sy)),
                box[0] + int(round(vb[2] * sx)), box[1] + int(round(vb[3] * sy)))
        crop = img.crop(rect)
        for prep in ("raw", "colorgray"):
            name = "%s%s" % (prep, "" if i == 0 else "·跳火苗")
            src = color_gray(crop) if prep == "colorgray" else crop
            readings = []
            for sc in scales:
                t = clean_text(engine.recognize(src, scale=sc))
                readings.append((t, heat_value(t)))
            rep, v, votes, _tot = _modal_reading(readings)
            detail[name] = readings
            modals.append((name, rep, v, votes))
    txt, val, why = decide_readings(modals)
    if val is None:
        # 全部配方都读不出 → sharp + 跳火苗框复核（覆盖基准图那种「淡字整块丢」的情况；
        # 只用于复核、不参与投票：实测 sharp 会把火苗读成 '川' 造出 '川1万' 这类假值）
        vb = HOT_BOXES_V[1]
        rect = (box[0] + int(round(vb[0] * sx)), box[1] + int(round(vb[1] * sy)),
                box[0] + int(round(vb[2] * sx)), box[1] + int(round(vb[3] * sy)))
        crop = img.crop(rect)
        vals = []
        for sc in scales:
            t = clean_text(engine.recognize(crop, scale=sc, prep="sharp"))
            vals.append((t, heat_value(t)))
        detail["sharp·跳火苗(复核)"] = vals
        rep, v, votes, _tot = _modal_reading(vals)
        if v is not None and votes >= max(2, len(scales) - 1):
            detail["why"] = "sharp_rescue"
            return rep, v, detail
        detail["why"] = why
        return "", None, detail
    detail["why"] = why
    return txt, val, detail


# 评分兜底：主读（原框 + sharp 阶梯投票）读不出时，换左边界再试几次。
# 取证（2026-09-22，12 张卡 × 30 组合）：把左边界从 71 移到 78，能把基准图 r1c2
# 那种「星标把数字挤得靠右」的卡救回成 '4.5'（3 档一致）。
# ⚠ 被否决的方案：**跟着星标右缘自适应** —— 星标与数字贴在一起时右缘算不准，
#   实测会把数字首位切掉（'3.6'→'36'、'4.3'→'3'），比固定框更差。
# 为什么敢用：裁切失败的形态是「丢小数点」（'36'/'43'/'4'），parse_score 直接返回 None，
#   所以这个兜底**只会补值、几乎不会造假值**（这也是它只在主读失败时才启用的原因）。
SCORE_RETRY_OFFSETS = (74.0, 78.0)   # 视图坐标：左边界候选（71 是主框）
SCORE_RETRY_RIGHT = 100.0            # 视图坐标：右边界（数字最远到 ~95）
SCORE_RETRY_SCALES = (4, 6, 8)
SCORE_RETRY_VOTES = 2                # 至少 2 档给出同一分值才采纳（单档可能是抖动）


def read_score_retry(engine, img, box, scales=SCORE_RETRY_SCALES):
    """评分兜底读法。返回 (文本, 值|None, detail)。

    只在主读没拿到值时调用：多左边界 × 双配方 × 多档尺度，取多数票。
    票数不足或出现并列 → 不给值（错值比空值更糟）。
    """
    sx = img.size[0] / float(VIEW_W)
    sy = img.size[1] / float(VIEW_H)
    votes = {}
    detail = {}
    reps = {}
    for lx in SCORE_RETRY_OFFSETS:
        rect = (box[0] + int(round(lx * sx)), box[1] + int(round(-7 * sy)),
                box[0] + int(round(SCORE_RETRY_RIGHT * sx)), box[1] + int(round(32.5 * sy)))
        crop = img.crop(rect)
        for prep in ("sharp", "colorgray"):
            name = "%s@%.0f" % (prep, lx)
            readings = []
            for sc in scales:
                src = color_gray(crop) if prep == "colorgray" else crop
                t = clean_text(engine.recognize(src, scale=sc) if prep == "colorgray"
                               else engine.recognize(crop, scale=sc, prep="sharp"))
                v, _hit = parse_score(t)
                readings.append((t, v))
                if v is not None:
                    votes[v] = votes.get(v, 0) + 1
                    reps.setdefault(v, t)
            detail[name] = readings
    if not votes:
        return "", None, detail
    best = max(votes.values())
    winners = [v for v, c in votes.items() if c == best]
    if len(winners) > 1 or best < SCORE_RETRY_VOTES:
        detail["why"] = "conflict(%s)" % "/".join(str(w) for w in sorted(winners)) \
            if len(winners) > 1 else "too_few_votes(%d)" % best
        return "", None, detail
    v = winners[0]
    return reps.get(v, ""), v, detail


class OcrEngine:
    """OCR 引擎封装。RapidOCR 为唯一后端，未安装时给出明确提示（不静默降级）。"""
    def __init__(self):
        self.engine = None
        self.status = "未加载"
        self.error = ""

    def load(self):
        try:
            from rapidocr_onnxruntime import RapidOCR
            self.engine = RapidOCR()
            self.status = "RapidOCR(onnxruntime) 就绪"
        except Exception as e:  # 引擎缺失必须显式报告，不能假装成功
            self.engine = None
            self.status = "OCR 引擎不可用"
            self.error = "%s: %s" % (type(e).__name__, e)
        return self.status

    @property
    def ready(self):
        return self.engine is not None

    def recognize(self, pil_img, scale=2, prep=None):
        """裁切图 -> 文本。scale 为放大倍数，小字建议 2~3；prep 为字段级预处理模式。"""
        if not self.ready:
            return ""
        try:
            w, h = pil_img.size
            if w == 0 or h == 0:
                return ""
            img = preprocess(pil_img, prep)
            if scale and scale > 1:
                img = img.resize((w * scale, h * scale), Image.LANCZOS)
            import numpy as np
            arr = np.array(img)[:, :, ::-1]  # RGB -> BGR
            result, _ = self.engine(arr)
            if not result:
                return ""
            # result: [[box, text, score], ...]，按纵向、横向排序拼成一行
            items = []
            for item in result:
                box = item[0]
                ys = [p[1] for p in box]
                xs = [p[0] for p in box]
                items.append((min(ys), min(xs), str(item[1])))
            items.sort()
            return "".join(t[2] for t in items)
        except Exception as e:
            self.error = "识别异常 %s: %s" % (type(e).__name__, e)
            return ""


# ---------------------------------------------------------------- adb 权限诊断
# `adb shell input swipe` 走的是 Android 的输入注入通道（InputManager.injectInputEvent）。
# 部分 ROM 把 shell 用户挡在 INJECT_EVENTS 之外，报：
#   java.lang.SecurityException: Injecting input events requires the caller
#   (or the source of the instrumentation, if any) to have the INJECT_EVENTS permission.
# 这是**手机侧的权限限制，不是工具 bug**（栈里是 InputShellCommand.sendSwipe，
# 说明命令已经正确下发到系统 shell，只是被安全策略拒了）。
# 合规解法只有两条：开 ROM 的对应开关，或者干脆不用自动上滑、改人手滑动。
# ⚠ 本工具不使用 root / sendevent / monkey 事件脚本 / 注入框架（无条件，不分场合）
#   —— 它们属于绕过 ROM 安全策略，会踩到本工具的合规红线（见文件头）。
ADB_INJECT_DENIED = "INJECT_EVENTS"

ADB_INJECT_FIXES = [
    "① 小米/红米（MIUI / HyperOS）：开发者选项里打开「USB 调试（安全设置）」"
    "（需登录小米账号并联网，打开后 adb 才能模拟点击/滑动）",
    "② 华为/荣耀：开发人员选项里打开「仅充电模式下允许 ADB 调试」与「允许模拟点击」",
    "③ 确认手机当前处于**主用户**：退出「应用分身 / 隐私空间 / 第二空间 / 工作资料」。"
    "副用户下 shell 无法向主屏注入事件（`adb shell am get-current-user` 应为 0）",
    "④ 多屏 / 折叠屏 / 投屏时指定主显示：`adb shell input -d 0 swipe x1 y1 x2 y2 500`",
    "⑤ 以上都不行就**别用自动上滑**：取消勾选「每次截屏后自动上滑」，"
    "改用「工具按间隔截屏 + 你在手机上手动上滑一页」，这条路径完全不依赖注入权限",
]


# ---------------------------------------------------------------- 上滑参数
# 大厅列表是**连续滚动**（底部常露出半个第三行），一屏不是一个固定单位，
# 所以「上滑」没有放之四海皆准的值，只能给出保守默认并允许现场微调。
# 2026-09-20 真机反馈「滑过头了」：原默认 幅度 55% + 时长 350ms 属「快速甩动」，
# 抬手后列表靠惯性继续滚，一次跨过一页多。改小幅度 + 拉长时长 = 慢速拖动，惯性小。
SWIPE_PCT_DEFAULT = 0.35   # 上滑距离为屏幕高度的百分比
SWIPE_MS_DEFAULT = 800     # 按下到抬起的时长(ms)：越长惯性越小


def swipe_args(w, h, percent=SWIPE_PCT_DEFAULT, duration=SWIPE_MS_DEFAULT, display=None):
    """构造 `adb shell input swipe` 的参数列表（纯函数，便于单测）。
    起点 y=78%、终点 y=(78% - 幅度)、x 取屏幕中线。"""
    x = int(w * 0.5)
    y1 = int(h * 0.78)
    y2 = int(h * (0.78 - percent))
    args = ["shell", "input"]
    if display is not None:
        args += ["-d", str(display)]
    args += ["swipe", str(x), str(y1), str(x), str(y2), str(duration)]
    return args


# ---------------------------------------------------------------- 滑动位移测量
# 「测试滑动」原来只判定「能不能注入」，日志一句「通过」——用户看不到到底滑了多少，
# 也就没法据此调幅度（2026-09-20 用户反馈「测试滑动不会实际滑动，不方便测试滑动幅度」）。
# 现在滑完再截一帧，用两帧比对量出**实际滚动像素**，把「滑过头」这种主观感受变成可比对的数。
MANUAL_MEASURE_WAIT = 5.0   # 手动测量时留给用户的操作窗口（秒）
SWIPE_SETTLE_SEC = 1.0      # 自动滑动后等惯性停下的**最小**等待（秒）
# 2026-09-21：用户反馈「测试的滑动每次距离都不一」。两个来源：
#   ① 固定等 1.0s 就截屏 —— 惯性还没跑完时量到的是**中间态**，每次停的位置不同 → 数值飘；
#   ② fling 手势本身有方差（Android 速度跟踪器 + 系统负载），同样参数也不是同一个落点。
# 对策分别是：轮询到「两帧不再变化」才截（下面 wait_scroll_stop），以及连测多次取中位数
# 并**如实报出离散度**（summarize_runs），不再拿单次测量当结论。
SCROLL_STOP_TIMEOUT = 4.0   # 轮询「滚停」的时间上限（秒），超时就用最后一帧
SCROLL_STOP_INTERVAL = 0.35 # 轮询间隔（秒）
SWIPE_RUNS_DEFAULT = 3      # 「测滑动」默认连测次数（1~5，界面可调）
# 大厅页顶部约 19.4% 是固定区（页签/标题，LOBBY 卡顶 168/864 = 0.194），不随列表滚动。
# 位移测量必须把它排除——否则列表块被拿去跟固定区比对，残差整体抬高、一律判「测不出」。
LIST_TOP_RATIO = 0.20


def _gray_small(img, np, target_h=400, max_w=1600, blur=1.2):
    """统一成小灰度图：既控制计算量，也让不同分辨率共用同一套阈值。

    **按高度缩放，不按宽度**（2026-09-20 实测修正）：测量的是**纵向**位移，纵向分辨率才是关键。
    按宽度缩到 420 的话，横屏 2400×1080 缩完只有 **189px 高**，模板块仅 22px —— 信息量太少，
    真机两帧根本匹配不上（表现为「找不到稳定匹配」）。改按高度 400 后，同一张图是 889×400。

    **缩放后还要轻度模糊**（同日再修）：高频细节（封面纹理、噪点、细字）对「半像素」错位
    极其敏感 —— 真机位移换算到缩略图上往往不是整数（如 520px / 2.25 = 231.1），正确位移处的
    残差会涨到跟错误位移差不多（实测纯噪声 520px：正确 17.9 vs 次优 20.0，比值 0.89，
    被显著性阈值判成「找不到稳定匹配」）。加 GaussianBlur(1.2) 后同一组降到 2.5 vs 6.3
    （比值 0.39），而 block 位置判定依旧精确（仍命中 232，真值 231.1）。
    """
    g = img.convert("L")
    w, h = g.size
    nh = target_h if h > target_h else h
    nw = max(1, int(round(w * nh / float(h))))
    if nw > max_w:                       # 极端宽画幅兜底，避免横向计算量爆炸
        nw = max_w
        nh = max(1, int(round(h * nw / float(w))))
    if (nw, nh) != (w, h):
        g = g.resize((nw, nh), Image.BILINEAR)
    if blur and blur > 0:
        g = g.filter(ImageFilter.GaussianBlur(blur))
    return np.asarray(g, dtype=np.float32)


def measure_scroll(prev, nxt, max_shift_ratio=0.92, top_ratio=LIST_TOP_RATIO, direction=1):
    """估计两帧之间的垂直滚动量：下一帧的内容相对上一帧移动了多少像素。

    direction=1：内容**向上**移（列表前滚），返回正值；
    direction=-1：内容**向下**移（列表回滚，align_to_grid 行界回滚用），返回**负值**。
    方向必须由调用方给定（滑动指令自己发的，方向已知）—— 不做双向搜索：
    双向会把候选集翻倍，周期别名（真值±行距）更容易抢票，正向测量的可靠性不能为此买单。

    返回 (shift_px|None, 说明)。shift_px 已按缩放比还原成**原图**像素（带符号）。

    **逐块投票，不是全局最优**（2026-09-21 重写）：旧版对所有块求「同一个位移下的中位残差」，
    隐含假设是**整屏内容一起移动**。但大厅页顶部有一条约占屏高 19.4% 的**固定区**（页签/标题，
    见 LOBBY 卡顶 168/864），它不随列表滚动 —— 位移一大，列表里的块被拿去跟**顶部固定区**比，
    残差被整体抬高，最佳与次优几乎并列（真机失败样本比值 0.96 / 0.98）→ 一律判「测不出」。
    现在改成：每个块自己投一票（选出该块的最佳位移），再按位移聚类取**最大簇**：
    固定区的块会投 0，列表区的块投真值，多数胜出；动效/换封面导致对不上的块直接弃权。
    """
    try:
        import numpy as np
    except Exception:
        return None, "缺少 numpy，无法测量位移"
    a = _gray_small(prev, np)
    b = _gray_small(nxt, np)
    if a.shape != b.shape:
        return None, "两帧尺寸不一致（%s vs %s）" % (prev.size, nxt.size)
    H, W = a.shape
    scale = float(prev.size[1]) / float(H)
    max_s = int(H * max_shift_ratio)
    bh = max(6, int(H * 0.09))
    bw = max(6, int(W * 0.22))
    # 只取**列表区**的块：顶部固定区（页签/标题）不参与滚动，取它只会污染投票。
    # 同时候选位移也受它约束：第一帧 y 处的内容落到第二帧 y-s，若 y-s 落进固定区，
    # 说明这块内容已经滚到固定区底下、在第二帧里根本不存在 —— 这样的候选必须排除。
    y0 = int(H * top_ratio)
    ys = [int(H * f) for f in (0.24, 0.32, 0.40, 0.48, 0.56, 0.64, 0.72, 0.80, 0.88)]
    xs = [int(W * f) for f in (0.06, 0.34, 0.62)]

    votes = []          # [(位移, y, x)] —— 每个可信块投一票
    nblocks = 0
    for y in ys:
        if y < y0 or y + bh > H:
            continue
        for x in xs:
            if x + bw > W:
                continue
            nblocks += 1
            tpl = a[y:y + bh, x:x + bw]
            # 该块能取到的位移上限：前滚时再大内容就落进顶部固定区了；
            # 回滚时内容往下走，上限由屏幕下沿约束。
            if direction < 0:
                smax = min(max_s, H - bh - y)
            else:
                smax = min(max_s, y - y0)
            cands = []
            s = 0
            while s <= smax:
                y2 = y + s if direction < 0 else y - s
                cands.append((float(np.abs(tpl - b[y2:y2 + bh, x:x + bw]).mean()), s))
                s += 2
            if len(cands) < 4:
                continue
            cands.sort()
            bestd, bests = cands[0]
            # 该块是否「可信」：最佳要显著优于次优，也要显著优于该块的平均失配水平。
            # 动效区 / 封面换图 / 界面切换的块过不了这道关，直接弃权，不参与投票。
            second = next((d for d, s2 in cands if abs(s2 - bests) > 4), None)
            base = float(np.median([d for d, _ in cands]))
            if second is None or bestd > 0.80 * second or bestd > 0.70 * base:
                continue
            if bests > smax - 6:
                continue
            votes.append((bests, bestd, base, y, x))

    if len(votes) < 3:
        return None, ("可比对的内容块不足（%d/%d）：界面可能已切换，或一次滚动幅度过大"
                      "（重叠区太小）——把「上滑幅度」调小到 0.20 再测一次" % (len(votes), nblocks))
    # 按位移聚类（±4px 内算同一簇）
    votes.sort()
    clusters = []
    cur = [votes[0]]
    for v in votes[1:]:
        if v[0] - cur[-1][0] <= 4:
            cur.append(v)
        else:
            clusters.append(cur)
            cur = [v]
    clusters.append(cur)

    def _cl_score(cl):
        return (len(cl),
                float(np.median([v[1] for v in cl])),
                float(np.median([v[2] for v in cl])),
                cl[len(cl) // 2][0])

    scored = [_cl_score(cl) for cl in clusters]
    max_sup = max(s[0] for s in scored)
    # 只在「票数够多」的簇里挑：小簇可能是固定区/动效的杂票
    pool = [s for s in scored if s[0] >= max(3, 0.5 * max_sup)]
    if not pool:
        return None, ("投票太分散（最大簇 %d 票 / 总 %d 票）：列表内容可能整页换掉了，"
                      "或存在大面积动效。请停在同一页再测。" % (max_sup, len(votes)))
    # 同票时**比残差**：卡片列表有固定行距，`真值` 与 `真值±行距` 都能对上（周期别名），
    # 票数会打平；但别名对上的是**别的卡片**，残差明显更高 —— 用残差把真值挑出来。
    sup, mad, base, s0 = sorted(pool, key=lambda t: (-t[0], t[1]))[0]
    quality = mad / base if base else 1.0
    if quality > 0.55:
        return None, ("匹配质量不足（残差 %.1f / 失配基线 %.1f = %.2f）：两帧内容差异过大，"
                      "可能是界面已切换或封面大面积重绘。请停在同一页再测。"
                      % (mad, base, quality))
    top = [v for v in votes if abs(v[0] - s0) <= 4]
    # 在最大簇内做 ±3px 的精修（步长 1），把 2px 粗搜的量化误差补回来
    # sgn：回滚时内容下移（y2 = y+s）且返回负值；前滚内容上移（y2 = y-s）返回正值。
    sgn = -1 if direction < 0 else 1
    best_s, best_d = s0, None
    for s in range(max(0, s0 - 3), min(max_s, s0 + 3) + 1):
        ds = []
        for v in top:
            y, x = v[3], v[4]
            y2 = y - sgn * s
            if y2 < y0 or y2 + bh > H:
                continue
            ds.append(float(np.abs(a[y:y + bh, x:x + bw] - b[y2:y2 + bh, x:x + bw]).mean()))
        if ds:
            d = float(np.median(ds))
            if best_d is None or d < best_d:
                best_d, best_s = d, s
    return sgn * int(round(best_s * scale)), ("命中 %d/%d 块，残差 %.1f（失配基线 %.1f）"
                                              % (len(top), len(votes), best_d, base))


def swipe_advice(finger_px, actual_px, page_px, pct=SWIPE_PCT_DEFAULT):
    """把「手指位移 / 实际滚动 / 一页高度」翻成人话判定 + 建议幅度（纯函数，便于单测）。

    返回 (判定, 说明, 建议幅度|None)。目标：一次滚动 ≈ 一页（2 行卡片）。
    建议幅度为 None 表示不该改（或测不出，给不出依据）。
    """
    if actual_px is None:
        return "测不出", "两帧对不上，可能界面已切换或列表没有滚动。回到列表页再测一次。", None
    if actual_px <= 2:
        return ("几乎没动",
                "实际滚动≈0。三种可能：列表已滚到底、当前页面不支持滚动、或注入没真正生效。"
                "先确认列表还能往下滚。", None)
    pr = actual_px / float(page_px) if page_px else 0.0
    ratio = actual_px / float(finger_px) if finger_px else 0.0
    # 按比例反推：想让实际滚动落到一页，幅度应乘以 页高/实际滚动
    new_pct = pct * (float(page_px) / float(actual_px))
    new_pct = max(0.10, min(0.80, round(new_pct, 2)))
    if pr > 1.3:
        return ("滑过头",
                "实际滚动 %dpx ≈ %.1f 页（是手指位移 %dpx 的 %.1f 倍）——惯性偏大，仍是甩动手势。"
                "建议把「上滑幅度」调到 %.2f、或拉长「时长」后再测一次。"
                % (actual_px, pr, finger_px, ratio, new_pct), new_pct)
    if pr < 0.7:
        return ("没滑够",
                "实际滚动 %dpx ≈ %.1f 页，不到一页，翻页会漏卡。"
                "建议把「上滑幅度」调到 %.2f 后再测一次。" % (actual_px, pr, new_pct), new_pct)
    return ("合适",
            "实际滚动 %dpx ≈ %.1f 页（手指位移 %dpx 的 %.1f 倍），一次大约翻一页，可以开始采样。"
            % (actual_px, pr, finger_px, ratio), None)


def wait_scroll_stop(adb, timeout=SCROLL_STOP_TIMEOUT, interval=SCROLL_STOP_INTERVAL,
                     min_wait=SWIPE_SETTLE_SEC * 0.4):
    """滑完之后**等列表真的停下**再截：轮询截屏，直到连续两帧位移为 0。

    固定 sleep 1s 是「每次距离都不一样」的头号来源 —— 惯性没跑完时量到的是中间态，
    而 fling 的衰减时长每次都不同（系统负载、抬手瞬间的速度估计都会变）。

    返回 (最后一帧|None, 耗时秒, 是否在超时前停稳)。
    """
    import time as _t
    t0 = _t.time()
    _t.sleep(min_wait)
    prev, err = adb.screencap()
    if prev is None:
        return None, _t.time() - t0, False
    while True:
        _t.sleep(interval)
        cur, err2 = adb.screencap()
        if cur is None:
            break
        shift, _why = measure_scroll(prev, cur)
        if shift is not None and shift <= 2:   # 两帧基本没动 = 已经停住（留 2px 容差）
            return cur, _t.time() - t0, True
        prev = cur
        # 硬截止：**比对完再判超时**。旧版只在循环头判断，而 measure_scroll + 截屏本身要
        # 花 0.3~1s，实测会一路跑到 4.9~5.1s 才停，日志里全是「仍未停稳」的假警报。
        if _t.time() - t0 >= timeout:
            break
    return prev, _t.time() - t0, False


def summarize_runs(values, page_px=0):
    """把连测 N 次的位移汇总成「中位数 + 离散度 + 稳定性判定」（纯函数，便于单测）。

    单次测量**不可信**：fling 的落点本身就是随机变量。这里不替用户把方差抹掉，
    而是把它算出来一起报出去 —— 离散度大时明确告诉他「这个值别直接拿去调参」。

    返回 dict：n / median / min / max / spread / ratio / verdict / advice。
    """
    vals = [v for v in (values or []) if v is not None]
    n = len(vals)
    if n == 0:
        return {"n": 0, "median": None, "min": None, "max": None, "spread": None,
                "ratio": None, "verdict": "测不出",
                "advice": "一次都没量出来。确认停在列表页、屏幕已点亮，再点一次。"}
    s = sorted(vals)
    mid = n // 2
    med = s[mid] if n % 2 else int(round((s[mid - 1] + s[mid]) / 2.0))
    lo, hi = s[0], s[-1]
    spread = hi - lo
    ratio = spread / float(med) if med else 0.0
    if med <= 2:
        return {"n": n, "median": med, "min": lo, "max": hi, "spread": spread,
                "ratio": ratio, "verdict": "几乎没动",
                "advice": ("%d 次都是 ≈0px：列表很可能已经滚到底，或当前页面不支持滚动。"
                           "先手动确认列表还能往下滚，再测。" % n)}
    if ratio <= 0.15:
        v = "稳定"
        a = ("%d 次波动 %dpx（占中位数 %.0f%%），可以信。用中位数 %dpx 调参："
             "把建议幅度填进去后复测一次确认即可。" % (n, spread, ratio * 100, med))
    elif ratio <= 0.35:
        v = "一般"
        a = ("%d 次波动 %dpx（占中位数 %.0f%%）——惯性还在起作用，单次值有偶然性。"
             "取中位数 %dpx 调参；想要更稳就把「时长」拉到 1200ms 以上（拉动而非甩动，惯性方差更小）。"
             % (n, spread, ratio * 100, med))
    else:
        v = "不稳定"
        a = ("%d 次波动 %dpx（占中位数 %.0f%%），**单次测量不可信**。两个常见原因："
             "① 手势仍是甩动（幅度大 + 时长短），惯性把落点撑开了；"
             "② 已经滚到列表末尾，靠后的几次被截断成 0。"
             "对策：把「时长」拉到 1200~1500ms、「幅度」调小，让手势变成拖动；"
             "或点「测手动滑动」取一个稳定的目标值。中位数 %dpx 仅供参考。"
             % (n, spread, ratio * 100, med))
    return {"n": n, "median": med, "min": lo, "max": hi, "spread": spread,
            "ratio": ratio, "verdict": v, "advice": a}


def plan_next_swipe(target_px, achieved_px, last_finger_px, last_actual_px,
                    gain_fallback=1.0):
    """闭环校正的纯计算：已知上一轮「手指位移 → 实际滚动」，求下一轮该给多少手指位移。

    Android 的 `input swipe` 是**开环**的：手指走多少，列表滚多少取决于阻尼与惯性，
    各机型、各列表都不同 —— 所以「精确」只能靠**边量边补**，不能靠算准一次。
    返回 (还需要滚多少, 本轮手指位移, 增益)。`还需要滚多少 <= 0` 表示已到位。
    """
    gain = gain_fallback
    if last_finger_px and last_actual_px and last_finger_px > 0:
        g = float(last_actual_px) / float(last_finger_px)
        # 异常保护：滑了却没动 / 反向，别让增益变成 0 或负数去反推出无穷大的手指位移
        if 0.05 < g < 20.0:
            gain = g
    remaining = int(target_px) - int(achieved_px)
    finger = int(round(remaining / gain)) if gain else int(round(remaining))
    return remaining, finger, gain


# ---------------------------------------------------------------- 实时屏幕流（2026-09-21）
# 用户问「每次滑动还是不一，不够精确，能实时监测手机屏幕吗」—— **能**，而且这是把
# 「测不准」根治掉的路子，不只是「看得见」：
#   * `screencap` 实测 2.11s/帧（≈0.5fps），只能抓「滑之前 / 滑之后」两帧。位移一大，
#     两帧重叠区就太小 → 匹配失败（日志里那句「测不出（两帧找不到稳定匹配）」）；
#     而且量到的是某一瞬间的值，惯性没跑完就是中间态 —— 这就是「每次都不一」的来源。
#   * `adb exec-out screenrecord --output-format=h264 -` 能把屏幕**连续**吐出来
#     （本机实测：121 帧 / 4.6s ≈ 26fps），用 ffmpeg 解成裸帧即可逐帧处理。
#   有了连续帧，位移就不必「两帧估计」，而是**沿帧链逐段积分**：每段只有几十 px，
#   必然匹配得上，总和就是这一滑的**完整真实位移** —— 惯性衰减快慢、什么时候停，
#   都不再影响结果（真机验证见知识库变更记录）。
# 合规边界不变：只读屏幕输出，不改客户端、不注入进程、不需要 root。
LIVE_MAX_SEC = 170          # screenrecord 单次上限（Android 硬限 180s，留余量）
LIVE_BITRATE = 4000000      # 4Mbps：量位移够用，再高只是白占 USB 带宽
LIVE_BUFFER_MAX = 200       # 环形缓冲保留的测量帧数（≈7s @26fps）
LIVE_SMALL_H = 400          # 存帧高度：与 _gray_small 的目标高度一致，不重复降质
LIVE_TAIL_SEC = 1.8         # 滑完之后继续录多久（覆盖惯性尾巴）
LIVE_WARMUP_SEC = 0.8       # 起流后先跑一会：头几帧可能是旧帧/未编码完的帧
LIVE_STEPS = (1, 2, 3, 5)   # 帧链步长：一段位移太大就自动跳帧比对，保证每段都搜得到
FFMPEG_INSTALL = (".venv\\Scripts\\pip install imageio-ffmpeg "
                  "-i https://pypi.tuna.tsinghua.edu.cn/simple")


def find_ffmpeg():
    """定位 ffmpeg：优先 imageio-ffmpeg 自带的静态二进制，其次系统 PATH。找不到返回空串。"""
    try:
        import imageio_ffmpeg
        p = imageio_ffmpeg.get_ffmpeg_exe()
        if p and os.path.exists(p):
            return p
    except Exception:
        pass
    try:
        return shutil.which("ffmpeg") or ""
    except Exception:
        return ""


class LiveScreen:
    """连续的手机屏幕流：`exec-out screenrecord` → ffmpeg 解 H.264 → BGR24 裸帧。

    对外只给三样东西：
      latest()      —— 最新一帧（原分辨率 RGB，用于显示 / 抓帧到主画布）
      burst()       —— 环形缓冲里的测量帧（灰度，高 400），按时间正序
      frame_scale   —— 把「测量帧像素」换算回「原图像素」的系数
    """

    def __init__(self, adb):
        self.adb = adb
        self.p_adb = None
        self.p_ff = None
        self.th = None
        self.stop_flag = False
        self.w = self.h = 0
        self.frame_scale = 1.0
        self.seq = 0          # 已收到的总帧数（单调递增：用来判断有没有新帧）
        self.err = ""
        self._t0 = 0.0
        self._lock = threading.Lock()
        self._last = None     # 最新原分辨率帧（PIL RGB）
        self._buf = []        # [(seq, 灰度小帧)] 环形缓冲

    # ------------------------------------------------------------ 启动 / 停止
    def start(self, size):
        w, h = int(size[0]), int(size[1])
        w -= w % 2            # screenrecord 要求宽高为偶数
        h -= h % 2
        ff = find_ffmpeg()
        if not ff:
            self.err = ("找不到 ffmpeg，无法解码 screenrecord 的 H.264 流。\n"
                        "在本工具目录执行一次：\n  " + FFMPEG_INSTALL)
            return False, self.err
        if not self.adb.path or not os.path.exists(self.adb.path):
            self.err = "adb 路径无效：%s" % (self.adb.path or "空")
            return False, self.err
        cmd = list(self.adb._base()) + [
            "exec-out", "screenrecord", "--output-format=h264",
            "--size", "%dx%d" % (w, h), "--bit-rate", str(LIVE_BITRATE),
            "--time-limit", str(LIVE_MAX_SEC), "-",
        ]
        try:
            self.p_adb = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                          stderr=subprocess.DEVNULL)
            # ⚠ 不要加 -probesize / -analyzeduration：实测会解出 0 帧（管道流下
            #   分析阶段拿不到足够数据就放弃），保持默认反而稳定（本机实测 26fps）。
            self.p_ff = subprocess.Popen(
                [ff, "-hide_banner", "-loglevel", "error",
                 "-f", "h264", "-i", "pipe:0", "-f", "rawvideo",
                 "-pix_fmt", "bgr24", "pipe:1"],
                stdin=self.p_adb.stdout, stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL)
            self.p_adb.stdout.close()   # 让 adb 端断开时 ffmpeg 能收到 EOF
        except Exception as e:
            self.err = "启动实时流失败：%s: %s" % (type(e).__name__, e)
            return False, self.err
        self.w, self.h = w, h
        self.frame_scale = float(h) / float(LIVE_SMALL_H) if h else 1.0
        self.stop_flag = False
        self.seq = 0
        self._t0 = time.time()
        self._buf = []
        self._last = None
        self.th = threading.Thread(target=self._reader, daemon=True)
        self.th.start()
        return True, ""

    def _reader(self):
        import numpy as np
        n = self.w * self.h * 3
        src = self.p_ff.stdout
        while not self.stop_flag:
            buf = b""
            while len(buf) < n:
                try:
                    chunk = src.read(n - len(buf))
                except Exception:
                    chunk = b""
                if not chunk:
                    break
                buf += chunk
            if len(buf) < n:
                break
            try:
                arr = np.frombuffer(buf, dtype=np.uint8).reshape(self.h, self.w, 3)
                # BGR24 → RGB；frombuffer 是只读视图，必须 ascontiguousarray 才能给 PIL
                img = Image.fromarray(np.ascontiguousarray(arr[:, :, ::-1]), "RGB")
                g = img.convert("L")
                gw, gh = g.size
                nh = LIVE_SMALL_H if gh > LIVE_SMALL_H else gh
                nw = max(1, int(round(gw * nh / float(gh))))
                small = g if (nw, nh) == (gw, gh) else g.resize((nw, nh), Image.BILINEAR)
                with self._lock:
                    self.seq += 1
                    self._last = img
                    self._buf.append((self.seq, small))
                    if len(self._buf) > LIVE_BUFFER_MAX:
                        del self._buf[:len(self._buf) - LIVE_BUFFER_MAX]
            except Exception as e:
                self.err = "解码帧失败：%s: %s" % (type(e).__name__, e)
                break

    def latest(self):
        with self._lock:
            return self._last

    def last_small(self):
        """返回 (seq, 最新测量帧|None)：实时读数用，避免每帧拷整个缓冲。"""
        with self._lock:
            return (self.seq, self._buf[-1][1]) if self._buf else (0, None)

    def burst(self):
        """环形缓冲里的全部测量帧（按时间正序），供 measure_scroll_total 积分。"""
        with self._lock:
            return [im for _, im in self._buf]

    def fps(self):
        el = time.time() - self._t0 if self._t0 else 0.0
        return (self.seq / el) if el > 0.5 else 0.0

    def stop(self):
        self.stop_flag = True
        for p in (self.p_ff, self.p_adb):
            try:
                if p is not None and p.poll() is None:
                    p.terminate()
            except Exception:
                pass
        if self.th is not None:
            self.th.join(timeout=3)
        # 兜底：本地进程被杀后，设备上的 screenrecord 偶尔还活着（会一直占 CPU 编码）。
        # 这里只做一次 best-effort 清理，失败不影响任何功能。
        try:
            subprocess.run(self.adb._base() + ["shell", "pkill", "-f", "screenrecord"],
                           timeout=5, capture_output=True)
        except Exception:
            pass


def measure_scroll_fast(prev, cur, max_s=150, col_step=3, top_ratio=LIST_TOP_RATIO,
                        direction=1):
    """连续帧之间的**快速**位移估计（实时刷新用，不是 measure_scroll 的替代品）。

    监视窗口要按 ~14fps 刷新累计位移，measure_scroll 的逐块投票是百毫秒级，太慢；
    这里改成整块 SAD：列方向每 3 列取 1、行方向只取两帧在最大位移下都存在的区间。
    精度低于逐块投票，但**相邻帧只走几 px ~ 几十 px**，不存在周期别名的风险。
    direction=-1 时内容向下移，返回**负值**（回滚读数用，监视窗口目前固定传 1）。

    返回 (位移px|None, 置信度 0~1)。None = 这一段不可信（换页 / 切界面 / 黑帧）。
    """
    try:
        import numpy as np
    except Exception:
        return None, 0.0
    try:
        a = np.asarray(prev if prev.mode == "L" else prev.convert("L"), dtype=np.float32)
        b = np.asarray(cur if cur.mode == "L" else cur.convert("L"), dtype=np.float32)
    except Exception:
        return None, 0.0
    if a.shape != b.shape or a.shape[0] < 60:
        return None, 0.0
    H = a.shape[0]
    y0 = int(H * top_ratio)
    top = y0 + max_s
    if top >= H - 20:                      # 图太矮：缩小区间，别让比对区空掉
        top = max(y0 + 8, int(H * 0.55))
    max_s = min(max_s, top - y0)
    A = a[top:H, ::col_step]
    if A.shape[0] < 20:
        return None, 0.0
    A = A - float(A.mean())                # 去亮度基线：录制期间亮度变化不该算进失配
    best_s, best_d = 0, None
    ds = []
    for s in range(0, max_s + 1):
        if direction < 0:
            if top + s + 1 >= H:           # 回滚：内容下移，比对区随 s 缩短
                break
            aa = A[:A.shape[0] - s]
            bs = b[top + s:H, ::col_step]
        else:
            aa = A
            bs = b[top - s:H - s, ::col_step]
        d = float(np.abs(aa - (bs - float(bs.mean()))).mean())
        ds.append(d)
        if best_d is None or d < best_d:
            best_d, best_s = d, s
    if not ds:
        return None, 0.0
    avg = sum(ds) / float(len(ds))
    conf = 1.0 - (best_d / avg) if avg > 1e-6 else 0.0
    if conf < 0.15:      # 最佳位置和「随便一个位置」差不多 → 这段不可信，别累加
        return None, conf
    return (-1 if direction < 0 else 1) * int(best_s), conf


def measure_scroll_total(frames, max_shift_ratio=0.45, direction=1):
    """沿帧链把一次滑动的滚动位移**逐段积分**（连续帧专用）。

    两帧比对的老办法在位移大时必然失败（重叠区太小）；连续帧下每段只有几十 px，
    每段都匹配得上，加起来就是这次滑动的**完整真实位移** —— 惯性衰减快慢、
    什么时候停，都不再影响结果。步长自适应：一段太大（快速甩动）就自动跳帧比对。
    direction=-1（回滚）时返回**负值**（每段 measure_scroll 返回负位移，求和保持符号）。

    返回 (总位移px|None, 明细dict)。位移单位是**输入帧的像素**，
    换算回原图还要再乘 `LiveScreen.frame_scale`。
    """
    n = len(frames)
    info = {"n": n, "links": 0, "bad": 0, "steps": [], "max_step": 0}
    if n < 2:
        return None, info
    steps, bad, i = [], 0, 0
    while i < n - 1:
        hit = False
        for st in LIVE_STEPS:
            j = i + st
            if j >= n:
                break
            s, _why = measure_scroll(frames[i], frames[j],
                                     max_shift_ratio=max_shift_ratio, direction=direction)
            if s is not None:
                steps.append(s)
                i = j
                hit = True
                break
        if not hit:
            bad += 1
            i += 1
    info["steps"] = steps
    info["links"] = len(steps)
    info["bad"] = bad
    info["max_step"] = max((abs(x) for x in steps), default=0)
    if not steps:
        return None, info
    return int(sum(steps)), info


def diagnose_adb_error(err_text):
    """把 adb 的原始报错压成一句人话 + 可执行对策。返回 (分类, 说明)。"""
    t = err_text or ""
    if ADB_INJECT_DENIED in t:
        return "inject_denied", (
            "手机拒绝了 adb 的输入注入（SecurityException：需要 INJECT_EVENTS 权限）。\n"
            "这不是工具的问题，是 ROM 的安全限制。按顺序试：\n  " + "\n  ".join(ADB_INJECT_FIXES))
    if "unauthorized" in t:
        return "unauthorized", "设备未授权：拔插数据线，在手机上点「允许 USB 调试」并勾选记住。"
    # 真机 adb 的三种离线文案都要覆盖（2026-09-20 自检 E 段实测漏判）：
    #   error: device 'abc' not found / error: no devices/emulators found / error: device offline
    if ("not found" in t) or ("no devices" in t) or ("offline" in t):
        return "offline", "设备未连接/离线：换 USB 口或数据线，先在工具里点「刷新设备」。"
    first = (t.strip().splitlines() or ["adb 未返回错误详情"])[0]
    return "other", first


# ---------------------------------------------------------------- ADB 封装
class Adb:
    def __init__(self, path=""):
        self.path = path or ""
        self.serial = ""

    def _base(self):
        cmd = [self.path]
        if self.serial:
            cmd += ["-s", self.serial]
        return cmd

    def run(self, args, timeout=15):
        if not self.path or not os.path.exists(self.path):
            return 1, "", "adb 路径无效：%s" % self.path
        try:
            p = subprocess.run(self._base() + args, capture_output=True, timeout=timeout)
            out = p.stdout.decode("utf-8", "ignore")
            err = p.stderr.decode("utf-8", "ignore")
            return p.returncode, out, err
        except Exception as e:
            return 1, "", "%s: %s" % (type(e).__name__, e)

    def devices(self):
        rc, out, err = self.run(["devices"])
        devs = []
        for line in out.splitlines()[1:]:
            line = line.strip()
            if not line or line.startswith("*"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                devs.append((parts[0], parts[1]))
        return devs, err

    def screencap(self):
        """返回 (PIL.Image|None, 错误信息)"""
        if not self.path or not os.path.exists(self.path):
            return None, "adb 路径无效"
        try:
            p = subprocess.run(self._base() + ["exec-out", "screencap", "-p"],
                               capture_output=True, timeout=20)
            data = p.stdout
            if not data or len(data) < 1000:
                return None, "截屏数据为空（%d 字节）%s" % (len(data), p.stderr.decode("utf-8", "ignore")[:120])
            import io
            img = Image.open(io.BytesIO(data))
            img.load()
            return img.convert("RGB"), ""
        except Exception as e:
            return None, "%s: %s" % (type(e).__name__, e)

    def screen_size(self):
        """取设备屏幕分辨率，返回 ((w,h)|None, 错误)。有 Override 时优先用 Override。

        ⚠ **不反映屏幕旋转**：手机横屏时 `wm size` 仍可能报竖屏值（2026-09-20 实测：
        `wm size` = 1080x2400，而 `screencap` 出来的帧是 **2400x1080**）。
        **凡是算滑动坐标的地方，必须用截屏的实际尺寸，不要用本函数的结果** ——
        否则 y 坐标会超出真实屏高，adb 不报错、滑动静默失效。
        """
        rc, out, err = self.run(["shell", "wm", "size"])
        if rc != 0:
            return None, diagnose_adb_error(err)[1]
        hits = re.findall(r"(\d+)x(\d+)", out or "")
        if not hits:
            return None, "无法解析 `wm size` 输出：%s" % (out or "").strip()
        w, h = hits[-1]          # 同时存在 Physical/Override 时，最后一个才是当前生效的
        return (int(w), int(h)), ""

    def screen_awake(self):
        """读 `dumpsys power` 的 mWakefulness，判断屏幕是否点亮。
        返回 (True/False/None, 原始值)：None = 读不出来（不猜）。
        用途：区分黑屏到底是「屏幕熄了」还是「界面禁截屏」，两者对策完全不同。"""
        rc, out, err = self.run(["shell", "dumpsys", "power"])
        if rc != 0 or not out:
            return None, diagnose_adb_error(err)[1]
        m = re.search(r"mWakefulness=(\w+)", out)
        if not m:
            return None, "dumpsys power 未见 mWakefulness"
        state = m.group(1)
        return (state == "Awake"), state

    def swipe_up(self, w, h, percent=SWIPE_PCT_DEFAULT, duration=SWIPE_MS_DEFAULT, display=None):
        """模拟上滑（用户手势层面的 input 注入，非进程注入）。

        **w/h 必须传「截屏的实际尺寸」**，不能传 `wm size` 的结果：`wm size` 不反映旋转，
        横屏下会给出竖屏尺寸，算出的 y 坐标超出真实屏高 —— adb 不报错、滑动静默失效
        （2026-09-20 实测：`wm size`=1080x2400 而帧是 2400x1080，y1=1872 越界，页面纹丝不动，
        而采样流程用的是帧尺寸所以正常 —— 表现为「采样滑动正常、测试滑动有问题」）。
        返回 (ok, 分类, 说明)：失败时说明已翻译成「哪个 ROM 开关没开」级别的对策。
        """
        if not w or not h:
            return False, "other", "拿不到屏幕尺寸，无法构造滑动坐标"
        args = swipe_args(w, h, percent=percent, duration=duration, display=display)
        ys = [int(args[args.index("swipe") + 2]), int(args[args.index("swipe") + 4])]
        if any(y < 0 or y >= h for y in ys):
            return False, "other", ("滑动坐标 %s 超出传入的屏幕高度 %d，滑动不会生效（多半是尺寸取错了）"
                                    % (ys, h))
        rc, out, err = self.run(args)
        if rc == 0:
            return True, "", ""
        kind, msg = diagnose_adb_error(err or out)
        return False, kind, msg

    def swipe_down(self, w, h, percent=SWIPE_PCT_DEFAULT, duration=SWIPE_MS_DEFAULT, display=None):
        """模拟下滑（列表回滚），坐标安全检查与 swipe_up 完全一致。

        实现：直接把 swipe_args 的起止 y 对调 —— 同一段轨迹反向走，注入通道不变。
        用途（2026-09-21）：对齐红线时若顶行刚越过行界，向前补滚会「追着行界跑」
        死循环，改为反向滚回当前行（见 align_to_grid 的行界悬崖注释）。
        """
        if not w or not h:
            return False, "other", "拿不到屏幕尺寸，无法构造滑动坐标"
        args = swipe_args(w, h, percent=percent, duration=duration, display=display)
        i = args.index("swipe")
        args[i + 2], args[i + 4] = args[i + 4], args[i + 2]   # 起止 y 对调 → 下滑
        ys = [int(args[i + 2]), int(args[i + 4])]
        if any(y < 0 or y >= h for y in ys):
            return False, "other", ("滑动坐标 %s 超出传入的屏幕高度 %d，滑动不会生效（多半是尺寸取错了）"
                                    % (ys, h))
        rc, out, err = self.run(args)
        if rc == 0:
            return True, "", ""
        kind, msg = diagnose_adb_error(err or out)
        return False, kind, msg


def is_blank(img):
    """判断截屏是否全黑/纯色。纯色有两种成因，对策完全不同，别混为一谈：
      ① 屏幕熄灭 / 锁屏 → 点亮并解锁后重截即可（最常见）；
      ② 界面设了 FLAG_SECURE → 截屏必黑，只能改用拍照导入。
    只判断「是不是纯色」，成因交给 explain_blank() 结合 mWakefulness 区分。"""
    g = img.convert("L")
    lo, hi = g.getextrema()
    return (hi - lo) < 8


def explain_blank(adb):
    """纯色截屏的成因判定 + 对症对策。返回一句可直接给用户看的中文说明。"""
    awake, state = adb.screen_awake()
    if awake is False:
        # 2026-09-20 真机实测：手机 Dozing（熄屏/锁屏）时 screencap 成功但整幅纯色，
        # 此时旧文案会误导用户去「拍照导入」，而正确做法是点亮屏幕。
        return ("截屏为纯色，且手机屏幕当前未点亮（mWakefulness=%s）——"
                "先点亮屏幕并解锁，再重新截屏。" % state)
    if awake is None:
        return ("截屏为纯色，屏幕状态读不出来（%s）。"
                "请先确认屏幕已点亮解锁；若仍然全黑，才是界面禁截屏，改用「导入图片」。" % state)
    return ("截屏为纯色，而屏幕已点亮（mWakefulness=%s）——"
            "该界面很可能禁止截屏（FLAG_SECURE），请改用另一台设备拍照后「导入图片」。" % state)


class LiveMonitor:
    """实时监视窗口：连续显示手机屏幕，并**实时读出累计滚动位移**。

    这是「滑得到底准不准」的观测工具：肉眼能看到列表实际滚了多少、什么时候停，
    配合累计位移读数，调「上滑幅度」就有依据了 —— 不用再靠「感觉滑过头了」。
    """

    REFRESH_MS = 70     # 显示刷新间隔（≈14fps；再快 Tkinter 主线程会被拖住）

    def __init__(self, master, app):
        self.app = app
        self.adb = app.adb
        self.live = LiveScreen(self.adb)
        self.running = False
        self.acc = 0              # 累计滚动（测量帧像素，显示时再换算回原图）
        self.prev_seq = 0
        self.prev_small = None
        self.tk_img = None

        top = tk.Toplevel(master)
        self.top = top
        top.title("实时屏幕监视（screenrecord 连续流）")
        top.geometry("720x700")
        top.minsize(420, 420)
        bar = ttk.Frame(top, padding=5)
        bar.pack(fill=tk.X)
        self.btn_start = ttk.Button(bar, text="开始", command=self.start)
        self.btn_start.pack(side=tk.LEFT)
        self.btn_stop = ttk.Button(bar, text="停止", command=self.stop, state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=4)
        ttk.Button(bar, text="清零累计", command=self.zero).pack(side=tk.LEFT, padx=4)
        ttk.Button(bar, text="抓到主画布", command=self.grab).pack(side=tk.LEFT, padx=4)
        self.var = tk.StringVar(value="未开始")
        ttk.Label(bar, textvariable=self.var).pack(side=tk.LEFT, padx=8)

        self.canvas = tk.Canvas(top, bg="#101010", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Label(top, text=("连续流 ≈26fps（screencap 只有 0.5fps）。「累计滚动」是从开始/清零起"
                             "列表实际滚过的像素：停稳后数字不再跳动，调「上滑幅度」就看它。"
                             "窗口开着时手机会持续编码投屏，不用就点「停止」。"),
                  wraplength=690, justify=tk.LEFT).pack(fill=tk.X, padx=6, pady=(0, 6))
        top.protocol("WM_DELETE_WINDOW", self.close)
        top.after(200, self.start)

    # ------------------------------------------------------------ 起停
    def start(self):
        if self.running:
            return
        self.adb.path = self.app.adb_path_var.get()
        # 主画布已经有帧就直接拿来取尺寸：省掉一次 ≈2s 的 screencap，
        # 首帧延迟从实测 4.7s 降到 ≈2.5s（首次出画面慢是「起流 + ffmpeg 缓冲」，不是卡死）
        before = getattr(self.app, "img", None)
        if before is None:
            before, err = self.adb.screencap()
            if before is None:
                self.var.set("截屏失败：%s" % err)
                return
        ok, err = self.live.start(before.size)
        if not ok:
            self.var.set("起流失败")
            self.app.log("实时监视：%s" % err)
            return
        self.running = True
        self.acc = 0
        self.prev_seq = 0
        self.prev_small = None
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)
        self.var.set("正在启动录制，首次出画面约 2~5 秒…")
        self.top.after(self.REFRESH_MS, self.tick)

    def tick(self):
        if not self.running:
            return
        img = self.live.latest()
        if img is not None:
            self._draw(img)
        seq, small = self.live.last_small()
        if small is not None and seq != self.prev_seq:
            if self.prev_small is not None:
                s, _conf = measure_scroll_fast(self.prev_small, small)
                if s is not None:
                    self.acc += s          # 逐帧累加：换页/黑帧那段返回 None，不计入
            self.prev_small = small
            self.prev_seq = seq
        if seq == 0:
            self.var.set("正在启动录制，首次出画面约 2~5 秒…")
        else:
            self.var.set("帧 %d｜%.0f fps｜累计滚动 %dpx"
                         % (seq, self.live.fps(), int(self.acc * self.live.frame_scale)))
        self.top.after(self.REFRESH_MS, self.tick)

    def _draw(self, img):
        cw = max(1, self.canvas.winfo_width())
        ch = max(1, self.canvas.winfo_height())
        w, h = img.size
        k = min(cw / float(w), ch / float(h))
        nw, nh = max(1, int(w * k)), max(1, int(h * k))
        self.tk_img = ImageTk.PhotoImage(img.resize((nw, nh), Image.BILINEAR))
        self.canvas.delete("all")
        self.canvas.create_image(cw // 2, ch // 2, image=self.tk_img)

    def zero(self):
        self.acc = 0
        self.var.set("累计已清零")

    def grab(self):
        img = self.live.latest()
        if img is None:
            self.app.log("实时监视：还没有帧可抓（流没起来？）")
            return
        self.app.img = img
        self.app.update_canvas()
        self.app.log("已从实时流抓一帧到主画布（%dx%d）" % img.size)

    def stop(self):
        self.running = False
        self.live.stop()
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.var.set("已停止")

    def close(self):
        self.stop()
        self.top.destroy()


# ---------------------------------------------------------------- 主界面
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("绿洲启元 地图数据采样器 · ADB + OCR")
        # 窗口尺寸自适应屏幕（2026-09-20：固定 1180x760 在小屏/笔记本上会超出屏幕，
        # 底部按钮被裁掉点不到）。按屏幕可用区取 min(1180, 92%宽) × min(760, 88%高)，
        # 超出的内容交给右栏滚动条 + 可拖拽分栏（见 build_ui）。
        sw = max(400, self.root.winfo_screenwidth())
        sh = max(300, self.root.winfo_screenheight())
        self.root.geometry("%dx%d" % (min(1180, int(sw * 0.92)), min(760, int(sh * 0.88))))
        self.root.minsize(640, 420)

        self.cfg = self.load_cfg()
        self.adb = Adb(self.cfg.get("adb_path", ""))
        self.ocr = OcrEngine()
        self.msgq = queue.Queue()

        self.img = None            # 当前 PIL 原图
        self.tk_img = None
        self.scale = 1.0           # 画布缩放比
        self.rects = {}            # 字段 -> (x0,y0,x1,y1)，基于原图坐标
        # 大厅网格模式下的「框选覆盖」：字段 -> 相对卡片左上角的 *视图* 坐标偏移。
        # 用户在大厅网格模式直接拖框时写这里，并优先于 LOBBY 的固定几何 ——
        # 否则用户拖了框既不生效也不报错（旧版就是这个静默行为）。
        self.field_override = {}
        self.cur_field = tk.StringVar(value=FIELDS[0])
        self.drawing = None
        self.records = {}          # 去重表：key -> record
        self.sampling = False
        self._last_sig = None      # 末页检测用的上一帧签名
        self._geom_upgraded = None  # 几何版本升级提示（非空时在日志里说明）
        # 闭环滚动的「增益」：实际滚动 / 手指位移。0 = 还没标定过。
        # 每次量出位移就更新它，下一次上滑直接用 target/gain 反推手指位移 —— 这是
        # 不用 root / sendevent 也能把误差收敛掉的唯一办法（见 precise_scroll）。
        self.swipe_gain = float(self.cfg.get("swipe_gain", 0.0) or 0.0)
        self.live_win = None       # 实时监视窗口（打开时才有值）

        # 几何版本守卫：早期版本把第一行卡片顶误标为 y=103、行距误标为 231，
        # 那批存档的 rects/row_step/card_h 已是错的。几何版本不一致时丢弃旧缓存，
        # 强制回到按真机截图标定的默认值，避免旧配置静默复活错误几何。
        saved_geom_ver = int(self.cfg.get("geom_version", 0))
        if saved_geom_ver != GEOM_VERSION:
            # 网格语义变过，这些键在旧存档里含义已不同，必须一起丢弃：
            #   rects   —— 旧版在大厅模式下拖的框其实一直不生效，留着只会误导
            #   ncol    —— 旧版从「大厅专有」改成「两模式共用」，曾被设成 2 导致只认两列
            #   card_*  —— 旧版是「卡片数/卡片步长（一列向下复制）」，现在是「行数/行距」
            for k in ("rects", "row_step", "card_h", "ncol",
                      "card_count", "card_step", "col_step"):
                self.cfg.pop(k, None)
            if saved_geom_ver:
                self._geom_upgraded = "%d -> %d" % (saved_geom_ver, GEOM_VERSION)
        self.cfg["geom_version"] = GEOM_VERSION
        for f in FIELDS:
            r = self.cfg.get("rects", {}).get(f)
            if r and len(r) == 4:
                self.rects[f] = tuple(r)

        # 大厅模式下按图预置字段框（配置里有自选坐标则以配置为准）。
        # 必须在 build_ui() 之前赋值 —— build_ui 末尾会 refresh_rect_tree() 把 self.rects 渲染出来；
        # 但 layout_mode_var 是 build_ui 里创建的，所以先按「配置优先」判一次，
        # build_ui 之后再按控件值兜底。
        cfg_mode = str(self.cfg.get("layout_mode", "lobby"))
        if cfg_mode == "lobby" and not self.rects:
            self.rects = {f: tuple(b) for f, b in LOBBY["fields"].items()}

        self.build_ui()
        # ⚠ layout_mode_var 等控件变量是在 build_ui 里创建的，提前访问会抛 AttributeError
        #   让程序直接起不来（2026-09-18 实测踩到）。这里只做兜底补一次。
        if self.layout_mode_var.get() == "lobby" and not self.rects:
            self.rects = {f: tuple(b) for f, b in LOBBY["fields"].items()}
            self.refresh_rect_tree()

        self.root.after(100, self.pump)
        threading.Thread(target=self.init_ocr, daemon=True).start()
        if self._geom_upgraded:
            self.log("布局几何已升级（v%s）：本页网格为 %d 行 × %d 列，旧坐标存档已丢弃并回到按图实测默认值"
                     % (self._geom_upgraded, INT_ROW_COUNT, len(LOBBY["col_x"])))

    # ------------------------------------------------------------ 配置
    def load_cfg(self):
        if os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def save_cfg(self):
        self.cfg["adb_path"] = self.adb_path_var.get()
        self.cfg["rects"] = {k: list(v) for k, v in self.rects.items()}
        self.cfg["card_count"] = self.card_count_var.get()
        self.cfg["card_step"] = self.card_step_var.get()
        self.cfg["col_step"] = self.col_step_var.get()
        self.cfg["ocr_scale"] = self.scale_var.get()
        self.cfg["layout_mode"] = self.layout_mode_var.get()
        self.cfg["ncol"] = self.ncol_var.get()
        self.cfg["row_step"] = self.row_step_var.get()
        self.cfg["card_h"] = self.card_h_var.get()
        # 上滑幅度/时长：用户按自己手机调过之后要能留下来（滑过头就靠这俩微调）
        self.cfg["swipe_pct"] = float(self.swipe_pct_var.get())
        self.cfg["swipe_ms"] = int(self.swipe_ms_var.get())
        self.cfg["swipe_runs"] = int(self.runs_var.get())
        self.cfg["precise_scroll"] = bool(self.precise_var.get())
        self.cfg["live_measure"] = bool(self.live_measure_var.get())
        self.cfg["align_grid"] = bool(self.align_var.get())
        # 增益只记在内存里不落盘：它是「本次运行实测出来的」，换页面/换机型就失效，
        # 写进配置反而会让下次启动用一个过期的系数去反推手指位移。
        self.cfg.pop("swipe_gain", None)
        try:
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(self.cfg, f, ensure_ascii=False, indent=2)
            self.log("配置已保存（本次未保存大厅模式的框选覆盖，覆盖值只在本次运行有效）")
        except Exception as e:
            self.log("配置保存失败：%s" % e)

    # ------------------------------------------------------------ 布局模式
    def on_layout_mode(self):
        """切换布局模式：大厅网格用按图标定的固定几何，自选框选把一张卡的框复制成整页网格"""
        mode = self.layout_mode_var.get()
        if mode == "lobby":
            self.rects = {f: tuple(b) for f, b in LOBBY["fields"].items()}
            tag = "已切换到「大厅网格」模式：整页按 3 列 × N 行识别，字段框取自几何表，一般无需手改"
        else:
            tag = ("已切换到「自选框选」模式：在第一张卡上拖框，再按 行数×列数"
                   "（%s×%s）复制到整页" % (self.card_count_var.get(), self.ncol_var.get()))
        self.refresh_rect_tree()
        self.update_canvas()
        self.log(tag)
        self.status_var.set(tag)

    def reset_layout(self):
        """把卡片网格与字段框恢复为按图实测的默认值，并清掉大厅模式的框选覆盖"""
        self.ncol_var.set(len(LOBBY["col_x"]))          # 3 列
        self.col_step_var.set(INT_COL_STEP)             # 真机列距 495
        self.card_count_var.set(INT_ROW_COUNT)          # 2 行
        self.card_step_var.set(INT_ROW_STEP)            # 真机行距 314
        self.row_step_var.set(LOBBY["row_step"])
        self.card_h_var.set(LOBBY["card_h"])
        self.rects = {f: tuple(b) for f, b in LOBBY["fields"].items()}
        self.field_override.clear()
        self.layout_mode_var.set("lobby")
        self.refresh_rect_tree()
        self.update_canvas()
        self.log("布局已按真机截图重置：%d 列 × %d 行，列距=%d 行距=%d(真机 px)，"
                 "行距=%d 卡高=%d（视觉 %dx%d 基准），框选覆盖已清空"
                 % (len(LOBBY["col_x"]), INT_ROW_COUNT, INT_COL_STEP, INT_ROW_STEP,
                    LOBBY["row_step"], LOBBY["card_h"], VIEW_W, VIEW_H))
        self.status_var.set("布局已重置")

    def cur_geom(self):
        """汇总当前生效的几何参数，并把用户可调项（列数/行距/卡高）覆盖进 LOBBY"""
        geom = dict(LOBBY)
        try:
            n = max(1, min(int(self.ncol_var.get()), len(LOBBY["col_x"])))
        except Exception:
            n = len(LOBBY["col_x"])
        geom["col_x"] = LOBBY["col_x"][:n]
        try:
            geom["row_step"] = max(10, int(self.row_step_var.get()))
            geom["card_h"] = max(10, int(self.card_h_var.get()))
        except Exception:
            pass
        return geom

    # ------------------------------------------------------------ UI
    def build_ui(self):
        top = ttk.Frame(self.root, padding=6)
        top.pack(side=tk.TOP, fill=tk.X)

        # 第一行：adb 与设备
        ttk.Label(top, text="adb 路径").grid(row=0, column=0, sticky="w")
        self.adb_path_var = tk.StringVar(value=self.cfg.get("adb_path", ""))
        ttk.Entry(top, textvariable=self.adb_path_var, width=52).grid(row=0, column=1, sticky="w")
        ttk.Button(top, text="浏览…", command=self.pick_adb).grid(row=0, column=2, padx=3)
        ttk.Button(top, text="刷新设备", command=self.refresh_devices).grid(row=0, column=3, padx=3)
        ttk.Label(top, text="设备").grid(row=0, column=4, padx=(12, 2))
        self.dev_var = tk.StringVar(value="")
        self.dev_box = ttk.Combobox(top, textvariable=self.dev_var, width=26, state="readonly")
        self.dev_box.grid(row=0, column=5, sticky="w")
        self.dev_box.bind("<<ComboboxSelected>>", self.on_dev_change)

        # 第二行：截图来源与操作
        ttk.Button(top, text="ADB 截屏", command=self.shot_from_adb).grid(row=1, column=0, pady=6, sticky="w")
        ttk.Button(top, text="导入图片…", command=self.load_image).grid(row=1, column=1, sticky="w")
        ttk.Button(top, text="导入文件夹…", command=self.load_folder).grid(row=1, column=2, sticky="w")
        ttk.Button(top, text="粘贴剪贴板", command=self.paste_clipboard).grid(row=1, column=3, sticky="w")
        ttk.Button(top, text="识别当前帧", command=lambda: self.recognize_current(save=True)).grid(row=1, column=4, sticky="w")

        # 第三行：卡片网格参数。绿洲大厅列表页实测一页 = 2 行 × 3 列 = 6 张卡。
        #   「列数」两种模式通用：大厅网格用它截取列边界，自选框选用它横向复制框；
        #   「行数 / 行距(px) / 列距(px)」是自选框选模式用的真机像素步长
        #   （默认值直接取真机实测：行距 314、列距 495）。
        pf = ttk.Frame(top)
        pf.grid(row=2, column=0, columnspan=6, sticky="w", pady=3)
        ttk.Label(pf, text="行数").pack(side=tk.LEFT)
        self.card_count_var = tk.IntVar(value=int(self.cfg.get("card_count", 2)))
        ttk.Spinbox(pf, from_=1, to=30, width=4, textvariable=self.card_count_var).pack(side=tk.LEFT, padx=(2, 8))
        ttk.Label(pf, text="行距(px)").pack(side=tk.LEFT)
        self.card_step_var = tk.IntVar(value=int(self.cfg.get("card_step", 314)))
        ttk.Spinbox(pf, from_=10, to=4000, width=6, textvariable=self.card_step_var).pack(side=tk.LEFT, padx=(2, 8))
        ttk.Label(pf, text="列数").pack(side=tk.LEFT)
        self.ncol_var = tk.IntVar(value=int(self.cfg.get("ncol", 3)))
        ttk.Spinbox(pf, from_=1, to=6, width=3, textvariable=self.ncol_var).pack(side=tk.LEFT, padx=(2, 8))
        ttk.Label(pf, text="列距(px)").pack(side=tk.LEFT)
        self.col_step_var = tk.IntVar(value=int(self.cfg.get("col_step", 495)))
        ttk.Spinbox(pf, from_=10, to=4000, width=6, textvariable=self.col_step_var).pack(side=tk.LEFT, padx=(2, 10))
        ttk.Label(pf, text="OCR 放大").pack(side=tk.LEFT)
        # 默认放大 4 倍：实测顶部 热度 那行字在 2x 下会把单位「万」丢掉（'111万' -> '111'，值差 1e4）
        self.scale_var = tk.IntVar(value=int(self.cfg.get("ocr_scale", 4)))
        ttk.Spinbox(pf, from_=1, to=8, width=4, textvariable=self.scale_var).pack(side=tk.LEFT, padx=(2, 10))
        ttk.Button(pf, text="保存配置", command=self.save_cfg).pack(side=tk.LEFT)

        # 第四行：大厅布局（按真机截图标定的固定几何）
        lf = ttk.Frame(top)
        lf.grid(row=3, column=0, columnspan=6, sticky="w", pady=3)
        self.layout_mode_var = tk.StringVar(value=self.cfg.get("layout_mode", "lobby"))
        ttk.Radiobutton(lf, text="大厅网格（按图固定布局）", value="lobby",
                        variable=self.layout_mode_var,
                        command=self.on_layout_mode).pack(side=tk.LEFT)
        ttk.Radiobutton(lf, text="自选框选（旧模式）", value="manual",
                        variable=self.layout_mode_var,
                        command=self.on_layout_mode).pack(side=tk.LEFT, padx=(8, 12))
        # 「列数」不在这里，已挪到上面的参数行（两种模式共用同一个列数）
        ttk.Label(lf, text="行距(view)").pack(side=tk.LEFT)
        self.row_step_var = tk.IntVar(value=int(self.cfg.get("row_step", LOBBY["row_step"])))
        ttk.Spinbox(lf, from_=10, to=1000, width=5, textvariable=self.row_step_var).pack(side=tk.LEFT, padx=(2, 10))
        ttk.Label(lf, text="卡高(view)").pack(side=tk.LEFT)
        self.card_h_var = tk.IntVar(value=int(self.cfg.get("card_h", LOBBY["card_h"])))
        ttk.Spinbox(lf, from_=10, to=1000, width=5, textvariable=self.card_h_var).pack(side=tk.LEFT, padx=(2, 10))
        ttk.Button(lf, text="按图重置布局", command=self.reset_layout).pack(side=tk.LEFT, padx=(6, 0))

        # 外层**纵向**分栏：拖它与日志区之间的分隔条即可改日志区高度
        # （日志原来固定 130px，识别一帧打十几行时看不到开头）。
        vpan = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        vpan.pack(fill=tk.BOTH, expand=True, padx=6, pady=4)

        # 内层**横向**分栏：左画布 + 右侧，拖中间分隔条改左右区域宽度
        # （2026-09-20：用户要求「区域大小可调整」；右栏内容超出时走滚动条，见下方滚动容器）。
        body = ttk.PanedWindow(vpan, orient=tk.HORIZONTAL)
        vpan.add(body, weight=1)
        self.vpan = vpan        # 留引用：自检要断言分栏结构（区域可调大小是否真的建起来了）
        self.body = body

        left = ttk.Frame(body)
        self.canvas = tk.Canvas(left, bg="#2b2b2b", highlightthickness=1, highlightbackground="#888")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        # 窗口尺寸变化后按新画布尺寸重算缩放并重绘（首帧 winfo_width 为 1，靠它纠正）
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # —— 右栏：Canvas 滚动容器（2026-09-20：右栏内容在小屏/横屏下超出屏幕，
        #    底部按钮点不到。加上下滚动条 + 鼠标滚轮；横向溢出也有水平滚动条兜底）——
        right = ttk.Frame(body, width=430)
        body.add(left, weight=1)
        body.add(right, weight=0)
        right.pack_propagate(False)

        rcanvas = tk.Canvas(right, highlightthickness=0)
        rvsb = ttk.Scrollbar(right, orient=tk.VERTICAL, command=rcanvas.yview)
        rhsb = ttk.Scrollbar(right, orient=tk.HORIZONTAL, command=rcanvas.xview)
        rcanvas.configure(yscrollcommand=rvsb.set, xscrollcommand=rhsb.set)
        rvsb.pack(side=tk.RIGHT, fill=tk.Y)
        rhsb.pack(side=tk.BOTTOM, fill=tk.X)
        rcanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.rcanvas = rcanvas   # 留引用供自检断言
        holder = ttk.Frame(rcanvas)
        holder.bind("<Configure>",
                    lambda _e: rcanvas.configure(scrollregion=rcanvas.bbox("all")))
        _rwin = rcanvas.create_window((0, 0), window=holder, anchor="nw")

        # holder 宽度跟随画布宽（列宽自适应），横向只在真的放不下时才出滚动条
        def _on_rcanvas_cfg(e):
            rcanvas.itemconfigure(_rwin, width=e.width)
        rcanvas.bind("<Configure>", _on_rcanvas_cfg)

        # 滚轮滚动右栏；文本框/树/下拉这类自带滚动的控件放行，不抢它们的事件
        def _on_wheel(e):
            try:
                wdg = self.root.nametowidget(e.widget) if e.widget else None
            except Exception:
                wdg = None
            # 鼠标就在右栏空白处（滚动容器本身）时也必须能滚 —— 不加这条的话，
            # 右栏大部分面积属于 rcanvas，会被下面的 tk.Canvas 放行规则挡掉，
            # 表现就是「滚轮在右栏没反应」，只有指到按钮/标签上才滚。
            if wdg is rcanvas:
                rcanvas.yview_scroll(-1 if e.delta > 0 else 1, "units")
                return
            if isinstance(wdg, (tk.Text, tk.Canvas, ttk.Treeview, ttk.Combobox, tk.Listbox, ttk.Spinbox)):
                return
            rcanvas.yview_scroll(-1 if e.delta > 0 else 1, "units")
        self.root.bind_all("<MouseWheel>", _on_wheel)

        right = holder   # 下面所有右栏控件装进滚动容器

        # 区域定义
        box = ttk.LabelFrame(right, text="1. 字段区域（大厅模式下已按图预置）", padding=5)
        box.pack(fill=tk.X, pady=3)
        fr = ttk.Frame(box)
        fr.pack(fill=tk.X)
        for f in FIELDS:
            ttk.Radiobutton(fr, text=f, value=f, variable=self.cur_field).pack(side=tk.LEFT, padx=3)
        self.rect_tree = ttk.Treeview(box, columns=("field", "rect"), show="headings", height=7)
        self.rect_tree.heading("field", text="字段")
        self.rect_tree.heading("rect", text="坐标(x0,y0,x1,y1)")
        self.rect_tree.column("field", width=80)
        self.rect_tree.column("rect", width=200)
        self.rect_tree.pack(fill=tk.X, pady=3)
        btns = ttk.Frame(box)
        btns.pack(fill=tk.X)
        ttk.Button(btns, text="清空框选", command=self.clear_rects).pack(side=tk.LEFT, padx=2)
        ttk.Button(btns, text="试识别一张卡", command=self.test_one_card).pack(side=tk.LEFT, padx=2)
        ttk.Button(btns, text="整帧诊断", command=self.diagnose_frame).pack(side=tk.LEFT, padx=2)

        # 采样
        samp = ttk.LabelFrame(right, text="2. 连续采样", padding=5)
        samp.pack(fill=tk.X, pady=3)
        row = ttk.Frame(samp)
        row.pack(fill=tk.X)
        ttk.Label(row, text="间隔(s)").pack(side=tk.LEFT)
        self.interval_var = tk.DoubleVar(value=2.0)
        ttk.Spinbox(row, from_=0.5, to=60, increment=0.5, width=6, textvariable=self.interval_var).pack(side=tk.LEFT)
        ttk.Label(row, text="次数").pack(side=tk.LEFT, padx=(8, 0))
        self.times_var = tk.IntVar(value=10)
        ttk.Spinbox(row, from_=1, to=500, width=6, textvariable=self.times_var).pack(side=tk.LEFT)
        swrow = ttk.Frame(samp)
        swrow.pack(fill=tk.X)
        self.swipe_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(swrow, text="每次截屏后自动上滑（adb input swipe）",
                        variable=self.swipe_var).pack(side=tk.LEFT)
        # 一键自检：adb 的输入注入常被 ROM 挡掉（SecurityException: INJECT_EVENTS），
        # 先点这里判定，比跑到一半才发现失败好。
        # 2026-09-20 升级：不再只报「是否允许注入」，而是真滑一次并量出实际滚动像素
        # —— 只说「通过」的话，用户看不到滑了多少，也就没法据此调幅度。
        ttk.Button(swrow, text="测滑动（连测取中位数）", command=self.test_swipe).pack(side=tk.LEFT, padx=6)
        # 只测一次：连测要滑好几下，调参时想看单次实际效果就用它（2026-09-21 用户要求）
        ttk.Button(swrow, text="只测一次", command=self.test_swipe_once).pack(side=tk.LEFT)
        # 不用输入注入也能标定：量「人手滑一页」实际滚了多少，作为自动上滑的目标值
        ttk.Button(swrow, text="测手动滑动", command=self.measure_manual_swipe).pack(side=tk.LEFT)
        # 上滑幅度/时长必须可调（2026-09-20 真机反馈「滑过头了」）：
        # 大厅列表是连续滚动（底部还会露出半个第三行），一屏不是一个固定单位；
        # 默认 55% 幅度 + 350ms 属于「快速甩动」，惯性会带着列表继续滚，于是跨过一页多。
        # 调小幅度 + 拉长按下的时长 = 慢速拖动，惯性小，落点可控。
        swp = ttk.Frame(samp)
        swp.pack(fill=tk.X)
        ttk.Label(swp, text="上滑幅度(屏高比)").pack(side=tk.LEFT)
        self.swipe_pct_var = tk.DoubleVar(value=float(self.cfg.get("swipe_pct", SWIPE_PCT_DEFAULT)))
        ttk.Spinbox(swp, from_=0.10, to=0.80, increment=0.05, width=6,
                    textvariable=self.swipe_pct_var).pack(side=tk.LEFT)
        ttk.Label(swp, text="时长(ms)").pack(side=tk.LEFT, padx=(8, 0))
        self.swipe_ms_var = tk.IntVar(value=int(self.cfg.get("swipe_ms", SWIPE_MS_DEFAULT)))
        ttk.Spinbox(swp, from_=150, to=2000, increment=50, width=6,
                    textvariable=self.swipe_ms_var).pack(side=tk.LEFT)
        ttk.Label(swp, text="（滑过头就调小幅度、拉长时长）").pack(side=tk.LEFT, padx=(6, 0))
        # 连测次数（2026-09-21：用户反馈「每次距离都不一」——fling 落点本身是随机变量，
        # 单次值不能拿来调参，所以默认连测 3 次取中位数，并把波动幅度一起报出来）
        rrow = ttk.Frame(samp)
        rrow.pack(fill=tk.X)
        ttk.Label(rrow, text="连测次数").pack(side=tk.LEFT)
        self.runs_var = tk.IntVar(value=int(self.cfg.get("swipe_runs", SWIPE_RUNS_DEFAULT)))
        ttk.Spinbox(rrow, from_=1, to=5, width=4, textvariable=self.runs_var).pack(side=tk.LEFT, padx=(2, 8))
        ttk.Label(rrow, text="（惯性有波动，连测取中位数才可信；波动大就拉长时长）").pack(side=tk.LEFT)
        # 精确滚动（2026-09-21）：`input swipe` 是开环的，一次定生死必然不准。
        # 开环后量出实际滚动、按「实测增益」反推补第二次 —— 误差 1~2 轮收敛。
        self.precise_var = tk.BooleanVar(value=bool(self.cfg.get("precise_scroll", True)))
        ttk.Checkbutton(rrow, text="精确滚动（滑不准就自动补齐到一页）",
                        variable=self.precise_var).pack(side=tk.LEFT, padx=(10, 0))
        # 实时流（2026-09-21）：screencap 只有 ≈0.5fps，只能抓「滑前/滑后」两帧，
        # 位移一大就匹配不上；screenrecord 连续流 ≈26fps，位移沿帧链积分，量的是整段。
        lvrow = ttk.Frame(samp)
        lvrow.pack(fill=tk.X)
        ttk.Button(lvrow, text="实时监视…", command=self.open_live).pack(side=tk.LEFT)
        ttk.Button(lvrow, text="实时测滑动（录整段）",
                   command=self.live_measure_swipe).pack(side=tk.LEFT, padx=6)
        self.live_measure_var = tk.BooleanVar(value=bool(self.cfg.get("live_measure", True)))
        ttk.Checkbutton(lvrow, text="用实时流测位移",
                        variable=self.live_measure_var).pack(side=tk.LEFT)
        ttk.Label(lvrow, text="（≈26fps，位移沿帧链积分；需 ffmpeg）").pack(side=tk.LEFT, padx=(6, 0))
        # 顶行对齐红线（2026-09-21 用户要求）：滑完之后下一批 6 张的上排 3 张
        # 顶部要精准贴在红线（first_row_y）处 —— 只按「一页」闭环会累积 ±12% 误差，
        # 必须用行间亮缝做**绝对反馈**，差多少补多少。
        arow = ttk.Frame(samp)
        arow.pack(fill=tk.X)
        ttk.Button(arow, text="对齐到红线", command=self.align_once).pack(side=tk.LEFT)
        self.align_var = tk.BooleanVar(value=bool(self.cfg.get("align_grid", True)))
        ttk.Checkbutton(arow, text="采样时滑动后自动对齐（顶行贴红线）",
                        variable=self.align_var).pack(side=tk.LEFT, padx=6)
        ttk.Label(arow, text="（量出顶行与红线差多少就补多少，精度 ±2px）").pack(side=tk.LEFT)
        wrow = ttk.Frame(samp)
        wrow.pack(fill=tk.X)
        self.wait_cover_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(wrow, text="等待封面加载完", variable=self.wait_cover_var).pack(side=tk.LEFT)
        ttk.Label(wrow, text="超时(s)").pack(side=tk.LEFT, padx=(6, 0))
        self.wait_to_var = tk.DoubleVar(value=4.0)
        ttk.Spinbox(wrow, from_=0.5, to=30, increment=0.5, width=5,
                    textvariable=self.wait_to_var).pack(side=tk.LEFT)
        ttk.Label(wrow, text="重试").pack(side=tk.LEFT, padx=(6, 0))
        self.retry_var = tk.IntVar(value=2)
        ttk.Spinbox(wrow, from_=0, to=5, width=3, textvariable=self.retry_var).pack(side=tk.LEFT)
        # 翻页截断检测：连续两帧内容几乎一致视为已到列表末尾
        prow = ttk.Frame(samp)
        prow.pack(fill=tk.X)
        self.stop_on_end_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(prow, text="检测到列表末尾自动停止", variable=self.stop_on_end_var).pack(side=tk.LEFT)
        self.dedup_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(prow, text="按地图名去重", variable=self.dedup_var).pack(side=tk.LEFT, padx=(8, 0))
        srow = ttk.Frame(samp)
        srow.pack(fill=tk.X, pady=3)
        self.btn_start = ttk.Button(srow, text="开始采样", command=self.start_sample)
        self.btn_start.pack(side=tk.LEFT, padx=2)
        self.btn_stop = ttk.Button(srow, text="停止", command=self.stop_sample, state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=2)

        # 结果
        res = ttk.LabelFrame(right, text="3. 结果（按地图名去重）", padding=5)
        res.pack(fill=tk.BOTH, expand=True, pady=3)
        cols = ("name", "heat", "score", "cmt", "tag", "st")
        self.tree = ttk.Treeview(res, columns=cols, show="headings")
        for c, t, w in zip(cols, ("地图名", "热度", "评分", "评论数", "标签", "状态"),
                           (150, 80, 55, 70, 110, 60)):
            self.tree.heading(c, text=t)
            self.tree.column(c, width=w)
        self.tree.pack(fill=tk.BOTH, expand=True)
        erow = ttk.Frame(res)
        erow.pack(fill=tk.X, pady=3)
        # 2026-09-20：用户要「表格」= Excel 工作簿，原来只有 CSV/JSON；同时补「打开输出目录」
        # （用户常不知道文件落在哪）与「导出异常可见」（原来异常只打 stderr，表现为点了没反应）。
        ttk.Button(erow, text="导出 Excel(.xlsx)", command=self.export_xlsx).pack(side=tk.LEFT, padx=2)
        ttk.Button(erow, text="导出 CSV", command=self.export_csv).pack(side=tk.LEFT, padx=2)
        ttk.Button(erow, text="导出 JSON", command=self.export_json).pack(side=tk.LEFT, padx=2)
        erow2 = ttk.Frame(res)
        erow2.pack(fill=tk.X, pady=(0, 3))
        ttk.Button(erow2, text="打开输出目录", command=self.open_out_dir).pack(side=tk.LEFT, padx=2)
        ttk.Button(erow2, text="清空结果", command=self.clear_records).pack(side=tk.LEFT, padx=2)
        ttk.Label(erow2, text="（文件落在工具目录的 out\\ 下）").pack(side=tk.LEFT, padx=(6, 0))

        # 日志
        logf = ttk.LabelFrame(vpan, text="日志 / 状态", padding=4, height=140)
        vpan.add(logf, weight=0)
        # 日志多了要能翻，也给一根滚动条（原来只能靠光标键挪）
        lvsb = ttk.Scrollbar(logf, orient=tk.VERTICAL)
        self.log_text = tk.Text(logf, height=6, wrap=tk.WORD, yscrollcommand=lvsb.set)
        lvsb.configure(command=self.log_text.yview)
        lvsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.log_scroll = lvsb
        self.status_var = tk.StringVar(value="就绪")
        ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w").pack(fill=tk.X, side=tk.BOTTOM)

        self.refresh_rect_tree()

    # ------------------------------------------------------------ 日志/消息泵
    def log(self, msg):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        self.msgq.put(("log", "[%s] %s" % (ts, msg)))

    def pump(self):
        """主线程消息泵：工作线程只入队，不直接操作控件"""
        try:
            while True:
                kind, payload = self.msgq.get_nowait()
                if kind == "log":
                    self.log_text.insert(tk.END, payload + "\n")
                    self.log_text.see(tk.END)
                elif kind == "status":
                    self.status_var.set(payload)
                elif kind == "image":
                    self.show_image(payload)
                elif kind == "swipe_off":
                    # 工作线程不能碰控件，只能入队；这里在主线程关掉「自动上滑」
                    self.swipe_var.set(False)
                elif kind == "records":
                    for rec in payload:
                        self.add_record(rec)
                elif kind == "sampling_done":
                    self.sampling = False
                    self.btn_start.config(state=tk.NORMAL)
                    self.btn_stop.config(state=tk.DISABLED)
                    self.status_var.set("采样结束，共 %d 条" % len(self.records))
        except queue.Empty:
            pass
        self.root.after(120, self.pump)

    def init_ocr(self):
        self.msgq.put(("status", "正在加载 OCR 引擎…"))
        st = self.ocr.load()
        self.msgq.put(("status", st))
        self.msgq.put(("log", "OCR 引擎：%s" % st))
        if not self.ocr.ready:
            self.msgq.put(("log", "错误：%s" % self.ocr.error))
            self.msgq.put(("log", "安装命令：.venv\\Scripts\\python.exe -m pip install rapidocr-onnxruntime -i https://pypi.tuna.tsinghua.edu.cn/simple"))

    # ------------------------------------------------------------ 设备
    def pick_adb(self):
        p = filedialog.askopenfilename(title="选择 adb.exe", filetypes=[("adb", "adb.exe"), ("exe", "*.exe")])
        if p:
            self.adb_path_var.set(p)
            self.adb.path = p
            self.log("已设置 adb：%s" % p)
            self.refresh_devices()

    def refresh_devices(self):
        self.adb.path = self.adb_path_var.get()
        if not self.adb.path or not os.path.exists(self.adb.path):
            self.log("adb 路径无效，请在 Android SDK platform-tools 中指定 adb.exe；无 adb 时可改用「导入图片」")
            return
        devs, err = self.adb.devices()
        vals = ["%s  [%s]" % (d, s) for d, s in devs]
        self.dev_box["values"] = vals
        if vals:
            self.dev_box.current(0)
            self.adb.serial = devs[0][0]
            self.log("发现设备：%s" % ", ".join("%s(%s)" % (d, s) for d, s in devs))
        else:
            self.log("未发现设备（%s）。请确认已开启 USB 调试并授权本机" % (err or "无输出"))

    def on_dev_change(self, _e=None):
        v = self.dev_var.get()
        if v:
            self.adb.serial = v.split("  ")[0].strip()
            self.log("已选设备：%s" % self.adb.serial)

    # ------------------------------------------------------------ 图像
    def show_image(self, img):
        self.img = img
        self.update_canvas()

    def update_canvas(self):
        if self.img is None:
            return
        cw = max(self.canvas.winfo_width(), 50)
        ch = max(self.canvas.winfo_height(), 50)
        iw, ih = self.img.size
        self.scale = min(cw / iw, ch / ih, 1.0)
        disp = self.img.resize((max(int(iw * self.scale), 1), max(int(ih * self.scale), 1)), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(disp)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
        # 拖框过程中不重画整页网格：find_cards 每帧要裁 9 个格子，边拖边画会卡手。
        # on_release 里 drawing 已清空，松手后会补画完整网格。
        if self.drawing is None:
            self.draw_all_rects()

    def draw_all_rects(self):
        """画出整页所有卡片的「卡片框 + 字段框」。
        与识别共用同一套 card_boxes / field_rect，做到「所见即所识别」。
        旧版按行距纵向复制、还把大厅模式的相对偏移当绝对像素画，画面上永远只有一列
        —— 这就是「一页 2 行 3 列却只能框选一列」的来源。"""
        if self.img is None:
            return
        for b in self.card_boxes(self.img):
            bx = b["box"]
            col_i, row_i = b.get("col", 0), b["row"]
            first = (row_i == 0 and col_i == 0)
            self.canvas.create_rectangle(bx[0] * self.scale, bx[1] * self.scale,
                                         bx[2] * self.scale, bx[3] * self.scale,
                                         outline="#00b4d8", width=2,
                                         dash=() if first else (4, 3))
            self.canvas.create_text(bx[0] * self.scale + 3, bx[1] * self.scale + 3,
                                    anchor="nw", fill="#00b4d8",
                                    text="%d行%d列" % (row_i + 1, col_i + 1))
            for f in FIELDS:
                rr = self.field_rect(self.img, f, bx, row_i, col_i)
                if not rr:
                    continue
                color = FIELD_COLORS.get(f, "#ffffff")
                self.canvas.create_rectangle(rr[0] * self.scale, rr[1] * self.scale,
                                             rr[2] * self.scale, rr[3] * self.scale,
                                             outline=color, width=2 if first else 1,
                                             dash=() if first else (3, 2))
                if first:
                    self.canvas.create_text(rr[0] * self.scale + 3, rr[1] * self.scale + 1,
                                            anchor="nw", text=f, fill=color)

    def on_canvas_configure(self, _e=None):
        if self.img is not None:
            self.update_canvas()

    def on_press(self, e):
        if self.img is None:
            return
        self.drawing = (e.x, e.y, e.x, e.y)

    def on_drag(self, e):
        if not self.drawing:
            return
        self.drawing = (self.drawing[0], self.drawing[1], e.x, e.y)
        self.update_canvas()
        x0, y0, x1, y1 = self.drawing
        self.canvas.create_rectangle(x0, y0, x1, y1, outline="#00ff88", width=2)

    def on_release(self, _e):
        if not self.drawing or self.img is None:
            return
        x0, y0, x1, y1 = self.drawing
        self.drawing = None
        ix0 = int(min(x0, x1) / self.scale)
        iy0 = int(min(y0, y1) / self.scale)
        ix1 = int(max(x0, x1) / self.scale)
        iy1 = int(max(y0, y1) / self.scale)
        if ix1 - ix0 < 4 or iy1 - iy0 < 4:
            self.update_canvas()
            return
        f = self.cur_field.get()
        if self.layout_mode_var.get() == "lobby":
            # 大厅网格模式：几何由几何表决定，但允许用户「框选覆盖」。
            # 把绝对像素框折算成「相对卡片左上角的视觉坐标偏移」，这样整页每张卡都跟着生效。
            # 旧版把框原样存进 self.rects 然后被 LOBBY 几何无视 —— 拖了没反应也不报错。
            rel = self.abs_to_card_relative(ix0, iy0, ix1, iy1)
            if rel is None:
                self.log("框选位置不在任何卡片上，已忽略（大厅网格模式只在卡片范围内生效）")
                self.update_canvas()
                return
            self.field_override[f] = rel
            self.log("已覆盖 %s：绝对(%d,%d,%d,%d) → 卡片相对视觉坐标 (%.1f,%.1f,%.1f,%.1f)"
                     % (f, ix0, iy0, ix1, iy1, rel[0], rel[1], rel[2], rel[3]))
        else:
            self.rects[f] = (ix0, iy0, ix1, iy1)
            self.log("已框选 %s：(%d,%d,%d,%d)，按 行数×列数（%s×%s）复制到整页"
                     % (f, ix0, iy0, ix1, iy1, self.card_count_var.get(), self.ncol_var.get()))
        self.refresh_rect_tree()
        self.update_canvas()

    def has_field_box(self, field):
        """该字段在当前模式下是否有可用的框。
        不能只看 self.rects：大厅网格模式的框来自几何表（或框选覆盖），
        self.rects 里可能只有用户手工存的那几个字段 —— 旧版据此判断，会把
        「入口按钮」这种没有手工框的字段在大厅模式下也无条件留空。"""
        if self.layout_mode_var.get() == "lobby":
            return bool(self.field_override.get(field)
                        or LOBBY["fields"].get(field)
                        or self.rects.get(field))
        return bool(self.rects.get(field))

    # ------------------------------------------------------------ 滑动自检
    def test_swipe(self, runs=None):
        """一键判定本机能不能用「自动上滑」，失败时给出对症的 ROM 侧对策。
        必须跑在主线程（按钮回调），因为要直接改复选框状态；采样线程里走 msgq。

        `runs` 显式传入则覆盖界面的「连测次数」（「只测一次」按钮传 1）。
        """
        self.adb.path = self.adb_path_var.get()
        if not self.adb.path or not os.path.exists(self.adb.path):
            self.log("先设置有效的 adb 路径（当前：%s）" % (self.adb.path or "空"))
            return
        devs, err = self.adb.devices()
        if not devs:
            self.log("没有可用设备：%s" % (diagnose_adb_error(err)[1] if err else
                                        "请连接手机、开启 USB 调试后再点「刷新设备」"))
            return
        # 真滑一次并量位移（旧行为只判「能不能注入」，看不到滑了多少，没法调幅度）。
        # 注意：**不传 screen_size()** —— wm size 不反映旋转，横屏下会算出越界坐标。
        # 滑动尺寸由工作线程用「截屏的实际尺寸」决定（与采样流程一致）。
        n = int(runs) if runs else int(self.runs_var.get())
        # 勾了实时流却没装 ffmpeg：明说并降级，别让用户以为是「测不准」
        if self.live_measure_var.get() and not find_ffmpeg():
            self.log("已勾选「用实时流测位移」，但本机没有 ffmpeg，本次退回两帧比对。\n"
                     "装一次就能用：  " + FFMPEG_INSTALL)
        self.status_var.set("正在测滑动…")
        threading.Thread(target=self._swipe_probe_worker,
                         args=(None, False, n), daemon=True).start()

    def test_swipe_once(self):
        """「只测一次」：不连测，只滑一下量一次 —— 调参时想看单次真实效果就用它。

        只测一次的值**不能**直接拿来调参（fling 落点本身有方差），日志里会明说。
        """
        self.test_swipe(runs=1)

    def measure_manual_swipe(self):
        """「测手动滑动」：不动用输入注入，量出**人手滑一次**实际滚动了多少像素。

        用途：① 本机 `input swipe` 被 ROM 拒绝时，仍能标定出「一页该滚多少」；
        ② 反过来验证自动滑动的落点是否接近人手翻页的效果。
        """
        self.adb.path = self.adb_path_var.get()
        if not self.adb.path or not os.path.exists(self.adb.path):
            self.log("先设置有效的 adb 路径（当前：%s）" % (self.adb.path or "空"))
            return
        devs, err = self.adb.devices()
        if not devs:
            self.log("没有可用设备：%s" % (diagnose_adb_error(err)[1] if err else
                                        "请连接手机、开启 USB 调试后再点「刷新设备」"))
            return
        self.status_var.set("准备测手动滑动…")
        threading.Thread(target=self._swipe_probe_worker,
                         args=(None, True, 1), daemon=True).start()

    def precise_scroll(self, target_px, max_rounds=3, tol=None, ms=None, direction=1):
        """闭环滚动到目标位移：滑一次 → 等滚停 → 量实际 → 按本轮实测增益补下一次。

        `input swipe` 是开环的，一次定生死必然不准；但只要**量得出**实际滚动
        （`measure_scroll`），就能把误差当成反馈量补掉 —— 1~2 轮收敛到 ±12%。
        `tol` 不传时取 max(12, 12%×目标)；对齐网格这类要精确到几个像素的场景
        由调用方显式传小容差（见 align_to_grid）。
        ms：本次闭环用的滑动时长（不传用界面上的 swipe_ms）；direction=1 上滑
        （列表前滚），-1 下滑（列表回滚，align_to_grid 行界回滚用）。
        返回 (累计滚动px|None, 轮数, 明细行)。
        """
        if tol is None:
            tol = max(12, int(0.12 * target_px))
        ms = int(ms) if ms is not None else int(self.swipe_ms_var.get())
        # 实时流优先：两帧比对量的是「某一瞬间」，实时流量的是整段惯性，闭环收敛快得多。
        use_live = self._live_ok()
        before, err = self.adb.screencap()
        if before is None:
            return None, 0, ["截屏失败：%s" % err]
        total = 0
        lines = []
        last_finger = 0
        last_actual = 0
        rounds = 0
        # 增益按方向隔离（2026-09-21 真机实测）：回滚的阻尼/fling 特性和前滚差别很大
        # （小回滚常撞触控 slop，学习增益会跌到 0.1），若混用会把前滚规划也带歪。
        # 回滚只在本次调用内学习，且不写回 self.swipe_gain（那是前滚标定值）。
        fallback_gain = (self.swipe_gain or 1.0) if direction > 0 else 1.0
        for r in range(1, max_rounds + 1):
            rounds = r
            need, finger, gain = plan_next_swipe(target_px, total, last_finger,
                                                 last_actual, fallback_gain)
            if abs(need) <= tol:
                break
            # 增益保护（2026-09-21 真机实测）：小位移补滚碰上触控 slop（31px 手指
            # 只滚 3px）时，学习增益会跌到 0.1，反推出 370px+ 的巨型手指位移，
            # 一 fling 就是几百 px，远超缺口。手指位移夹到「3×缺口+30px」内：
            # 正常阻尼区间（增益 0.5~1.5）完全不受影响。
            finger = min(finger, 3 * need + 30)
            w, h = before.size
            # 手指位移换算成「屏高比」，并夹到可滑区间（单次最多 80% 屏高）
            pct = max(0.02, min(0.80, finger / float(h)))
            if use_live:
                res = self._live_measure_one(pct, ms, (w, h), direction=direction)
                if res["err"]:
                    lines.append("第 %d 次实时测量失败（%s），后续改用两帧比对"
                                 % (r, res["err"].splitlines()[0]))
                    use_live = False
                    continue
                sw = res["swipe"]
                if not sw[0]:
                    lines.append("第 %d 次滑动失败（%s）：%s"
                                 % (r, sw[1], sw[2].splitlines()[0] if sw[2] else ""))
                    return (total or None), rounds, lines
                shift = res["total"]
                shift = int(round(shift * res["scale"])) if shift is not None else None
                if direction < 0 and shift is not None:
                    shift = -shift        # 回滚的带符号位移 → 本次闭环的进度量（正数）
                why = "%d 帧 / %d 段（%d 段对不上）" % (res["info"]["n"], res["info"]["links"],
                                                  res["info"]["bad"])
                stopped = True
            else:
                if direction < 0:
                    ok, kind, msg = self.adb.swipe_down(w, h, percent=pct, duration=ms)
                else:
                    ok, kind, msg = self.adb.swipe_up(w, h, percent=pct, duration=ms)
                if not ok:
                    lines.append("第 %d 次滑动失败（%s）：%s"
                                 % (r, kind, msg.splitlines()[0] if msg else ""))
                    return (total or None), rounds, lines
                after, waited, stopped = wait_scroll_stop(self.adb)
                if after is None:
                    lines.append("第 %d 次后帧截屏失败" % r)
                    break
                shift, why = measure_scroll(before, after, direction=direction)
                if direction < 0 and shift is not None:
                    shift = -shift        # 回滚的带符号位移 → 进度量（正数）
                before = after
            if shift is None:
                lines.append("第 %d 次量不出位移（%s）" % (r, why))
                break
            last_finger = int(h * pct)
            last_actual = shift
            if direction > 0:
                self.swipe_gain = gain     # 只持久化前滚标定；回滚增益不跨调用复用
            total += shift
            lines.append("第 %d 次：还差 %dpx → 手指 %dpx（增益 %.2f）→ 实际 %dpx，累计 %dpx%s"
                         % (r, need, last_finger, gain, shift, total,
                             "" if stopped else "（未停稳）"))
        return (total or None), rounds, lines

    def _page_px(self, h):
        """一页 = 2 行卡片；行距 INT_ROW_STEP 在 1920x864 下标定，按屏高等比换算。"""
        row_px = int(round(INT_ROW_STEP * h / 864.0))
        return 2 * row_px

    # ------------------------------------------------------------ 顶行对齐红线
    def align_to_grid(self, max_rounds=5):
        """把视口内第一张**完整**卡片的顶边精确对到「红线」（first_row_y）上。

        用户要求（2026-09-21）：滑完之后，下一批 6 张地图的**上排 3 张顶部要精准
        贴在红线处** —— 只按「一页」闭环滚会累积 ±12% 的误差，几页之后顶行就
        半截在视口外、OCR 框全部错位。这里改用**绝对反馈**：直接量出当前顶行
        卡顶与红线的差（`grid_drift`，靠行间亮缝定位，精度 ±2px），差多少补多少。

        行界悬崖（2026-09-21 真机实测）：cut 状态下检测器指向**下一行**的行界，
        若此时补滚过冲哪怕 30px，就越过那条例行界，目标立刻跳到再下一行 ——
        实测 156→333→329→357 追着行界跑的死循环，永远差一步。对策：越界量
        s_past = 行距 - 偏差 还不大（≤ max(80, 25%行距)）时，改为**反向滚回
        当前行**（swipe_down），目标只有几十 px，绝对复测下能真正收敛。

        只在「大厅网格」模式下有意义（自选框选没有固定网格）。
        返回 (最终偏差px|None, 轮数, 明细行)。
        """
        lines = []
        for r in range(1, max_rounds + 1):
            img, err = self.adb.screencap()
            if img is None:
                lines.append("第 %d 轮：截屏失败（%s）" % (r, err))
                return None, r, lines
            drift, info = grid_drift(img)
            if drift is None:
                lines.append("第 %d 轮：量不出顶行位置（%s）" % (r, info.get("why", "未知")))
                return None, r, lines
            tol = max(5, int(round(0.02 * info["R"])))
            lines.append("第 %d 轮：顶行卡顶 %d（目标 %d，状态 %s）→ 偏差 %+dpx"
                         % (r, info.get("first_top", -1), info["T"],
                            info.get("state", "?"), info.get("drift", drift)))
            if not info.get("spacing_ok", True):
                # spacing_ok=False 在真机上有两种成因，不能一概停止（2026-09-22 实测）：
                #   ① 已滚到列表末尾 / 封面误判（旧结论，确实该停）；
                #   ② **首行被裁**时，检测到的第一个「边界」是视口内第二条缝，
                #      它与后续边界的间距天然不满足行距。
                #      生产帧 shot_20260922_140417_001 正是这种（spacing=False）；
                #      实测该帧首行完整、只需 +11px 正向微调，故不能停 —— 停下就把
                #      错位状态固化了。此时照常进入下面的补滚分支。
                lines.append("⚠ 缝隙间距与行距不符（可能缝落在封面浅色平坦区），"
                             "但仍有正向偏差 %+dpx → 继续微调" % drift)
            if 0 <= drift <= tol:
                return drift, r, lines
            state = info.get("state", "?")
            # 校正滑动用慢速（≥1200ms）：同一行程越长释放速度越低，fling 惯性越小 ——
            # 真机实测 800ms 时实际滚动仍系统性超过手指行程 30~40%，过冲就跨行界。
            ms = max(1200, int(self.swipe_ms_var.get()))
            # 2026-09-22：drift 恒为 ≥0（见 grid_drift 注释，scrolled_past 已证伪删除），
            # 故不再有「反向回滚首行」的分支；两种状态都是向下滚补齐。
            s_past = info["R"] - drift if state == "cut" else 0
            if 0 < s_past <= max(80, int(round(0.25 * info["R"]))):
                lines.append("  顶行已越过本行行界 %dpx → 反向滚回当前行（避免追行界死循环）"
                             % s_past)
                got, rounds, sub = self.precise_scroll(s_past, max_rounds=2, tol=tol,
                                                       ms=ms, direction=-1)
            else:
                got, rounds, sub = self.precise_scroll(drift, max_rounds=2, tol=tol, ms=ms)
            for l in sub:
                lines.append("  补滚 %dpx｜%s" % (s_past if 0 < s_past else drift, l))
            if got is None:
                lines.append("第 %d 轮：补滚量不出位移，停止对齐（保持当前位置）" % r)
                return None, r, lines
        img, err = self.adb.screencap()
        if img is not None:
            drift, info = grid_drift(img)
            if drift is not None:
                _tol = max(5, int(round(0.02 * info["R"])))
                lines.append("收敛检查：最终偏差 %+dpx%s"
                             % (info.get("drift", drift),
                                "" if abs(drift) <= _tol else "（⚠ 未收敛到容差内，建议再点一次）"))
                return drift, max_rounds, lines
        return None, max_rounds, lines

    def align_once(self):
        """「对齐到红线」按钮：立即量偏差并补滚到位（独立于采样流程，便于验证）。"""
        self.adb.path = self.adb_path_var.get()
        if not self.adb.path or not os.path.exists(self.adb.path):
            self.log("先设置有效的 adb 路径（当前：%s）" % (self.adb.path or "空"))
            return
        devs, err = self.adb.devices()
        if not devs:
            self.log("没有可用设备：%s" % (diagnose_adb_error(err)[1] if err else
                                        "请连接手机、开启 USB 调试后再点「刷新设备」"))
            return
        if self.layout_mode_var.get() != "lobby":
            self.log("对齐网格只在「大厅网格」模式下有效（自选框选没有固定网格）")
            return
        self.status_var.set("对齐顶行到红线…")
        threading.Thread(target=self._align_worker, daemon=True).start()

    def _align_worker(self):
        drift, rounds, lines = self.align_to_grid()
        for l in lines:
            self.msgq.put(("log", "对齐｜%s" % l))
        if drift is None:
            self.msgq.put(("status", "对齐失败"))
        else:
            self.msgq.put(("status", "对齐完成：偏差 %dpx" % drift))
            self.msgq.put(("log", "对齐完成：顶行偏差 %+dpx（%d 轮）。红线 = 视觉 y 91，"
                                  "顶行卡顶应贴在这里；偏差 >0 表示整行还偏在红线下方，"
                                  "继续点「对齐」可再收敛一轮。"
                           % (drift, rounds)))

    # ------------------------------------------------------------ 实时屏幕流
    def _live_ok(self):
        """是否走实时流路径：界面勾选了 + 本机有 ffmpeg。缺 ffmpeg 时调用方应自行降级。"""
        v = getattr(self, "live_measure_var", None)
        return bool(v is not None and v.get() and find_ffmpeg())

    def _live_measure_one(self, pct, ms, size, direction=1):
        """起流 → 滑一次 → 录完惯性尾巴 → 停流 → 沿帧链积分出**整段**真实位移。

        返回 dict：err / total(测量帧px或None) / info / swipe=(ok,kind,msg) / scale。
        direction=1 上滑（前滚）/ -1 下滑（回滚），位移都取大小的积分。
        """
        live = LiveScreen(self.adb)
        ok, err = live.start(size)
        if not ok:
            return {"err": err, "total": None, "swipe": (False, "other", ""),
                    "info": {"n": 0, "links": 0, "bad": 0, "steps": [], "max_step": 0},
                    "scale": 1.0}
        try:
            time.sleep(LIVE_WARMUP_SEC)      # 头几帧可能是编码未完成的旧帧
            w, h = size
            if direction < 0:
                sw = self.adb.swipe_down(w, h, percent=pct, duration=ms)
            else:
                sw = self.adb.swipe_up(w, h, percent=pct, duration=ms)
            # 录到惯性跑完为止：不用猜「等几秒才停」，直接把整段都录下来
            time.sleep(max(LIVE_TAIL_SEC, ms / 1000.0 + 1.0))
        finally:
            live.stop()
        total, info = measure_scroll_total(live.burst(), direction=direction)
        return {"err": "", "total": total, "info": info, "swipe": sw,
                "scale": live.frame_scale}

    def open_live(self):
        """打开「实时监视」窗口：连续看手机屏幕 + 实时读累计滚动位移。"""
        self.adb.path = self.adb_path_var.get()
        if not self.adb.path or not os.path.exists(self.adb.path):
            self.log("先设置有效的 adb 路径（当前：%s）" % (self.adb.path or "空"))
            return
        devs, err = self.adb.devices()
        if not devs:
            self.log("没有可用设备：%s" % (diagnose_adb_error(err)[1] if err else
                                        "请连接手机、开启 USB 调试后再点「刷新设备」"))
            return
        if not find_ffmpeg():
            self.log("实时监视需要 ffmpeg 解码 H.264 流，但本机没找到。\n在本工具目录执行一次：\n  "
                     + FFMPEG_INSTALL)
            return
        self.live_win = LiveMonitor(self.root, self)
        self.log("已打开实时监视窗口（screenrecord 连续流 ≈26fps）。"
                 "滑一次看「累计滚动」读数，停稳后不再跳动 —— 那就是这次的真实位移。")

    def live_measure_swipe(self):
        """「实时测滑动」：录下**整段**滑动（含惯性尾巴），沿帧链积分出真实位移。

        与「测滑动」的区别：后者只截滑前/滑后两帧，位移一大就匹配不上；
        这里每一帧都在，量的是完整过程 —— 也就是「每次都不一」要的那个稳定值。
        """
        self.adb.path = self.adb_path_var.get()
        if not self.adb.path or not os.path.exists(self.adb.path):
            self.log("先设置有效的 adb 路径（当前：%s）" % (self.adb.path or "空"))
            return
        devs, err = self.adb.devices()
        if not devs:
            self.log("没有可用设备：%s" % (diagnose_adb_error(err)[1] if err else
                                        "请连接手机、开启 USB 调试后再点「刷新设备」"))
            return
        if not find_ffmpeg():
            self.log("实时测滑动需要 ffmpeg 解码 H.264 流，但本机没找到。\n在本工具目录执行一次：\n  "
                     + FFMPEG_INSTALL)
            return
        self.status_var.set("实时测滑动…")
        threading.Thread(target=self._live_probe_worker,
                         args=(int(self.runs_var.get()),), daemon=True).start()

    def _live_probe_worker(self, runs=SWIPE_RUNS_DEFAULT):
        """实时流版本的连测：每次都录下整段滑动并积分，最后仍走 `_report_runs` 汇总。"""
        pct = float(self.swipe_pct_var.get())
        ms = int(self.swipe_ms_var.get())
        before, err = self.adb.screencap()
        if before is None:
            self.msgq.put(("log", "实时测滑动：截屏取不到（%s）" % err))
            self.msgq.put(("status", "测滑动失败"))
            return
        if is_blank(before):
            self.msgq.put(("log", "实时测滑动：%s" % explain_blank(self.adb)))
            self.msgq.put(("status", "测滑动失败"))
            return
        w, h = before.size
        page_px = self._page_px(h)
        finger_px = int(h * pct)
        vals = []
        for i in range(max(1, int(runs))):
            r = self._live_measure_one(pct, ms, (w, h))
            if r["err"]:
                self.msgq.put(("log", "实时测滑动：%s" % r["err"]))
                self.msgq.put(("status", "测滑动失败"))
                return
            ok, kind, msg = r["swipe"]
            if not ok:
                self.msgq.put(("log", "滑动自检失败（%s）：\n%s" % (kind, msg)))
                self.msgq.put(("status", "滑动自检失败：%s" % kind))
                if kind == "inject_denied":
                    self.msgq.put(("swipe_off", None))
                    self.msgq.put(("log", "已自动取消勾选「自动上滑」。\n"
                                          "要标定幅度可点「测手动滑动」：它不用输入注入，"
                                          "量的是你手动滑一页实际滚了多少像素。"))
                return
            info, px = r["info"], None
            if r["total"] is not None:
                px = int(round(r["total"] * r["scale"]))
            self.msgq.put(("log", "第 %d 次：滚动 %s｜录 %d 帧 / 积分 %d 段"
                           "（最大单段 %dpx，%d 段对不上）"
                           % (i + 1, ("%dpx" % px) if px is not None else "测不出",
                              info["n"], info["links"], info["max_step"], info["bad"])))
            vals.append(px)
            if px is not None and px <= 2:
                self.msgq.put(("log", "第 %d 次几乎没动 —— 多半已滚到列表末尾，提前结束连测。" % (i + 1)))
                break
            time.sleep(0.6)
        self._report_runs(vals, finger_px, page_px)

    def _swipe_probe_worker(self, size, manual, runs=SWIPE_RUNS_DEFAULT):
        """滑动测量的工作线程：截前帧 →（自动滑 / 等手滑）→ 等滚停 → 截后帧 → 比对量位移。

        `size` 现在固定传 None —— 滑动坐标一律用**截屏的实际尺寸**（before.size）。
        自动模式连测 `runs` 次（默认 3）取中位数：fling 落点本身是随机的，
        单次值不能拿来调参（2026-09-21 用户反馈「每次距离都不一」）。
        """
        if manual:
            before, err = self.adb.screencap()
            if before is None:
                self.msgq.put(("log", "测滑动失败：截屏取不到（%s）" % err))
                self.msgq.put(("status", "测滑动失败"))
                return
            if is_blank(before):
                self.msgq.put(("log", "测滑动失败：%s" % explain_blank(self.adb)))
                self.msgq.put(("status", "测滑动失败"))
                return
            self.msgq.put(("log", "已截下第一帧。请在 %.0f 秒内，在手机上按你平时翻页的力度手动上滑一次…"
                           % MANUAL_MEASURE_WAIT))
            self.msgq.put(("status", "请在手机上手动上滑一次…"))
            time.sleep(MANUAL_MEASURE_WAIT)
            self._report_scroll(before, None, "手动滑动")
            return

        # —— 自动模式：连测 runs 次，取中位数 ——
        # 勾选了「用实时流测位移」且本机有 ffmpeg 时走实时流：录整段 + 沿帧链积分，
        # 比两帧比对稳得多（两帧比对在位移大时会「测不出」）。
        if self._live_ok():
            self._live_probe_worker(runs)
            return
        pct = float(self.swipe_pct_var.get())
        ms = int(self.swipe_ms_var.get())
        vals = []
        page_px = 0
        H = 0
        for i in range(max(1, int(runs))):
            before, err = self.adb.screencap()
            if before is None:
                self.msgq.put(("log", "第 %d 次：截屏取不到（%s）" % (i + 1, err)))
                break
            if is_blank(before):
                self.msgq.put(("log", "第 %d 次：%s" % (i + 1, explain_blank(self.adb))))
                break
            # 滑动坐标必须用截屏尺寸：wm size 不反映旋转，横屏下会算出越界 y（实测踩过）
            w, h = before.size
            H, page_px = h, self._page_px(h)
            ok, kind, msg = self.adb.swipe_up(w, h, percent=pct, duration=ms)
            if not ok:
                self.msgq.put(("log", "滑动自检失败（%s）：\n%s" % (kind, msg)))
                self.msgq.put(("status", "滑动自检失败：%s" % kind))
                if kind == "inject_denied":
                    self.msgq.put(("swipe_off", None))
                    self.msgq.put(("log", "已自动取消勾选「自动上滑」。\n"
                                          "要标定幅度可点「测手动滑动」：它不用输入注入，"
                                          "量的是你手动滑一页实际滚了多少像素。"))
                return
            # 必须等列表**真的停下**再截：惯性没跑完时量到的是中间态，而 fling 衰减时长
            # 每次都不同 —— 这正是「每次距离都不一」的主要来源（2026-09-21 用户反馈）。
            after, waited, stopped = wait_scroll_stop(self.adb)
            if after is None:
                self.msgq.put(("log", "第 %d 次：后帧截屏失败，量不出位移" % (i + 1)))
                break
            shift, why = measure_scroll(before, after)
            tail = "" if stopped else "（⚠ 等了 %.1fs 仍未停稳，该次结果偏小）" % waited
            self.msgq.put(("log", "第 %d 次：滚动 %s｜等滚停 %.1fs%s"
                           % (i + 1,
                              ("%dpx" % shift) if shift is not None else "测不出（%s）" % why,
                              waited, tail)))
            vals.append(shift)
            if shift is not None and shift <= 2:
                self.msgq.put(("log", "第 %d 次几乎没动 —— 多半已滚到列表末尾，提前结束连测。" % (i + 1)))
                break
        self._report_runs(vals, int(H * pct), page_px)

    def _report_runs(self, vals, finger_px, page_px):
        """连测结果的汇总输出：逐次值 + 中位数 + 离散度 + 稳定性判定 + 调参建议。"""
        s = summarize_runs(vals, page_px)
        if s["n"] == 0:
            self.msgq.put(("log", "滑动测量：%s" % s["advice"]))
            self.msgq.put(("status", "测滑动：量不出位移"))
            return
        self.msgq.put(("log", "连测 %d 次：%s"
                       % (s["n"], " / ".join(str(v) if v is not None else "测不出" for v in vals))))
        self.msgq.put(("log", "中位数 %dpx（最小 %s / 最大 %s，波动 %spx）→ 稳定性：%s"
                       % (s["median"], s["min"], s["max"], s["spread"], s["verdict"])))
        self.msgq.put(("log", s["advice"]))
        if s["n"] == 1:
            self.msgq.put(("log", "（这是「只测一次」的单次值：fling 落点本身有方差，"
                                  "单次结果有偶然性。要拿去调参请用「测滑动（连测取中位数）」。）"))
        if s["median"] and s["median"] > 2 and page_px:
            pct = float(self.swipe_pct_var.get())
            verdict, advice, new_pct = swipe_advice(finger_px, s["median"], page_px, pct=pct)
            self.msgq.put(("log", "按中位数判定：%s —— %s" % (verdict, advice)))
            if new_pct is not None:
                self.msgq.put(("log", "把「上滑幅度」改成 %.2f 后复测一次确认。" % new_pct))
            self.msgq.put(("status", "连测 %d 次：中位数 %dpx（%s / %s）"
                           % (s["n"], s["median"], s["verdict"], verdict)))
        else:
            self.msgq.put(("status", "连测 %d 次：%s" % (s["n"], s["verdict"])))

    def _report_scroll(self, before, finger_px, title):
        """截后帧 + 量位移 + 给调参建议。finger_px=None 表示手动模式（没有手指位移可比）。"""
        after, err = self.adb.screencap()
        if after is None:
            self.msgq.put(("log", "%s：后帧截屏失败（%s），量不出位移" % (title, err)))
            self.msgq.put(("status", "测滑动失败"))
            return
        if is_blank(after):
            self.msgq.put(("log", "%s：后帧为纯色（%s），量不出位移" % (title, explain_blank(self.adb))))
            self.msgq.put(("status", "测滑动失败"))
            return
        shift, why = measure_scroll(before, after)
        H = before.size[1]
        page_px = self._page_px(H)
        if shift is None:
            self.msgq.put(("log", "%s：%s，量不出位移（%s）" % (title, why, "两帧对不上")))
            self.msgq.put(("status", "测滑动：量不出位移"))
            return
        pct = float(self.swipe_pct_var.get())
        if finger_px is None:
            pr = shift / float(page_px)
            self.msgq.put(("log", "%s：实际滚动 %dpx（占屏高 %.0f%%），约 %.1f 页（一页=2 行卡片≈%dpx）"
                           % (title, shift, shift * 100.0 / H, pr, page_px)))
            if pr >= 0.7:
                self.msgq.put(("log", "这就是「翻一页」的目标量。可据此设自动上滑："
                                      "从当前幅度 %.2f 起测，看自动滑动的实际滚动是否接近 %dpx。"
                                      % (pct, shift)))
            else:
                self.msgq.put(("log", "这一手滑不到一页，作为参考值偏小；可以再用力滑一次重测。"))
            self.msgq.put(("status", "手动滑动实测 %dpx" % shift))
            return
        verdict, advice, new_pct = swipe_advice(finger_px, shift, page_px, pct=pct)
        self.msgq.put(("log", "%s：手指位移 %dpx（幅度 %.0f%% × 屏高 %d）｜实际滚动 %dpx（占屏高 %.0f%%）"
                       % (title, finger_px, pct * 100, H, shift, shift * 100.0 / H)))
        self.msgq.put(("log", "判定：%s —— %s" % (verdict, advice)))
        if new_pct is not None:
            self.msgq.put(("log", "提示：把「上滑幅度」改成 %.2f 后再点一次本按钮复测；"
                                  "惯性是非线性的，建议复测 1~2 次收敛。" % new_pct))
        self.msgq.put(("status", "滑动实测 %dpx（%s）" % (shift, verdict)))

    def abs_to_card_relative(self, ix0, iy0, ix1, iy1):
        """把整帧绝对像素框折算成「相对卡片左上角的视觉坐标偏移」。
        先找出框中心落在哪张卡片上，再减去该卡片的视觉原点；找不到返回 None。"""
        try:
            cx = (ix0 + ix1) / 2.0
            cy = (iy0 + iy1) / 2.0
            for b in self.card_boxes(self.img):
                bx = b["box"]
                if bx[0] <= cx <= bx[2] and bx[1] <= cy <= bx[3]:
                    sx = self.img.size[0] / float(VIEW_W)
                    sy = self.img.size[1] / float(VIEW_H)
                    return (ix0 / sx - bx[0] / sx, iy0 / sy - bx[1] / sy,
                            ix1 / sx - bx[0] / sx, iy1 / sy - bx[1] / sy)
        except Exception as e:
            self.log("框选折算失败：%s" % e)
        return None

    def refresh_rect_tree(self):
        """把当前生效的字段框列出来。
        大厅网格模式下框来自几何表（相对卡片左上角的视觉坐标），若用户拖过框则显示覆盖值。"""
        for it in self.rect_tree.get_children():
            self.rect_tree.delete(it)
        in_lobby = self.layout_mode_var.get() == "lobby"
        for f in FIELDS:
            ov = self.field_override.get(f)
            if in_lobby:
                src = LOBBY["fields"].get(f)
                if ov:
                    desc = "覆盖 %s" % (tuple(round(v, 1) for v in ov),)
                elif src:
                    desc = "几何表 %s" % (tuple(round(v, 1) for v in src),)
                else:
                    nb = self.rects.get(f)
                    desc = ("自定义 %s" % (tuple(nb),)) if nb else "本页无此字段"
            else:
                r = self.rects.get(f)
                desc = ("框选 %s" % (tuple(r),)) if r else "未框选"
            self.rect_tree.insert("", tk.END, values=(f, desc))

    def clear_rects(self):
        """清空框选与大厅模式的框选覆盖，回到几何表默认值。"""
        self.rects.clear()
        self.field_override.clear()
        if self.layout_mode_var.get() == "lobby":
            self.rects = {f: tuple(b) for f, b in LOBBY["fields"].items()}
        self.refresh_rect_tree()
        self.update_canvas()
        self.log("已清空框选与覆盖，回到按图实测的几何表默认值")

    # ------------------------------------------------------------ 载入图像
    def shot_from_adb(self):
        self.adb.path = self.adb_path_var.get()
        img, err = self.adb.screencap()
        if img is None:
            self.log("截屏失败：%s" % err)
            messagebox.showerror("截屏失败", err)
            return
        if is_blank(img):
            why = explain_blank(self.adb)
            self.log("警告：%s" % why)
            messagebox.showwarning("疑似黑屏", why)
        self.show_image(img)
        self.log("截屏成功：%dx%d" % img.size)

    def load_image(self):
        p = filedialog.askopenfilename(filetypes=[("图片", "*.png;*.jpg;*.jpeg;*.bmp"), ("所有", "*.*")])
        if p:
            self.open_path(p)

    def load_folder(self):
        d = filedialog.askdirectory()
        if not d:
            return
        files = []
        for ext in ("png", "jpg", "jpeg", "bmp"):
            files += [os.path.join(d, f) for f in os.listdir(d) if f.lower().endswith("." + ext)]
        files.sort()
        if not files:
            self.log("文件夹内无图片")
            return
        self.log("导入 %d 张图片，开始批量识别…" % len(files))
        threading.Thread(target=self.batch_files, args=(files,), daemon=True).start()

    def paste_clipboard(self):
        try:
            img = ImageGrab.grabclipboard()
            if img is None:
                self.log("剪贴板中没有图片")
                return
            self.show_image(img.convert("RGB"))
            self.log("已粘贴剪贴板图片：%dx%d" % img.size)
        except Exception as e:
            self.log("粘贴失败：%s" % e)

    def open_path(self, p):
        try:
            img = Image.open(p).convert("RGB")
            self.show_image(img)
            self.log("已载入：%s (%dx%d)" % (p, img.size[0], img.size[1]))
        except Exception as e:
            self.log("载入失败：%s" % e)

    # ------------------------------------------------------------ 识别
    def crop_safe(self, img, r):
        """按原图坐标裁切；越界时返回 None（不静默补黑边，避免识别脏数据）"""
        w, h = img.size
        x0, y0, x1, y1 = r
        if x0 < 0 or y0 < 0 or x1 > w or y1 > h or x1 <= x0 or y1 <= y0:
            return None
        return img.crop((x0, y0, x1, y1))

    def card_boxes(self, img):
        """按当前几何参数算出本帧所有待识别卡片的像素框。
        大厅模式走 LOBBY 固定网格（3 列 × N 行）；
        自选模式把用户框定的那一张按「行数 × 列数」复制成整页网格。"""
        if self.layout_mode_var.get() == "lobby":
            geom = self.cur_geom()
            return find_cards(img, geom)
        # 自选模式：用户在第 1 张卡上拖好的各字段框为基准，整块按 (列距, 行距) 平移到每张卡。
        # 这里回传的是「整块字段框的并集」平移后的外接框 —— 它只用于
        # ① recognize_frame 的屏幕边缘截断判断，② 把 row/col 传给 field_rect 做平移。
        # ⚠ 2026-09-20 修：旧版只按行下移、col 恒为 0，所以一页 3 列时右边两列整列丢失。
        try:
            nrow = max(1, int(self.card_count_var.get()))
            ncol = max(1, int(self.ncol_var.get()))
            step_y = int(self.card_step_var.get())
            step_x = int(self.col_step_var.get())
        except Exception:
            nrow, ncol, step_y, step_x = 1, 1, 0, 0
        rs = [r for r in self.rects.values() if r]
        if not rs:
            return []
        x0 = min(r[0] for r in rs)
        y0 = min(r[1] for r in rs)
        x1 = max(r[2] for r in rs)
        y1 = max(r[3] for r in rs)
        out = []
        # 行优先：与页面上「先左右后上下」的阅读顺序一致，序号才对得上
        for r_i in range(nrow):
            for c_i in range(ncol):
                dx = c_i * step_x
                dy = r_i * step_y
                out.append({"col": c_i, "row": r_i,
                            "box": (x0 + dx, y0 + dy, x1 + dx, y1 + dy),
                            "state": "normal"})
        return out

    def field_rect(self, img, field, box, row=0, col=0):
        """把「字段框」换算成本帧里的真机像素框。
        大厅模式：box 是卡片框，字段框 = 卡片框 + LOBBY 里按图实测的相对偏移；
                  若该字段有「框选覆盖」，用覆盖值替代 LOBBY 几何。
        自选模式：字段框 = 用户自己拖的框，按 (col×列距, row×行距) 平移到目标卡片。
        两处历史缺陷已修：① 自选模式曾无条件套用大厅偏移，用户拖的框完全不生效；
                          ② 只按行下移、没有列平移，一页 3 列时右边两列全丢。"""
        if self.layout_mode_var.get() != "lobby":
            r = self.rects.get(field)
            if not r:
                return None
            try:
                step_y = int(self.card_step_var.get())
                step_x = int(self.col_step_var.get())
            except Exception:
                step_y = step_x = 0
            dx, dy = col * step_x, row * step_y
            return (r[0] + dx, r[1] + dy, r[2] + dx, r[3] + dy)
        vb = self.field_override.get(field) or LOBBY["fields"].get(field) or self.rects.get(field)
        if not vb:
            return None
        sx = img.size[0] / float(VIEW_W)
        sy = img.size[1] / float(VIEW_H)
        # 同 find_cards：用 round 而不是截断，避免 1px 偏移把淡字读丢
        return (int(round(box[0] + vb[0] * sx)), int(round(box[1] + vb[1] * sy)),
                int(round(box[0] + vb[2] * sx)), int(round(box[1] + vb[3] * sy)))

    def recognize_card(self, img, box, geom, source_tag, ts, row=0, col=0):
        """识别单张卡片：按「相对卡片左上角」的偏移裁各字段，再 OCR + 解析。
        row/col 是该卡在整页网格里的 0 基行列号，自选模式下靠它把基准框平移到本卡。"""
        sc = int(self.scale_var.get())
        rec = {"时间": ts, "来源": source_tag, "列": None, "行": None, "序号": None,
               "卡片状态": CARD_STATE["normal"]}
        filled = 0
        # 「本页不可用」是大厅列表页的属性（该页卡片上就没有评论数这个数字），
        # 不能带到自选模式：自选模式下用户亲手拖了框，就必须按框去读。
        unavail = FIELD_PAGE_UNAVAILABLE if self.layout_mode_var.get() == "lobby" else set()
        for f in FIELDS:
            # 本页不可用字段（如评论数：本页列表卡片上没有这个数字）直接留空
            if f in unavail or not self.has_field_box(f):
                if f in unavail:
                    rec[f + "_留空原因"] = "本页无此字段"
                rec[f] = ""
                rec[f + "_值"] = None
                continue
            rr = self.field_rect(img, f, box, row, col)
            crop = self.crop_safe(img, rr) if rr else None
            if crop is None:
                rec[f] = ""
                rec[f + "_值"] = None
                continue
            # 读字段。热度/评分压在封面彩字上，按 FIELD_PREP 走预处理，且失败会自动放大重试。
            # 大厅网格模式下这两项再加一层专用读法（2026-09-22）：热度走多配方投票（防前导
            # 数字丢失的静默错值），评分在主读失败时换左边界兜底（详见 read_heat / read_score_retry）。
            lobby = self.layout_mode_var.get() == "lobby"
            if lobby and f == "热度":
                txt, v, hdet = read_heat(self.ocr, img, box)
                if v is None:
                    b_txt, b_v = read_field(self.ocr, crop, f, sc)   # 老读法兜底
                    if b_v is not None or b_txt:
                        txt, v = b_txt, b_v
                rec["_heat_read"] = {k: [t for t, _v in vs]
                                     for k, vs in hdet.items() if isinstance(vs, list)}
                rec["_heat_why"] = hdet.get("why", "")
            elif lobby and f == "评分":
                txt, v = read_field(self.ocr, crop, f, sc)
                if v is None:
                    r_txt, r_v, r_det = read_score_retry(self.ocr, img, box)
                    if r_v is not None:
                        txt, v = r_txt, r_v
                        rec["_score_retry"] = "ok"
                    else:
                        rec["_score_retry"] = r_det.get("why", "no_value")
            else:
                txt, v = read_field(self.ocr, crop, f, sc)
            # 展示列只放「解析命中的真值串」：原始 OCR 串常被星标/封面杂字污染
            # （'74.3'、'co4.5'、'73.3万福'），那些是噪声不是识别值；原始串留在隐藏列复核。
            if f in NUMERIC_FIELDS and v is not None:
                _v2, _hit = FIELD_PARSERS.get(f, parse_number)(txt)
                if _hit and _hit != txt:
                    rec["_raw_" + f] = txt
                    txt = _hit
            rec[f] = txt
            if f in NUMERIC_FIELDS:
                rec[f + "_值"] = v
                # 留痕：读到了东西但被判越界放弃的，记下原值便于在日志里核查
                if v is None and txt:
                    _raw, _rv = parse_number(txt)
                    if _rv is not None:
                        rec["_reject_" + f] = _rv
            if txt:
                filled += 1
        rec["_filled"] = filled
        return rec

    def recognize_frame(self, img, source_tag=""):
        """识别一帧：先判页态，再逐卡片识别。返回 (记录列表, 页态, 说明)"""
        if not self.ocr.ready:
            self.log("OCR 引擎未就绪，跳过识别")
            return [], "ocr_missing", "OCR 引擎未就绪"
        state, why = detect_page_state(img)
        if state in ("blank", "invalid"):
            self.log("页态=%s：%s" % (state, why))
            return [], state, why
        boxes = self.card_boxes(img)
        if not boxes:
            self.log("未定位到任何卡片（%s）" % why)
            return [], "no_card", "未定位到卡片"
        geom = self.cur_geom()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        out = []
        skipped = 0        # 真正被丢弃、没进结果的
        marked = 0         # 进了结果但打了「封面未加载」标记的
        for i, c in enumerate(boxes):
            box = c["box"]
            if box[2] > img.size[0] or box[3] > img.size[1]:
                skipped += 1
                continue                      # 卡片被屏幕边缘截断，跳过而不是硬裁
            rec = self.recognize_card(img, box, geom, source_tag, ts,
                                      row=c["row"], col=c.get("col", 0))
            rec["列"] = c["col"] + 1
            rec["行"] = c["row"] + 1
            rec["序号"] = i + 1
            # 卡片状态：封面未加载 → 加载中（仍写入结果，只是打标记，不计入 skipped）
            if c.get("state") == "loading":
                rec["卡片状态"] = CARD_STATE["downloading"]
                marked += 1
                rec["_skip_reason"] = "封面未加载完成"
            # 完全无文字（热度与地图名都空）视为无效卡片，不写入
            if not rec.get("地图名") and rec.get("热度_值") is None:
                skipped += 1
                rec["_skip_reason"] = rec.get("_skip_reason") or "无有效文字"
                continue
            out.append(rec)
        note = ("卡片 %d 个，有效 %d 条，丢弃 %d 个，标「封面未加载」%d 个（%s）"
                % (len(boxes), len(out), skipped, marked, why))
        return out, state, note

    def recognize_current(self, save=False):
        if self.img is None:
            self.log("当前没有图像")
            return
        tag = ""
        if save:
            tag = os.path.join(SHOTS_DIR, "shot_%s.png" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
            self.img.save(tag)
        recs, state, note = self.recognize_frame(self.img, os.path.basename(tag))
        for r in recs:
            self.add_record(r)
        self.log("本帧识别 %d 条｜页态=%s｜%s" % (len(recs), state, note))

    def diagnose_frame(self):
        """整帧诊断：页态 + 定位到的卡片 + 每卡字段命中情况，落 crops/diag_*.png 供核对"""
        if self.img is None:
            self.log("当前没有图像")
            return
        if not self.ocr.ready:
            self.log("OCR 引擎未就绪")
            return
        state, why = detect_page_state(self.img)
        boxes = self.card_boxes(self.img)
        self.log("页态=%s（%s）｜定位卡片 %d 个" % (state, why, len(boxes)))
        # 画框留档
        vis = self.img.copy()
        from PIL import ImageDraw
        d = ImageDraw.Draw(vis)
        for c in boxes:
            color = (255, 80, 80) if c.get("state") == "loading" else (0, 220, 120)
            d.rectangle(list(c["box"]), outline=color, width=2)
            d.text((c["box"][0] + 4, c["box"][1] + 4), "c%d r%d" % (c["col"] + 1, c["row"] + 1),
                   fill=color)
        geom = self.cur_geom()
        for f in FIELDS:
            if boxes and self.has_field_box(f):
                rr = self.field_rect(self.img, f, boxes[0]["box"],
                                     boxes[0]["row"], boxes[0].get("col", 0))
                if rr:
                    d.rectangle(list(rr), outline=(255, 210, 0), width=2)
        p = os.path.join(CROPS_DIR, "diag_%s.png" % datetime.datetime.now().strftime("%H%M%S"))
        vis.save(p)
        self.log("诊断图已存：%s（红框=封面未加载，绿框=正常，黄框=字段区域）" % p)
        recs, _s, note = self.recognize_frame(self.img, "diag")
        for r in recs:
            self.log("  c%s r%s 名='%s' 热度=%s 评分=%s 评论=%s 标签='%s' 按钮='%s' 状态=%s"
                     % (r.get("列"), r.get("行"), r.get("地图名"), r.get("热度"),
                        r.get("评分"), r.get("评论数"), r.get("标签"), r.get("入口按钮"),
                        r.get("卡片状态")))
        self.log("诊断汇总：%s" % note)

    def test_one_card(self):
        """只识别第一张卡片，并把原始裁切图存到 crops/ 便于核对 OCR 效果"""
        if self.img is None:
            self.log("当前没有图像")
            return
        if not self.ocr.ready:
            self.log("OCR 引擎未就绪")
            return
        boxes = self.card_boxes(self.img)
        if not boxes:
            self.log("未定位到卡片")
            return
        geom = self.cur_geom()
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        rec = self.recognize_card(self.img, boxes[0]["box"], geom, "test", ts,
                                  row=boxes[0]["row"], col=boxes[0].get("col", 0))
        for f in FIELDS:
            if not self.has_field_box(f):
                continue
            for ri in range(min(2, len(boxes))):
                rr = self.field_rect(self.img, f, boxes[ri]["box"],
                                     row=boxes[ri]["row"], col=boxes[ri].get("col", 0))
                if rr is None:
                    continue
                crop = self.crop_safe(self.img, rr)
                if crop is None:
                    self.log("%s r%d：区域越界 %s" % (f, ri + 1, rr))
                    continue
                p = os.path.join(CROPS_DIR, "crop_%s_r%d.png" % (f, ri + 1))
                crop.save(p)
                if ri == 0:
                    self.log("%s：OCR='%s' 解析=%s（裁切图 %s）"
                             % (f, rec.get(f), rec.get(f + "_值"), p))
        self.log("卡片状态=%s" % rec.get("卡片状态"))

    # ------------------------------------------------------------ 记录
    def add_record(self, rec):
        if self.dedup_var.get():
            key = str(rec.get("地图名") or "").strip()
        else:
            key = ""
        if not key:
            key = "%s#c%s-r%s" % (rec.get("来源", ""), rec.get("列"), rec.get("行"))
        self.records[key] = rec
        vals = (rec.get("地图名", ""),
                rec.get("热度", ""),
                rec.get("评分", ""),
                rec.get("评论数", ""),
                rec.get("标签", ""),
                rec.get("卡片状态", ""))
        if self.tree.exists(key):
            self.tree.item(key, values=vals)
        else:
            self.tree.insert("", tk.END, iid=key, values=vals)

    def clear_records(self):
        self.records.clear()
        for it in self.tree.get_children():
            self.tree.delete(it)

    # ------------------------------------------------------------ 采样
    def start_sample(self):
        if self.sampling:
            return
        if not self.rects:
            messagebox.showwarning("提示", "请先框选至少「地图名」和「热度」两个字段")
            return
        self.sampling = True
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)
        self.status_var.set("采样中…")
        threading.Thread(target=self.sample_worker, daemon=True).start()

    def stop_sample(self):
        self.sampling = False
        self.btn_stop.config(state=tk.DISABLED)
        self.btn_start.config(state=tk.NORMAL)
        self.status_var.set("已停止")

    def sample_worker(self):
        n = int(self.times_var.get())
        iv = float(self.interval_var.get())
        do_swipe = bool(self.swipe_var.get())
        # 对齐只在「大厅网格」模式下生效：自选框选没有固定网格，谈不上「贴红线」
        do_align = (bool(self.align_var.get())
                    and self.layout_mode_var.get() == "lobby")
        self.adb.path = self.adb_path_var.get()
        need_align = do_align          # 第一帧之前也要对齐（用户可能手动滚过）
        for i in range(n):
            if not self.sampling:
                break
            if need_align:
                drift, rounds, lines = self.align_to_grid()
                for l in lines:
                    self.msgq.put(("log", "对齐｜%s" % l))
                if drift is None:
                    self.msgq.put(("log", "顶行对齐失败，按当前位置继续识别"))
                elif abs(drift) <= max(5, 8):
                    self.msgq.put(("log", "顶行已对齐红线（偏差 %+dpx，%d 轮）" % (drift, rounds)))
                else:
                    # 不能再无条件写「已对齐」：偏差超容差时必须如实报（2026-09-22 用户实测）。
                    self.msgq.put(("log", "⚠ 顶行未对齐红线：偏差 %+dpx（%d 轮）"
                                          "—— 整行仍偏在红线下方，"
                                          "本轮识别结果可能整体错位，建议再点一次「对齐到红线」"
                                   % (drift, rounds)))
                need_align = False
            img, err = self.grab_with_retry(i + 1, n)
            if img is None:
                break
            tag = "shot_%s_%03d.png" % (datetime.datetime.now().strftime("%Y%m%d_%H%M%S"), i + 1)
            path = os.path.join(SHOTS_DIR, tag)
            img.save(path)
            self.msgq.put(("image", img))
            recs, state, note = self.recognize_frame(img, tag)
            self.msgq.put(("records", recs))
            self.msgq.put(("log", "第 %d/%d 次：有效 %d 条，累计 %d 条｜页态=%s｜%s"
                           % (i + 1, n, len(recs), len(self.records), state, note)))
            # 翻页截断：连续两帧列表区几乎一致 → 已滚到底，主动停
            if self.stop_on_end_var.get() and self.same_as_last(img):
                self.msgq.put(("log", "连续两帧内容一致，判定已到列表末尾，停止翻页"))
                break
            if state in ("empty_or_loading",):
                self.msgq.put(("log", "列表区疑似空态/加载中，本次不翻页"))
            elif do_swipe:
                pct = float(self.swipe_pct_var.get())
                ms = int(self.swipe_ms_var.get())
                if self.precise_var.get():
                    # 闭环补齐。对齐模式开启时粗滑目标取 **0.85 页**：闭环本身有
                    # ±12% 误差，目标整一页时实际滚量可能超过两行（2×行距），
                    # 顶行对齐就会跳过一整行卡（丢数据）；少滚 15% 再由对齐补齐，
                    # 落点必然落在「本批第一行还没到、上一行已滚走」的区间里。
                    page = self._page_px(img.size[1])
                    target = int(page * 0.85) if do_align else page
                    got, rounds, lines = self.precise_scroll(target)
                    for l in lines:
                        self.msgq.put(("log", "精确滚动｜%s" % l))
                    if got is None:
                        self.msgq.put(("log", "精确滚动量不出位移，本次按普通上滑处理"))
                        ok, kind, msg = self.adb.swipe_up(img.size[0], img.size[1],
                                                          percent=pct, duration=ms)
                    else:
                        ok, kind, msg = True, "", ""
                        self.msgq.put(("log", "精确滚动：目标 %dpx，%d 轮后累计 %dpx（增益 %.2f）"
                                       % (target, rounds, got, self.swipe_gain or 0.0)))
                else:
                    ok, kind, msg = self.adb.swipe_up(img.size[0], img.size[1],
                                                      percent=pct, duration=ms)
                if ok:
                    # 采样时同样要等滚停：只靠「间隔」兜底的话，间隔调小（如 0.5s）
                    # 下一帧就是在滚动途中截的 —— 一半是上一页、一半是下一页，
                    # 表现为「翻页忽多忽少 / 同一页被截两次」。
                    _f, waited, stopped = wait_scroll_stop(self.adb)
                    self.msgq.put(("log", "已上滑：幅度 %.0f%%（%d px）时长 %dms｜等滚停 %.1fs%s"
                                   % (pct * 100, int(img.size[1] * pct), ms, waited,
                                      "" if stopped else "（⚠ 未停稳，下一帧可能仍在滚动）")))
                    need_align = do_align      # 滑完下一帧前重新对齐
                if not ok:
                    self.msgq.put(("log", "上滑失败（%s）：%s" % (kind, msg)))
                    if kind == "inject_denied":
                        # 注入被 ROM 拒绝时继续跑只会反复截同一页（去重后看起来"没数据"），
                        # 必须停下来并把复选框关掉，而不是静默空转。
                        self.msgq.put(("swipe_off", None))
                        self.msgq.put(("log", "已停止本次采样。替代做法：不勾「自动上滑」，"
                                              "按间隔截屏、你在手机上手动上滑一页。"))
                        break
            if i < n - 1:
                time.sleep(iv)
        self.msgq.put(("sampling_done", None))

    def grab_with_retry(self, idx, total):
        """截屏 + 重试；封面未加载完时按「等待封面加载完」设置轮询等待。"""
        retry = int(self.retry_var.get())
        wait_to = float(self.wait_to_var.get())
        wait_cover = bool(self.wait_cover_var.get())
        last_err = ""
        for attempt in range(retry + 1):
            if not self.sampling:
                return None, "已停止"
            img, err = self.adb.screencap()
            if img is not None:
                if is_blank(img):
                    self.msgq.put(("log", "第 %d/%d 次为黑屏，停止：%s"
                                   % (idx, total, explain_blank(self.adb))))
                    return None, "黑屏"
                if wait_cover:
                    img = self.wait_cover_loaded(img, wait_to)
                return img, ""
            last_err = err
            if attempt < retry:
                self.msgq.put(("log", "第 %d/%d 次截屏失败（%s），%ds 后重试 %d/%d"
                               % (idx, total, err, 1, attempt + 1, retry)))
                time.sleep(1.0)
        self.msgq.put(("log", "第 %d/%d 次截屏重试耗尽：%s" % (idx, total, last_err)))
        return None, last_err

    def wait_cover_loaded(self, img, timeout):
        """封面未加载完成时轮询等待：以「未加载卡片数」是否下降作为加载完成的判据。
        超时后原样返回最后一次截屏，并在日志说明（不静默假装加载完成）。"""
        t0 = time.time()
        best = img
        while time.time() - t0 < timeout and self.sampling:
            boxes = self.card_boxes(best)
            pending = [b for b in boxes if b.get("state") == "loading"]
            if not pending:
                return best
            time.sleep(0.4)
            nxt, err = self.adb.screencap()
            if nxt is None:
                self.msgq.put(("log", "等待封面时截屏失败：%s（沿用上一帧）" % err))
                return best
            prev_pending = len(pending)
            best = nxt
            now_pending = len([b for b in self.card_boxes(best) if b.get("state") == "loading"])
            if now_pending < prev_pending:
                self.msgq.put(("log", "封面加载中：%d → %d 张未加载" % (prev_pending, now_pending)))
        left = len([b for b in self.card_boxes(best) if b.get("state") == "loading"])
        if left:
            self.msgq.put(("log", "等待封面超时（%.1fs），仍有 %d 张封面未加载，按当前帧识别" % (timeout, left)))
        return best

    def same_as_last(self, img):
        """列表区感知哈希比对，判断是否已滚到底（同一帧重复出现）"""
        import numpy as np
        try:
            sx = img.size[0] / float(VIEW_W)
            sy = img.size[1] / float(VIEW_H)
            a = LOBBY["list_area"]
            box = (int(a[0] * sx), int(a[1] * sy), int(a[2] * sx), int(a[3] * sy))
            small = img.crop(box).convert("L").resize((16, 8))
            arr = np.asarray(small, dtype="float32")
            sig = (arr > arr.mean()).flatten()
            if self._last_sig is not None:
                diff = float((sig != self._last_sig).sum()) / float(len(sig))
                self._last_sig = sig
                return diff < 0.04        # 差异 <4% 视为同一屏
            self._last_sig = sig
        except Exception as e:
            self.msgq.put(("log", "末页检测异常（忽略）：%s" % e))
        return False

    def batch_files(self, files):
        for p in files:
            try:
                img = Image.open(p).convert("RGB")
            except Exception as e:
                self.msgq.put(("log", "读取失败 %s：%s" % (p, e)))
                continue
            recs, state, note = self.recognize_frame(img, os.path.basename(p))
            self.msgq.put(("records", recs))
            self.msgq.put(("log", "%s：有效 %d 条｜页态=%s｜%s" % (os.path.basename(p), len(recs), state, note)))
        self.msgq.put(("sampling_done", None))

    COLS = EXPORT_COLS          # 兼容旧引用（界面/其它代码可能还在用 self.COLS）

    def _stamp(self, ext):
        return os.path.join(OUT_DIR, "oasis_maps_%s.%s"
                            % (datetime.datetime.now().strftime("%Y%m%d_%H%M%S"), ext))

    def _do_export(self, ext, writer):
        """统一的导出外壳：空表提示 / 异常可见 / 成功给完整路径。

        异常必须在这里接住 —— 按钮回调里抛出的异常只会打到 stderr，而 GUI 程序没有控制台，
        用户看到的就是「点了没反应」（2026-09-20「结果无法导出为表格」的成因之一：
        CSV 正被 Excel 打开时再次导出会 PermissionError，异常不可见）。
        """
        if not self.records:
            self.log("没有可导出的数据：结果表是空的。先采样一次，或导入图片后点「整帧诊断」/「试识别一张卡」。")
            messagebox.showinfo("导出", "结果表是空的，还没有可导出的数据。")
            return
        p = self._stamp(ext)
        try:
            n = writer(list(self.records.values()), p)
        except PermissionError:
            self.log("导出失败：目标文件被占用（%s）—— 先在 Excel / WPS 里关闭同名文件再导出。" % p)
            messagebox.showerror("导出失败", "文件已被占用，请先关闭已打开的：\n%s" % os.path.basename(p))
            return
        except ImportError as e:
            cmd = (".venv\\Scripts\\python.exe -m pip install openpyxl "
                   "-i https://pypi.tuna.tsinghua.edu.cn/simple")
            self.log("导出失败：缺少依赖（%s）。安装命令：%s" % (e, cmd))
            messagebox.showerror("导出失败", "缺少 openpyxl，无法写 Excel。\n在工具目录下执行：\n%s" % cmd)
            return
        except Exception as e:
            self.log("导出失败（%s）：%s" % (type(e).__name__, e))
            messagebox.showerror("导出失败", "%s: %s" % (type(e).__name__, e))
            return
        self.log("已导出：%s（%d 条）" % (p, n))
        self.status_var.set("已导出 %d 条 → %s" % (n, p))
        messagebox.showinfo("导出完成", "%s\n共 %d 条" % (p, n))

    def export_xlsx(self):
        self._do_export("xlsx", write_xlsx)

    def export_csv(self):
        self._do_export("csv", write_csv)

    def export_json(self):
        self._do_export("json", write_json)

    def open_out_dir(self):
        """打开输出目录（Windows 资源管理器）—— 用户常常不知道文件落在哪。"""
        try:
            os.startfile(OUT_DIR)
            self.log("输出目录：%s" % OUT_DIR)
        except Exception as e:
            self.log("打不开输出目录（%s）：%s\n目录路径：%s" % (type(e).__name__, e, OUT_DIR))


# ---------------------------------------------------------------- 导出
# 写文件的函数放在模块级：不弹窗、不碰控件，自检才能直接断言（按钮方法只做外壳）。


def export_rows(records):
    """按导出列顺序整理成行，缺的字段补空串（纯函数，便于单测）。"""
    return [{c: r.get(c, "") for c in EXPORT_COLS} for r in records]


def write_csv(records, path):
    """写 CSV。用 utf-8-sig —— Excel 双击直接打开且中文不乱码。返回写入行数。"""
    rows = export_rows(records)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EXPORT_COLS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return len(rows)


def write_json(records, path):
    """写 JSON（UTF-8，中文不转义）。返回写入行数。"""
    rows = export_rows(records)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    return len(rows)


def write_xlsx(records, path):
    """写 Excel 工作簿（.xlsx）。返回写入行数。

    缺 openpyxl 时抛 ImportError，由调用方翻译成可执行的安装命令 —— 不在函数里静默降级，
    否则用户会拿到一个「点了没反应」的按钮。
    """
    from openpyxl import Workbook          # 依赖隔离在 .venv 里，不在模块顶层 import
    from openpyxl.styles import Font
    rows = export_rows(records)
    wb = Workbook()
    ws = wb.active
    ws.title = "地图数据"
    ws.append(EXPORT_COLS)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in rows:
        line = []
        for c in EXPORT_COLS:
            v = r.get(c, "")
            if c in EXPORT_NUM_COLS:
                # 数值列写数字：空字符串写 None，避免 Excel 里出现 0
                line.append(v if isinstance(v, (int, float)) else None)
            else:
                line.append("" if v is None else v)
        ws.append(line)
    ws.freeze_panes = "A2"                 # 冻结表头，滚动时不丢列名
    for i, c in enumerate(EXPORT_COLS, start=1):
        w = max(len(str(c)), *(len(str(r.get(c, ""))) for r in rows)) if rows else len(str(c))
        ws.column_dimensions[ws.cell(row=1, column=i).column_letter].width = min(38, max(8, w + 2))
    wb.save(path)
    return len(rows)



def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
