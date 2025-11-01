import tkinter

WIDTH = 960
HEIGHT = 720
ball_x = WIDTH/2
ball_y = HEIGHT/5
ball_vx = 10
ball_vy = 10
bar_x = WIDTH/2
bar_y = HEIGHT-80

def main(): # メイン処理を行う関数
    global ball_x, ball_y, ball_vx, ball_vy
    ball_x = ball_x + ball_vx
    ball_y = ball_y + ball_vy
    if ball_x<10 or WIDTH-10<ball_x:
        ball_vx = -ball_vx
    if ball_y<10 or HEIGHT-10<ball_y:
        ball_vy = -ball_vy
    cvs.delete("all")
    cvs.create_image(WIDTH/2, HEIGHT/2, image=bg)
    cvs.create_oval(ball_x-10, ball_y-10, ball_x+10, ball_y+10, fill="red")
    cvs.create_rectangle(bar_x-50, bar_y-5, bar_x+50, bar_y+5, fill="blue")
    root.after(33, main)

root = tkinter.Tk()
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="bg.png")
main()
root.mainloop()
