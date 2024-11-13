import tkinter as tk
import random
import time

# Set up constants
DICE_SIZE = 50
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6
REWARD = 4
PENALTY = 1

class DiceMathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Math Game")
        
        # Initialize variables
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.score = 0
        self.start_time = None
        self.sum_answer = 0
        
        # Set up GUI elements
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)
        
        self.timer_label = tk.Label(root, text="Time Left: 30s", font=("Arial", 14))
        self.timer_label.grid(row=1, column=0)
        
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.grid(row=1, column=1)
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=self.check_answer)
        self.submit_button.grid(row=2, column=2, padx=5, pady=5)
        
        self.start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=self.start_game)
        self.start_button.grid(row=3, column=1, pady=5)
        
        # Predefined dice faces as numbers and dots
        self.dice_faces = [
            ([], 1), (["top-left", "bottom-right"], 2),
            (["top-left", "center", "bottom-right"], 3),
            (["top-left", "top-right", "bottom-left", "bottom-right"], 4),
            (["top-left", "top-right", "center", "bottom-left", "bottom-right"], 5),
            (["top-left", "top-right", "center-left", "center-right", "bottom-left", "bottom-right"], 6)
        ]

    def start_game(self):
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.score = 0
        self.start_time = time.time()
        self.update_timer()
        self.generate_dice()
        
    def generate_dice(self):
        self.canvas.delete("all")
        self.sum_answer = 0
        dice_count = random.randint(MIN_DICE, MAX_DICE)
        
        for _ in range(dice_count):
            die = random.choice(self.dice_faces)
            self.draw_die(die[0])
            self.sum_answer += die[1]

    def draw_die(self, dots):
        x = random.randint(0, CANVAS_WIDTH - DICE_SIZE)
        y = random.randint(0, CANVAS_HEIGHT - DICE_SIZE)
        
        self.canvas.create_rectangle(x, y, x + DICE_SIZE, y + DICE_SIZE, outline="black", width=2)
        
        dot_positions = {
            "top-left": (x + 10, y + 10),
            "top-right": (x + DICE_SIZE - 10, y + 10),
            "center": (x + DICE_SIZE / 2, y + DICE_SIZE / 2),
            "center-left": (x + 10, y + DICE_SIZE / 2),
            "center-right": (x + DICE_SIZE - 10, y + DICE_SIZE / 2),
            "bottom-left": (x + 10, y + DICE_SIZE - 10),
            "bottom-right": (x + DICE_SIZE - 10, y + DICE_SIZE - 10),
        }
        
        for dot in dots:
            dx, dy = dot_positions[dot]
            self.canvas.create_oval(dx - 5, dy - 5, dx + 5, dy + 5, fill="black")
        
    def check_answer(self):
        response = self.entry.get()
        if response.isdigit() and int(response) == self.sum_answer:
            self.correct_answers += 1
            self.score += REWARD
        else:
            self.incorrect_answers += 1
            self.score -= PENALTY
        self.entry.delete(0, tk.END)
        self.update_score()
        self.generate_dice()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        
    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        time_left = QUIZ_DURATION - elapsed_time
        self.timer_label.config(text=f"Time Left: {time_left}s")
        
        if time_left > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.canvas.delete("all")
        self.canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2,
                                text=f"Game Over!\nScore: {self.score}\nCorrect: {self.correct_answers}\nIncorrect: {self.incorrect_answers}",
                                font=("Arial", 16), fill="black")
        self.start_button.config(state=tk.NORMAL)

# Initialize and run the game
root = tk.Tk()
app = DiceMathApp(root)
root.mainloop()
