print("好きな整数を入力してください")
print("何も入力せずにEnterを押すと終了します")
while True:
    s = input("入力する値は ")
    if s=="": break
    n = int(s)
    i = int(n/1000)
    t = i%10
    print("その数の千の位の数字は", t, "です")
