import tkinter as tk
import random as rnd
import os

WIDTH, HEIGHT = 1200, 720
FLOOR_Y = 600
SIZE = 24
BLOCKS = 50
floor = [1]*BLOCKS
space = 0
p1_x = 300
p1_y = FLOOR_Y
p1_yp = 0
p1_jump = False
scene = "タイトル"
timer = 0
dist = 0
mouse_x, mouse_y = 0, 0
mouse_c = False

def move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def click(e):
    global mouse_c
    mouse_c = True

def release(e):
    global mouse_c
    mouse_c = False

def text(x, y, txt, siz, col):
    fnt = ("System", siz)
    cvs.create_text(x+1, y+1, text=txt, font=fnt, fill="black")
    cvs.create_text(x, y, text=txt, font=fnt, fill=col)

def main():
    global floor
    global mouse_c, space, p1_x, p1_y, p1_yp, p1_jump, scene, timer, dist

    timer += 1
    cvs.delete("all")
    cvs.create_image(WIDTH/2, HEIGHT/2, image=bg)
    for i in range(BLOCKS):
        if floor[i]==1:
            cvs.create_image(i*SIZE+SIZE/2, FLOOR_Y+56, image=block)
    ani = int(timer/3)%4
    cvs.create_image(p1_x, p1_y, image=player[ani])
    text(120, 40, "distance "+str(dist), 30, "white")

    if scene == "タイトル":
        text(WIDTH/2, HEIGHT*0.2, "Jump Action Game", 30, "gold")
        text(WIDTH/2, HEIGHT*0.4, "HELP! PRINCESS", 60, "pink")
        text(WIDTH/2, HEIGHT*0.7, "Click to start.", 40, "skyblue")
        if mouse_c == True:
            floor = [1]*BLOCKS
            p1_x = 300
            p1_y = FLOOR_Y
            p1_yp = 0
            p1_jump = False
            scene = "ゲーム"
            timer = 0
            dist = 1000
    
    if scene == "ゲーム":
        if p1_x > mouse_x and p1_x > 30:
            p1_x -= 12
        if p1_x < mouse_x and p1_x < WIDTH-30:
            p1_x += 12
        if p1_jump == False:
            fx = int(p1_x / SIZE)
            if floor[fx]==0:    #穴に落ちる
                scene = "ゲームオーバー"
                timer = 0
            if mouse_c==True:
                p1_yp = -60
                p1_jump = True
        else:
            p1_y += p1_yp
            p1_yp += 6
            if p1_y >= FLOOR_Y:
                p1_jump = False
        
        dist -= 1
        if dist==0:
            scene = "ゲームクリア"
            timer = 0
        if dist%30==0:
            space = rnd.randint(2, 12)
        floor.pop(0)
        if space==0:
            floor.append(1)
        else:
            floor.append(0)
            space -= 1

    if scene=="ゲームオーバー":
        if timer < 50:
            p1_y += 6
        else:
            text(WIDTH/2, HEIGHT*0.33, "GAME OVER", 60, "red")
        if timer>150:
            scene = "タイトル"
    
    if scene=="ゲームクリア":
        cvs.create_image(p1_x+60, p1_y, image=princess)
        text(WIDTH/2, HEIGHT*0.33, "Congratulations!", 60, "pink")
        if timer>150:
            scene = "タイトル"
    
    root.after(50, main)

root = tk.Tk()
root.title("Jump Action Game")
root.resizable(False, False)
root.bind("<Motion>", move)
root.bind("<Button>", click)
root.bind("<ButtonRelease>", release)
cvs = tk.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))   #1つ上のディレクトを取得
img_path = os.path.join(BASE_DIR, "sample\\AppendixA", "image")
bg = tk.PhotoImage(file=img_path + "\\bg.png")
block = tk.PhotoImage(file=img_path + "\\block.png")
princess = tk.PhotoImage(file=img_path + "\\princess.png")
player = [
    tk.PhotoImage(file=img_path + "\\player0.png"),
    tk.PhotoImage(file=img_path + "\\player1.png"),
    tk.PhotoImage(file=img_path + "\\player0.png"),
    tk.PhotoImage(file=img_path + "\\player2.png")
]
main()
root.mainloop()