import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            raise ValueErro

        bmi = weight / (height ** 2)
        bmi_result = f"Your BMI is: {bmi:.2f}"

        if bmi < 18.5:
            category = "Underweight"
            color = "orange"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_text = f"{bmi_result}\nCategory: {category}"
        result_label.config(text=result_text, fg=color)


    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers.")

def reset_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="", fg="black")

def save_result_to_file(bmi, category):
    with open("bmi_result.txt", "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{now}] BMI: {bmi:.2f}, Category: {category}\n")

# GUI Setup
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("320x300")
window.configure(bg="#f0f0f0")

tk.Label(window, text="Weight (kg):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_weight = tk.Entry(window, font=("Arial", 12))
entry_weight.pack()

tk.Label(window, text="Height (m):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_height = tk.Entry(window, font=("Arial", 12))
entry_height.pack()

tk.Button(window, text="Calculate BMI", font=("Arial", 12), bg="green", fg="white", command=calculate_bmi).pack(pady=10)
tk.Button(window, text="Reset", font=("Arial", 12), bg="gray", fg="white", command=reset_fields).pack()

result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=15)

tk.Label(window, text="Result is also saved in 'bmi_result.txt'", font=("Arial", 9), bg="#f0f0f0", fg="gray").pack(pady=5)

window.mainloop()
