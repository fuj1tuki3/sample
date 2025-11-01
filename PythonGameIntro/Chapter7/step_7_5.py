import tkinter
import random

WIDTH, HEIGHT = 480, 720
bg_y = 0
pl_x = 0
pl_y = 0
COM_MAX = 10
com_x = [0]*COM_MAX
com_y = [0]*COM_MAX

def set_car(): # 車の初期座標を代入
    global pl_x, pl_y
    pl_x = int(WIDTH/2)
    pl_y = int(HEIGHT/2)
    for i in range(COM_MAX):
        com_x[i] = 172+46*(i%4)
        com_y[i] = 560+60*int(i/4)

def move(e): # マウスを動かした時
    global pl_x, pl_y
    pl_x = int(0.8*pl_x+0.2*e.x)
    pl_y = int(0.8*pl_y+0.2*e.y)
    if pl_x<160: pl_x = 160
    if pl_x>320: pl_x = 320

def main(): # メイン処理を行う関数
    global bg_y
    bg_y = (bg_y+30)%HEIGHT
    cvs.delete("all")
    cvs.create_image(240, bg_y-360, image=bg)
    cvs.create_image(240, bg_y+360, image=bg)
    cvs.create_image(pl_x, pl_y, image=mycar)

    for i in range(COM_MAX): # 敵の車の処理
        com_y[i] = com_y[i] + 5 + i%5
        if com_y[i]>HEIGHT+40:
            com_x[i] = random.randint(160, 320)
            com_y[i] = -60*i
        cvs.create_image(com_x[i], com_y[i], image=comcar)
        dx = abs(com_x[i]-pl_x)
        dy = abs(com_y[i]-pl_y)
        if dx<26 and dy<44:
            cvs.create_rectangle(pl_x-16, pl_y-24, pl_x+16, pl_y+24, fill="white")
    root.after(33, main)

root = tkinter.Tk()
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
mycar = tkinter.PhotoImage(file="image/car_red.png")
comcar = tkinter.PhotoImage(file="image/car_yellow.png")
set_car()
main()
root.mainloop()
