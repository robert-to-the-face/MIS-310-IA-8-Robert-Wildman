import tkinter as tk
from tkinter import messagebox


# Constants
FEET_PER_GALLON = 112
LABOR_HOURS_PER_GALLON = 8

def calculate():
    try:
        feet_wall = float(entry_wall.get())
        price_paint = float(entry_paint_price.get())
        labor_rate = float(entry_labor_rate.get())

        if feet_wall <= 0 or price_paint <= 0 or labor_rate <= 0:
            raise ValueError

        gallons =(feet_wall / FEET_PER_GALLON)
        labor_hours = gallons * LABOR_HOURS_PER_GALLON
        paint_cost = gallons * price_paint
        labor_cost = labor_hours * labor_rate
        total_cost = paint_cost + labor_cost

        # Display results
        label_result.config(text=(
            f"Gallons of paint: {gallons}\n"
            f"Hours of labor: {labor_hours}\n"
            f"Paint cost: ${paint_cost:,.2f}\n"
            f"Labor cost: ${labor_cost:,.2f}\n"
            f"Total cost: ${total_cost:,.2f}"
        ))

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter positive numbers for all fields.")

# GUI setup
main_window = tk.Tk()
main_window.title("Paint Job Estimator")
main_window.geometry("400x350")
main_window.resizable(False, False)

# Inputs
tk.Label(main_window, text="Wall space (sq ft):").pack(pady=5)
entry_wall = tk.Entry(main_window)
entry_wall.pack()

tk.Label(main_window, text="Paint price per gallon:").pack(pady=5)
entry_paint_price = tk.Entry(main_window)
entry_paint_price.pack()

tk.Label(main_window, text="Labor rate per hour:").pack(pady=5)
entry_labor_rate = tk.Entry(main_window)
entry_labor_rate.pack()

# Calculate button
tk.Button(main_window, text="Calculate", command=calculate, bg="lightblue").pack(pady=15)

# Results
label_result = tk.Label(main_window, text="", justify="left", font=("Courier", 10))
label_result.pack(pady=10)

# Run the application
main_window.mainloop()