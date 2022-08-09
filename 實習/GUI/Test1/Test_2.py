from tkinter import *

ui = Tk()
ui.title("tets1")
ui.configure(bg="lightyellow")

screen_w = ui.winfo_screenwidth()
screen_h = ui.winfo_screenheight()

w = screen_w/3
h = screen_h/3

x = 400
y = 200

x = (screen_w - w)/2
y = (screen_h - h)/2

p_x = screen_w/100
p_y = screen_h/100


ui.geometry("%dx%d+%d+%d" % (w,h,x,y))

lab1_type = '"寬：%d" %(screen_w) + "高：%d" %(screen_h), bg="lightblue", relief="groove"'


lab1 = Label(ui, 
            text="a寬：%d"%(screen_w) + "高：%d" %(screen_h),
            bg="lightgreen",
            relief="groove",
            width=20,
            height=3,
            anchor="s"
            )

lab1.pack(anchor="nw",side="top")


lab2 = Label(ui, 
            text="b寬：%d" % (screen_w) + "高：%d" % (screen_h),
            bg="white",
            relief="groove",
            width=20,
            height=3,
            anchor="center"
            )

lab2.pack(anchor="w",side="left",fill=BOTH,expand=True)


lab3 = Label(ui, 
            text="c寬：%d" % (screen_w) + "高：%d" % (screen_h),
            bg="lightblue",
            relief="groove",
            width=20,
            height=3,
            anchor="n",
            wraplength=100
            )

lab3.pack(anchor="w",side="bottom",fill=BOTH,expand=True)


ui.mainloop()