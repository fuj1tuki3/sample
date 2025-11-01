import tkinter
import time

WIDTH, HEIGHT = 960, 720
bg_y = 0
pl_x, pl_y = 0, HEIGHT-40
cl_x, cl_y = 0, 0
fire = False
SIZE = 80
enemy = [
    [0,0,1,1,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0,0,0,0,1]
]

def move(e): # マウスを動かした時
    global pl_x
    pl_x = int(pl_x*0.9+e.x*0.1)

def click(e): # クリックした時
    global cl_x, cl_y, fire
    cl_x = e.x
    cl_y = e.y
    fire = True

def effect(cx, cy): # 敵を倒した演出
    for i in range(10):
        cvs.create_oval(cx, cy, cx+SIZE, cy+SIZE, fill="red")
        cvs.update()
        time.sleep(0.01)
        cvs.create_oval(cx, cy, cx+SIZE, cy+SIZE, fill="yellow")
        cvs.update()
        time.sleep(0.01)

def main(): # メイン処理を行う関数
    global bg_y, fire
    bg_y = (bg_y+2)%HEIGHT
    cvs.delete("all")
    cvs.create_image(WIDTH/2, bg_y-HEIGHT/2, image=bg)
    cvs.create_image(WIDTH/2, bg_y+HEIGHT/2, image=bg)
    for y in range(3):
        for x in range(12):
            if enemy[y][x]==1:
                X = x*SIZE + SIZE/2
                Y = y*SIZE + SIZE/2
                cvs.create_image(X, Y, image=invader)
    cvs.create_image(pl_x, pl_y, image=fighter)
    if fire==True: # 画面をクリックした時
       cvs.create_line(pl_x, pl_y, cl_x, cl_y, fill="cyan", width=3)
       fire = False
       ax = int(cl_x/SIZE) # 添え字（列の値）を計算
       ay = int(cl_y/SIZE) # 添え字（行の値）を計算
       if 0<=ax and ax<=11 and 0<=ay and ay<=2: # 敵の配列の範囲内
           if enemy[ay][ax]==1: # 敵が存在する場合
               effect(ax*SIZE, ay*SIZE) # エフェクトを表示
               enemy[ay][ax] = 0 # 敵を消す
    root.after(33, main)

root = tkinter.Tk()
root.title("ギャラクシー・ディフェンダー")
root.resizable(False, False)
root.bind("<Motion>", move)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
fighter = tkinter.PhotoImage(file="image/fighter.png")
invader = tkinter.PhotoImage(file="image/invader.png")
main()
root.mainloop()
