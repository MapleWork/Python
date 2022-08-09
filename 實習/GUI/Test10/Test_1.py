import json
import tkinter as tk
from tkinter import *
from  tkinter import ttk 
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
from click import command

m=0
name_lab_list=[]
name_content_list=[]

phone_lab_list=[]
phone_content_list=[]

email_lab_list=[]
email_content_list=[]

data_file_path=""

with open("Test9/login.json", mode="r", encoding="utf-8-sig") as file:
    data = json.load(file)

def c_json():
    data1 = []
    data2 = []
    data3 = []

    for i in name_lab_list:
        data1.append(i.get())
        
    for i in name_content_list:
        data2.append(i.get()) 

    data3=dict(zip(data1,data2))

    file_path =asksaveasfilename(initialdir = "./",initialfile="user",defaultextension="json",
                                 title = "選擇儲存資料夾",filetypes = (("json","*.json"),("all files","*.*")))
                                 
    if file_path =="":
        return
    
    with open(file_path,mode="w",encoding="utf-8-sig") as file:
        json.dump(data3,file,ensure_ascii=False)


def cls_():
    global m
    global data_file_path

    for i in name_content_list:
        i.destroy()
    for i in phone_content_list:
        i.destroy()
    for i in email_content_list:
        i.destroy()

    m=0
    name_content_list.clear()
    phone_content_list.clear()
    email_content_list.clear()
    data_file_path = ""


def add():
    global m

    exec('name_content_'+str(m)+'=Entry(root,font="微軟正黑體 16 bold",selectbackground="#323232",selectforeground="#ffffff",selectborderwidth=1)')
    exec('name_content_'+str(m)+'.grid(row='+(str(3+m))+',column=0,pady=10,padx=10,sticky=W+E)')
    name_content_list.append(eval('name_content_'+str(m)))

    exec('phone_content_'+str(m)+'=Entry(root,font="微軟正黑體 16 bold",selectbackground="#323232",selectforeground="#ffffff",selectborderwidth=1)')
    exec('phone_content_'+str(m)+'.grid(row='+(str(3+m))+',column=1,pady=10,sticky=W+E,padx=10)')
    phone_content_list.append(eval('phone_content_'+str(m)))

    exec('email_content_'+str(m)+'=Entry(root,font="微軟正黑體 16 bold",selectbackground="#323232",selectforeground="#ffffff",selectborderwidth=1)')
    exec('email_content_'+str(m)+'.grid(row='+(str(3+m))+',column=2,pady=10,padx=10,sticky=W+E)')
    email_content_list.append(eval('email_content_'+str(m)))

    m+=1


