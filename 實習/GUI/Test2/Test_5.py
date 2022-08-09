from re import I
from tkinter import *

ui = Tk()
ui.title("ex3")
ui.configure(bg="lightyellow")

screen_w = ui.winfo_screenwidth()
screen_h = ui.winfo_screenheight()

w = screen_w/3
h = screen_h/2

x = (screen_w - w)/2
y = (screen_h - h)/2

ui.geometry("%dx%d+%d+%d" % (w,h,x,y))

i=0
def a1():
    global i
    i += 1
    lab1["text"] = "按鈕點擊次數："+str(i)

lab1 = Label(ui,
            text="本文內容...",
            bg="#ffffff",
            fg="#555555",
            width=30,
            height=2,
            anchor="w",
            relief="groove",
            bd=2
            )

btn1 = Button(ui,
            text="點擊",
            bg="#a9a9a9",
            fg="#000000",
            width=10,
            height=2,
            anchor="center",
            relief="groove",
            bd=2,
            activebackground="#ffffff",
            activeforeground="#000fff",
            command=a1
            )

lab1.pack(pady=40)
btn1.pack()

ui.mainloop()