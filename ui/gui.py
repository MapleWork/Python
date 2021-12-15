# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:42:59 2020

@author: user
"""

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        #按鈕
        self.button = tk.Button(self)
        self.button["text"] = "按鈕"
        self.button.grid(row=0, column=0, sticky=tk.N+tk.W)
        
        #選項紐 (可複選)
        self.checkbutton = tk.Checkbutton(self)
        self.checkbutton["text"] = "選項紐 (可複選)"
        self.checkbutton.grid(row=1, column=0, sticky=tk.N+tk.W)
        
        #文字方塊
        self.entry = tk.Entry(self)
        self.entry.grid(row=2, column=0, sticky=tk.N+tk.W)
        
        #標籤
        self.label = tk.Label(self)
        self.label["text"] = "標籤"
        self.label.grid(row=3, column=0, sticky=tk.N+tk.W)
        
        #表單
        self.listbox = tk.Listbox(self)
        self.listbox["height"] = 5
        self.listbox.insert(0, "表單")
        self.listbox.insert(1, "Python")
        self.listbox.insert(2, "Java")
        self.listbox.insert(3, "Swift")
        self.listbox.insert(4, "JavaScript")
        self.listbox.insert(5, "C")
        self.listbox.grid(row=4, column=0, sticky=tk.N+tk.W)
        
        #下拉式選單
        self.optionList = ("Python", "Java", "Swift")
        self.v = tk.StringVar()
        self.v.set("下拉式選單")
        self.optionmenu = tk.OptionMenu(self, self.v, *self.optionList)
        self.optionmenu.grid(row=5, column=0, sticky=tk.N+tk.W)
        
        #選項紐(單選)
        self.radiobutton = tk.Radiobutton(self)
        self.radiobutton["text"] = "選項紐(單選)"
        self.radiobutton.grid(row=6, column=0, sticky=tk.N+tk.W)
        
        
        #捲軸控制值
        self.scale = tk.Scale(self)
        self.scale.grid(row=7, column=0, sticky=tk.N+tk.W)
        
        #可微調輸入控鍵
        self.spinbox = tk.Spinbox(self, from_=0, to=10)
        self.spinbox.grid(row=8, column=0, sticky=tk.N+tk.W)
        
        #文字區域 (可換行)
        self.text = tk.Text(self)
        self.text["height"] = 10
        self.text["width"] = 50
        self.text.grid(row=9, column=0, sticky=tk.N+tk.W)
                
root = tk.Tk()
app = Application(root)
root.mainloop()
