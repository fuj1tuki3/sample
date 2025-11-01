import tkinter

FNT = ("Times New Roman", 40)
def move(e):
    cvs.delete("all")
    s = "({}, {})".format(e.x, e.y)
    cvs.create_text(400, 200, text=s, font=FNT)

root = tkinter.Tk()
root.title("マウスポインタの座標")
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=400)
cvs.pack()
root.mainloop()
