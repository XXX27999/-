# -*- coding: utf-8 -*-
"""启动 GUI、用真实大厅截图跑一帧识别、按 winfo 几何实拍窗口，产出 preview.png。"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

try:
    ctypes_dpi = ctypes = __import__("ctypes")
    ctypes_dpi.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

from PIL import Image, ImageGrab  # noqa: E402
import tkinter as tk  # noqa: E402
from OasisOcrSampler import App, LOBBY  # noqa: E402

root = tk.Tk()
app = App(root)
root.deiconify()
# 强制放到可见屏幕内：Windows 有时会把窗口扔到 (2200,...) 这类位子，
# 那样 ImageGrab 抓到的整幅是黑的（2026-09-20 实测）。
root.update_idletasks()
root.geometry("1180x760+20+20")
root.lift()
root.attributes("-topmost", True)
for _ in range(20):
    root.update_idletasks()
    root.update()
    time.sleep(0.05)

# 用真实大厅截图 + 按图标定的大厅几何
SHOT = os.path.join(HERE, "crops", "lobby_real.png")
im = None
if os.path.exists(SHOT):
    im = Image.open(SHOT).convert("RGB")
    app.layout_mode_var.set("lobby")
    app.rects = {f: tuple(b) for f, b in LOBBY["fields"].items()}
    app.refresh_rect_tree()
    app.show_image(im)

# 等 OCR 引擎加载完成（后台线程），最多 60 秒
for _ in range(600):
    root.update_idletasks()
    root.update()
    if app.ocr.ready or app.ocr.status == "OCR 引擎不可用":
        break
    time.sleep(0.1)

nrec = 0
if app.ocr.ready and im is not None:
    recs, state, note = app.recognize_frame(im, "preview_lobby.png")
    for r in recs:
        app.add_record(r)
    nrec = len(recs)
    app.log("预览帧识别 %d 条（页态=%s，%s）" % (len(recs), state, note))

for _ in range(30):
    root.update_idletasks()
    root.update()
    time.sleep(0.05)

x = root.winfo_rootx()
y = root.winfo_rooty()
w = root.winfo_width()
h = root.winfo_height()
shot = ImageGrab.grab(bbox=(x - 8, y - 38, x + w + 8, y + h + 8))
out = os.path.join(HERE, "preview.png")
shot.save(out)

# 抓黑就说明窗口没真正画出来，直接报错而不是交一张黑图
lo, hi = shot.convert("L").getextrema()
black = hi < 16
if black:
    print("WARN preview 抓到全黑图（窗口未渲染），bbox=(%d,%d,%d,%d) 极差=%d"
          % (x, y, w, h, hi - lo))
else:
    print("done")

with open(os.path.join(HERE, "_preview_result.txt"), "w", encoding="utf-8") as f:
    f.write("ocr=%s\n" % app.ocr.status)
    f.write("records=%d\n" % nrec)
    f.write("bbox=(%d,%d,%d,%d)\n" % (x - 8, y - 38, x + w + 8, y + h + 8))
    f.write("black=%s\n" % black)
    f.write("preview=%s\n" % out)

root.destroy()
