import tkinter
root = tkinter.Tk()
root.title("配列で色を定義")
cvs = tkinter.Canvas(width=840, height=160)

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(7):
    X = i*120
    cvs.create_rectangle(X, 0, X+120, 160, fill=rainbow[i], width=0)

cvs.pack()
root.mainloop()
