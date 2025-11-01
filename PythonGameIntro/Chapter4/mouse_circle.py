import tkinter

mx = 400
my = 300
def move(e):
    global mx, my
    mx = e.x
    my = e.y

cx = 400
cy = 300
cr = 50
def main():
    global cx, cy
    if cy>my: cy -= 5
    if cy<my: cy += 5
    if cx>mx: cx -= 5
    if cx<mx: cx += 5
    cvs.delete("all")
    cvs.create_oval(cx-cr, cy-cr, cx+cr, cy+cr, fill="blue", outline="cyan")
    root.after(50, main)

root = tkinter.Tk()
root.title("ポインタを追い掛ける図形")
root.resizable(False, False)
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
main()
root.mainloop()
