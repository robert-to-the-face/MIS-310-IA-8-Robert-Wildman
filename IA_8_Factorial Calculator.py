import tkinter as tk
from tkinter import messagebox

def calculate_factorial():
    try:
        number = int(entry.get())
        if number < 0:
            raise ValueError("Number must be nonnegative.")

        factorial = 1
        for factor in range(1, number + 1):
            factorial *= factor

        result_label.config(text=f"The factorial of {number} is {factorial:,d}")
    except ValueError:
        messagebox.showerror("Invalid Input")

# Set up the main window
main_window = tk.Tk()
main_window.title("Factorial Calculator")

# Create and place widgets
tk.Label(main_window, text="Enter a nonnegative integer:").pack(pady=5)

entry = tk.Entry(main_window)
entry.pack(pady=5)

tk.Button(main_window, text="Calculate Factorial", command=calculate_factorial).pack(pady=5)

result_label = tk.Label(main_window, text="")
result_label.pack(pady=10)

# Start the GUI event loop
main_window.mainloop()
