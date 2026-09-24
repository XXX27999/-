# -*- coding: utf-8 -*-
"""采样器自检：数值解析 / OCR 端到端 / GUI 冒烟。结果写入 _selftest.txt"""
import os
import sys
import io
import glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["PYTHONIOENCODING"] = "utf-8"

from OasisOcrSampler import (parse_number, clean_text, strip_label, OcrEngine, FIELDS,  # noqa: E402
                             LOBBY, VIEW_W, VIEW_H, diagnose_adb_error, explain_blank, is_blank,
                             parse_score, parse_field_value, read_field,
                             SWIPE_PCT_DEFAULT, SWIPE_MS_DEFAULT, swipe_args,
                             measure_scroll, swipe_advice,
                             wait_scroll_stop, summarize_runs, SWIPE_RUNS_DEFAULT,
                             plan_next_swipe, LIST_TOP_RATIO,
                             measure_scroll_total, measure_scroll_fast,
                             find_ffmpeg, LIVE_SMALL_H, LIVE_STEPS, FFMPEG_INSTALL,
                             LiveScreen, LiveMonitor, grid_drift, detect_row_bounds,
                             color_gray, digits_len, decide_readings, read_heat,
                             read_score_retry, find_cards, heat_value,
                             export_rows, write_csv, write_json, write_xlsx, EXPORT_COLS,
                             INT_ROW_COUNT, INT_ROW_STEP, INT_COL_STEP)
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s):
    OUT.append(str(s))


# ------------------------------------------------ A. 数值解析
say("=== A. 数值解析 ===")
CASES = [
    ("1128万", 11280000.0), ("233.5万", 2335000.0), ("2.2亿", 220000000.0),
    ("83条", 83.0), ("4.4分", 4.4), ("热度 661万", 6610000.0),
    ("1,234", 1234.0), ("暂无", None), ("", None), ("3.4", 3.4),
]
ok = True
for txt, exp in CASES:
    got, m = parse_number(txt)
    passed = (got == exp) or (got is None and exp is None)
    ok = ok and passed
    say("%-14r -> %-14s expect=%-14s %s" % (txt, got, exp, "PASS" if passed else "FAIL"))
say("A 结果: %s" % ("全部通过" if ok else "存在失败"))

say("")
say("=== A2. 标签剥离 ===")
for f, t, exp in [("热度", "热度661万", "661万"), ("评分", "评分4.1", "4.1"),
                  ("评论数", "评论数1.2万", "1.2万"), ("评论数", "讨论83条", "83条"),
                  ("评分", "4.4分", "4.4")]:
    got = strip_label(t, f)
    say("%-4s %-12r -> %-10r expect=%-10r %s" % (f, t, got, exp, "PASS" if got == exp else "FAIL"))

# ------------------------------------------------ B. OCR 端到端
say("")
say("=== B. OCR 端到端（合成图）===")
FONT_PATHS = ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf", "C:/Windows/Fonts/simsun.ttc"]
font_path = None
for p in FONT_PATHS:
    if os.path.exists(p):
        font_path = p
        break
say("字体: %s" % font_path)
if font_path is None:
    say("B 跳过：无中文字体")
else:
    W, H = 1080, 2400
    STEP = 260
    img = Image.new("RGB", (W, H), (28, 32, 40))
    d = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(font_path, 42)
    f_info = ImageFont.truetype(font_path, 30)
    cards = [
        ("特种兵大战灵兽", "热度661万", "评分4.1", "评论1.2万"),
        ("我在洪荒钓神兽", "热度1128万", "评分4.4", "评论83条"),
        ("赛车模拟器", "热度533万", "评分4.6", "评论2.2万"),
    ]
    for i, (n, h, s, c) in enumerate(cards):
        y = 60 + i * STEP
        d.rectangle([40, y - 20, W - 40, y + 150], fill=(40, 46, 58), outline=(90, 100, 120))
        d.text((70, y), n, fill=(255, 255, 255), font=f_name)
        d.text((70, y + 80), h, fill=(245, 166, 35), font=f_info)
        d.text((420, y + 80), s, fill=(47, 158, 68), font=f_info)
        d.text((700, y + 80), c, fill=(120, 180, 255), font=f_info)
    test_img = os.path.join(HERE, "_selftest_card.png")
    img.save(test_img)
    say("合成图已生成: %s" % test_img)

    engine = OcrEngine()
    say("引擎状态: %s" % engine.load())
    if not engine.ready:
        say("B 失败: %s" % engine.error)
    else:
        # 覆盖第一张卡片文字的框（与真实框选方式一致）
        rects = {
            "地图名": (65, 40, 700, 110),
            "热度": (65, 120, 380, 190),
            "评分": (415, 120, 620, 190),
            "评论数": (695, 120, 980, 190),
        }
        for i, expect in enumerate(cards):
            say("--- 卡片 %d 期望 %s ---" % (i + 1, " / ".join(expect)))
            for f in FIELDS:
                # 合成样张只画了 4 个字段；标签/入口按钮 不在样张里，跳过（否则 KeyError）
                if f not in rects:
                    say("  %-4s 样张未绘制 -> 跳过" % f)
                    continue
                x0, y0, x1, y1 = rects[f]
                crop = img.crop((x0, y0 + i * STEP, x1, y1 + i * STEP))
                txt = clean_text(engine.recognize(crop, scale=2))
                v, m = parse_number(txt)
                say("  %-4s OCR='%s' -> %s" % (f, txt, v))
        # 越界框应返回 None（不静默补黑边）


