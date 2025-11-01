def life_check(val):
    if val>0:
        print("まだ戦えます")
    else:
        print("もう戦えません")

print("体力値100で関数を実行")
life_check(100)
print("体力値0で関数を実行")
life_check(0)
