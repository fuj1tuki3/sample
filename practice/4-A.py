import tkinter as tk
import os

scene = "タイトル"  # シーン管理用変数
p_x = 0
p_a = 0

def pkey(e):
    global scene
    if e.keysym == "space":
        scene = "ゲーム"
    if e.keysym == "Return":
        scene = "タイトル"

def main():
    global p_x, p_a
    cvs.delete("all")
    cvs.create_image(480, 320, image=bg)
    if scene == "タイトル":
        cvs.create_image(480, 320, image=ilst)
        cvs.create_text(480, 180, text="Ｎｉｎｊａ Ｒｕｎ", font= ("System", 100),fill="lime")
        cvs.create_text(480, 420, text="press <SPACE> key", font= ("System", 40),fill="cyan")
    if scene == "ゲーム":
        p_x += 40
        if p_x > 960:
            p_x = 0
        p_a = p_a + 1
        cvs.create_image(p_x, 400, image=player[p_a%4])
        print(p_a%4)
    root.after(100, main)
    
root = tk.Tk()
root.bind("<Key>", pkey)
cvs = tk.Canvas(width=960, height=640)
cvs.pack()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))   #1つ上のディレクトを取得
img_path = os.path.join(BASE_DIR, "sample\\Chapter4", "image")
print(img_path)
ilst = tk.PhotoImage(file=img_path+"\\illust.png")
bg = tk.PhotoImage(file=img_path+"\\bg.png")
player = [
    tk.PhotoImage(file=img_path+"\\ninja0.png"),
    tk.PhotoImage(file=img_path+"\\ninja1.png"),
    tk.PhotoImage(file=img_path+"\\ninja2.png"),
    tk.PhotoImage(file=img_path+"\\ninja3.png")
]
main()
root.mainloop()