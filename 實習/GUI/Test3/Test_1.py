from tkinter import *

ui = Tk()
ui.title("濾鏡")
ui.configure(bg="#efefef")

screen_w = ui.winfo_screenwidth()
screen_h = ui.winfo_screenheight()

global ui_w, ui_h
ui_w = screen_w/3
ui_h = screen_h/2

x = (screen_w - ui_w)/2
y = (screen_h - ui_h)/2

ui.geometry("%dx%d+%d+%d" % (ui_w,ui_h,x,y))


def open_image():
    print("123")

def lab4_img():
    print("123")

def image_blur():
    print("123")

def image_sharpen():
    print("123")

def image_contour():
    print("123")

def aa():
    print("123")

def image_save():
    print("123")

def btn_view_down(event):
    print("123")

def btn_view_up(event):
    print("123")


lab1=Label(ui,
            text="原始照片",
            bg="#efefef",
            font="微軟正黑體 16 bold underline", 
            fg="#333333"
            )

lab2=Label(ui,
            text="",
            bg="#ffffff",
            font="微軟正黑體 20 underline", 
            fg="#333333",
            relief="groove",
            bd=1
            )

lab3=Label(ui,
            text="濾淨效果",
            bg="#efefef",
            font="微軟正黑體 16 bold underline", 
            fg="#333333"
            )

lab4=Label(ui,
            text="",
            bg="#ffffff",
            font="微軟正黑體 20 underline", 
            fg="#333333",
            relief="groove",
            bd=1
            )


btn1=Button(ui,
            text="疊加",
            bg="#a9a9a9",
            fg="#000000",
            font="微軟正黑體 16 bold", 
            anchor="center",
            relief="groove",
            bd=2,
            activebackground="#ffffff",
            activeforeground="#000fff",
            command=aa
            )

btn_open=Button(ui,
                text="開啟圖片",
                bg="#a9a9a9",
                fg="#000000",
                font="微軟正黑體 16 bold", 
                anchor="center",
                relief="groove",
                bd=2,
                activebackground="#ffffff",
                activeforeground="#000fff",
                command=open_image
                )

btn_save=Button(ui,
                text="儲存圖片",
                bg="#a9a9a9",
                fg="#000000",
                font="微軟正黑體 16 bold", 
                anchor="center",
                relief="groove",
                bd=2,
                activebackground="#ffffff",
                activeforeground="#000fff",
                command=image_save
                )

btn_blur=Button(ui,
                text="模糊",
                bg="#a9a9a9",
                fg="#000000",
                font="微軟正黑體 16 bold", 
                anchor="center",
                relief="groove",
                bd=2,
                activebackground="#ffffff",
                activeforeground="#000fff",
                command=image_blur
                )

btn_sharpen=Button(ui,
                text="銳利",
                bg="#a9a9a9",
                fg="#000000",
                font="微軟正黑體 16 bold", 
                anchor="center",
                relief="groove",
                bd=2,
                activebackground="#ffffff",
                activeforeground="#000fff",
                command=image_sharpen
                )

btn_contour= Button(ui,
           text="線條",
           bg="#a9a9a9",
           fg="#000000",
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff",
           activeforeground="#000fff",
           command=image_contour
           )

btn_view= Button(ui,
           text="比對",
           bg="#a9a9a9",
           fg="#000000",
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff",
           activeforeground="#000fff"
           )

lab1.place(relwidth=0.2,relheight=0.1,relx=0.15,rely=0.1)
lab2.place(relwidth=0.4,relheight=0.6,relx=0.05,rely=0.2)
lab3.place(relwidth=0.2,relheight=0.1,relx=1-0.15-0.2,rely=0.1)
lab4.place(relwidth=0.4,relheight=0.6,relx=1-0.05-0.4,rely=0.2)


btn1.place(relwidth=0.12,relheight=0.1)
btn_open.place(relwidth=0.2,relheight=0.1,relx=0.12)
btn_save.place(relwidth=0.2,relheight=0.1,relx=0.32)
btn_blur.place(relwidth=0.12,relheight=0.1,relx=0.52)
btn_sharpen.place(relwidth=0.12,relheight=0.1,relx=0.64)
btn_contour.place(relwidth=0.12,relheight=0.1,relx=0.76)
btn_view.place(relwidth=0.12,relheight=0.1,relx=0.88)



ui.mainloop()