import tkinter as tk
import math

x1= 200
y1= 200
r1= 60
x2= 500
y2= 300
r2= 120

def pkey(e):
    global x1, y1
    if e.keysym == "Up":
        y1 -= 10
    if e.keysym == "Down":
        y1 += 10
    if e.keysym == "Left":
        x1 -= 10
    if e.keysym == "Right":
        x1 += 10
    d= math.sqrt((x1-x2)* (x1-x2)+ (y1-y2)* (y1-y2))
    col= "red"
    if d<= r1 + r2:
        col = "pink"
    cvs.delete("RED_CIRCLE")
    cvs.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill= col, outline= "white", tags="RED_CIRCLE")

root= tk.Tk()
root.title("円によるヒットチェック")
root.bind("<Key>", pkey)
cvs = tk.Canvas(width=800, height= 600, bg= "black")
cvs.pack()
cvs.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill= "red", outline= "white", tag= "RED_CIRCLE")
cvs.create_oval(x2-r2, y2-r2, x2+r2, y2+r2, fill="blue", outline="white")
root.mainloop()