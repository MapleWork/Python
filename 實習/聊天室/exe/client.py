import sys
import pymysql
from tkinter import *
from tkinter import messagebox

fon = ("微軟正黑體", 16)
myUser = ""
UserPassword = {}
usersList = {}


class Application():
    def __init__(self):
        self.titleTop = Label(root, text="聊天群", fg="black", font=fon)
        self.titleTop.pack(side='top', fill='both')

        self.f1 = Frame(root, width=10, height=100)
        self.f1.pack(side="bottom", fill='x')

        self.listboxLeft = Listbox(root, width=55, height=16, font=fon, yscrollcommand="true")
        self.listboxLeft.pack(side='left', fill='y')

        self.fRight = Frame(root, width=140)
        self.fRight.pack(side='right', fill="both", expand="no")

        self.f_labelTop = Label(self.fRight, text="用戶列表", fg="black", font=fon, padx=20)
        self.f_labelTop.pack(side='top',fill='y')

        self.f_listboxBottom = Listbox(self.fRight, font=fon)
        self.f_listboxBottom.pack(side='top', fill="both", expand="yes")

        self.textBottom = Text(self.f1, width=44, height=3, font=fon, yscrollcommand="true", padx=5)
        self.textBottom.pack(side="left", fill='both')

        self.buttonR = Button(self.f1, width=9, text="更新", font=fon, command=self.show)
        self.buttonR.pack(side='right', fill='y')

        self.buttonR = Button(self.f1, width=10, text="發送", font=fon, command=self.sendThreadProcess)
        self.buttonR.pack(side='right', fill='y')

        

    def sendThreadProcess(self):
        var = self.textBottom.get(1.0, END)

        db = pymysql.connect(host='localhost', user='root', password='Maple_roro4499', database='test')
        cursor = db.cursor()
      
        Login_sql = f""" SELECT User From root where User={myUser} """
        cursor.execute(Login_sql)
        content = str(cursor.fetchone()[0])

        if myUser == content:
            sql = """ INSERT IGNORE INTO test(User, Data) VALUES('%s','%s') """ % (myUser, var)
            cursor.execute(sql)
            db.commit()
            db.close()
        else:
            print("Error")

        self.listboxLeft.insert("end", var)
        self.textBottom.delete(0.0, END)

    def show(self):
        db = pymysql.connect(host='localhost', user='root', password='Maple_roro4499', database='test')
        cursor = db.cursor()
        
        sql = "SELECT User, Data FROM test"
        cursor.execute(sql)
        var = cursor.fetchall()
        i=0
        for row in var:
            for j in range(len(row)):
                self.listboxLeft.insert(END, row[j])
            i+=1

        db.commit()
        db.close()


    def closeWin(self):
        root.destroy()



class loginWin(Frame):
    def lon_req(self):
        global myUser, UserPassword

        db = pymysql.connect(host='localhost', user='root', password='Maple_roro4499', database='test')
        cursor = db.cursor()

        myUser = self.entry01.get()
        UserPassword = self.entry02.get()

        sql = "SELECT User, Password FROM root"
        cursor.execute(sql)
        
        result = cursor.fetchall()
        name_list = [it[0] for it in result]
        if not (myUser and UserPassword):
            messagebox.showwarning(title=' 警告 ', message=' 使用者名稱或密碼不能為空 ')
        elif myUser in name_list:
            if UserPassword == result[name_list.index(myUser)][1]:
                messagebox.showinfo(title=' 歡迎您 ', message='        登入成功！ \r\n 當前登入帳號號為： ' + myUser)
                login.destroy()
            else:
                messagebox.showerror(title=' 錯誤 ', message=' 密碼輸入錯誤 ')
        else:
            messagebox.showerror(title=' 錯誤 ', message=' 沒有這個帳號 ')

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.frame01 = Frame(login, width=400, height=100)
        self.frame02 = Frame(login, width=400, height=100)
        self.frame03 = Frame(login, width=400, height=100)
        self.frame04 = Frame(login, width=400, height=100)

        self.frame01.pack()
        self.frame02.pack()
        self.frame03.pack()
        self.frame04.pack()

        self.tittle01 = Label(self.frame01, text="歡迎登入", font=fon)
        self.label01 = Label(self.frame02, text="用戶名：", font=fon)
        self.label02 = Label(self.frame03, text="密   碼：", font=fon)
        self.entry01 = Entry(self.frame02, width=15, font=fon, bg='white', xscrollcommand='true')
        self.entry02 = Entry(self.frame03, width=15, font=fon, bg='white', xscrollcommand='true', show="*")
        self.B_login = Button(self.frame04, width=10, height=1, text="登入", font=fon, command=self.lon_req)
        self.B_regist = Button(self.frame04, width=10, height=1, text="註冊", font=fon, command=regist)

        self.tittle01.pack(pady=20)
        self.label01.pack(side='left', fill='both', padx=20, pady=20)
        self.label02.pack(side='left', fill='both', padx=20, pady=20)
        self.entry01.pack(side='right', fill='x', pady=20)
        self.entry02.pack(side='right', fill='x', pady=20)
        self.B_login.pack(side='right', fill='both', padx=20, pady=20)
        self.B_regist.pack(side='left', fill='both', padx=20, pady=20)

    def closeWin(self):
        login.destroy()
        sys.exit()

