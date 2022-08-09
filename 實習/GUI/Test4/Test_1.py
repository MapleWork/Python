from glob import glob
from logging import root
from tkinter import *

def pagy1():
    global root
    root = Tk()
    root.title("1")
    root.configure(bg="#000000")

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    w = screen_w/2
    h = screen_h/2

    x = (screen_w - w)/2
    y = (screen_h - h)/2

    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    root.focus_force()

    btn1 = Button (root, text="視窗2", bg="#ffffff", fg="#000000", width=30, anchor="center", font="微軟正黑體 20 bold", bd=2, command=c1)
    btn1.pack(side="bottom")

    root.mainloop()


def pagy2():
    global root2
    root2 = Tk()
    root2.title("2")
    root2.configure(bg="#555555")

    screen_w = root2.winfo_screenwidth()
    screen_h = root2.winfo_screenheight()

    w = screen_w/2
    h = screen_h/2

    x = (screen_w - w)/2
    y = (screen_h - h)/2

    root2.geometry("%dx%d+%d+%d" % (w,h,x,y))
    root2.focus_force()
    

    btn2 = Button (root2, text="反視窗1", bg="#ffffff", fg="#000000", width=30, anchor="center", font="微軟正黑體 20 bold", bd=2, command=c2)
    btn2.pack(side="bottom")

    root2.mainloop()


def c1():
    try:
        root.destroy()
    except:
        pass
    pagy2()

def c2():
    try:
        root2.destroy()
    except:
        pass
    pagy1()

pagy1()