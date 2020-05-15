from tkinter import *
import math


def leftClickButton(event):
    Result =float(textBoxWeight.get()) / math.pow(float(textBoxHight.get()) / 100, 2)
    print(float(Result))

    if Result <= 18.5:
        labelResult.configure(text="คุณมีน้ำหนักน้อยเกินไป")
    elif Result >= 18.6 and Result <= 22.9:
        labelResult.configure(text="คุณมีน้ำหนักปกติ")
    elif Result >= 23.0 and Result <= 24.9:
        labelResult.configure(text="โรคอ้วนระดับ 1")
    elif Result >= 25.0 and Result <= 29.9:
        labelResult.configure(text="โรคอ้วนระดับ 2")
    elif Result >= 30:
        labelResult.configure(text="โรคอ้วนระดับ 3")


MainWindow = Tk()
labelHight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHight.grid(row=0, column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ค่า BMI :")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()