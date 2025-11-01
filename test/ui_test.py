import tkinter as tk
from decimal import Decimal, ROUND_HALF_UP
import time

#変数宣言
p_hp_ulimit = 100
p_mp_ulimit = 70
p_hp = 100
p_mp = 70
mp_clogged = 0
mp_clg_p = round(Decimal(str(p_mp_ulimit)) * Decimal("0.01"), 2)
cloging_deley = True
s_name=["fire","ice"]
s_mp=[15,27]
is_waiting = False #長押し判定
status_effect=[["breast_ex","pregnancy","parasitism"],[False,False,False]]     #breast_expansion:膨乳, pregnancy:妊娠, parasitism:寄生

# フレーム計測用
last_time = time.time()
frame_count = 0

#搾乳
def milking(e=None):
    global mp_clogged, p_mp_ulimit, p_mp, is_waiting
    #print("～搾乳中～")
    if is_waiting:
        if mp_clogged > 0:    #MP固定域あり
            mp_clogged = mp_clogged - 2
            p_mp = p_mp - 2
        elif p_mp > 0:        #MP固定域
            p_mp = p_mp - 2
        is_waiting = False
    else:
        pass    #押されていないなら何もしない

#キーの値を取得
def key_press(e):
    global is_waiting
    #aを押すと搾乳
    if e.keysym.lower() == "a" and not is_waiting:
        is_waiting = True
        root.after(500, lambda: milking(e))    #0.5秒ごとに実行
    status_bar()

def key_press_relese(e):
    global is_waiting
    if e.keysym.lower() == "a":
        is_waiting = False

# #mp使用不可領域増加
# def mp_cloging():
#     global p_mp_ulimit, p_mp, mp_clogged, cloging_deley
#     if cloging_deley == True:
#         cloging_deley = False
#         root.after(3000, mp_cloging)
#     #mpが最大なら蓄積開始
#     elif p_mp_ulimit <= p_mp:
#         mp_clogged = mp_clogged + (p_mp_ulimit / 10)

#     if p_mp_ulimit < mp_clogged:
#         mp_clogged = mp_clogged - (mp_clogged-p_mp_ulimit)

#     cloging_deley = True
#     root.after(3000, mp_cloging)

#mp自動回復
def auto_mp_charge():
    global p_mp, p_mp_ulimit, cloging_deley, mp_clogged, mp_clg_p, is_waiting
    if p_mp < p_mp_ulimit and not is_waiting:
        p_mp = p_mp + 1
    elif cloging_deley:
        cloging_deley = False
        root.after(1000, auto_mp_charge)
        return
    elif p_mp >= p_mp_ulimit and p_mp_ulimit >= mp_clogged and not cloging_deley:
        mp_clogged = mp_clogged + mp_clg_p
        if p_mp_ulimit < mp_clogged:
            mp_clogged = mp_clogged - (mp_clogged - p_mp_ulimit)
        root.after(2000, auto_mp_charge)
        return
    root.after(800, auto_mp_charge)

#スキル使用
def skill(e):
    global p_mp, p_mp_ulimit, mp_clogged, s_mp
    if p_mp - mp_clogged >= s_mp[0]:
        p_mp = p_mp - s_mp[0]
        #print(p_mp)
        print("スキルを使いました：消費MP ", s_mp[0])
    else:
        print("MPが不足しています!")
        print("現在MP ", p_mp)
        print("使用不可MP ", mp_clogged)

#ステータスバー表示
def status_bar():
    global p_hp_ulimit, p_mp_ulimit, p_hp, p_mp, mp_clogged, p_img
    ui_pos_y = 5
    #cvs.delete("all")
    #cvs.create_image(300, 200, image=p_img)
    cvs.create_rectangle(5, ui_pos_y, p_hp_ulimit + 5, 15, fill= "#726285", outline= "black")
    cvs.create_rectangle(5, ui_pos_y, p_hp + 5, 15, fill= "#FC004C")
    ui_pos_y =+ 20
    cvs.create_rectangle(5, ui_pos_y, p_mp_ulimit + 5, ui_pos_y+10, fill= "#726285", outline= "black")
    cvs.create_rectangle(5, ui_pos_y, p_mp + 5, ui_pos_y+10, fill= "#F8F8C9")
    if mp_clogged > 0:
        cvs.create_rectangle(5, ui_pos_y, mp_clogged + 5, ui_pos_y+10, fill= "#EC73B0", outline="#EC73B0")
    cvs.create_rectangle(5, ui_pos_y, p_mp_ulimit + 5, ui_pos_y+10, fill= None, outline= "black")

def update_fps():
    global last_time, frame_count

    frame_count += 1
    current_time = time.time()
    elapsed = current_time - last_time

    # 1秒ごとにFPS更新
    if elapsed >= 1.0:
        fps = frame_count / elapsed
        frame_count = 0
        last_time = current_time
    else:
        fps = frame_count / max(elapsed, 0.001)
    
    disp_fps.delete("fps")
    disp_fps.create_text(390, 10, text=f"FPS: {fps:.2f}", anchor="ne", font=("Arial", 22), fill="red", tags="fps")
    

    # 0.01秒後に次のフレーム
    root.after(16, update_fps)

#main
def main():
    global p_mp
    status_bar()
    root.after(1000, main)

root = tk.Tk()
root.title("ステータステスト")
root.resizable(False, False)        #ウィンドウサイズを固定する
#root.bind("<ButtonPress>", skill)
root.bind("<Key>", key_press)
root.bind("<KeyRelease>", key_press_relese)
cvs = tk.Canvas(width= 800,height= 600, bg="#495c4d")
disp_fps = tk.Canvas(root, width=400, height=200)
#p_img = tk.PhotoImage(file="test/image/bg.png")
cvs.pack()
disp_fps.pack()
main()
auto_mp_charge()
update_fps()
root.mainloop()