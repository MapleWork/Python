import secrets
from tkinter import *
import json

data = {"acc":"a12345678", "pow":"123456"}
with open("Test5/ex3/user.json", mode="w", encoding="utf-8-sig") as file:
    json.dump(data, file, ensure_ascii=False)

with open("Test5/ex3/user.json", mode="r", encoding="utf-8-sig") as file:
    data = json.load(file)

print(data)

def login():
    acc_data = data["acc"]
    pow_data = data["pow"]

    if acc_data == acc1.get() and pow_data == pow1.get():
        lab4["text"] = "登入成功"
    else:
        lab4["text"] = "登入失敗"

def cls_acc_pow():
    acc1.delete(0, END)
    pow1.delete(0, "end")

def reset_pow():
    def ui_reset_pow():
        with open("Test5/ex3/user.json", mode="w+", encoding="utf-8-sig") as file:
            data["pow"] = ent1.get()
            print(data)
            json.dump(data, file, ensure_ascii=False)

        re_pow_ui.destroy()

    re_pow_ui = Tk()
    re_pow_ui.title("重設密碼")
    re_pow_ui.configure(bg="#323232")

    screen_w = re_pow_ui.winfo_screenwidth()
    screen_h = re_pow_ui.winfo_screenheight()

    w = screen_w/2
    h = screen_h/2

    x = (screen_w - w)/2
    y = (screen_h - h)/2

    re_pow_ui.geometry("%dx%d+%d+%d" % (w,h,x,y))
    re_pow_ui.focus_force()


    lab1 = Label(re_pow_ui, text="輸入密碼", font="微軟正黑體 12 bold", bg="#323232", fg="#f0f0f0")
    btn1 = Button(re_pow_ui, text="重設", font="微軟正黑體 12 bold", width="10", command=ui_reset_pow)
    ent1 = Entry(re_pow_ui, font="微軟正黑體 12 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1)

    lab1.pack()
    ent1.pack()
    btn1.pack(pady=10)

    re_pow_ui.mainloop()


root = Tk()
root.title("ex3-1")
root.configure(bg="#323232")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

w=screen_w/2
h=screen_h/2

x = (screen_w - w)/2
y = (screen_h - h)/2

root.geometry("%dx%d+%d+%d" % (w,h,x,y))

root.focus_force()


lab1 = Label(root, text="後台系統", font="微軟正黑體 36 bold", bg="#323232", fg="#f0f0f0")
lab2 = Label(root, text="帳號", font="微軟正黑體 12 bold", bg="#323232", fg="#f0f0f0")
lab3 = Label(root, text="密碼", font="微軟正黑體 12 bold", bg="#323232", fg="#f0f0f0")
lab4 = Label(root, text="", font="微軟正黑體 10 bold", bg="#323232", fg="#f03333")

login1 = Button(root, text="登入", font="微軟正黑體 12 bold", width="10", command=login)
re1 = Button(root, text="清除", font="微軟正黑體 12 bold", width="10", command=cls_acc_pow)
repow1 = Button(root, text="重設密碼", font="微軟正黑體 12 bold", width="10", command=reset_pow)

acc1 = Entry(root, font="微軟正黑體 12 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1)
pow1 = Entry(root, font="微軟正黑體 12 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1, show="*")

lab2.pack(pady=5)
acc1.pack(pady=3)

lab3.pack(pady=5)
pow1.pack(pady=3)

lab4.pack(pady=5)
login1.pack(pady=5)
re1.pack(pady=5)
repow1.pack(pady=5)

root.mainloop()