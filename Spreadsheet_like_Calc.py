import tkinter as tk
from tkinter import ttk, messagebox
import math
import csv


class EnhancedSpreadsheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Spreadsheet with Operations")
        self.root.geometry("1200x700")

        # Configuration variables
        self.num_rows = tk.IntVar(value=3)
        self.num_columns = tk.IntVar(value=3)

        # Operation options
        self.operations = ["+", "-", "*", "/", "pow", "sqrt", "sin", "cos", "tan"]

        # Widgets storage
        self.entries = []  # To store all Entry widgets
        self.combo_boxes = []  # To store all ComboBox widgets
        self.results = []  # To store result labels
        self.selected_cells = []  # To track selected cells

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        # Row and Column selectors
        ttk.Label(self.root, text="Rows:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Spinbox(self.root, from_=1, to=10, textvariable=self.num_rows, width=5, command=self.generate_grid).grid(row=0, column=1)

        ttk.Label(self.root, text="Columns:").grid(row=0, column=2, padx=5, pady=5)
        ttk.Spinbox(self.root, from_=1, to=10, textvariable=self.num_columns, width=5, command=self.generate_grid).grid(row=0, column=3)

        # Generate button
        ttk.Button(self.root, text="Generate Grid", command=self.generate_grid).grid(row=0, column=4, padx=5, pady=5)

        # Action buttons
        ttk.Button(self.root, text="Export to CSV", command=self.export_to_csv).grid(row=0, column=5, padx=5, pady=5)
        ttk.Button(self.root, text="Apply to Selected Cells", command=self.apply_to_selected).grid(row=0, column=6, padx=5, pady=5)
        ttk.Button(self.root, text="Column-wise Operation", command=self.column_operations).grid(row=0, column=7, padx=5, pady=5)
        ttk.Button(self.root, text="Multi-row Operation", command=self.multi_row_operations).grid(row=0, column=8, padx=5, pady=5)

        # Grid Frame
        self.grid_frame = ttk.Frame(self.root)
        self.grid_frame.grid(row=1, column=0, columnspan=9, padx=10, pady=10)

        # Initialize grid
        self.generate_grid()

    def generate_grid(self):
        # Clear existing grid
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.entries.clear()
        self.combo_boxes.clear()
        self.results.clear()
        self.selected_cells.clear()

        rows = self.num_rows.get()
        columns = self.num_columns.get()

        # Create grid of entry widgets and combo boxes
        for row in range(rows):
            entry_row = []
            combo_row = []
            for col in range(columns):
                # Entry widget
                entry = ttk.Entry(self.grid_frame, width=10)
                entry.grid(row=row * 2, column=col, padx=5, pady=5)
                entry.bind("<Button-1>", lambda e, r=row, c=col: self.select_cell(r, c))  # Bind click to select cell
                entry_row.append(entry)

                # ComboBox widget (for operations)
                combo = ttk.Combobox(self.grid_frame, values=self.operations, state="readonly", width=8)
                combo.grid(row=row * 2 + 1, column=col, padx=5, pady=5)
                combo.set("+")  # Default operation
                combo_row.append(combo)

            self.entries.append(entry_row)
            self.combo_boxes.append(combo_row)

            # Result label
            result_label = ttk.Label(self.grid_frame, text="Result", relief="sunken", width=15)
            result_label.grid(row=row * 2, column=columns, padx=5, pady=5)
            self.results.append(result_label)

        # Add calculate button
        ttk.Button(self.grid_frame, text="Calculate", command=self.calculate_results).grid(row=rows * 2, column=0, columnspan=columns + 1, pady=10)

    def select_cell(self, row, col):
        if (row, col) in self.selected_cells:
            self.selected_cells.remove((row, col))
        else:
            self.selected_cells.append((row, col))
        #messagebox.showinfo("Selected Cells", f"Selected Cells: {self.selected_cells}")

    def calculate_results(self):
        for row, (entry_row, combo_row, result_label) in enumerate(zip(self.entries, self.combo_boxes, self.results)):
            try:
                # Collect values from the row
                values = [float(entry.get()) if entry.get() else 0 for entry in entry_row]
                operations = [combo.get() for combo in combo_row]

                # Perform chained operations
                result = values[0]
                for i in range(1, len(values)):
                    operation = operations[i - 1]
                    if operation == "+":
                        result += values[i]
                    elif operation == "-":
                        result -= values[i]
                    elif operation == "*":
                        result *= values[i]
                    elif operation == "/":
                        if values[i] != 0:
                            result /= values[i]
                        else:
                            raise ValueError("Division by zero")
                    elif operation == "pow":
                        result = math.pow(result, values[i])
                    elif operation == "sqrt":
                        result = math.sqrt(result)
                    elif operation == "sin":
                        result = math.sin(math.radians(result))
                    elif operation == "cos":
                        result = math.cos(math.radians(result))
                    elif operation == "tan":
                        result = math.tan(math.radians(result))
                    else:
                        raise ValueError(f"Unsupported operation: {operation}")

                # Update result label
                result_label.config(text=f"{result:.2f}")
            except Exception as e:
                messagebox.showerror("Error", f"Error calculating row {row + 1}: {e}")

    def apply_to_selected(self):
        try:
            for row, col in self.selected_cells:
                value = float(self.entries[row][col].get())
                operation = self.combo_boxes[row][col].get()

                # Perform operation
                if operation == "sqrt":
                    result = math.sqrt(value)
                elif operation == "sin":
                    result = math.sin(math.radians(value))
                elif operation == "cos":
                    result = math.cos(math.radians(value))
                elif operation == "tan":
                    result = math.tan(math.radians(value))
                else:
                    result = value  # Default if no special operation

                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Error applying operation: {e}")

    def column_operations(self):
        try:
            for col in range(self.num_columns.get()):
                values = [float(self.entries[row][col].get()) for row in range(self.num_rows.get()) if self.entries[row][col].get()]
                total = sum(values)
                #messagebox.showinfo("Column Operation", f"Column {col + 1}: Total = {total}")
        except Exception as e:
            messagebox.showerror("Error", f"Error in column operations: {e}")

    def multi_row_operations(self):
        try:
            for row in range(self.num_rows.get()):
                values = [float(self.entries[row][col].get()) for col in range(self.num_columns.get()) if self.entries[row][col].get()]
                total = sum(values)
                #messagebox.showinfo("Row Operation", f"Row {row + 1}: Total = {total}")
        except Exception as e:
            messagebox.showerror("Error", f"Error in row operations: {e}")

    def export_to_csv(self):
        try:
            with open("spreadsheet_results.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for row in self.entries:
                    writer.writerow([entry.get() for entry in row])
            messagebox.showinfo("Export Successful", "Results exported to spreadsheet_results.csv")
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting to CSV: {e}")


# Run the application
root = tk.Tk()
app = EnhancedSpreadsheet(root)
root.mainloop()
