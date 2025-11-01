import tkinter as tk
import random as rnd
import os

FNT = ("System", 40)
holes = [0,0,0,0,0]
scene = "タイトル"
score = 0
time = 0
key = ""

# #rnd.seed(0)
# for i in range(20):
#     r = rnd.randint(0, 99)
#     print(r, end=",")

def pkey(e):
    global scene, score, time, key
    key = e.keysym

def main():
    global scene, score, time, key

    cvs.delete("all")
    for i in range(5):
        x = 200 * i + 100
        cvs.create_image(x, 160, image=img[holes[i]])
        cvs.create_text(x, 280, text=i+1, font=FNT, fill="yellow")
        if holes[i] == 2:
            holes[i] = 0

    cvs.create_text(200, 30, text="SCORE "+str(score), font=FNT, fill="white")
    cvs.create_text(800, 30, text="TIME "+str(time), font=FNT, fill="yellow")

    if scene == "タイトル":
        cvs.create_text(500, 100, text="Mogura Tataki Game", font=FNT, fill="pink")
        cvs.create_text(500, 200,text= "[S]tart", font=FNT, fill="cyan")
        if key=="s":
            scene = "ゲーム"
            score = 0
            time = 100

    if scene == "ゲーム":
        r = rnd.randint(0, 4)
        holes[r] = 1
        if "1"<= key and key <="5":
            m = int(key)-1
            x = m*200+100
            cvs.create_image(x, 60, image=ham)
            if holes[m] == 1:
                holes[m] = 2
                score = score+100
        time = time - 1
        if time == 0:
            scene = "ゲームオーバー"
    # cvs.create_image(x, 60, image=ham)
    # r = rnd.randint(0, 4)
    # holes[r] = 1

    # if "1"<= key and key <="5":
    #     m = int(key)-1
    #     x = m*200+100
    #     cvs.create_image(x, 60, image=ham)
    #     if holes[m] == 1:
    #         holes[m] = 2
    # if holes[r] == 0:
    #     holes[r] = 1
    # else:
    #     holes[r] = 0
    # print(holes)

    if scene=="ゲームオーバー":
        cvs.create_text(500, 100, text="GAME END", font=FNT, fill="red")
        cvs.create_text(500, 200, text="[R]eplay", font=FNT, fill="lime")
        if key == "r":
            scene = "ゲーム"
            score = 0
            time = 100

    key = ""
    root.after(200, main)

root = tk.Tk()
root.title("モグラたたきゲーム")
root.resizable(False, False)
root.bind("<Key>", pkey)
cvs = tk.Canvas(width=1000, height=320)
cvs.pack()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))   #1つ上のディレクトを取得
img_path = os.path.join(BASE_DIR, "sample\\Chapter5", "image")
img = [
    tk.PhotoImage(file=img_path +"\\hole.png"),
    tk.PhotoImage(file=img_path +"\\mole.png"),
    tk.PhotoImage(file=img_path +"\\hit.png")
]

ham = tk.PhotoImage(file=img_path +"\\hammer.png")
main()
root.mainloop()