def create():
    global root
    root = Tk()
    root.title("新增人員")
    root.configure(bg="#323232")

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    w = screen_w/1.5
    h = screen_h/1.5

    x = (screen_w - w)/2
    y = (screen_h - h)/2

    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    root.focus_force()


    btn1 = Button(root, text="+", font="微軟正黑體 16 bold", width="10", command=add)
    btn2 = Button(root, text="讀取", font="微軟正黑體 16 bold", width="10")
    btn3 = Button(root, text="儲存", font="微軟正黑體 16 bold", width="10")
    btn4 = Button(root, text="另存", font="微軟正黑體 16 bold", width="10", command=c_json)
    btn5 = Button(root, text="清除", font="微軟正黑體 16 bold", width="10", command=cls_)

    name = Label(root,text="姓名",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")
    phone = Label(root,text="電話",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")
    email = Label(root,text="信箱",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")

    btn1.grid(row=1,column=0,pady=10,padx=10)
    btn2.grid(row=1,column=1,pady=10,padx=10)
    btn3.grid(row=1,column=2,pady=10,padx=10)
    btn4.grid(row=1,column=3,pady=10,padx=10)

    name.grid(row=2,column=0,pady=10,padx=10)
    phone.grid(row=2,column=1,pady=10,padx=10)
    email.grid(row=2,column=2,pady=10,padx=10)
    btn5.grid(row=2,column=3,pady=10,padx=10)

    root.mainloop()

def page1():
    global root
    root = Tk()
    root.title("新增人員")
    root.configure(bg="#323232")

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    w = screen_w/2
    h = screen_h/2

    x = (screen_w - w)/2
    y = (screen_h - h)/2

    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    root.focus_force()

    btn1 = Button(root, text="新增人員", font="微軟正黑體 16 bold", width="10",command=create)
    

    name_ent1 = Label(root,text="姓名",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")
    phone_ent2 = Label(root,text="電話",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")
    email_ent3 = Label(root,text="信箱",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")

    ent1 = Label(root,text="123",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")
    ent2 = Label(root,text="",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")
    ent3 = Label(root,text="",font="微軟正黑體 16 bold",width="10",bg="#323232",fg="#f0f0f0")

    
    name_ent1.grid(row=1,column=0,pady=10,padx=10)
    phone_ent2.grid(row=1,column=1,pady=10,padx=10)
    email_ent3.grid(row=1,column=2,pady=10,padx=10)

    btn1.grid(row=1,column=3,pady=10,padx=10)

    ent1.grid(row=2,column=0,pady=10,padx=10)
    ent2.grid(row=2,column=1,pady=10,padx=10)
    ent3.grid(row=2,column=2,pady=10,padx=10)

    root.mainloop()


def login():
    acc_data = data["acc"]
    pow_data = data["pow"]
    
    if acc_data == acc1.get() and pow_data == pow1.get():
        lab5["text"] = "登入成功"
        page1()

    else:
        lab5["text"] = "登入失敗"
        acc1.delete(0, END)
        pow1.delete(0, "end")


def reset_pow():
    def ui_reset_pow():
        with open("Test10/login.json",mode="w+",encoding="utf-8-sig") as file:
            data["pow"]=ent1.get() 
            print(data)
            json.dump(data,file,ensure_ascii=False)

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
    ent1 = Entry(re_pow_ui, font="微軟正黑體 12 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1, show="*")

    lab1.pack()
    ent1.pack()
    btn1.pack(pady=10)

    re_pow_ui.mainloop()


root = Tk()
root.title("Project")
root.configure(bg="#323232")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

w=screen_w/2
h=screen_h/1.8

x = (screen_w - w)/2
y = (screen_h - h)/2

root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.focus_force()

jpg1 = Image.open("Test9/1.jpg")
jpg1_w,jpg1_h = jpg1.size
re=0.6
jpg1_resize = jpg1.resize((int(jpg1_w*re),int(jpg1_h*re)))
jpg1_tk = ImageTk.PhotoImage(jpg1_resize)


lab = Label(root, bg="#323232", fg="#ffffff", relief="groove", bd=5, padx=5, pady=5, image=jpg1_tk)
lab2 = Label(root, text="帳號：", font="微軟正黑體 16 bold", bg="#323232", fg="#f0f0f0")
lab3 = Label(root, text="密碼：", font="微軟正黑體 16 bold", bg="#323232", fg="#f0f0f0")
lab5 = Label(root, text="", font="微軟正黑體 12 bold", bg="#323232", fg="#f03333")

login1 = Button(root, text="登入", font="微軟正黑體 12 bold", width="10", command=login)
repow1 = Button(root, text="忘記密碼", font="微軟正黑體 12 bold", width="10", command=reset_pow)

acc1 = Entry(root, font="微軟正黑體 12 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1)
pow1 = Entry(root, font="微軟正黑體 12 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1, show="*")


lab.place(relx=0.3,rely=0.05)

lab2.place(relwidth=0.2,relheight=0.05,relx=0.1,rely=0.55)
acc1.place(relwidth=0.2,relheight=0.05,relx=0.25,rely=0.55)

lab3.place(relwidth=0.2,relheight=0.05,relx=0.43,rely=0.55)
pow1.place(relwidth=0.2,relheight=0.05,relx=0.58,rely=0.55)

lab5.place(relwidth=0.15,relheight=0.08,relx=0.43,rely=0.8)

login1.place(relwidth=0.15,relheight=0.08,relx=0.55,rely=0.68)
repow1.place(relwidth=0.15,relheight=0.08,relx=0.3,rely=0.68)

root.mainloop()