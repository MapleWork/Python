from tkinter import *

def pagy1():
    global root
    root = Tk()
    root.title("1")
    root.configure(bg="#000")
    
    screen_w = root.winfo_screenwidth() #回傳螢幕寬的像素
    screen_h = root.winfo_screenheight() #回傳螢幕高的像素
    
    w=screen_w/4 #設定視窗 寬度為螢幕的四分之一
    h=screen_h/3 #設定視窗 高度為螢幕的三分之一
    
    x = (screen_w - w)/2 #設定視窗X軸 為視窗X軸的一半
    y = (screen_h - h)/2 #設定視窗Y軸 為視窗Y軸的一半
    
    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    root.focus_force()
    
    btn1=Button(root,
           text="開啟視窗2", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=30,
           anchor="center",
           font="微軟正黑體 20 bold",
           bd=2,
           command=cl
           )
    
    btn1.pack(side="bottom")
    
    root.mainloop()



def pagy2():
    global root2
    root2 = Tk()
    root2.title("2")
    root2.configure(bg="lightyellow")
    
    screen_w = root2.winfo_screenwidth() #回傳螢幕寬的像素
    screen_h = root2.winfo_screenheight() #回傳螢幕高的像素
    
    w=screen_w/4 #設定視窗 寬度為螢幕的四分之一
    h=screen_h/3 #設定視窗 高度為螢幕的三分之一
    
    x = (screen_w - w)/2 #設定視窗X軸 為視窗X軸的一半
    y = (screen_h - h)/2 #設定視窗Y軸 為視窗Y軸的一半
    
    root2.geometry("%dx%d+%d+%d" % (w,h,x,y))
    root2.focus_force()
    
    btn2=Button(root2,
           text="返回視窗1", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=30,
           anchor="center",
           font="微軟正黑體 20 bold",
           bd=2,
           command=c2
           )
    
    btn2.pack(side="bottom")
    
    root2.mainloop()


def cl():
    try:  
        root.destroy()
    except:  
        pass
    pagy2()

    
def c2():
    try:  
        root2.destroy()
    except:  
        pass
    pagy1()

pagy1()

