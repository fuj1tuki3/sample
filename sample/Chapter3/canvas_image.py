import tkinter
root = tkinter.Tk()
root.title("キャンバスに画像を表示")
cvs = tkinter.Canvas(width=1080, height=720)
img = tkinter.PhotoImage(file="image/chap3_illust.png")
cvs.create_image(540, 360, image=img)
cvs.pack()
root.mainloop()
