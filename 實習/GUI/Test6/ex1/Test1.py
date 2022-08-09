import json
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


m = 0
title_lab_list=[]
content_lab_list=[]
data_content_list=[]
data_title_list=[]
data_file_path=""

def open_json():
    data1 = ""
    data2 = "" 
    cls_()

    global data_file_path
    data_file_path = askopenfilename(initialdir="./", title="開啟就檔", filetypes=(("常見資料交換格式", "*.json"),('所有檔案',"*.*")))
    if data_file_path =="":
        return
    
    with open(data_file_path, mode="r", encoding="utf-8-sig") as file:
        data1 = json.load(file)
    
    data2 = list(data1)

    for i in range(len(data2)):
        print(data2[i], ":", data1[data2[i]])

    for j in range(0, len(data1)):
        add_ent()

    index = 0
    for i in data_title_list:
        i.insert(0, data2[index])
        index += 1

    index = 0
    for i in data_content_list:
        i.insert(0, data1[data2[index]])
        index+=1


def c_json():

    data3 = []
    data4 = []
    data5 = []

    for i in data_title_list:
        data3.append(i.get())

    for i in data_content_list:
        data4.append(i.get())

    data5 = dict(zip(data3, data4))
    print(data5)

    file_path = asksaveasfilename(initialdir="./", initialfile="123", defaultextension="json",title="選擇儲存資料夾", filetypes=(("json","*.json"), ("all files", "*.*")))

    if file_path =="":
        return
    
    with open(file_path, mode="w", encoding="utf-8-sig") as file:
        json.dump(data5, file, ensure_ascii=False)

def s_json():
    data3 = []
    data4 = []
    data5 = []

    for i in data_title_list:
        data3.append(i.get())

    for i in data_content_list:
        data4.append(i.get())

    data5 = dict(zip(data3, data4))

    global data_file_path
    if data_file_path =="":
        return

    with open(data_file_path, mode="w", encoding="utf-8-sig") as file:
        json.dump(data5, file, ensure_ascii=False)


def add_ent():
    global m
    exec('title_lab_'+str(m)+'=Label(root, text="KEY'+(str(m))+'", font="微軟正黑體 12 bold", width="10", bg="#323232",fg="#f0f0f0")')
    exec('title_lab_'+str(m)+'.grid(row='+str(3+m)+',column=0,pady=10,padx=10)')
    title_lab_list.append(eval('title_lab_'+str(m)))

    exec('data_title_'+str(m)+'=Entry(root, font="微軟正黑體 16 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1)')
    exec('data_title_'+str(m)+'.grid(row='+str(3+m)+',column=1,sticky=W+E,pady=10,padx=10)')
    data_title_list.append(eval('data_title_'+str(m)))

    exec('content_lab_'+str(m)+'=Label(root, text="值'+(str(m))+'", font="微軟正黑體 12 bold", width="10", bg="#323232",fg="#f0f0f0")')
    exec('content_lab_'+str(m)+'.grid(row='+str(3+m)+',column=2,pady=10,padx=10)')
    content_lab_list.append(eval('content_lab_'+str(m)))

    exec('data_content_'+str(m)+'=Entry(root, font="微軟正黑體 16 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1)')
    exec('data_content_'+str(m)+'.grid(row='+str(3+m)+',column=3,sticky=W+E,pady=10,padx=10)')
    data_content_list.append(eval('data_content_'+str(m)))

    m+=1

def cls_():
    for i in title_lab_list:
        i.destroy()
    for i in data_title_list:
        i.destroy()
    for i in content_lab_list:
        i.destroy()
    for i in data_content_list:
        i.destroy()

    global m
    global data_file_path

    m=0
    title_lab_list.clear()
    content_lab_list.clear()
    data_content_list.clear()
    data_title_list.clear()
    data_file_path = ""


root = Tk()
root.title("ex1")
root.configure(bg="#323232")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

w = screen_w/2
h = screen_h/2

x = (screen_w - w)/2
y = (screen_h - h)/2

root.geometry("+%d+%d" % (x,y))
root.focus_force()


lab1 = Label(root, text="Json 編譯器", font="微軟正黑體 32 bold", bg="#323232", fg="#f0f0f0")

open_json_btn = Button(root, text="開啟", font="微軟正黑體 16 bold", width="10", command=open_json)
s_json_btn = Button(root, text="儲存", font="微軟正黑體 16 bold", width="10", command=s_json)
add_data_btn = Button(root, text="+", font="微軟正黑體 16 bold", width="10", command=add_ent)
cls_btn = Button(root, text="清空", font="微軟正黑體 16 bold", width="10", command=cls_)
c_json_btn = Button(root, text="另存", font="微軟正黑體 16 bold", width="10", command=c_json)
title_lab_0 = Label(root, text="KEY(範本)", font="微軟正黑體 12 bold", width="10", bg="#323232", fg="#f0f0f0")
content_lab_0 = Label(root, text="值(範本)", font="微軟正黑體 12 bold", width="10", bg="#323232", fg="#f0f0f0")

data_title_0 = Entry(root, font="微軟正黑體 16 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1)
data_content_0 = Entry(root, font="微軟正黑體 16 bold", selectbackground="#323232", selectforeground="#ffffff", selectborderwidth=1)

lab1.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

open_json_btn.grid(row=1, column=0, pady=5, padx=10)
s_json_btn.grid(row=1, column=1, pady=3, padx=10)
c_json_btn.grid(row=1, column=2, pady=3, padx=10)
cls_btn.grid(row=1, column=3, pady=3, padx=10)
add_data_btn.grid(row=2, column=0, pady=3, padx=10, sticky=W+E)

title_lab_0.grid(row=3, column=0, pady=10, padx=10)
data_title_0.grid(row=3, column=1, pady=10, padx=10)

content_lab_0.grid(row=3, column=2, pady=10, padx=10)
data_content_0.grid(row=3, column=3, pady=10, padx=10)


root.mainloop()