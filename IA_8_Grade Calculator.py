import tkinter as tk
from tkinter import messagebox


def calc_average(s1, s2, s3, s4, s5):
    return (s1 + s2 + s3 + s4 + s5) / 5.0


def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def display_results():
    try:
        scores = []
        for entry in score_entries:
            score = float(entry.get())
            scores.append(score)

        average = calc_average(scores[0], scores[1], scores[2], scores[3], scores[4])

        result_text = "Score\tNumeric Grade\tLetter Grade\n"
        result_text += "---------------------------------------\n"

        i = 0
        while i < len(scores):
            result_text += f"Score {i + 1}:\t{scores[i]:.2f}\t\t{determine_grade(scores[i])}\n"
            i += 1

        result_text += f"\nAverage:\t{average:.2f}\t\t{determine_grade(average)}"

        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all scores.")


# Set up GUI window
main_window = tk.Tk()
main_window.title("Grade Calculator")

# Input labels and fields
score_entries = []
i = 0
while i < 5:
    tk.Label(main_window, text=f"Enter score {i + 1}:").grid(row=i, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(main_window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    score_entries.append(entry)
    i += 1

# Submit button
submit_button = tk.Button(main_window, text="Calculate Grades", command=display_results)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(main_window, text="", justify="left", font=("Courier", 10))
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI
main_window.mainloop()