from tkinter import *
from PIL import Image,ImageTk 


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


jpg1 = Image.open("Test1/ex2.jpg")
jpg1_w,jpg1_h = jpg1.size
print(jpg1_w, jpg1_h)
re=0.6
jpg1_resize = jpg1.resize((int(jpg1_w*re),int(jpg1_h*re)))
jpg1_tk = ImageTk.PhotoImage(jpg1_resize)


lab1 = Label(ui,
            text="我是\n標籤",
            bg="#3355aa",
            font="微軟正黑體 20 bold underline overstrike",
            fg="#ffffff",
            relief="groove",
            bd=5,
            padx=10,
            pady=10,

            image=jpg1_tk,
            compound="bottom"
            )

lab1.pack()
ui.mainloop()