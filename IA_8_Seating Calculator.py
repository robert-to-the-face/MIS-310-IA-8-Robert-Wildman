import tkinter as tk
from tkinter import messagebox

# Global constants
CLASS_A_SEAT_PRICE = 20
CLASS_B_SEAT_PRICE = 15
CLASS_C_SEAT_PRICE = 10

# Main GUI application
def calculate_income():
    try:
        countA = int(entry_classA.get())
        countB = int(entry_classB.get())
        countC = int(entry_classC.get())

        if countA < 0 or countB < 0 or countC < 0:
            raise ValueError("Negative input not allowed.")

        incomeA = countA * CLASS_A_SEAT_PRICE
        incomeB = countB * CLASS_B_SEAT_PRICE
        incomeC = countC * CLASS_C_SEAT_PRICE
        total = incomeA + incomeB + incomeC

        result_text.set(
            f"Income from class A seats: ${incomeA:,.2f}\n"
            f"Income from class B seats: ${incomeB:,.2f}\n"
            f"Income from class C seats: ${incomeC:,.2f}\n"
            f"Total income: ${total:,.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid non-negative integers.")

# GUI Setup
window = tk.Tk()
window.title("Stadium Seating Income Calculator")
window.geometry("400x300")

# Labels and entries
tk.Label(window, text="Enter number of Class A seats:").pack(pady=5)
entry_classA = tk.Entry(window)
entry_classA.pack()

tk.Label(window, text="Enter number of Class B seats:").pack(pady=5)
entry_classB = tk.Entry(window)
entry_classB.pack()

tk.Label(window, text="Enter number of Class C seats:").pack(pady=5)
entry_classC = tk.Entry(window)
entry_classC.pack()

# Button to calculate income
tk.Button(window, text="Calculate Income", command=calculate_income).pack(pady=10)

# Result display
result_text = tk.StringVar()
tk.Label(window, textvariable=result_text, justify="left", font=("Courier", 10)).pack(pady=10)

# Start GUI loop
window.mainloop()