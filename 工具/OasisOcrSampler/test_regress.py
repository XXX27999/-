# -*- coding: utf-8 -*-
"""大厅识别回归测试：用真实大厅截图逐卡片验证各字段的定位与 OCR。
结果写 _regress.txt（增量落盘，中途被杀也能看到已完成部分）。
运行：.venv\\Scripts\\python.exe test_regress.py
"""
import os
import io
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "_regress.txt")
LOG = os.path.join(HERE, "_run_out.txt")
L = []


def say(s):
    L.append(str(s))
    io.open(OUT, "w", encoding="utf-8").write("\n".join(L))


try:
    import numpy as np
    from PIL import Image, ImageDraw
    from rapidocr_onnxruntime import RapidOCR
    import OasisOcrSampler as S

    IMG = Image.open(os.path.join(HERE, "crops", "lobby_real.png")).convert("RGB")
    RW, RH = IMG.size
    SX, SY = RW / S.VIEW_W, RH / S.VIEW_H
    eng = RapidOCR()

    def ocr(crop, scale=4, prep=None):
        """放大后 OCR，按「上->左」排序拼接，返回清洗后的文本。prep 走与主程序同一套预处理。"""
        if crop is None or crop.width < 2 or crop.height < 2:
            return ""
        im = S.preprocess(crop, prep)
        im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
        res, _ = eng(np.array(im)[:, :, ::-1])
        if not res:
            return ""
        it = sorted((min(p[1] for p in r[0]), min(p[0] for p in r[0]), str(r[1])) for r in res)
        return S.clean_text("".join(t[2] for t in it))

    class _Eng:
        """把本地的 ocr() 包成主程序 read_field 需要的引擎接口。"""
        recognize = staticmethod(lambda img, scale=2, prep=None: ocr(img, scale=scale, prep=prep))

    ENG = _Eng()

    def field_box(card, f):
        """字段框 = 卡片框 + LOBBY 相对偏移（与主程序 field_rect 同口径，用 round 换算）。"""
        vb = S.LOBBY["fields"].get(f)
        if not vb:
            return None
        return (int(round(card["box"][0] + vb[0] * SX)), int(round(card["box"][1] + vb[1] * SY)),
                int(round(card["box"][0] + vb[2] * SX)), int(round(card["box"][1] + vb[3] * SY)))

    say("图像 %dx%d  scale=%.4f/%.4f  几何版本 v%d" % (RW, RH, SX, SY, S.GEOM_VERSION))

    state, why = S.detect_page_state(IMG)
    say("页态 = %s（%s）" % (state, why))

    cards = S.find_cards(IMG, S.LOBBY)
    say("卡片定位 = %d 个" % len(cards))
    for c in cards:
        say("  c%d r%d box=%s" % (c["col"] + 1, c["row"] + 1, c["box"]))

    say("")
    say("=== 逐卡片逐字段识别（放大 4x）===")
    vis = IMG.copy()
    d = ImageDraw.Draw(vis)
    ok = bad = 0
    for c in cards:
        d.rectangle(list(c["box"]), outline=(0, 230, 120), width=3)
        say("c%d r%d [%s]" % (c["col"] + 1, c["row"] + 1, c["box"]))
        for f in S.FIELDS:
            if f in S.FIELD_PAGE_UNAVAILABLE:
                say("    %-5s 本页不可用 -> 留空" % f)
                continue
            b = field_box(c, f)
            if b is None:
                say("    %-5s 无框" % f)
                continue
            if b[2] > RW or b[3] > RH or b[0] < 0 or b[1] < 0:
                say("    %-5s 越界 %s" % (f, b))
                continue
            d.rectangle(b, outline=(255, 215, 0), width=2)
            # 与主程序同一路径：走 read_field（含预处理与放大重试）
            t, v = S.read_field(ENG, IMG.crop(b), f, 4)
            if f in S.NUMERIC_FIELDS:
                raw_v, _m = S.parse_number(t)
                if v is None:
                    bad += 1
                    if raw_v is not None:
                        say("    %-5s '%s'  -> 越界被拦下（原值 %g 未采纳）" % (f, t, raw_v))
                    else:
                        say("    %-5s '%s'  -> 未读出有效数值" % (f, t))
                else:
                    ok += 1
                    say("    %-5s '%s'  -> 值=%g" % (f, t, v))
            else:
                if t:
                    ok += 1
                else:
                    bad += 1
                say("    %-5s '%s'" % (f, t))

    say("")
    say("小结：识别成功 %d 项，异常 %d 项" % (ok, bad))

    p = os.path.join(HERE, "crops", "regress_boxes.png")
    vis.save(p)
    say("可视化 = %s" % p)
    io.open(LOG, "w", encoding="utf-8").write("OK\n")
except Exception:
    io.open(LOG, "w", encoding="utf-8").write(traceback.format_exc())
    say("异常：见 _run_out.txt")
