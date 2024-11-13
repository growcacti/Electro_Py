import tkinter as tk
from tkinter import messagebox

def depth_first_search(possible_board, diagonal_right_collisions, diagonal_left_collisions, boards, n):
    row = len(possible_board)
    if row == n:
        boards.append(possible_board[:])
        return
    for col in range(n):
        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue
        depth_first_search(
            possible_board + [col],
            diagonal_right_collisions + [row - col],
            diagonal_left_collisions + [row + col],
            boards,
            n,
        )

def n_queens_solution(n):
    boards = []
    depth_first_search([], [], [], boards, n)
    return boards

class NQueensApp(tk.Tk):
    def __init__(self, n=8):
        super().__init__()
        self.title(f"{n}-Queens Problem")
        self.n = n
        self.board_solutions = n_queens_solution(n)
        self.solution_index = 0
        self.create_widgets()
        self.display_solution(self.solution_index)

    def create_widgets(self):
        self.grid_frame = tk.Frame(self)
        self.grid_frame.grid(row=0, column=0, padx=10, pady=10)
        self.grid_buttons = [
            [tk.Label(self.grid_frame, width=4, height=2, relief="solid") for _ in range(self.n)]
            for _ in range(self.n)
        ]
        for i in range(self.n):
            for j in range(self.n):
                self.grid_buttons[i][j].grid(row=i, column=j)

        self.controls = tk.Frame(self)
        self.controls.grid(row=1, column=0, pady=10)
        self.prev_button = tk.Button(self.controls, text="Previous", command=self.show_previous_solution)
        self.prev_button.grid(row=0, column=0, padx=5)
        self.next_button = tk.Button(self.controls, text="Next", command=self.show_next_solution)
        self.next_button.grid(row=0, column=1, padx=5)
        
        self.solution_label = tk.Label(self.controls, text="")
        self.solution_label.grid(row=0, column=2, padx=10)

    def display_solution(self, index):
        for i in range(self.n):
            for j in range(self.n):
                self.grid_buttons[i][j].config(text="", bg="white")

        solution = self.board_solutions[index]
        for row, col in enumerate(solution):
            self.grid_buttons[row][col].config(text="Q", bg="lightblue")
        
        self.solution_label.config(text=f"Solution {index + 1} of {len(self.board_solutions)}")

    def show_previous_solution(self):
        if self.solution_index > 0:
            self.solution_index -= 1
            self.display_solution(self.solution_index)
        else:
            messagebox.showinfo("Info", "This is the first solution.")

    def show_next_solution(self):
        if self.solution_index < len(self.board_solutions) - 1:
            self.solution_index += 1
            self.display_solution(self.solution_index)
        else:
            messagebox.showinfo("Info", "This is the last solution.")

if __name__ == "__main__":
    app = NQueensApp(n=8)
    app.mainloop()
