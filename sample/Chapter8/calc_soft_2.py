import tkinter
import tkinter.messagebox

def btn_on(typ):
    try:
        v1 = float(e1.get())
        v2 = float(e2.get())
        if typ=="+": ans = str(v1+v2)
        if typ=="-": ans = str(v1-v2)
        if typ=="*": ans = str(v1*v2)
        if typ=="/":
            if v2==0:
                tkinter.messagebox.showinfo("","0で割ることはできません")
                return
            ans = str(v1/v2)
        lbl["text"] = "= "+ans
    except:
        tkinter.messagebox.showinfo("","エントリーに数字を入力してください")

def btn_add(): btn_on("+") # ＋ボタンを押した時に呼ぶ関数
def btn_sub(): btn_on("-") # －ボタンを押した時に呼ぶ関数
def btn_mul(): btn_on("*") # ×ボタンを押した時に呼ぶ関数
def btn_div(): btn_on("/") # ÷ボタンを押した時に呼ぶ関数

root = tkinter.Tk()
root.geometry("500x200")
root.title("計算アプリ2")
FNT = ("System", 12)
e1 = tkinter.Entry(width=10, font=FNT)
e1.place(x=10, y=10)
e2 = tkinter.Entry(width=10, font=FNT)
e2.place(x=210, y=10)
lbl = tkinter.Label(text="= ?", font=FNT)
lbl.place(x=300, y=10)
b1 = tkinter.Button(text="＋", font=FNT, command=btn_add)
b1.place(x=110, y=10)
b2 = tkinter.Button(text="－", font=FNT, command=btn_sub)
b2.place(x=110, y=50)
b3 = tkinter.Button(text="×", font=FNT, command=btn_mul)
b3.place(x=160, y=10)
b4 = tkinter.Button(text="÷", font=FNT, command=btn_div)
b4.place(x=160, y=50)
root.mainloop()
