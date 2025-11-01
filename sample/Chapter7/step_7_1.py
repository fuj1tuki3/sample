import tkinter

WIDTH, HEIGHT = 480, 720
bg_y = 0

def main(): # メイン処理を行う関数
    global bg_y
    bg_y = bg_y + 2
    if bg_y>=HEIGHT: bg_y = bg_y - HEIGHT
    cvs.delete("all")
    cvs.create_image(240, bg_y-360, image=bg)
    cvs.create_image(240, bg_y+360, image=bg)
    root.after(33, main)

root = tkinter.Tk()
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
main()
root.mainloop()
