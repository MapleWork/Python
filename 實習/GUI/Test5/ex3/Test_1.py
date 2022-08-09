from tkinter import *

def load_txt1():
    ent1.delete(0, "end")
    with open("Test5/ex3/txt1.txt", mode="r", encoding="utf-8") as file:
        data1 = file.read()
    ent1.insert(0,data1)

def output_ent1():
    lab1["text"]=ent1.get()


root = Tk()
root.title("ex3")
root.configure(bg="#323232")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

w=screen_w/2
h=screen_h/2

x = (screen_w - w)/2
y = (screen_h - h)/2

root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.focus_force()


btn1 = Button(root, text="讀取檔案", font="微軟正黑體 24 bold", command=load_txt1)
btn2 = Button(root, text="傳送資料", font="微軟正黑體 24 bold", command=output_ent1)
ent1 = Entry(root, font="微軟正黑體 36 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1, justify=CENTER)
lab1 = Label(root, text="目前無資料", font="微軟正黑體 36 bold")


btn1.pack(side="top", pady=10)
btn2.pack(pady=10)
ent1.pack(pady=10)
lab1.pack(pady=10)

root.mainloop()