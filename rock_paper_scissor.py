'''
-1 rock
0 paper
1 scissor
'''

import random
import tkinter as tk

try:
    import winsound  # Windows sound
    SOUND = True
except ImportError:
    SOUND = False


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("RPS Arena — Human vs Machine")
        self.root.geometry("350x400")
        self.root.resizable(False, False)

        self.choices = (-1, 0, 1)
        self.names = {
            -1: "🪨 Rock",
             0: "📄 Paper",
             1: "✂️ Scissors"
        }

        self.user_score = 0
        self.computer_score = 0

        self.create_ui()

    def create_ui(self):
        tk.Label(
            self.root,
            text="RPS ARENA",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.score_label = tk.Label(
            self.root,
            text="You: 0  |  Computer: 0",
            font=("Arial", 12)
        )
        self.score_label.pack(pady=5)

        self.result_label = tk.Label(
            self.root,
            text="Make your move",
            font=("Arial", 14)
        )
        self.result_label.pack(pady=20)

        for value, name in self.names.items():
            tk.Button(
                self.root,
                text=name,
                width=18,
                command=lambda v=value: self.play(v)
            ).pack(pady=4)

        tk.Button(
            self.root,
            text="🔄 Reset Game",
            width=18,
            command=self.reset_game
        ).pack(pady=20)

    def decide_winner(self, user, computer):
        if user == computer:
            return "draw"
        elif (user == -1 and computer == 1) or \
             (user == 0 and computer == -1) or \
             (user == 1 and computer == 0):
            return "win"
        else:
            return "lose"

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        outcome = self.decide_winner(user_choice, computer_choice)

        if outcome == "win":
            self.user_score += 1
            text = "YOU WIN!"
            color = "green"
            self.play_sound(800)
        elif outcome == "lose":
            self.computer_score += 1
            text = "YOU LOSE!"
            color = "red"
            self.play_sound(300)
        else:
            text = "DRAW"
            color = "orange"
            self.play_sound(500)

        self.result_label.config(
            text=f"You: {self.names[user_choice]}\n"
                 f"Computer: {self.names[computer_choice]}\n\n{text}",
            fg=color
        )

        self.score_label.config(
            text=f"You: {self.user_score}  |  Computer: {self.computer_score}"
        )

        self.flash_animation()

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="You: 0  |  Computer: 0")
        self.result_label.config(text="Make your move", fg="black")

    def play_sound(self, freq):
        if SOUND:
            winsound.Beep(freq, 150)
        else:
            self.root.bell()

    def flash_animation(self):
        self.root.after(100, lambda: self.result_label.config(font=("Arial", 16, "bold")))
        self.root.after(300, lambda: self.result_label.config(font=("Arial", 14)))


# ---- RUN APP ----
root = tk.Tk()
app = RockPaperScissors(root)
root.mainloop()