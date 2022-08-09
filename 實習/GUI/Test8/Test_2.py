from tkinter import *

ui = Tk()
ui.title("計算練習")
ui.configure(bg="#efefef")
screen_w = ui.winfo_screenwidth()
screen_h = ui.winfo_screenheight()

global ui_w, ui_h
ui_w = screen_w/3
ui_h = screen_h/2

x = (screen_w - ui_w)/2
y = (screen_h - ui_h)/2

ui.geometry("%dx%d+%d+%d" % (ui_w,ui_h,x,y))
ui.focus_force()


def run_1():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '%0.2f+%0.2f=%0.2f\n' % (a,b, a+b)
    txt.insert(END, s)
    inp1.delete(0, END)
    inp2.delete(0, END)


lab1 = Label(ui, text='輸入兩個數，按下按鈕進行加法計算')
inp1 = Entry(ui)
inp2 = Entry(ui)
txt = Text(ui)


btn = Button(ui, text="執行",anchor="center",command=run_1)


lab1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)
btn.place(relx=0.35,rely=0.4, relwidth=0.3, relheight=0.1)
txt.place(rely=0.6, relheight=0.4)

ui.mainloop()