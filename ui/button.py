# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:04:16 2020

@author: user
"""
from tkinter import *

ui = Tk()
ui.title("ex2-1")
ui.configure(bg="lightyellow")

screen_w = ui.winfo_screenwidth() #回傳螢幕寬的像素
screen_h = ui.winfo_screenheight() #回傳螢幕高的像素

w=screen_w/5 #設定視窗 寬度為螢幕的五分之一
h=screen_h/4 #設定視窗 高度為螢幕的四分之一

x = (screen_w - w)/2 #設定視窗X軸 為視窗X軸的一半
y = (screen_h - h)/2 #設定視窗Y軸 為視窗Y軸的一半

ui.geometry("%dx%d+%d+%d" % (w,h,x,y))


"""----------------------------------------------------------------------------------"""

i=0
def a1():
    global i
    i += 1
    lab1["text"]=" 按鈕點擊次數 : "+ str(i)


"""----------------------------------------------------------------------------------"""

lab1=Label(ui,
           text=" 本文內容...", #文字內容
           bg="#ffffff", #背景色
           fg="#555555", #文字顏色
           width=30,
           height=2,
           anchor="w",
           relief="groove",
           bd=2
           )

btn1=Button(ui,
           text="點擊", #文字內容
           bg="#a9a9a9", #背景色
           fg="#000000", #文字顏色
           width=10,
           height=2,
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff", #按下按鈕時的背景顏色。
           activeforeground="#000fff", #按下按鈕時的文字顏色。
           #state=DISABLED    #禁止按鈕使用。    
           command=a1
           )


"""----------------------------------------------------------------------------------"""
lab1.pack(pady=40)
btn1.pack()

"""----------------------------------------------------------------------------------"""

ui.mainloop()
