import tkinter

WIDTH = 960
HEIGHT = 720
ball_x = WIDTH/2
ball_y = HEIGHT/5
ball_vx = 10
ball_vy = 10
bar_x = WIDTH/2
bar_y = HEIGHT-80
score = 0
hisco = 1000

def move(e): # マウスを動かした時
    global bar_x
    bar_x = e.x
    if bar_x<50:
        bar_x = 50
    if bar_x>WIDTH-50:
        bar_x = WIDTH-50

def text(x, y, txt, siz, col): # 影付き文字の表示
    fnt = ("Times New Roman", siz)
    cvs.create_text(x+1, y+1, text=txt, font=fnt, fill="black")
    cvs.create_text(x, y, text=txt, font=fnt, fill=col)

def main(): # メイン処理を行う関数
    global ball_x, ball_y, ball_vx, ball_vy, score, hisco
    ball_x = ball_x + ball_vx
    ball_y = ball_y + ball_vy
    if ball_x<10 or WIDTH-10<ball_x:
        ball_vx = -ball_vx
    if ball_y<10 or HEIGHT-10<ball_y:
        ball_vy = -ball_vy
    dx = ball_x - bar_x
    dy = ball_y - bar_y
    if -60<dx and dx<60 and -20<dy and dy<0:
        ball_vy = -10
        score = score + 100
        if score>hisco:
            hisco = score
    cvs.delete("all")
    cvs.create_image(WIDTH/2, HEIGHT/2, image=bg)
    cvs.create_oval(ball_x-10, ball_y-10, ball_x+10, ball_y+10, fill="red")
    cvs.create_rectangle(bar_x-50, bar_y-5, bar_x+50, bar_y+5, fill="blue")
    text(200, 30, "SCORE "+str(score), 28, "cyan")
    text(WIDTH-200, 30, "HI-SC "+str(hisco), 28, "gold")
    root.after(33, main)

root = tkinter.Tk()
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="bg.png")
main()
root.mainloop()
