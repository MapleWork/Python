from tkinter import *
import tkinter as tk1
    
class SampleApp(tk1.Tk):
    def __init__(self):
        tk1.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk1.Frame):
    def __init__(self, master123):
        tk1.Frame.__init__(self, master123)
        
        tk1.Label(self, 
                 text="Start page", 
                 font=('Helvetica', 18, "bold")
                 ).pack(side="top",
                        fill="x",
                        pady=5)
                        
        tk1.Button(self, 
                  text="Go to page one",
                  command=lambda: master123.switch_frame(PageOne)).pack()
        
        tk1.Button(self, text="Go to page two",
                  command=lambda: master123.switch_frame(PageTwo)).pack()

class PageOne(tk1.Frame):
    def __init__(self, master123):
        tk1.Frame.__init__(self, master123)
        tk1.Frame.configure(self,bg='blue')
        tk1.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk1.Button(self, text="Go back to start page",
                  command=lambda:master123.switch_frame(StartPage)).pack()

class PageTwo(tk1.Frame):
    def __init__(self, master123):
        tk1.Frame.__init__(self, master123)
        tk1.Frame.configure(self,bg='red')
        tk1.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk1.Button(self, text="Go back to start page",
                  command=lambda: master123.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    
    app.mainloop()