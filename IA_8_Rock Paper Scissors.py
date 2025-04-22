import tkinter as tk
import random

# Possible throws
OPTIONS = ['Rock', 'Paper', 'Scissors']

# Game logic using conditional logic
def determine_winner(player, computer):
    if player == computer:
        return 'Tie'
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return 'Player'
    else:
        return 'Computer'

# Define variables for Dark mode colors
dark_bg = "#1e1e1e"
light_text = "#f0f0f0"
but_background = "#333333"
button = "#444444"
accent = "#61dafb"

class RPSGame:
    def __init__(self, main_window):
        self.master = main_window
        main_window.geometry("580x500")
        main_window.title("Rock, Paper, Scissors")
        main_window.configure(bg=dark_bg)
    #Create Counters
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0

        self.info_label = tk.Label(main_window, text="Choose your throw:", font=("OCR A Extended", 14),
                                   bg=dark_bg, fg=accent)
        self.info_label.pack(pady=10)

        self.button_frame = tk.Frame(main_window, bg=dark_bg)
        self.button_frame.pack()


        self.buttons = []
        for option in OPTIONS:
            btn = tk.Button(self.button_frame, text=option, width=10, font=("OCR A Extended", 12),
                            bg=but_background, fg=light_text, activebackground=button,
                            relief=tk.FLAT, command=lambda opt=option: self.play_round(opt))
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            self.buttons.append(btn)

        self.result_label = tk.Label(main_window, text="", font=("OCR A Extended", 12),
                                     bg=dark_bg, fg=light_text)
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(main_window, text=self.get_score_text(), font=("OCR A Extended", 12),
                                    bg=dark_bg, fg=accent)
        self.score_label.pack(pady=10)

        self.reset_button = tk.Button(main_window, text="Reset Game", command=self.reset_game,
                                      font=("OCR A Extended", 10), bg=but_background, fg=light_text,
                                      activebackground=but_background, relief=tk.FLAT)
        self.reset_button.pack(pady=5)

    def play_round(self, player_choice):
        computer_choice = random.choice(OPTIONS)
        winner = determine_winner(player_choice, computer_choice)

        if winner == 'Player':
            self.player_score += 1
            result_text = f"You chose {player_choice}, Computer chose {computer_choice}. You win!"
        elif winner == 'Computer':
            self.computer_score += 1
            result_text = f"You chose {player_choice}, Computer chose {computer_choice}. Computer wins!"
        else:
            self.tie_score += 1
            result_text = f"You both chose {player_choice}. It's a tie!"

        self.result_label.config(text=result_text)
        self.score_label.config(text=self.get_score_text())

    def get_score_text(self):
        return f"Player: {self.player_score} | Computer: {self.computer_score} | Ties: {self.tie_score}"

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.result_label.config(text="")
        self.score_label.config(text=self.get_score_text())

# Run the GUI app
if __name__ == "__main__":
    main_window = tk.Tk()
    app = RPSGame(main_window)
    main_window.mainloop()

