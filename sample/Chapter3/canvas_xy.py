import tkinter
root = tkinter.Tk()
root.title("x軸とy軸を引く")
cvs = tkinter.Canvas(width=800, height=600, bg="white")
cvs.create_line(0, 300, 800, 300, fill="red")
cvs.create_line(400, 0, 400, 600, fill="blue")
cvs.pack()
root.mainloop()
