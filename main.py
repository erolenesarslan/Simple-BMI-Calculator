from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.resizable(False, False)
window.title("BMI Calculator")

text1 = Label(window, text="Enter your Weight (kg)", padx=20, pady=10)
text1.pack()

entry1 = Entry(width=20)
entry1.pack()

text2 = Label(window, text="Enter your Height (cm)", padx=20, pady=10)
text2.pack()

entry2 = Entry(width=20)
entry2.pack()

#Button
def calculate():
    if entry1.get() == "" or entry2.get() == "":
        messagebox.showerror("Error", "Please enter both values")
        return
    weight = entry1.get()
    height = entry2.get()
    try:
        meter = float(height) / 100
        bmi = float(weight) / meter ** 2
        bmi = round(bmi, 2)
    except ValueError:
        messagebox.showerror("Error", "Please enter both values numerically")
        return

    if bmi < 18.5:
        text3.config(text=f"Your BMI is {bmi}, you are under weight")
    elif 18.5 <= bmi < 25:
        text3.config(text=f"Your BMI is {bmi}, you are normal")
    elif 25 <= bmi < 30:
        text3.config(text=f"Your BMI is {bmi}, you are overweight")
    elif 30 <= bmi < 35:
        text3.config(text=f"Your BMI is {bmi}, you are obese")
    else:
        text3.config(text=f"Your BMI is {bmi}, you are extremely obese")

calculatebtn = Button(window, text="Calculate", command=calculate)
calculatebtn.pack()

text3 = Label(window, text="", padx=20, pady=10)
text3.pack()
window.mainloop()