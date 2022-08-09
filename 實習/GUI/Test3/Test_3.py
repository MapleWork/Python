import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

def open_file():
    openfilename=fd.askopenfilename(initialdir="/", title="開啟檔案",\
                                    filetypes=(("圖片檔","*.jpg;*.png"),("所有檔案","*.*")))

    print(openfilename)

    try:
        with open(openfilename,'r') as file:
            print(file.read())
    except:
        print("檔案不存在")

def save_file():
    f = fd.asksaveasfile(mode="w", defaultextension="*.*")
    if f is None:
        return
    f.write("Hello World!")
    f.close()

root = tk.Tk()
root.title("檔案開啟&儲存檔案")
ttk.Button(root, text="檔案開啟", command=open_file).pack()
ttk.Button(root, text="儲存檔案", command=save_file).pack()
root.mainloop()
