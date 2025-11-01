import tkinter
import math
import maze_data1

WIDTH, HEIGHT = 1200, 600
MAZE = maze_data1.DATA
ROW, COL, SIZE, COLOR1, COLOR2 = maze_data1.get_param()
pl_x, pl_y, pl_a = maze_data1.init_player()
WALL = 9
FNT = ("Times New Roman", 20)

def wall(x, y): # 壁の判定
    ax, ay = int(x/SIZE), int(y/SIZE)
    if MAZE[ay][ax]==WALL: return True
    return False

def pkey(e): # キー入力（プレイヤーの移動）
    global pl_x, pl_y, pl_a
    key = e.keysym
    if key=="Left": pl_a -= 10
    if key=="Right": pl_a += 10
    if pl_a<0: pl_a += 360
    if pl_a>359: pl_a -= 360
    s = 0
    if key=="Up": s = 1
    if key=="Down": s = -1
    if s!=0:
        xp = s*math.cos(math.pi*pl_a/180)
        yp = s*math.sin(math.pi*pl_a/180)
        for i in range(5):
            if wall(pl_x+xp, pl_y+yp): break
            pl_x += xp
            pl_y += yp

def draw_3d_space(sx, sy, sa): # 三次元空間を計算
    cvs.create_rectangle(480, 0, 1200, 300, fill="navy", outline="")
    for i in range(20): # 床の描画
        col = "#{:02x}{:02x}{:02x}".format(192-8*i, 224-8*i, 255-8*i)
        cvs.create_rectangle(480, 300+15*i, 1200, 300+15*(i+1), fill=col, outline="")
    wall_w = 4
    wall_x = 482
    wall_y = 300
    rd = -45
    for i in range(180):
        rx, ry = sx, sy
        xp = math.cos(math.pi*(sa+rd)/180)/5
        yp = math.sin(math.pi*(sa+rd)/180)/5
        while wall(rx, ry)==False:
            rx += xp
            ry += yp
        cvs.create_line(sx, sy, rx, ry, fill="yellow")
        dis = math.sqrt((rx-sx)**2 + (ry-sy)**2) * math.cos(math.pi*rd/180)
        wall_h = 8000/dis
        if wall_h>HEIGHT: wall_h = HEIGHT
        col = COLOR1
        if wall(rx-0.5, ry)==False or wall(rx+0.5, ry)==False:
            col = COLOR2
        cvs.create_rectangle(wall_x-wall_w/2, wall_y-wall_h/2, wall_x+wall_w/2, wall_y+wall_h/2, fill=col, outline="")
        wall_x += wall_w
        rd = rd + 0.5

COLOR = ["black", "blue", "black", "black", "black", "black", "black", "black", "black", "gray"]

def draw_2d_map(): # 二次元の地図を表示
    for y in range(ROW):
        for x in range(COL):
            X, Y = x*SIZE, y*SIZE
            cvs.create_rectangle(X, Y, X+SIZE, Y+SIZE, fill=COLOR[MAZE[y][x]])
    cvs.create_oval(pl_x-5, pl_y-5, pl_x+5, pl_y+5, fill="red")
    cvs.create_text(200, 500, text="("+str(int(pl_x))+","+str(int(pl_y))+")", font=FNT, fill="white")
    cvs.create_text(200, 550, text=pl_a, font=FNT, fill="white")

def main(): # メイン処理
    cvs.delete("all")
    draw_2d_map()
    draw_3d_space(pl_x, pl_y, pl_a)
    if MAZE[int(pl_y/SIZE)][int(pl_x/SIZE)]==1:
        cvs.create_text(WIDTH/2, HEIGHT/2, text="おめでとう！\nゴールに到着しました。", font=FNT, fill="white")
        return
    root.after(50, main)

root = tkinter.Tk()
root.title("3Dダンジョン ラビリンス・エクスプローラー")
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT, bg="black")
cvs.pack()
main()
root.mainloop()
