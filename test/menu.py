import tkinter as tk

root = tk.Tk()

# Aキーが押されているかを保持するフラグ
is_waiting = False

# 長押し判定＆繰り返し処理
def check_a():
    if is_waiting:
        print("a")  # ← 長押し中に実行したい処理
        root.after(100, check_a)  # 0.1秒ごとにチェック
    else:
        # 押されていない場合は何もしない
        pass

# キー押下イベント
def on_key_press(event):
    global is_waiting
    if event.keysym.lower() == "a" and not is_waiting:
        is_waiting = True
        check_a()  # 長押し処理開始

# キー離したイベント
def on_key_release(event):
    global is_waiting
    if event.keysym.lower() == "a":
        is_waiting = False  # 長押し終了

# バインド設定
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

root.mainloop()
