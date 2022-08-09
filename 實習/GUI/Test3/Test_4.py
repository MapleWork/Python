from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from tkinter import filedialog as fd
import os


ui = Tk()
ui.title("濾鏡練習")
ui.configure(bg="#efefef")
screen_w = ui.winfo_screenwidth()
screen_h = ui.winfo_screenheight()

global ui_w, ui_h
ui_w = screen_w/2
ui_h = screen_h/2

x = (screen_w - ui_w)/2
y = (screen_h - ui_h)/2

ui.geometry("%dx%d+%d+%d" % (ui_w,ui_h,x,y))

def open_image():
    openfilename=fd.askopenfilename(initialdir="/", title="開啟檔案",\
                                    filetypes=(("圖片檔","*.jpg;*.png"),("所有檔案","*.*")))
    print(openfilename)

    global filename_
    filename = os.path.split(openfilename)[1]
    print(os.path.split(openfilename)[1])
    filename_ = filename.split('.')
    print(filename_)

    jpg1 = Image.open(openfilename)
    jpg1_w,jpg1_h = jpg1.size
    print(jpg1_w,jpg1_h)

    global re
    if jpg1_w >= jpg1_h and jpg1_w > ui_w*0.4:
        re=(ui_w*0.4)/jpg1_w
    elif jpg1_h >= jpg1_w and jpg1_h > ui_h*0.6:
        re=(ui_h*0.6)/jpg1_h
    else:
        re=1

    global jpg1_tk
    jpg1_resize = jpg1.resize((int(jpg1_w*re), int(jpg1_h*re)))
    jpg1_tk = ImageTk.PhotoImage(jpg1_resize)
    lab2.configure(image=jpg1_tk)
    lab2.image = jpg1_tk
    global jpg2
    jpg2 = jpg1

def lab4_img():
    global jpg2_tk
    jpg2_tk = ImageTk.PhotoImage(out_jpg_resize)
    lab4.configure(image=jpg2_tk)
    lab4.image = jpg2_tk

#模糊
def image_blur():
    global out_jpg, out_jpg_resize
    out_jpg = jpg2.filter(ImageFilter.BLUR)

    jpg2_w, jpg2_h = jpg2.size
    out_jpg_resize = jpg2.resize((int(jpg2_w*re), int(jpg2_h*re)))
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.BLUR)
    lab4_img()

#銳利
def image_sharpen():
    global out_jpg, out_jpg_resize
    out_jpg = jpg2.filter(ImageFilter.SHARPEN)

    jpg2_w, jpg2_h = jpg2.size
    out_jpg_resize = jpg2.resize((int(jpg2_w*re),int(jpg2_h*re)))
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.SHARPEN)
    lab4_img()

#黑白線條
def image_contour():
    global out_jpg, out_jpg_resize
    out_jpg = jpg2.filter(ImageFilter.CONTOUR)
    out_jpg =  out_jpg.convert("1")

    jpg2_w, jpg2_h = jpg2.size
    out_jpg_resize = jpg2.resize((int(jpg2_w*re),int(jpg2_h*re)))
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.CONTOUR)
    out_jpg_resize = out_jpg_resize.convert("1")
    lab4_img()

#顏色疊加
def aa():
    global out_jpg, out_jpg_resize
    jpg2_col = Image.new('RGB', jpg2.size, "#faebd7")
    out_jpg = jpg2.filter(ImageFilter.SHARPEN)
    out_jpg = Image.blend(out_jpg, jpg2_col, 0.2)

    jpg2_w, jpg2_h = jpg2.size
    out_jpg_resize = jpg2.resize((int(jpg2_w*re), int(jpg2_h*re)))
    jpg2_col = Image.new('RGB', out_jpg_resize.size, "#faebd7")
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.SHARPEN)
    out_jpg_resize= Image.blend(out_jpg_resize, jpg2_col, 0.2)
    lab4_img()

def image_save():
    out_jpg.save(filename_[0]+"_uot.jpg")

def btn_view_down(event):
    lab4.configure(image=jpg1_tk)
    lab4.image = jpg1_tk

def btn_view_up(event):
    lab4.configure(image=jpg2_tk)
    lab4.image = jpg2_tk

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

btn1.place(relwidth=0.08,relheight=0.1,relx=0.46,rely=0.70)
btn_open.place(relwidth=0.15,relheight=0.1,relx=0.05+0.2-0.075,rely=0.85)
btn_save.place(relwidth=0.15,relheight=0.1,relx=1-0.05-0.4+0.125,rely=0.85)
btn_blur.place(relwidth=0.08,relheight=0.1,relx=0.46,rely=0.25)
btn_sharpen.place(relwidth=0.08,relheight=0.1,relx=0.46,rely=0.40)
btn_contour.place(relwidth=0.08,relheight=0.1,relx=0.46,rely=0.55)
btn_view.place(relwidth=0.08,relheight=0.1,relx=0.46,rely=0.85)

btn_view.bind('<ButtonPress-1>',btn_view_down)
btn_view.bind('<ButtonRelease-1>',btn_view_up)

lab4.bind('ButtonPress-3',btn_view_down)
lab4.bind('ButtonRelease-3',btn_view_up)

ui.mainloop()