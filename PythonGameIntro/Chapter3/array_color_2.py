import tkinter
root = tkinter.Tk()
root.title("二次元配列で色を定義")
cvs = tkinter.Canvas(width=800, height=600, bg="black")

color = [
    ["brown", "red", "orange", "gold"],
    ["darkgreen", "green", "limegreen", "lime"],
    ["navy", "blue", "skyblue", "cyan"]
]

for y in range(3):
    for x in range(4):
        X = x*200
        Y = y*200
        cvs.create_oval(X, Y, X+200, Y+200, fill=color[y][x])

cvs.pack()
root.mainloop()
