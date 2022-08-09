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

lab1=Label(ui,
            text="A",
            bg="#ffffff",
            fg="#000000",
            width=20,
            height=4,
            anchor="center",
            relief="groove",
            bd=2
            )

lab2=Label(ui,
            text="B",
            bg="#ffffff",
            fg="#000000",
            width=20,
            height=4,
            anchor="center",
            relief="groove",
            bd=2
            )

lab3=Label(ui,
            text="C",
            bg="#ffffff",
            fg="#000000",
            width=20,
            height=4,
            anchor="center",
            relief="groove",
            bd=2
            )

lab4=Label(ui,
            text="D",
            bg="#ffffff",
            fg="#000000",
            width=20,
            height=4,
            anchor="center",
            relief="groove",
            bd=2
            )

lab5=Label(ui,
            text="E",
            bg="#ffffff",
            fg="#000000",
            width=20,
            height=4,
            anchor="center",
            relief="groove",
            bd=2
            )

lab6=Label(ui,
            text="F",
            bg="#ffffff",
            fg="#000000",
            width=20,
            height=4,
            anchor="center",
            relief="groove",
            bd=2
            )


lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1)
lab3.grid(row=0,column=2)

lab4.grid(row=1,column=0)
lab5.grid(row=1,column=1)
lab6.grid(row=1,column=2)


ui.mainloop()