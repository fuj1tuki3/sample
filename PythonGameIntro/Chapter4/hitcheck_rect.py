import tkinter
import math

x1 = 200
y1 = 200
w1 = 80
h1 = 120
x2 = 400
y2 = 300
w2 = 240
h2 = 120

def move(e):
    global x1, y1
    x1 = e.x
    y1 = e.y
    col = "red"
    if abs(x1-x2)<=(w1+w2)/2 and abs(y1-y2)<=(h1+h2)/2:
        col = "pink"
    cvs.delete("RED_RECT")
    cvs.create_rectangle(x1-w1/2, y1-h1/2, x1+w1/2, y1+h1/2, fill=col, outline="white", tag="RED_RECT")

root = tkinter.Tk()
root.title("矩形によるヒットチェック")
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
cvs.create_rectangle(x1-w1/2, y1-h1/2, x1+w1/2, y1+h1/2, fill="red", outline="white", tag="RED_RECT")
cvs.create_rectangle(x2-w2/2, y2-h2/2, x2+w2/2, y2+h2/2, fill="blue", outline="white")
root.mainloop()
