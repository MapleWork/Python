from tkinter import *



def win1():

# 練習一
    win1 = Tk()
    win1.title("smile")
    win1.geometry("600x400+10+10")
    win1.maxsize(500,300)
    win1.minsize(400,100)
    win1.configure(bg='#fffaaf')
    win1.iconbitmap("Test1/icon1.ico")

    win1.mainloop()


def ui():

# 練習二
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

    ui.mainloop()


#win1()
ui()