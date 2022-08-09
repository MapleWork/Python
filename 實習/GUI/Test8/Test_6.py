from re import I, L
from tkinter import *
from tkinter import messagebox


class MenuBar(Menu):
    def __init__(self, root):
        Menu.__init__(self, root)

        file = Menu(self, tearoff=False)
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as")
        file.add_separator()
        file.add_command(label="Exit", underline=1, command=self.quit)
        
        self.add_cascade(label="File", underline=0, menu=file)

        edit = Menu(self, tearoff=0)
        edit.add_command(label="Undo")  
        edit.add_separator()     
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        self.add_cascade(label="Edit", menu=edit)

        help = Menu(self, tearoff=0)
        help.add_command(label="About", command=self.about)
        self.add_cascade(label="Help", menu=help)

    
    def exit(self):
        self.exit


    def about(self):
        messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')
    

class MenuDemo(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    root=MenuDemo()
    root.title("App")
    root.configure(bg="#efefef")
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    global ui_w, ui_h
    ui_w = screen_w/2
    ui_h = screen_h/2

    x = (screen_w - ui_w)/2
    y = (screen_h - ui_h)/2

    root.geometry("%dx%d+%d+%d" % (ui_w,ui_h,x,y))

    root.mainloop()