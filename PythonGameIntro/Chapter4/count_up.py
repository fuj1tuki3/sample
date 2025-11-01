import tkinter

n = 0
def count():
    global n
    n = n + 1
    cvs.delete("all")
    cvs.create_text(200, 100, text=n, font=("System", 80))
    root.after(1000, count)

root = tkinter.Tk()
root.title("リアルタイム処理")
cvs = tkinter.Canvas(width=400, height=200)
cvs.pack()
count()
root.mainloop()
