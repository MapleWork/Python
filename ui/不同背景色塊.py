# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:04:16 2020

@author: user
"""


from tkinter import *

ui = Tk()
ui.title("ex3-2")
ui.configure(bg="lightyellow")

screen_w = ui.winfo_screenwidth() #回傳螢幕寬的像素
screen_h = ui.winfo_screenheight() #回傳螢幕高的像素

w=screen_w/3 #設定視窗 寬度為螢幕的三分之一
h=screen_h/2 #設定視窗 高度為螢幕的三分之一

x = (screen_w - w)/2 #設定視窗X軸 為視窗X軸的一半
y = (screen_h - h)/2 #設定視窗Y軸 為視窗Y軸的一半

ui.geometry("%dx%d+%d+%d" % (w,h,x,y))


"""----------------------------------------------------------------------------------"""

lab1=Label(ui,
           text="a", #文字內容
           bg="#3355aa", #背景色
           fg="#ffffff", #文字顏色
           width=30,
           height=5,
           anchor="center",
           relief="groove",
           bd=2
           )

lab2=Label(ui,
           text="b", #文字內容
           bg="#aa55aa", #背景色
           fg="#ffffff", #文字顏色
           width=30,
           height=5,
           anchor="center",
           relief="groove",
           bd=2           
           )

lab3=Label(ui,
           text="c", #文字內容
           bg="#33aa00", #背景色
           fg="#ffffff", #文字顏色
           width=30,
           height=5,
           anchor="center",
           relief="groove",
           bd=2           
           )


"""----------------------------------------------------------------------------------"""

lab1.pack(side="left",anchor="s",fill=X)
lab2.pack(side="top",anchor="e",expand=1,fill=Y)
lab3.pack(side="top",anchor="n")















"""----------------------------------------------------------------------------------"""
ui.mainloop()
