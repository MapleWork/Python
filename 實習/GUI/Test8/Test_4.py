import tkinter as tk
from turtle import heading


root = tk.Tk()
root.geometry("800x600")
root.title("BMI")

return_msg = tk.StringVar()
height_msg = tk.IntVar()
weight_msg = tk.IntVar()


def BMI():
    BMI_value = round(weight_msg.get() / ((height_msg.get() / 100)** 2),2)
    return_msg.set("BMI 計算後數值 = " + str(BMI_value)+"\n"+BMI_Status(BMI_value))

def BMI_Status(BMI_value):
    if BMI_value < 18.5:
        return "BMI 過低，體重過輕"
    elif BMI_value < 24:
        return "BMI 正常，標準體位"
    else:
        if BMI_value < 27:
            return "BMI 過高，體重過重"
        elif BMI_value < 30:
            return "BMI 過高，輕度肥胖"
        elif BMI_value < 35:
            return "BMI 過高，中度肥胖"
        else:
            return "BMI 過高，重度肥胖"


height_label = tk.Label(root, text="輸入身高：", foreground="red", font=("標楷體", 12), padx=30, pady=20)
height_label.pack()

height_entry = tk.Entry(root, foreground="Blue", textvariable=height_msg)
height_entry.pack()

weight_label = tk.Label(root, text="輸入體重：", foreground="red", font=("標楷體", 12), padx=30, pady=20)
weight_label.pack()

weight_entry = tk.Entry(root, foreground="Blue", textvariable=weight_msg)
weight_entry.pack()

returnMsg_label = tk.Label(root, textvariable=return_msg, foreground="red", font=("標楷體", 12), padx=30, pady=20)
returnMsg_label.pack()


bmi_button = tk.Button(root, text="BMI 測量", foreground="Blue", font=("標楷體", 12), padx=30, pady=20, command=BMI)
bmi_button.pack()



root.mainloop()