import tkinter

WIDTH, HEIGHT = 480, 720
bg_y = 0
pl_x = int(WIDTH/2)
pl_y = int(HEIGHT/2)

def move(e): # マウスを動かした時
    global pl_x, pl_y
    pl_x = int(0.8*pl_x+0.2*e.x)
    pl_y = int(0.8*pl_y+0.2*e.y)
    if pl_x<160: pl_x = 160
    if pl_x>320: pl_x = 320

def main(): # メイン処理を行う関数
    global bg_y
    bg_y = (bg_y+2)%HEIGHT
    cvs.delete("all")
    cvs.create_image(240, bg_y-360, image=bg)
    cvs.create_image(240, bg_y+360, image=bg)
    cvs.create_image(pl_x, pl_y, image=mycar)
    root.after(33, main)

root = tkinter.Tk()
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
mycar = tkinter.PhotoImage(file="image/car_red.png")
main()
root.mainloop()
