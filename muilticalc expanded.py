import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FlexibleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Flexible Configurable Calculator")
        self.root.geometry("800x700")
        
        # Variables
        self.num_entries = tk.IntVar(value=2)
        self.entries = []
        self.results = []
        
        # UI Components
        self.setup_ui()

    def setup_ui(self):
        # Number of Entries Selection
        ttk.Label(self.root, text="Number of Variables:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        num_entry_spinbox = ttk.Spinbox(self.root, from_=2, to=10, textvariable=self.num_entries, command=self.update_entries)
        num_entry_spinbox.grid(row=0, column=1, padx=10, pady=5)

        # Entries Frame
        self.entries_frame = ttk.Frame(self.root)
        self.entries_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.update_entries()

        # Operations Section
        ttk.Label(self.root, text="Select Operation:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.operation_combo = ttk.Combobox(self.root, values=dir(math), state="readonly", width=20)
        self.operation_combo.grid(row=2, column=1, padx=10, pady=5)
        self.operation_combo.set("sin")  # Default operation
        
        ttk.Button(self.root, text="Apply Operation", command=self.apply_operation).grid(row=2, column=2, padx=10, pady=5)

        # Power and Sum Section
        ttk.Label(self.root, text="Raise to Power (N):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.power_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.power_var, width=10).grid(row=3, column=1, padx=10, pady=5)
        ttk.Button(self.root, text="Compute Power Sum", command=self.compute_power_sum).grid(row=3, column=2, padx=10, pady=5)

        # Roots Section
        ttk.Label(self.root, text="Root Degree (N):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.root_degree_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.root_degree_var, width=10).grid(row=4, column=1, padx=10, pady=5)
        ttk.Button(self.root, text="Compute Roots", command=self.compute_roots).grid(row=4, column=2, padx=10, pady=5)

        # Result Display
        ttk.Label(self.root, text="Result:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.result_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.result_var, state="readonly", width=50).grid(row=5, column=1, columnspan=2, padx=10, pady=5)

        # Graphing Section
        ttk.Button(self.root, text="Plot Results", command=self.plot_results).grid(row=6, column=0, columnspan=3, pady=10)

        # Canvas for Graph
        self.canvas_frame = ttk.Frame(self.root)
        self.canvas_frame.grid(row=7, column=0, columnspan=4, pady=10)
        
    def update_entries(self):
        # Clear current entries
        for widget in self.entries_frame.winfo_children():
            widget.destroy()
        self.entries.clear()

        # Create new entries
        for i in range(self.num_entries.get()):
            ttk.Label(self.entries_frame, text=f"Variable {i + 1}:").grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(self.entries_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

    def apply_operation(self):
        try:
            # Retrieve values
            values = [float(entry.get()) for entry in self.entries if entry.get()]
            operation = self.operation_combo.get()
            
            # Apply operation
            if hasattr(math, operation):
                func = getattr(math, operation)
                self.results = [func(val) for val in values]
                self.result_var.set(", ".join(map(str, self.results)))
            else:
                raise ValueError("Invalid Operation")
        except Exception as e:
            messagebox.showerror("Error", f"Could not calculate: {e}")

    def compute_power_sum(self):
        try:
            # Retrieve values
            values = [float(entry.get()) for entry in self.entries if entry.get()]
            power = float(self.power_var.get())
            
            # Compute power sum
            self.results = [val ** power for val in values]
            result_sum = sum(self.results)
            self.result_var.set(f"Power Sum: {result_sum}, Values: {self.results}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not compute power sum: {e}")

    def compute_roots(self):
        try:
            # Retrieve values
            values = [float(entry.get()) for entry in self.entries if entry.get()]
            root_degree = float(self.root_degree_var.get())
            
            # Compute roots
            self.results = [val ** (1 / root_degree) for val in values]
            self.result_var.set(f"Roots: {self.results}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not compute roots: {e}")

    def plot_results(self):
        if not self.results:
            messagebox.showerror("Error", "No results to plot.")
            return
        
        # Create a matplotlib figure
        fig, ax = plt.subplots()
        ax.plot(self.results, marker="o")
        ax.set_title("Results Plot")
        ax.set_xlabel("Index")
        ax.set_ylabel("Result Values")

        # Embed matplotlib figure in Tkinter Canvas
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()  # Clear previous canvas
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas.draw()

# Run the application
root = tk.Tk()
app = FlexibleCalculator(root)
root.mainloop()
