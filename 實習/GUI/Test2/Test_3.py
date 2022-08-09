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

ui.columnconfigure(0,weight=1)
ui.rowconfigure(1,weight=1)

lab1=Label(ui,
            text="輸入搜尋文字",
            bg="#ffffff",
            fg="#555555",
            width=30,
            height=5,
            anchor="w",
            relief="groove",
            bd=2
            )

lab2=Label(ui,
            text="搜尋",
            bg="#a9a9a9",
            fg="#000000",
            width=10,
            height=5,
            anchor="center",
            relief="groove",
            bd=2
            )

lab3=Label(ui,
            text="(本文內容...)",
            bg="#ffffff",
            fg="#000000",
            width=30,
            height=5,
            anchor="nw",
            relief="groove",
            bd=2
            )

lab1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=W+E+S+N)

ui.mainloop()