from tkinter import *
from PIL import ImageTk, Image
import cv2

root = Tk()
root.title("Video")
root.configure(bg="#efefef")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

global ui_w, ui_h
ui_w = screen_w/3
ui_h = screen_h/2

x = (screen_w - ui_w)/2
y = (screen_h - ui_h)/2

root.geometry("%dx%d+%d+%d" % (ui_w,ui_h,x,y))

app = Frame(root, bg="white")
app.grid()


lmian = Label(app)
lmian.grid()

video = cv2.VideoCapture('Test5/GasGasGas.mp4')


def video_play():
    _, frame = video.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmian.imgtk = imgtk
    lmian.configure(image=imgtk)
    lmian.after(1, video_play)



video_play()
root.mainloop()