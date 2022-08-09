from tkinter import *


def load_txt1():
    text1.delete("1.0", "end")
    with open("Test5/ex4/txt1.txt", mode="r", encoding="utf-8") as file:
        data1 = file.read()
    text1.insert("insert", data1)

def save_txt1():
    lab1Content = text1.get("1.0", END)
    with open("Test5/ex4/txt1.txt", mode="w", encoding="utf-8") as file:
        file.write(lab1Content)
        print("存檔成功")


root = Tk()
root.title("Test")
root.configure(bg="#323232")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

w=screen_w/2
h=screen_h/2

x = (screen_w - w)/2
y = (screen_h - h)/2

root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.focus_force()


btn1 = Button(root, text="讀取檔案", command=load_txt1)
btn2 = Button(root, text="儲存檔案", command=save_txt1)
text1 = Text(root)

btn1.pack(pady=10)
btn2.pack(pady=10)
text1.pack(pady=10)

root.mainloop()