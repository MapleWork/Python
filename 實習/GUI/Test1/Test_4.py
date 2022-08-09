from tkinter import *

ui = Tk()
ui.title("ex3")
ui.configure(bg="lightyellow")

screen_w = ui.winfo_screenwidth()
screen_h = ui.winfo_screenheight()

w = screen_w/3
h = screen_h/3

x = (screen_w - w)/2
y = (screen_h - h)/2

ui.geometry("%dx%d+%d+%d" % (w,h,x,y))


lab1 = Label(ui,
            text="我是\n標籤",
            bg="#3355aa",
            width=20,
            height=5,
            font="微軟正黑體 20 bold underline overstrike",
            fg="#ffffff",
            anchor="se",
            relief="groove",
            bd=5,
            padx=10,
            pady=10
            )

lab1.pack()
ui.mainloop()