import tkinter
import random

WIDTH, HEIGHT = 1200, 720
FLOOR_Y = 600
SIZE = 24
BLOCKS = 50
floor = [1]*BLOCKS
space = 0
pl_x = 300
pl_y = FLOOR_Y
pl_yp = 0
pl_jump = False
scene = "タイトル"
timer = 0
dist = 0
mouse_x, mouse_y = 0, 0
mouse_c = False

def move(e): # マウスを動かした時
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def click(e): # クリックした時
    global mouse_c
    mouse_c = True

def release(e): # 離した時
    global mouse_c
    mouse_c = False

def text(x, y, txt, siz, col): # 影付き文字の表示
    fnt = ("Times New Roman", siz)
    cvs.create_text(x+1, y+1, text=txt, font=fnt, fill="black")
    cvs.create_text(x, y, text=txt, font=fnt, fill=col)

def main(): # メイン処理行う関数
    global floor
    global mouse_c, space, pl_x, pl_y, pl_yp, pl_jump, scene, timer, dist

    timer += 1
    cvs.delete("all")
    cvs.create_image(WIDTH/2, HEIGHT/2, image=bg)
    for i in range(BLOCKS):
        if floor[i]==1:
            cvs.create_image(i*SIZE+SIZE/2, FLOOR_Y+56, image=block)
    ani = int(timer/3)%4
    cvs.create_image(pl_x, pl_y, image=player[ani])
    text(120, 40, "distance "+str(dist), 30, "white")

    if scene=="タイトル": # タイトル画面
        text(WIDTH/2, HEIGHT*0.2, "Jump Action Game", 30, "gold")
        text(WIDTH/2, HEIGHT*0.4, "HELP! PRINCESS", 60, "pink")
        text(WIDTH/2, HEIGHT*0.7, "Click to start.", 40, "skyblue")
        if mouse_c==True:
            floor = [1]*BLOCKS
            pl_x = 300
            pl_y = FLOOR_Y
            pl_yp = 0
            pl_jump = False
            scene = "ゲーム"
            timer = 0
            dist = 1000

    if scene=="ゲーム": # ゲーム中
        if pl_x>mouse_x and pl_x>30:
            pl_x -= 12
        if pl_x<mouse_x and pl_x<WIDTH-30:
            pl_x += 12
        if pl_jump==False:
            fx = int(pl_x/SIZE)
            if floor[fx]==0: # 穴に落ちた？
                scene = "ゲームオーバー"
                timer = 0
            if mouse_c==True:
                pl_yp = -60
                pl_jump = True
        else:
            pl_y += pl_yp
            pl_yp += 6
            if pl_y>=FLOOR_Y: pl_jump = False
        dist -= 1
        if dist==0:
            scene = "ゲームクリア"
            timer = 0
        if dist%30==0: space = random.randint(2, 12)
        floor.pop(0)
        if space==0:
            floor.append(1)
        else:
            floor.append(0)
            space -= 1

    if scene=="ゲームオーバー": # ゲームオーバー
        if timer<50:
            pl_y += 6
        else:
            text(WIDTH/2, HEIGHT*0.33, "GAME OVER", 60, "red")
        if timer>150: scene = "タイトル"

    if scene=="ゲームクリア": # ゲームクリア
        cvs.create_image(pl_x+60, pl_y, image=princess)
        text(WIDTH/2, HEIGHT*0.33, "Congratulations!", 60, "pink")
        if timer>150: scene = "タイトル"

    root.after(50, main)

root = tkinter.Tk()
root.title("Jump Action Game")
root.resizable(False, False)
root.bind("<Motion>", move)
root.bind("<Button>", click)
root.bind("<ButtonRelease>", release)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
block = tkinter.PhotoImage(file="image/block.png")
princess = tkinter.PhotoImage(file="image/princess.png")
player = [
    tkinter.PhotoImage(file="image/player0.png"),
    tkinter.PhotoImage(file="image/player1.png"),
    tkinter.PhotoImage(file="image/player0.png"),
    tkinter.PhotoImage(file="image/player2.png")
]
main()
root.mainloop()
