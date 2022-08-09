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

lab1 = Label(ui,
            text="a",
            bg="#3355aa",
            fg="#ffffff",
            width=30,
            height=5,
            anchor="center",
            relief="groove",
            bd=2
            )

lab2 = Label(ui,
            text="b",
            bg="#aa55aa",
            fg="#ffffff",
            width=30,
            height=5,
            anchor="center",
            relief="groove",
            bd=2
            )

lab3 = Label(ui,
            text="c",
            bg="#33aa00",
            fg="#ffffff",
            width=30,
            height=5,
            anchor="center",
            relief="groove",
            bd=2
            )

lab1.pack(side="left", anchor="s", fill=X)
lab2.pack(side="top", anchor="e",expand=1 , fill=Y)
lab3.pack(side="top", anchor="n")

ui.mainloop()