from tkinter import *

def run():
    lab1.config(text=var.get())

root = Tk()
root.title("ex2")
root.configure(bg="#323232")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

w = screen_w/4
h = screen_h/2.5

x = (screen_w - w)/2
y = (screen_h - h)/2

root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.focus_force()

var = StringVar()
var.set(1)

lab1 = Label(root, text="123", font="微軟正黑體 20 bold", bg="#323232", fg="#fafafa")
lab1.pack(pady=5)

rad1 = Radiobutton(root, bg="#323232", fg="#ff0000", activebackground="#323232", activeforeground="#ff0000", text="第一項", font="微軟正黑體 20 bold", variable=var, value="第一項",command=run)
rad1.pack(pady=5)
rad2 = Radiobutton(root, bg="#323232", fg="#ff0000", activebackground="#323232", activeforeground="#ff0000", text="第二項", font="微軟正黑體 20 bold", variable=var, value="第二項",command=run)
rad2.pack(pady=5)

root.mainloop()