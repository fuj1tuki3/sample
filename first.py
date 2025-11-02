import tkinter as tk
import os

p_x = 0
p_y = 0
scene = "タイトル"
title_menu_y = 310
select_pos_y = 310
waiting = False
title_manu_txt = ["始めから", "続きから", "設定", "終了"]

def pkey(e):
    global scene, select_pos_y, title_menu_y, title_manu_txt
    if e.keysym == "x" or e.keysym == "Return":
        start_game()
        print("ゲームスタート：", scene)
    # if e.keysym == "":
    #     scene = "タイトル"
    if e.keysym == "Up" and scene == "タイトル":
        cvs.delete("select")
        select_pos_y -= 30
        if select_pos_y < 310:
            select_pos_y = select_pos_y + 120
        i = int((select_pos_y - 310) / 30)
        cvs.create_text(310, select_pos_y, text=title_manu_txt[i], font=("System", 20), fill="white", anchor="nw", tag="select")
    if e.keysym == "Down" and scene == "タイトル":
        cvs.delete("select")
        select_pos_y += 30
        if select_pos_y >= 420:
            select_pos_y = select_pos_y - 120
        i = int((select_pos_y - 310) / 30)
        cvs.create_text(310, select_pos_y, text=title_manu_txt[i], font=("System", 20), fill="white", anchor="nw", tag="select")

def start_game():
    global scene
    scene = "ゲーム"

def title_menu():
    global scene
    cvs.create_text(400, 200, text="First Games", font=("System", 80), fill="orange")
    cvs.create_rectangle(300, 300, 500, 430, fill="gray", outline="", width=0)
    for i in range(4):
        cvs.create_text(310, title_menu_y + i*30, text=title_manu_txt[i], font=("System", 20), fill="black", anchor="nw")
    cvs.create_text(310, select_pos_y, text=title_manu_txt[0], font=("System", 20), fill="white", anchor="nw", tag="select")

def main():
    global p_x, p_y, scene, waiting, title_menu_y
    cvs.delete("all")
    if scene == "タイトル":
        title_menu()

root = tk.Tk()
root.title("First Games")
root.resizable(False, False)
root.bind("<Key>", pkey)
#root.bind("<KeyRelease>", release)
cvs = tk.Canvas(width=800, height=600, bg="blue")
cvs.pack()
main()
root.mainloop()