import tkinter
import time
import random

WIDTH, HEIGHT = 960, 720
bg_y = 0
pl_x, pl_y = int(WIDTH/2), HEIGHT-40
cl_x, cl_y = 0, 0
fire = False
SIZE = 80
enemy = []
for i in range(9):
    enemy.append([0,0,0,0,0,0,0,0,0,0,0,0])
scene = "タイトル"
timer = 0
score = 0

def move(e): # マウスを動かした時
    global pl_x
    if scene=="ゲーム":
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

def text(x, y, txt, siz, col): # 影付き文字の表示
    fnt = ("Times New Roman", siz)
    cvs.create_text(x+1, y+1, text=txt, font=fnt, fill="black")
    cvs.create_text(x, y, text=txt, font=fnt, fill=col)

def main(): # メイン処理を行う関数
    global bg_y, fire, scene, timer, score
    timer += 1
    bg_y = (bg_y+2)%HEIGHT
    cvs.delete("all")
    cvs.create_image(WIDTH/2, bg_y-HEIGHT/2, image=bg)
    cvs.create_image(WIDTH/2, bg_y+HEIGHT/2, image=bg)
    for y in range(9):
        for x in range(12):
            if enemy[y][x]==1:
                X = x*SIZE + SIZE/2
                Y = y*SIZE + SIZE/2
                cvs.create_image(X, Y, image=invader)
    cvs.create_image(pl_x, pl_y, image=fighter)
    text(WIDTH*0.5, 30, "SCORE "+str(score), 30, "white")

    if scene=="タイトル":
        text(WIDTH*0.5, HEIGHT*0.3, "GALAXY DEFENDER", 60, "cyan")
        if timer%30<15:
            text(WIDTH*0.5, HEIGHT*0.6, "Clock to start!", 30, "lime")
        if fire==True:
            for y in range(8):
                for x in range(12):
                    enemy[y][x] = 0
            scene = "ゲーム"
            timer = 0
            score = 0
            fire = False

    if scene=="ゲーム":
        if timer%30==0: # 30フレームに1回、敵全体を下に移動
            for y in range(8, 0, -1):
                for x in range(12):
                    enemy[y][x] = enemy[y-1][x]
            for x in range(12): # 一番上の行に新たな敵を配置
                enemy[0][x] = random.choice([0,0,0,1])
            for x in range(12): # 侵略されたか（一番下の行に敵がいるか）調べる
                if enemy[8][x]==1:
                    scene = "ゲームオーバー"
                    timer = 0
        if fire==True: # 画面をクリックした時
           cvs.create_line(pl_x, pl_y, cl_x, cl_y, fill="cyan", width=3)
           fire = False
           ax = int(cl_x/SIZE) # 添え字（列の値）を計算
           ay = int(cl_y/SIZE) # 添え字（行の値）を計算
           if 0<=ax and ax<=11 and 0<=ay and ay<=8: # 敵の配列の範囲内
               if enemy[ay][ax]==1: # 敵が存在する場合
                   effect(ax*SIZE, ay*SIZE) # エフェクトを表示
                   enemy[ay][ax] = 0 # 敵を消す
                   score += 100

    if scene=="ゲームオーバー":
        text(WIDTH*0.5, HEIGHT*0.4, "GAME OVER", 60, "red")
        if timer>=30*5:
            scene = "タイトル"
            fire = False

    root.after(33, main)

root = tkinter.Tk()
root.title("ギャラクシー・ディフェンダー完全版")
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
