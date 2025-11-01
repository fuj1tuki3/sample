QUESTION = [
    "任天堂の国民的人気キャラ「マリオ」の弟の名前は？",
    "モンスターボールを投げて「ポケモン」を仲間にする人気RPGといえば？",
    "RPG「ドラゴンクエスト」で最初に出てくるマスコット的な青い敵は？"
    ]
ANSWER = ["ルイージ", "ポケットモンスター",  "スライム"]

def quiz():
    score = 0
    for i in range(3):
        ans = input(QUESTION[i])
        if ans==ANSWER[i]:
            print("正解です！")
            score = score + 1
        else:
            print("違います。答えは"+ANSWER[i])
    print(score, "問、正解しました。")

quiz()