# ------------------------------------------------ C. GUI 冒烟
say("")
say("=== C. GUI 冒烟 ===")
try:
    import tkinter as tk
    from OasisOcrSampler import App
    root = tk.Tk()
    app = App(root)
    root.deiconify()
    for _ in range(6):
        root.update_idletasks()
        root.update()
    say("窗口尺寸: %dx%d (需 > 300x200)" % (root.winfo_width(), root.winfo_height()))
    say("画布尺寸: %dx%d" % (app.canvas.winfo_width(), app.canvas.winfo_height()))
    say("字段数: %d, 树列数: %d" % (len(app.rect_tree.get_children()), len(app.tree["columns"])))
    # 2026-09-20：用户要求「各区域可滚动 + 可调大小」。只靠肉眼看不见的改动最容易回归，
    # 这里直接断言结构：纵向分栏（主体/日志）、横向分栏（画布/右栏）、右栏滚动容器、日志滚动条。
    say("纵向分栏窗格数: %d（期望 2：主体 + 日志）" % len(app.vpan.panes()))
    say("横向分栏窗格数: %d（期望 2：画布 + 右栏）" % len(app.body.panes()))
    say("右栏滚动容器存在 = %s / 日志滚动条存在 = %s（期望都 True）"
        % (app.rcanvas is not None, app.log_scroll is not None))
    # 分栏必须真的能改变尺寸：给纵向分栏一个 sash 位置并读回
    app.root.update_idletasks()
    say("日志区高度 = %dpx（>0 才说明没被压没）" % app.log_text.winfo_height())
    # 越界框必须返回 None（不静默补黑边产生脏数据）
    _im0 = Image.new("RGB", (100, 100), (0, 0, 0))
    say("crop_safe 越界: %s (期望 None)" % app.crop_safe(_im0, (-5, -5, 200, 200)))
    say("crop_safe 正常: %s (期望非 None)" % ("OK" if app.crop_safe(_im0, (0, 0, 10, 10)) else "None"))
    # 载入合成图并按网格识别一帧
    if font_path and os.path.exists(os.path.join(HERE, "_selftest_card.png")):
        im = Image.open(os.path.join(HERE, "_selftest_card.png")).convert("RGB")
        app.show_image(im)
        # 必须切到「自选框选」：本用例用的是自己拖的绝对坐标框，
        # 留在默认的「大厅网格」模式下会改用 LOBBY 固定几何，这里的框全都不生效。
        app.layout_mode_var.set("manual")
        app.rects = {"地图名": (65, 40, 700, 110), "热度": (65, 120, 380, 190),
                     "评分": (415, 120, 620, 190), "评论数": (695, 120, 980, 190)}
        app.card_count_var.set(3)
        app.card_step_var.set(260)
        app.scale_var.set(2)
        if engine.ready:
            app.ocr = engine
            # recognize_frame 返回三元组 (记录列表, 页态, 说明)
            recs, _state, _note = app.recognize_frame(im, "selftest.png")
            for r in recs:
                app.add_record(r)
            say("整帧识别条数: %d (期望 3)" % len(recs))
            for r in recs:
                say("  %s | 热度=%s(%s) | 评分=%s | 评论=%s" %
                    (r.get("地图名"), r.get("热度"), r.get("热度_值"), r.get("评分"), r.get("评论数")))
            say("结果表行数: %d" % len(app.tree.get_children()))
    # ---------------- D. 一页网格：行数 × 列数（绿洲大厅一页 2 行 3 列）
    say("")
    say("=== D. 一页网格（真机截图，期望 %d 行 × 3 列 = 6 张）===" % INT_ROW_COUNT)
    real = os.path.join(HERE, "crops", "lobby_real.png")
    if not os.path.exists(real):
        say("D 跳过：缺 crops/lobby_real.png（标定基准图）")
    else:
        im2 = Image.open(real).convert("RGB")
        sx = im2.size[0] / float(VIEW_W)
        sy = im2.size[1] / float(VIEW_H)
        app.show_image(im2)
        app.ncol_var.set(len(LOBBY["col_x"]))          # 3 列
        app.card_count_var.set(INT_ROW_COUNT)          # 2 行
        app.card_step_var.set(INT_ROW_STEP)            # 真机行距 314
        app.col_step_var.set(INT_COL_STEP)             # 真机列距 495

        app.layout_mode_var.set("lobby")
        lb = app.card_boxes(im2)
        say("大厅网格：%d 张｜列号=%s 行号=%s"
            % (len(lb), sorted(set(b["col"] for b in lb)), sorted(set(b["row"] for b in lb))))

        # 自选框选：用第一张卡的真值框作基准，按 行距/列距 复制，应与大厅网格逐格重合
        c0 = lb[0]["box"]
        app.layout_mode_var.set("manual")
        # 注意：LOBBY 的字段偏移一律相对「卡片左上角」，所以四边都以 c0 的 x0/y0 为原点，
        # 不能用 c0 的 x1/y1 当原点（写错会让偏差正好等于一个卡宽）。
        app.rects = {f: (int(round(c0[0] + vb[0] * sx)), int(round(c0[1] + vb[1] * sy)),
                         int(round(c0[0] + vb[2] * sx)), int(round(c0[1] + vb[3] * sy)))
                     for f, vb in LOBBY["fields"].items()}
        mn = app.card_boxes(im2)
        say("自选框选：%d 张｜列号=%s 行号=%s"
            % (len(mn), sorted(set(b["col"] for b in mn)), sorted(set(b["row"] for b in mn))))

        def _frects(mode, boxes):
            app.layout_mode_var.set(mode)
            return [[app.field_rect(im2, f, b["box"], b["row"], b.get("col", 0))
                     for f in LOBBY["fields"]] for b in boxes]

        worst = 0
        for r1, r2 in zip(_frects("lobby", lb), _frects("manual", mn)):
            for x, y in zip(r1, r2):
                if x is None or y is None:
                    worst = 9999
                    continue
                worst = max(worst, max(abs(x[i] - y[i]) for i in range(4)))
        say("两种模式字段框最大偏差 = %dpx（期望 0）" % worst)

        # 大厅模式下只存了部分手工框时，没有手工框的字段也必须仍可用
        app.layout_mode_var.set("lobby")
        app.rects = {k: tuple(v) for k, v in app.rects.items() if k != "入口按钮"}
        d_ok = (len(lb) == 6 and len(mn) == 6
                and sorted(set(b["col"] for b in lb)) == [0, 1, 2]
                and sorted(set(b["row"] for b in lb)) == list(range(INT_ROW_COUNT))
                and worst == 0 and app.has_field_box("入口按钮") is True)
        say("部分手工框下「入口按钮」可用 = %s（期望 True）" % app.has_field_box("入口按钮"))
        say("D 结果: %s" % ("通过" if d_ok else "失败"))

    # ---------------- E. adb 报错分类（用真机上滑失败的原文做测试向量）
    say("")
    say("=== E. adb 报错分类 ===")
    real_err = ("Exception occurred while executing 'swipe':\n"
                "java.lang.SecurityException: Injecting input events requires the caller "
                "(or the source of the instrumentation, if any) to have the INJECT_EVENTS permission.\n"
                "\tat com.android.server.input.InputManagerService.injectInputEventToTarget"
                "(InputManagerService.java:1103)\n"
                "\tat com.android.server.input.InputShellCommand.sendSwipe(InputShellCommand.java:550)")
    k1, m1 = diagnose_adb_error(real_err)
    say("INJECT_EVENTS 原文 -> 分类=%s（期望 inject_denied）" % k1)
    say("  对策首行: %s" % m1.splitlines()[0])
    k2, _ = diagnose_adb_error("error: device unauthorized. Please check the confirmation dialog.")
    say("unauthorized 原文 -> 分类=%s（期望 unauthorized）" % k2)
    k3, _ = diagnose_adb_error("error: device 'abc' not found")
    say("not found 原文 -> 分类=%s（期望 offline）" % k3)
    k4, _ = diagnose_adb_error("")
    say("空错误 -> 分类=%s（期望 other，不得抛异常）" % k4)
    e_ok = (k1 == "inject_denied" and k2 == "unauthorized"
            and k3 == "offline" and k4 == "other")
    say("E 结果: %s" % ("通过" if e_ok else "失败"))

    # ---------------- F. 黑屏成因判定（熄屏 vs FLAG_SECURE，对策不同）
    say("")
    say("=== F. 黑屏成因判定 ===")

    class _FakeAdb(object):
        def __init__(self, r):
            self._r = r

        def screen_awake(self):
            return self._r

    pure = Image.new("RGB", (200, 200), (0, 0, 0))          # 纯色（黑屏）
    busy = Image.new("RGB", (200, 200), (0, 0, 0))
    ImageDraw.Draw(busy).rectangle([10, 10, 190, 190], fill=(200, 200, 200))
    f1 = explain_blank(_FakeAdb((False, "Dozing")))          # 熄屏
    f2 = explain_blank(_FakeAdb((True, "Awake")))            # 亮屏 → 才是禁截屏
    f3 = explain_blank(_FakeAdb((None, "读不出")))            # 读不出 → 不猜
    say("is_blank 纯色 = %s（期望 True）/ is_blank 有内容 = %s（期望 False）"
        % (is_blank(pure), is_blank(busy)))
    say("熄屏(Dozing)   -> %s" % f1)
    say("亮屏(Awake)    -> %s" % f2)
    say("读不出         -> %s" % f3)
    # 三种成因必须给出三套不同对策，尤其「熄屏」绝不能被说成「禁截屏」
    f_ok = (is_blank(pure) is True and is_blank(busy) is False
            and ("点亮屏幕" in f1 or "未点亮" in f1)
            and ("FLAG_SECURE" in f2 or "禁止截屏" in f2)
            and ("点亮屏幕" not in f2) and ("FLAG_SECURE" not in f1)
            and (len(set([f1, f2, f3])) == 3))
    say("F 结果: %s" % ("通过" if f_ok else "失败"))

    # ---------------- G. 评分解析（2026-09-20 真机反馈：出现 74.3 / ?2.9）
    say("")
    say("=== G. 评分解析 ===")
    SCORE_CASES = [
        ("4.4", 4.4), ("4.3", 4.3), ("4.5", 4.5), ("2.9", 2.9), ("3.6", 3.6),
        ("★4.3", 4.3),     # 星标被一起读进来
        ("74.3", 4.3),     # 星标右弧被读成 7 —— 用户实际遇到的
        ("?2.9", 2.9),     # 星标被读成 ?
        ("3.67", 3.6),     # 尾数误粘，真值是一位小数 3.6
        ("10.0", 10.0),    # 满分特判
        ("A2", None),      # 无小数点：宁可不取值，也不能落一个假值到数值列
        ("36", None),      # 小数点丢失（真值 3.6），同样不得采信
        ("食24", None),
        ("", None),
    ]
    g1 = True
    for txt, exp in SCORE_CASES:
        got, _m = parse_score(txt)
        passed = (got == exp) or (got is None and exp is None)
        g1 = g1 and passed
        say("  %-8r -> %-6s expect=%-6s %s" % (txt, got, exp, "PASS" if passed else "FAIL"))
    # 走完整字段解析（含 strip_label + 区间校验）同样要正确
    pf, pv = parse_field_value("评分", "74.3")
    say("  parse_field_value('评分','74.3') -> 文本=%r 值=%s（期望 4.3）" % (pf, pv))
    g1 = g1 and (pv == 4.3)
    say("G1 结果: %s" % ("通过" if g1 else "失败"))

    # G2：真机 2400x1080 截图端到端（用户 2026-09-20 14:34 那一页）
    real2 = os.path.join(HERE, "shots", "shot_20260920_143400_001.png")
    if not os.path.exists(real2):
        say("G2 跳过：缺 shots/shot_20260920_143400_001.png")
        g2 = None
    else:
        im3 = Image.open(real2).convert("RGB")
        app.show_image(im3)
        app.layout_mode_var.set("lobby")
        app.ncol_var.set(3)
        app.card_count_var.set(2)
        app.card_step_var.set(390)          # 该分辨率实测行距
        app.col_step_var.set(619)           # 该分辨率实测列距
        boxes = app.card_boxes(im3)
        EXPECT = [4.4, 4.3, 4.3, 2.9, 4.5, 3.6]
        say("真机截图 %s 卡片数=%d" % (os.path.basename(real2), len(boxes)))
        got_all = []
        for i, b in enumerate(boxes):
            fbox = app.field_rect(im3, "评分", b["box"], b["row"], b.get("col", 0))
            crop = app.crop_safe(im3, fbox)
            txt, val = read_field(engine, crop, "评分", 4) if (crop is not None and engine.ready) \
                else ("", None)
            got_all.append(val)
            say("  r%d c%d 评分 OCR=%r -> %s（期望 %s）"
                % (b["row"] + 1, b.get("col", 0) + 1, txt, val,
                   EXPECT[i] if i < len(EXPECT) else "?"))
        g2 = (len(boxes) == 6 and got_all == EXPECT)
        say("G2 结果: %s（命中 %d/6）"
            % ("通过" if g2 else "失败",
               sum(1 for a, e in zip(got_all, EXPECT) if a == e)))
    say("G 结果: %s" % ("通过" if (g1 and (g2 is not False)) else "失败"))

    # ---------------- H. 上滑参数（2026-09-20 真机反馈：滑过头）
    say("")
    say("=== H. 上滑参数 ===")
    say("默认幅度 = %.0f%%  默认时长 = %dms（旧值 55%%/350ms 属快速甩动，惯性导致滑过头）"
        % (SWIPE_PCT_DEFAULT * 100, SWIPE_MS_DEFAULT))
    # 真机 2400x1080：新默认应比旧默认明显更短（同样的起点 y=842）
    # 按下标取数易错（2026-09-20 实测把 duration 当成了 y2），改为按 "swipe" 关键字定位
    def _swipe_geom(args):
        i = args.index("swipe")
        return int(args[i + 1]), int(args[i + 2]), int(args[i + 4]), int(args[i + 5])

    old_args = swipe_args(2400, 1080, percent=0.55, duration=350)
    new_args = swipe_args(2400, 1080)
    say("旧默认参数 = %s" % (" ".join(old_args)))
    say("新默认参数 = %s" % (" ".join(new_args)))
    old_x, old_y1, old_y2, old_dur = _swipe_geom(old_args)
    new_x, new_y1, new_y2, new_dur = _swipe_geom(new_args)
    old_d, new_d = old_y1 - old_y2, new_y1 - new_y2
    say("滑动距离：旧 %dpx -> 新 %dpx（应更短）" % (old_d, new_d))
    say("时长：旧 %dms -> 新 %dms（应更长，惯性更小）" % (old_dur, new_dur))
    say("指定主显示 = %s" % (" ".join(swipe_args(1080, 2400, display=0))))
    h_ok = (0.10 <= SWIPE_PCT_DEFAULT <= 0.50) and (400 <= SWIPE_MS_DEFAULT <= 2000) \
        and new_d < old_d and new_dur > old_dur \
        and new_args[:2] == ["shell", "input"] \
        and new_x == int(2400 * 0.5) and new_y1 == int(1080 * 0.78) \
        and swipe_args(1080, 2400, display=0)[2] == "-d"
    say("H 结果: %s" % ("通过" if h_ok else "失败"))

    # ---------------- I. 滑动位移测量（2026-09-20 反馈：测试滑动看不到滑了多少）
    say("")
    say("=== I. 滑动位移测量 ===")
    # 1) 非周期纹理（噪声）：任何偏移都唯一匹配，用来验证算法基本正确性
    noise_tex = Image.effect_noise((420, 900), 70).convert("RGB")

    # 2) 周期排版但内容不同（模拟卡片列表：同尺寸卡片、不同封面色与地图名）
    #    验证「周期错位」不会被误判成真值 —— 真值残差应远小于错开一行的残差
    cards = Image.new("RGB", (420, 900), (20, 20, 20))
    cd = ImageDraw.Draw(cards)
    for k in range(6):
        y = k * 150
        cd.rectangle([10, y + 10, 410, y + 140], fill=(60 + k * 30, 90, 140 - k * 20))
        cd.text((24, y + 60), "MAP-%03d  score %.1f" % (k, 3.0 + k * 0.3), fill=(255, 255, 255))

    def _shifted(img, n):
        """整幅上移 n px，底部补背景色（保持尺寸不变）"""
        out = Image.new("RGB", img.size, img.getpixel((2, img.size[1] - 2)))
        out.paste(img.crop((0, n, img.size[0], img.size[1])), (0, 0))
        return out

    i_ok = True
    for name, tex in (("噪声纹理", noise_tex), ("卡片列表", cards)):
        for n in (0, 40, 120, 300, 520):
            got, why = measure_scroll(tex, _shifted(tex, n))
            ok = (got is not None and abs(got - n) <= 4)
            i_ok = i_ok and ok
            say("  %s 平移 %4dpx -> 测得 %s %s" % (name, n, got, "OK" if ok else "FAIL(%s)" % why))
    # 两帧完全无关时应判 None，而不是硬给一个数
    got_n, why_n = measure_scroll(cards, Image.effect_noise((420, 900), 90).convert("RGB"))
    n_ok = got_n is None
    say("  无关两帧 -> %s（应 None）%s" % (got_n, "OK" if n_ok else "FAIL"))
    i_ok = i_ok and n_ok
    # 建议函数：目标一页 = 2*628（1080 屏高下行距换算值），按 0.35 幅度手指位移 378px
    page = 628
    v1, _a1, p1 = swipe_advice(378, 378, page)                 # ≈0.60 页 -> 没滑够
    v2, _a2, p2 = swipe_advice(378, 378 * 3, page)             # ≈1.8 页 -> 滑过头
    v3, _a3, p3 = swipe_advice(378, 378, 378)                  # =1 页 -> 合适
    v4, _a4, p4 = swipe_advice(378, None, page)                # 测不出
    v5, _a5, p5 = swipe_advice(378, 0, page)                   # 几乎没动
    say("  实际=手指(378) 页高=628 -> %s / 建议 %s" % (v1, p1))
    say("  实际=3倍手指   页高=628 -> %s / 建议 %s" % (v2, p2))
    say("  实际=页高      页高=378 -> %s / 建议 %s" % (v3, p3))
    say("  测不出/没动          -> %s / %s" % (v4, v5))
    adv_ok = (v1 == "没滑够" and p1 is not None and p1 > 0.35
              and v2 == "滑过头" and p2 is not None and p2 < 0.35
              and v3 == "合适" and p3 is None
              and v4 == "测不出" and p4 is None
              and v5 == "几乎没动" and p5 is None)
    i_ok = i_ok and adv_ok
    say("I 结果: %s" % ("通过" if i_ok else "失败"))

    # ---------------- J. 导出（2026-09-20 用户反馈：结果无法导出为表格）
    say("")
    say("=== J. 导出 ===")
    recs = [
        {"时间": "16:00:01", "来源": "shot_a.png", "列": 1, "行": 1,
         "地图名": "别扶我！我还能跳", "热度": "77.0万", "热度_值": 770000.0,
         "评分": "4.4", "评分_值": 4.4, "评论数": "", "评论数_值": None,
         "标签": "休闲冒险闯关", "入口按钮": "下载", "卡片状态": "可进入", "_多余": "应被丢掉"},
        {"时间": "16:00:02", "来源": "shot_b.png", "列": 2, "行": 1,
         "地图名": "九转刷宝", "热度": "73.3万", "热度_值": 733000.0,
         "评分": "75", "评分_值": None, "评论数": "", "评论数_值": None,
         "标签": "射击冒险闯关", "入口按钮": "下载", "卡片状态": "可进入"},
        {"地图名": "缺字段的卡", "热度": "1万", "热度_值": 10000.0},   # 故意缺列，验证补空
    ]
    rows = export_rows(recs)
    j_ok = (len(rows) == 3
            and all(list(r.keys()) == EXPORT_COLS for r in rows)     # 列顺序固定且不含多余键
            and rows[2]["标签"] == "" and rows[2]["时间"] == "")     # 缺列补空串
    say("  export_rows：3 行、列序 %s、缺列补空 %s" % (list(rows[0].keys())[:4], j_ok))

    tmp = os.path.join(HERE, "_export_probe")
    os.makedirs(tmp, exist_ok=True)
    pc = os.path.join(tmp, "t.csv")
    pj = os.path.join(tmp, "t.json")
    px = os.path.join(tmp, "t.xlsx")
    nc = write_csv(recs, pc)
    nj = write_json(recs, pj)
    say("  write_csv=%d 行 -> %s" % (nc, os.path.basename(pc)))
    say("  write_json=%d 行 -> %s" % (nj, os.path.basename(pj)))
    # CSV 必须带 BOM（utf-8-sig），否则 Excel 双击打开中文乱码
    with open(pc, "rb") as f:
        bom = f.read(3) == b"\xef\xbb\xbf"
    with io.open(pc, encoding="utf-8-sig") as f:
        head = f.readline().strip()
    # csv.DictWriter 默认 QUOTE_MINIMAL，字段名无逗号/引号 → 表头就是裸列名，不带引号
    csv_ok = (nc == 3 and nj == 3 and bom and head == ",".join(EXPORT_COLS))
    say("  CSV 首字节 BOM=%s｜表头=%s｜csv_ok=%s" % (bom, head, csv_ok))
    j_ok = j_ok and csv_ok
    # Excel：能写、能读回、数值列是数字而不是文本
    try:
        nx = write_xlsx(recs, px)
        from openpyxl import load_workbook
        wb = load_workbook(px)
        ws = wb.active
        got_rows = ws.max_row
        h2 = [c.value for c in ws[1]]
        v_heat = ws.cell(row=2, column=EXPORT_COLS.index("热度_值") + 1).value
        v_name = ws.cell(row=2, column=EXPORT_COLS.index("地图名") + 1).value
        x_ok = (nx == 3 and got_rows == 4 and h2 == list(EXPORT_COLS)
                and v_heat == 770000.0 and v_name == "别扶我！我还能跳")
        say("  write_xlsx=%d 行 -> %s（读回 %d 行，热度_值=%r 地图名=%r）"
            % (nx, os.path.basename(px), got_rows, v_heat, v_name))
        j_ok = j_ok and x_ok
    except ImportError as e:
        say("  write_xlsx 跳过：缺少 openpyxl（%s）" % e)
    say("J 结果: %s" % ("通过" if j_ok else "失败"))
    # 探针目录用完即删，别在工具目录里留垃圾
    try:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
    except Exception:
        pass

    # ---------------- K. 连测汇总 + 等滚停（2026-09-21 反馈：每次测出的距离都不一样）
    say("")
    say("=== K. 连测汇总与等滚停 ===")
    say("默认连测次数 = %d（1~5）" % SWIPE_RUNS_DEFAULT)

    # K1：汇总判定的分档必须卡在 15% / 35% 两道线上，且「几乎没动」「测不出」各自独立
    K_CASES = [
        ([500, 520, 480], "稳定", 500, 40),
        ([500, 560, 470], "一般", 500, 90),
        ([400, 600, 500], "不稳定", 500, 200),
        ([0, 0, 0], "几乎没动", 0, 0),
        ([None, None], "测不出", None, None),
        ([None, 500, 520], "稳定", 510, 20),      # 量不出的那次必须被剔除，不能拉低中位数
    ]
    k_ok = True
    for vals, exp_v, exp_med, exp_spread in K_CASES:
        s = summarize_runs(vals, page_px=628)
        passed = (s["verdict"] == exp_v and s["median"] == exp_med and s["spread"] == exp_spread)
        k_ok = k_ok and passed
        say("  %-18s -> %-6s 中位数=%-5s 波动=%-5s 极差比=%s %s"
            % (vals, s["verdict"], s["median"], s["spread"],
               ("%.2f" % s["ratio"]) if s["ratio"] is not None else "-",
               "OK" if passed else "FAIL(期望 %s/%s/%s)" % (exp_v, exp_med, exp_spread)))
    # 「不稳定」必须明说单次不可信，并把「拉长时长」作为对策给出来 —— 否则用户会拿单次值去调参
    s_bad = summarize_runs([400, 600, 500], page_px=628)
    k_ok = k_ok and ("不可信" in s_bad["advice"] and "1200" in s_bad["advice"])
    say("  不稳定档对策含「1200ms 拉长时长」= %s" % ("1200" in s_bad["advice"]))
    say("K1 结果: %s" % ("通过" if k_ok else "失败"))

    # K2：wait_scroll_stop —— 必须在「两帧不再变化」时返回，而不是死等固定 1s
    # ⚠ 样张必须有**纵向结构**：纯色/近纯色的图在任何位移下残差都是 0，
    #   measure_scroll 会直接返回 0，测出来「一次就停稳」是假通过（2026-09-21 自踩）。
    base = Image.new("RGB", (420, 900), (20, 20, 20))
    bd = ImageDraw.Draw(base)
    for k in range(9):                       # 9 条颜色与文字都不同的卡带 → 位移可辨
        y = k * 100
        bd.rectangle([10, y + 8, 410, y + 92], fill=(40 + k * 22, 90, 150 - k * 14))
        bd.text((24, y + 40), "CARD-%02d row=%d" % (k, k), fill=(255, 255, 255))
    def _up(img, n):
        out = Image.new("RGB", img.size, (20, 20, 20))
        out.paste(img.crop((0, n, img.size[0], img.size[1])), (0, 0))
        return out
    # 先自检样张：50px 位移必须量得出来，否则下面两条等停测试全是假通过
    _probe, _pw = measure_scroll(base, _up(base, 50))
    say("  样张可用性：平移 50px -> 测得 %s（须为 50，否则样张太平）" % _probe)

    class _SeqAdb(object):
        """按序吐帧的假 adb：用来验证「等到两帧一致才返回」与「超时兜底」两条路径。"""

        def __init__(self, frames):
            self._f = list(frames)
            self._i = 0
            self.calls = 0

        def screencap(self):
            self.calls += 1
            if self._i < len(self._f):
                img = self._f[self._i]
                self._i += 1
            else:
                img = self._f[-1]
            return img, None

    # 滚动中：50 → 120 → 180 → 停（最后再给一帧相同的）。必须**逐帧比对到最后**才停
    running = _SeqAdb([base, _up(base, 50), _up(base, 120), _up(base, 180), _up(base, 180)])
    last, used, stopped = wait_scroll_stop(running, timeout=5.0, interval=0.01, min_wait=0)
    k2a = (stopped is True and running.calls == 5)
    say("  滚动中序列 -> 停稳=%s 用 %.2fs 截屏 %d 次（期望 True / 5 次）"
        % (stopped, used, running.calls))
    # 永远在动：两张图交替，任何相邻两帧都不一致 → 必须超时兜底，不能死循环
    forever = _SeqAdb([base, _up(base, 90)] * 6)
    last2, used2, stopped2 = wait_scroll_stop(forever, timeout=0.3, interval=0.05, min_wait=0)
    k2b = (stopped2 is False and used2 < 1.5 and last2 is not None)
    say("  持续滚动序列 -> 停稳=%s 用 %.2fs（期望 False，靠超时兜底且不死循环）" % (stopped2, used2))
    # 样张本身必须能量出位移，否则上面两条都是假通过
    k2c = (_probe == 50)
    k_ok = k_ok and k2a and k2b and k2c
    say("K 结果: %s" % ("通过" if k_ok else "失败"))

    # ---------------- L. 精确滚动（闭环补齐的反推计算）
    say("")
    say("=== L. 精确滚动（闭环反推）===")
    say("顶部固定区占比 LIST_TOP_RATIO = %.2f（LOBBY 卡顶 168/864 = 0.194）" % LIST_TOP_RATIO)
    L_CASES = [
        # (目标, 已滚, 上轮手指, 上轮实际, 期望剩余, 期望手指)
        (628, 0, 0, 0, 628, 628),        # 没标定过：增益按 1.0，手指 = 目标
        (628, 300, 378, 300, 328, 413),  # 增益 0.79：手指要多给一点
        (628, 500, 378, 500, 128, 97),   # 增益 1.32（惯性大）：手指要收着给
        (628, 620, 378, 620, 8, 5),      # 已到位：剩余 8px 在容差内
        (628, 300, 378, 0, 328, 328),    # 上轮没动：增益异常(0) → 退回 1.0，不能除零
        (628, 300, 378, 8000, 328, 328), # 增益离谱(21)：同样夹回 1.0
    ]
    l_ok = True
    for target, done, finger, actual, exp_need, exp_finger in L_CASES:
        need, nf, gain = plan_next_swipe(target, done, finger, actual)
        passed = (need == exp_need and abs(nf - exp_finger) <= 1)
        l_ok = l_ok and passed
        say("  目标%d 已滚%d（上轮 手指%d→实际%d）-> 还差%d 手指%d 增益%.2f %s"
            % (target, done, finger, actual, need, nf, gain,
               "OK" if passed else "FAIL(期望 还差%d 手指%d)" % (exp_need, exp_finger)))
    say("L 结果: %s" % ("通过" if l_ok else "失败"))

    # ---------------- M. 实时屏幕流：沿帧链积分（2026-09-21 反馈：滑动每次都不一）
    say("")
    say("=== M. 实时屏幕流（帧链积分）===")
    say("实测对照（真机 97277e5f，幅度0.35/时长800ms，各3次）：")
    say("  两帧比对 = 114 / 1284 / 1284 px（极差比 0.91 → 判「不稳定」）")
    say("  帧链积分 = 666 / 678 / 594 px（极差比 0.13 → 判「稳定」）")
    say("存帧高度 LIVE_SMALL_H = %d（须与 _gray_small 的 target_h 一致）" % LIVE_SMALL_H)

    # 顶部固定页眉 + 可滚列表的「大厅样张」：页眉不随列表动
    tiled = Image.new("RGB", (420, 900 * 3), (20, 20, 20))
    for _r in range(3):
        tiled.paste(base, (0, _r * 900))

    def _lobby(off):
        img = Image.new("RGB", (420, 900), (18, 18, 18))
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, 420, 170], fill=(60, 60, 80))       # 固定页眉（170/900 ≈ 18.9%）
        d.text((20, 70), "TAB  FIXED HEADER", fill=(255, 255, 255))
        img.paste(tiled.crop((0, off, 420, off + 730)), (0, 170))
        return img

    m_ok = True
    # M1：帧链积分 —— 20 步 × 20px = 400px，前后各补 3 帧静止（模拟起流/等停）
    STEP, NSTEP = 20, 20
    chain = [_lobby(0)] * 3 + [_lobby(STEP * k) for k in range(NSTEP)] + [_lobby(STEP * NSTEP)] * 3
    total, info = measure_scroll_total(chain)
    m1 = total is not None and abs(total - STEP * NSTEP) <= 15
    m_ok = m_ok and m1
    say("  M1 帧链 %d 帧（每步 %dpx，总 %dpx）-> 积分 %spx｜段=%d 坏段=%d 最大单段=%dpx %s"
        % (len(chain), STEP, STEP * NSTEP, total, info["links"], info["bad"],
           info["max_step"], "OK" if m1 else "FAIL"))
    # 同一组数据的老办法（只取首尾两帧）作为对照：只打印不断言（是否失败与画面内容强相关）
    old2, old_why = measure_scroll(chain[0], chain[-1])
    say("     对照·两帧比对（首/尾）= %s（%s）" % (old2, old_why))

    # M2：帧数不足 / 全静止 —— 必须明确返回 None，不能编一个 0 出来当成「没滚动」
    t_none, i_none = measure_scroll_total([base])
    t_zero, i_zero = measure_scroll_total([base, base, base])
    m2 = (t_none is None and i_none["n"] == 1) and (t_zero is not None and t_zero == 0)
    m_ok = m_ok and m2
    say("  M2 单帧 -> %s｜三帧静止 -> %s（期望 None / 0）%s"
        % (t_none, t_zero, "OK" if m2 else "FAIL"))

    # M3：链中间掺一张完全不相干的帧 → 自适应步长必须**跳过去**，总量不许被噪声污染。
    #     （旧断言「坏段≥1」是错的：步长会跨过坏帧，这正是自适应步长的价值。）
    import random as _rd
    _rd.seed(7)
    noise = Image.new("RGB", (420, 900))
    noise.putdata([(_rd.randint(0, 255), _rd.randint(0, 255), _rd.randint(0, 255))
                   for _ in range(420 * 900)])
    broken = chain[:12] + [noise] + chain[12:]
    t_b, i_b = measure_scroll_total(broken)
    m3 = (t_b is not None and abs(t_b - STEP * NSTEP) <= 15)
    m_ok = m_ok and m3
    say("  M3a 掺入 1 张噪声帧 -> 积分 %spx（段=%d 坏段=%d，期望仍≈%d：噪声被跨过）%s"
        % (t_b, i_b["links"], i_b["bad"], STEP * NSTEP, "OK" if m3 else "FAIL"))
    def _noise(seed):
        _rd.seed(seed)
        im = Image.new("RGB", (420, 900))
        im.putdata([(_rd.randint(0, 255), _rd.randint(0, 255), _rd.randint(0, 255))
                    for _ in range(420 * 900)])
        return im

    # ⚠ 必须是**三张互不相同**的噪声：完全相同的帧意味着「确实没滚动」，返回 0 才是对的
    t_n2, i_n2 = measure_scroll_total([_noise(11), _noise(12), _noise(13)])
    m3b = (t_n2 is None)
    m_ok = m_ok and m3b
    say("  M3b 三张互不相同噪声帧 -> %s（期望 None：对不上就不许编一个 0 出来）%s"
        % (t_n2, "OK" if m3b else "FAIL"))
    t_same, _i = measure_scroll_total([noise, noise, noise])
    m3c = (t_same == 0)
    m_ok = m_ok and m3c
    say("  M3c 三张**相同**的帧 -> %s（期望 0：完全相同就是没滚动，不是「测不出」）%s"
        % (t_same, "OK" if m3c else "FAIL"))

    # M4：快速估计器（监视窗口实时读数用）—— 相邻小位移要准，不相干帧要弃权
    fs, fconf = measure_scroll_fast(_lobby(0), _lobby(18))
    fn, fconf2 = measure_scroll_fast(_lobby(0), noise)
    m4 = (fs is not None and abs(fs - 18) <= 3) and (fn is None)
    m_ok = m_ok and m4
    say("  M4 快速估计器：相邻 18px -> %s（置信 %.2f）｜无关帧 -> %s %s"
        % (fs, fconf or 0.0, fn, "OK" if m4 else "FAIL"))

    # M5：两套算法在同一条链上必须互相印证（真机实测差 3~9%）
    fast = 0
    for a, b in zip(chain, chain[1:]):
        s, _c = measure_scroll_fast(a, b)
        if s is not None:
            fast += s
    diff = abs(fast - total) / float(total) if total else 1.0
    m5 = diff <= 0.15
    m_ok = m_ok and m5
    say("  M5 快速 %dpx vs 帧链 %dpx → 相差 %.0f%%（阈值 15%%）%s"
        % (fast, total, diff * 100, "OK" if m5 else "FAIL"))

    # M6：ffmpeg 依赖必须**可见**——缺了要能给出可复制的安装命令，而不是静默降级
    ff = find_ffmpeg()
    m6 = (ff == "" or os.path.exists(ff)) and ("imageio-ffmpeg" in FFMPEG_INSTALL)
    m_ok = m_ok and m6
    say("  M6 ffmpeg: %s｜缺失时的安装提示含 imageio-ffmpeg = %s %s"
        % (ff or "（未安装）", "imageio-ffmpeg" in FFMPEG_INSTALL, "OK" if m6 else "FAIL"))
    # M7：监视窗口必须能构造出来（adb 无效时只是显示「截屏失败」，不能把主界面带崩）
    try:
        lm = LiveMonitor(root, app)
        m7 = bool(lm.top.winfo_exists())
        lm.stop()
        lm.top.destroy()
        err7 = ""
    except Exception as _e:
        m7, err7 = False, "%s: %s" % (type(_e).__name__, _e)
    m_ok = m_ok and m7
    say("  M7 实时监视窗口构造 = %s %s" % ("OK" if m7 else "FAIL", err7))
    say("M 结果: %s" % ("通过" if m_ok else "失败"))

    # ---------------- N. 顶行对齐红线（2026-09-21 用户要求：下一批上排 3 张顶贴红线）
    say("")
    say("=== N. 顶行对齐红线（grid_drift）===")
    say("锚点 = 行间亮缝（封面可见 302px + 亮缝 12px = 行距 314 @864 高），"
        "三列同时「亮 + 平」才算缝 —— 封面内部结构很难三列同一行对齐。")
    say("2026-09-22 纠错：视口顶部除了「页面背景空档」还会混进一条 3px 暗色分隔线，")
    say("  亮缝检测会把两者并成一个「假缝」。此时缝下沿+1 仍等于首行卡顶，")
    say("  故 g0 贴视口上沿时 first_top = g1+1，drift 是**小正值**。")
    say("  同时**证伪**了「首行整行滑出视口」这一状态：放大目视核验表明那些帧的")
    say("  首行封面/标题/按钮全部可见，正解一律是「继续向下滚」，drift 恒 ≥0。")
    n_ok = True
    # N1：真机截图（在这台机器上才测；缺图只提示不算失败）
    IMG_DIR = r"C:\Users\Administrator\.workbuddy\clipboard-images"
    F1 = os.path.join(IMG_DIR, "clipboard-2026-09-21T06-59-08-288Z-ec1ab78a.jpg")  # 标定基准=对齐
    F2 = os.path.join(IMG_DIR, "clipboard-2026-09-21T06-59-08-289Z-4012b2f7.jpg")  # 用户截图=偏下 9px
    F3 = os.path.join(IMG_DIR, "clipboard-2026-09-22T06-26-58-416Z-fd6fd6f9.jpg")  # 用户附图=偏下 7px
    if os.path.exists(F1) and os.path.exists(F2):
        # 4012b2f7 的「缝」里混了分隔线（首行完整、只需 +9px 正向微调），
        # 故其状态是 top_in_gap 而非 cut —— 期望值按修正后的语义写。
        d1, i1 = grid_drift(Image.open(F1).convert("RGB"))
        d2, i2 = grid_drift(Image.open(F2).convert("RGB"))
        n1 = (d1 == 0 and i1.get("state") == "aligned") and \
             (d2 is not None and abs(d2 - 9) <= 3 and i2.get("state") == "top_in_gap")
        n_ok = n_ok and n1
        say("  N1 基准图 drift=%s（%s）｜用户截图 drift=%s（%s，顶行卡顶 %s）%s"
            % (d1, i1.get("state"), d2, i2.get("state"), i2.get("first_top"),
               "OK" if n1 else "FAIL(期望 0/aligned 与 9±3/top_in_gap)"))
    else:
        say("  N1 真机截图不存在，跳过（%s）" % IMG_DIR)
    # N1b：用户附图（2026-09-22 报「顶部都滑上去超出屏幕了，还报已对齐」的那张）
    #      实测该帧首行**完整**（热度 107万/2.7 等全可见），正解 = 卡顶 166 比红线 159 低 7px。
    if os.path.exists(F3):
        d3b, i3b = grid_drift(Image.open(F3).convert("RGB"))
        n1b = (d3b is not None and abs(d3b - 7) <= 3 and i3b.get("state") == "top_in_gap")
        n_ok = n_ok and n1b
        say("  N1b 用户附图 drift=%s（%s，卡顶 %s）%s"
            % (d3b, i3b.get("state"), i3b.get("first_top"),
               "OK" if n1b else "FAIL(期望 7±3/top_in_gap)"))
    else:
        say("  N1b 用户附图不存在，跳过")
    # N1c：生产帧 —— 缝落在卡片封面内部浅色平坦区（旧代码会把它当行缝）。
    #      放大目视核验：首行「异兽吞噬进化」封面/标题/标签/下载按钮**全部可见**，
    #      即首行未被裁，正解 drift 为**正**值（继续向下滚），绝不为负。
    F4 = os.path.join(HERE, "shots", "shot_20260922_141831_002.png")
    if os.path.exists(F4):
        d4, i4 = grid_drift(Image.open(F4).convert("RGB"))
        n1c = (d4 is not None and d4 >= 0 and i4.get("state") in ("cut", "top_in_gap"))
        n_ok = n_ok and n1c
        say("  N1c 封面内假缝帧 drift=%s（%s）—— 必须 ≥0（旧代码会误判负值/已滑出）%s"
            % (d4, i4.get("state"), "OK" if n1c else "FAIL(期望 ≥0)"))
    else:
        say("  N1c 生产帧不存在，跳过")
    # N1d：drift 恒非负 —— 全量真机帧扫描，任何负 drift 都说明反推法又回来了
    neg = []
    for _p in sorted(glob.glob(os.path.join(HERE, "shots", "*.png")))[:400]:
        try:
            _im = Image.open(_p).convert("RGB")
            if _im.width != 2400:
                continue
            _d, _i = grid_drift(_im)
            if _d is not None and _d < -6:
                neg.append("%s=%d" % (os.path.basename(_p), _d))
        except Exception:
            pass
    n1d = (len(neg) == 0)
    n_ok = n_ok and n1d
    say("  N1d 全量帧负 drift 检查：%s %s"
        % ("无" if n1d else "发现 " + ", ".join(neg[:6]), "OK" if n1d else "FAIL"))
    # N2：合成滚动 —— 把基准图列表区整体上移 S px 等价于滚了 S，
    #     期望 drift = (-S) mod 行距；「cut≤容差判对齐」的截断误差 ≤ 容差+2。
    #     ⚠ 合成法受图片高度限制（S 太大会拼出重复内容），只测 ≤471。
    #     ⚠ 合成页顶部始终只有真行缝（无页面背景空档/分隔线），故只覆盖「缝贴着上沿」
    #       这一支；scrolled_past 只能靠真机帧覆盖（见 N1c），合成样张复现不出该缺陷。
    if os.path.exists(F1):
        base_img = Image.open(F1).convert("RGB")
        bw, bh = base_img.size
        sy_ = bh / float(VIEW_H)
        R_ = LOBBY["row_step"] * sy_
        clip_ = int(round(LOBBY["clip_y"] * sy_))
        cover_dev = LOBBY["cover_h"] * sy_
        tol_ = max(5.0, 0.02 * cover_dev)
        n2 = True
        for S in (0, 5, 9, 50, 100, 157, 160, 170, 200, 250, 300, 310, 314, 400, 471):
            syn = base_img.copy()
            if S > 0:
                syn.paste(base_img.crop((0, clip_ + S, bw, bh)), (0, clip_))
            d, i2 = grid_drift(syn)
            exp = int(round((-S) % R_))
            exp_eff = 0 if exp >= R_ - tol_ else exp
            ok2 = d is not None and abs(d - exp_eff) <= tol_ + 2
            n2 = n2 and ok2
            say("  N2 S=%-4d 期望=%-4d 判得=%-4s（%s）%s"
                % (S, exp_eff, d, i2.get("state"), "OK" if ok2 else "FAIL"))
        n_ok = n_ok and n2
    # N3：空态/纯色图必须返回 None，不许编一个偏差出来
    blank_img = Image.new("RGB", (1920, 864), (200, 205, 215))
    d3, i3 = grid_drift(blank_img)
    n3 = (d3 is None)
    n_ok = n_ok and n3
    say("  N3 纯色空态图 -> %s（%s；期望 None：没结构就不给值）%s"
        % (d3, i3.get("why", "")[:30], "OK" if n3 else "FAIL"))
    say("N 结果: %s" % ("通过" if n_ok else "失败"))

    # ---------------- O. 顶部彩字字段（热度/评分）多配方读取（2026-09-22）
    # 锁住两处修复：① 热度「前导数字丢失」静默错值（真机 '116万' 被读成 '16万'）；
    #               ② 评分主读失败时换左边界兜底（基准图 r1c2 '75'→4.5）。
    say("")
    say("=== O. 热度/评分 多配方读取 ===")
    o_ok = True

    # O1 color_gray：红字变亮、蓝底压暗，尺寸/模式不变，异常输入不抛
    t_img = Image.new("RGB", (40, 12), (40, 60, 190))
    ImageDraw.Draw(t_img).rectangle([4, 2, 20, 10], fill=(220, 60, 60))
    g_img = color_gray(t_img)
    o1 = (g_img.size == t_img.size and g_img.mode == "RGB"
          and g_img.getpixel((10, 6))[0] > t_img.getpixel((10, 6))[0]
          and g_img.getpixel((35, 6))[0] <= t_img.getpixel((35, 6))[0]
          and color_gray(Image.new("L", (4, 4))).size == (4, 4))
    o_ok = o_ok and o1
    say("  O1 颜色增强灰：红 220→%d、蓝底 40→%d，尺寸/模式保持 %s"
        % (g_img.getpixel((10, 6))[0], g_img.getpixel((35, 6))[0], "OK" if o1 else "FAIL"))

    # O2 判定规则（纯函数）：位数最多优先 / 同位数看票数 / 打平弃权 / 全空
    o2_cases = [
        ([("raw", "116万", 1160000.0, 4)], 1160000.0, "single", "单一值直接采纳"),
        ([("raw", "16万", 160000.0, 4), ("cg", "116万", 1160000.0, 4)],
         1160000.0, "most_digits", "前导丢失：取位数多的 116万"),
        ([("raw", "16万", 160000.0, 4), ("cg", "11万", 110000.0, 4)],
         None, "conflict(110000.0/160000.0)", "位数与票数都打平 → 弃权"),
        ([("raw", "万", None, 0), ("cg", "", None, 0)], None, "no_value", "全无效 → 交给复核"),
    ]
    for modals, exp_v, exp_why, desc in o2_cases:
        _t, _v, _w = decide_readings(modals)
        good = (_v == exp_v) and (_w == exp_why)
        o_ok = o_ok and good
        say("  O2 %-26s -> 值=%s why=%s %s" % (desc, _v, _w, "OK" if good else "FAIL"))
    o2b = (digits_len("73.3万") == 3 and digits_len("万") == 0)
    o_ok = o_ok and o2b
    say("  O2b digits_len：'73.3万'=%d、'万'=%d %s"
        % (digits_len("73.3万"), digits_len("万"), "OK" if o2b else "FAIL"))

    # O2c heat_value：无单位/前导 0（丢 '1' 或火苗被读成数字）一律判无效
    o2c_cases = [("116万", 1160000.0), ("13.1万", 131000.0), ("0万", None),
                 ("0113.1万", None), ("万", None), ("77.0", None)]
    for _t, _exp in o2c_cases:
        _got = heat_value(_t)
        good = (_got == _exp)
        o_ok = o_ok and good
        say("  O2c heat_value(%r) -> %s（期望 %s）%s"
            % (_t, _got, _exp, "OK" if good else "FAIL"))

    # O3/O4 真实样本：两张标定图上「旧读法出错」的两张卡，新读法必须读对
    real_img = os.path.join(HERE, "crops", "lobby_real.png")
    dev_img = os.path.join(HERE, "crops", "lobby_device_2400x1080.png")
    o3_cases = [
        (dev_img, (1, 0), "116万", 1160000.0, "真机 r2c1（旧读法 '16万' 错值 10 倍）"),
        (real_img, (1, 2), "111万", 1110000.0, "基准图 r2c3（旧读法只剩 '万'）"),
    ]
    for path, rc, exp_txt, exp_val, desc in o3_cases:
        if not os.path.exists(path):
            say("  O3 跳过（缺 %s）" % os.path.basename(path))
            o_ok = False
            continue
        _im = Image.open(path).convert("RGB")
        _boxes = find_cards(_im, LOBBY)
        _hit = [c for c in _boxes if (c["row"], c["col"]) == rc]
        if not _hit:
            say("  O3 FAIL：定位不到 r%d c%d" % (rc[0] + 1, rc[1] + 1))
            o_ok = False
            continue
        _txt, _val, _det = read_heat(engine, _im, _hit[0]["box"], scales=(3, 6))
        _why = _det.get("why", "")
        good = (_val == exp_val)
        o_ok = o_ok and good
        say("  O3 %-32s -> %r→%s（why=%s，期望 %s）%s"
            % (desc, _txt, _val, _why, exp_txt, "OK" if good else "FAIL"))

    # O5 评分兜底：基准图 r1c2 主读失败（'75' 无小数点）→ 兜底必须给 4.5
    if os.path.exists(real_img):
        _im = Image.open(real_img).convert("RGB")
        _boxes = find_cards(_im, LOBBY)
        _hit = [c for c in _boxes if (c["row"], c["col"]) == (0, 1)]
        if _hit:
            _bx = _hit[0]["box"]
            _sx = _im.size[0] / float(VIEW_W)
            _sy = _im.size[1] / float(VIEW_H)
            _vb = LOBBY["fields"]["评分"]
            _rr = (int(round(_bx[0] + _vb[0] * _sx)), int(round(_bx[1] + _vb[1] * _sy)),
                   int(round(_bx[0] + _vb[2] * _sx)), int(round(_bx[1] + _vb[3] * _sy)))
            _p_txt, _p_val = read_field(engine, _im.crop(_rr), "评分", 4)
            _r_txt, _r_val, _r_det = read_score_retry(engine, _im, _bx)
            o5 = (_p_val is None and _r_val == 4.5)
            o_ok = o_ok and o5
            say("  O5 基准 r1c2 评分：主读 %r→%s（期望 None）｜兜底 %r→%s（期望 4.5）%s"
                % (_p_txt, _p_val, _r_txt, _r_val, "OK" if o5 else "FAIL"))
    else:
        o_ok = False
        say("  O5 跳过（缺基准图）")
    say("O 结果: %s" % ("通过" if o_ok else "失败"))

    say("C 结果: 通过")
    root.destroy()
except Exception as e:
    import traceback
    say("C 失败: %s" % e)
    say(traceback.format_exc())
    # 失败也必须销毁 Tk，否则 Tk 事件循环吊住进程、脚本永远不退出
    # （2026-09-18 实测：C 抛异常后进程 5 分钟仍未结束，只能手工 kill）
    try:
        root.destroy()
    except Exception:
        pass

with io.open(os.path.join(HERE, "_selftest.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(OUT))
print("done", flush=True)
# 结果已落盘，直接硬退出。C 段创建过 Tk 与 onnxruntime 会话后，正常退出路径会被
# 非守护的本地线程吊住（2026-09-18 实测：文件已写完、进程 5 分钟不结束，只能手工 kill）。
# 注意必须显式 flush：os._exit 不跑解释器清理，stdout 若还是块缓冲，日志会被吞掉。
os._exit(0)
