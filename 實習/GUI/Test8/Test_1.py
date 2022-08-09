import os
from re import L
import tkinter as tk

from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from tkinter import filedialog as fd


ui = Tk()
ui.title("Test")
ui.configure(bg="lightblue")

screen_w = ui.winfo_screenwidth()
screen_h = ui.winfo_screenheight()

w = screen_w/2
h = screen_h/2

x = (screen_w - w)/2
y = (screen_h - h)/2

ui.geometry("%dx%d+%d+%d" % (w,h,x,y))


en = tk.Entry(ui,
            bg="#ffffff",
            fg="#555555",
            width=30,
            relief="groove",
            bd=2,
            show=None)

lb = tk.Listbox(ui)

def add():
    var=en.get()
    lb.insert('end',var)
    en.delete(0,'end')

def delete():
    lb.delete(lb.curselection())

btn1=Button(ui,
            text="新增",
            bg="#a9a9a9",
            fg="#000000",
            font="微軟正黑體 16 bold", 
            anchor="center",
            relief="groove",
            bd=2,
            activebackground="#ffffff",
            activeforeground="#000fff",
            command=add
            )

btn2=Button(ui,
            text="刪除",
            bg="#a9a9a9",
            fg="#000000",
            font="微軟正黑體 16 bold", 
            anchor="center",
            relief="groove",
            bd=2,
            activebackground="#ffffff",
            activeforeground="#000fff",
            command=delete
            )

en.pack(pady=40)
lb.pack()

btn1.place(relwidth=0.15,relheight=0.1,relx=0.55,rely=0.7)
btn2.place(relwidth=0.15,relheight=0.1,relx=0.30,rely=0.7)


ui.mainloop()