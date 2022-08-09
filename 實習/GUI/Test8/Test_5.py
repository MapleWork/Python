import pymysql
import tkinter  as tk 
from tkinter import messagebox

db = pymysql.connect(host='35.189.184.24', user='root', password='Maple_roro4499', database="test", charset="utf8")
cur = db.cursor()

root = tk.Tk()
root.geometry("800x600")
root.title("新增登入")

return_msg = tk.StringVar()
height_msg = tk.IntVar()
weight_msg = tk.IntVar()


name_label = tk.Label(root, text="輸入姓名：", foreground="blue", font="微軟正黑體 16 bold")
name_label.place(relwidth=0.2,relheight=0.1,relx=0.15,rely=0.1)

phone_label = tk.Label(root, text="輸入電話：", foreground="blue", font="微軟正黑體 16 bold")
phone_label.place(relwidth=0.2,relheight=0.1,relx=0.15,rely=0.2)


var_name = tk.StringVar()
entry_name = tk.Entry(root, textvariable=var_name)
entry_name.place(relwidth=0.2,relheight=0.05,relx=0.35,rely=0.125)

var_phone = tk.StringVar()
entry_phone = tk.Entry(root, textvariable=var_phone)
entry_phone.place(relwidth=0.2,relheight=0.05,relx=0.35,rely=0.225)


def name():
    name = var_name.get()
    phone = var_phone.get()


    try:
        sql = """INSERT INTO test(Name, Phone) VALUES(%s,%s)"""

        cur.execute(sql, (name, phone))
        
        if not(name and phone):
            tk.messagebox.showwarning(title="警告", message="不能為空")

        print("存檔成功")
    
    except:
        db.rollback()
        print("存檔失敗")

    db.commit()

btn_Click = tk.Button(root, bg="#ffffff", text="新增", command=name)
btn_Click.place(relwidth=0.2,relheight=0.05,relx=0.25,rely=0.35)

root.mainloop()