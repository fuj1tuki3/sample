import random
import time
print("""
石取りゲームのルール：
石の数が乱数で決まります(15～22個)
先攻、後攻もランダムに決まります。
プレイヤーとコンピューターが交互に1～3個ずつ取ります。
最後の1個を取ることになったほうの負けです。
残りが3個以下で全部取ってしまうと負けとします。
""")

stone = random.randint(15, 22)
turn = random.randint(0, 1)
take = 0

while stone>0:
    turn = 1 - turn
    print("-"*40)
    for i in range(stone):
        print("●", end="")
    print(" 石の数:", stone)
    if turn==0:
        print("あなたの番")
        while True:
            i = input("いくつ取りますか？")
            if i=="1" and stone>0:
                take = 1
                break
            if i=="2" and stone>1:
                take = 2
                break
            if i=="3" and stone>2:
                take = 3
                break
        print("あなたは", take, "取りました")
    else:
        print("コンピューターの番")
        take = (stone-1)%4
        if take==0:
            take = random.randint(1,3)
            if take>stone: take = stone
        time.sleep(2)
        print(take, "取りました")
    stone = stone - take
    time.sleep(2)

print("-------------- ゲーム終了 --------------")
if turn==1:
    print("あなたの勝ち！")
else:
    print("コンピューターの勝ち！")
