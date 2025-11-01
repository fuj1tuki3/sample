import tkinter as tk

def move(e):
    cvs.delete("all")
    s = "({}, {})".format(e.x, e.y)
    cvs.create_text(400, 200, text=s)

root = tk.Tk()
root.title("マウスポインタの座標")
root.bind("<Motion>", move)
cvs = tk.Canvas(width=800, height=400)
cvs.pack()
root.mainloop()