class registers(Frame):
    def sign_up(self):
        db = pymysql.connect(host='localhost', user='root', password='Maple_roro4499', database='test')
        cursor = db.cursor()

        User = self.entry01.get()
        Password = self.entry02.get()
        Confirm_Password = self.entry03.get()

        try:
            insert_sql = "INSERT INTO root(User, Password) VALUES ('%s', '%s')" % (User, Password)
            read_sql = f""" SELECT * FROM root where User="{User}" and Password="{Password}" """

            user_data = cursor.execute(read_sql)
            if not (User and Password):
                messagebox.showwarning(title=' 警告 ', message=' 註冊賬號或密碼不能為空 ')

            elif Password != Confirm_Password:
                messagebox.showwarning(title=' 警告 ', message=' 兩次密碼輸入不一致，請重新輸入 ')

            else:
                if user_data.real:
                    messagebox.showwarning(title=' 警告 ', message=' 該註冊賬號已存在 ')
                    reg.destroy()
                else:
                    cursor.execute(insert_sql)
                    messagebox.showinfo(title=' 恭喜您 ', message='       註冊成功！ \r\n 註冊賬號為： ' + User)
                    print("資料庫成功")
                    reg.destroy()
                    db.commit()
                    cursor.close()
                    
        except IOError:
            print("資料庫失敗")
            db.rollback()
            db.close()
           
        # try:
        #     insert_User_sql = "INSERT INTO test(User) VALUES ('%s')" % (User)
        #     User_sql = f""" SELECT User FROM test where User="{User}" """

        #     user_data = cursor.execute(User_sql)
        #     cursor.execute(insert_User_sql)

        #     db.commit()
        #     cursor.close()
        
        # except IOError:
        #     print("資料庫失敗")
        #     db.rollback()
        #     db.close()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place()
        self.createWidget()

    def createWidget(self):
        self.lable01 = Label(reg, text="用 戶 名：", font=fon)
        self.lable02 = Label(reg, text="密   碼：", font=fon)
        self.lable03 = Label(reg, text="確認密碼：", font=fon)
        self.entry01 = Entry(reg, font=fon)
        self.entry02 = Entry(reg, font=fon, show="·")
        self.entry03 = Entry(reg, font=fon, show="·")
        self.b1 = Button(reg, text='註冊', font=fon, command=self.sign_up)
        self.b2 = Button(reg, text='取消', font=fon, command=self.cancel)

        self.lable01.place(x=10, y=25)
        self.lable02.place(x=10, y=85)
        self.lable03.place(x=10, y=145)
        self.entry01.place(x=130, y=25)
        self.entry02.place(x=130, y=85)
        self.entry03.place(x=130, y=145)
        self.b1.place(x=80, y=210)
        self.b2.place(x=280, y=210)

    def cancel(self):
        reg.destroy()
    
    

def raise_above_all(win):
    win.attributes('-topmost', 1)
    win.attributes('-topmost', 0)

def rootStart():
    global root
    root = Tk()
    root.title("聊天")
    root.geometry("800x600+300+100")
    root.resizable(0, 0)
    app1 = Application()
    root.protocol("WM_DELETE_WINDOW", app1.closeWin)
    raise_above_all(root)
    root.mainloop()

def loginStart():
    global login
    login = Tk()
    login.title("用戶登入")
    login.geometry("400x300+600+200")
    login.resizable(0, 0)
    app2 = loginWin(master=login)
    login.protocol("WM_DELETE_WINDOW", app2.closeWin)
    raise_above_all(login)
    login.mainloop()

def regist():
    global reg
    reg = Tk()
    reg.title("用戶註冊")
    reg.geometry("400x300+600+200")
    reg.resizable(0, 0)
    app3 = registers(master=reg)
    reg.protocol("WM_DELETE_WINDOW", app3.sign_up)
    raise_above_all(reg)
    reg.mainloop()

if __name__ == '__main__':
    loginStart()
    rootStart()