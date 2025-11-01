"""s= "Hello python"
print(s)

print("テストメッセージです")
print('test')
print(6+2)
"""

#input
""" p_NAME = input("名前を入力してください：")
print(p_NAME,"さんですね。")

p_HP = 100
p_ATK = 10
p_DEF = 0

print("ステータス")
print("----------------")
print("名前　 ： ",p_NAME)
print("体力　 ： ",p_HP)
print("攻撃力 ： ",p_ATK)
print("防御力 ： ",p_DEF)
print("----------------") """

""" #list
life = [100,400,1000]
print("life[0]の値は",life[0])

p_HP = 500
life[0] = p_HP
print(life)

maze = [
    ["■","▽","■","■"],
    ["■","□","□","■"],
    ["■","■","!!","■"]
    ]

print(maze[0])
print(maze[1])
print(maze[2]) """

#リアルタイム処理--------------------------------------------------------------------------------------------------------------------------------------
import os
import tkinter as tk

n = 0

#グローバル変数
def count():
    global n, p_img
    n = n + 1
    cvs.delete("all")     #画面の表示を全削除
    cvs.create_image(300, 200, image=p_img)
    cvs.create_text(10, 10, text=n, font=("System", 10), fill="green")
    root.after(1000, count)     #after(ミリ秒, 呼び出す関数)

""" current_dir = os.getcwd()
print(f"現在の作業ディレクトリ: {current_dir}")
try:
    with open("image/test.png", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"エラー: {e}") """

#ウィンドウ表示
root = tk.Tk()
p_img = tk.PhotoImage(file="test/image/bg.png")
root.title("リアルタイム処理")
cvs = tk.Canvas(width=780, height=520, bg="#443344")
cvs.pack()
count()
root.mainloop()

#bind(イベントの種類, 呼び出す関数)
