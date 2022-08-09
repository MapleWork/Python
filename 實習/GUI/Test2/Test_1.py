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
            text="輸入搜尋文字",
            bg="#ffffff",
            fg="#555555",
            width=30,
            height=2,
            anchor="w",
            relief="groove",
            bd=2
            )

lab2=Label(ui,
            text="搜尋",
            bg="#999999",
            fg="#000000",
            width=10,
            height=2,
            anchor="center",
            relief="groove",
            bd=2
            )
            
lab3=Label(ui,
            text="(本文內容)",
            bg="#ffffff",
            fg="#000000",
            width=30,
            height=5,
            anchor="center",
            relief="groove",
            bd=2
            )


lab3.pack(side="bottom",
            padx=5,
            pady=5,
            fill=BOTH,
            expand=1
            )

lab1.pack(side="left",
            anchor="n",
            padx=5,
            pady=5,
            fill=X,
            expand=1
            )

lab2.pack(side="left",
            anchor="ne",
            padx=5,
            pady=5,
            fill=X
            )



ui.mainloop()