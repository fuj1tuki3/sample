import tkinter

FNT = ("Times New Roman", 60)
COLOR = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
def pkey(e):
    k = e.keysym
    if "1"<=k and k<="7":
        c = int(k)-1
        cvs.delete("all")
        cvs["bg"] = COLOR[c]
        cvs.create_text(300, 150, text=COLOR[c], fill="white", font=FNT)

root = tkinter.Tk()
root.title("1～7キーを押そう")
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=600, height=300)
cvs.pack()
root.mainloop()
