import tkinter
import tkinter.messagebox

def btn_on():
    try:
        v1 = float(e1.get())
        v2 = float(e2.get())
        ans = str(v1+v2)
        l2["text"] = "= "+ans
    except:
        tkinter.messagebox.showinfo("","エントリーに数字を入力してください")

root = tkinter.Tk()
root.geometry("400x200")
root.title("計算アプリ")
e1 = tkinter.Entry(width=10)
e1.place(x=10, y=10)
l1 = tkinter.Label(text="+")
l1.place(x=110, y=10)
e2 = tkinter.Entry(width=10)
e2.place(x=170, y=10)
l2 = tkinter.Label(text="= ?")
l2.place(x=260, y=10)
bu = tkinter.Button(text="計算", command=btn_on)
bu.place(x=10, y=50)
root.mainloop()
