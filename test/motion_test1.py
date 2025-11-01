import tkinter as tk

bgc = "#ffffff"

FNT = ("Times New Roman", 40)
def move(e):
    global bgc
    cvs.delete("all")
    cvs.create_rectangle(0, 0, 800, 400, fill=bgc) 
    s = "({},{})".format(e.x, e.y)
    FNTC = "#ffffff"
    if bgc == "#ffffff":
        FNTC = "#000000"
    else:
        FNTC = "#ffffff"
    cvs.create_text(400, 200, text=s, font= FNT, fill=FNTC)
    

def click(e):
    global bgc
    if bgc == "#ffffff":
        bgc = "#000000"
    else:
        bgc = "#ffffff"    
    cvs.delete("all")
    cvs.create_rectangle(0, 0, 800, 400, fill=bgc) 
    FNTC = "#ffffff"
    if bgc == "#ffffff":
        FNTC = "#000000"
    else:
        FNTC = "#ffffff"
    cvs.create_text(400, 200, text="クリックしました", font= FNT, fill=FNTC)

root = tk.Tk()
p_img = tk.PhotoImage(file="test/image/bg.png")
root.title("マウスポインタの座標")
root.bind("<Motion>", move)
root.bind("<Button>", click)
cvs = tk.Canvas(width= 800,height= 400)
cvs.pack()
root.mainloop()