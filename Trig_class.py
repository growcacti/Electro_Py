import tkinter as tk
import math

class TriangleSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Triangle Solver")
        self.root.geometry("600x700")
        
        # Initialize GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Input labels and entries
        tk.Label(self.root, text="Side a").grid(row=0, column=0)
        self.entry_a = tk.Entry(self.root)
        self.entry_a.grid(row=0, column=1)

        tk.Label(self.root, text="Side b").grid(row=1, column=0)
        self.entry_b = tk.Entry(self.root)
        self.entry_b.grid(row=1, column=1)

        tk.Label(self.root, text="Side c").grid(row=2, column=0)
        self.entry_c = tk.Entry(self.root)
        self.entry_c.grid(row=2, column=1)

        tk.Label(self.root, text="Angle A").grid(row=3, column=0)
        self.entry_A = tk.Entry(self.root)
        self.entry_A.grid(row=3, column=1)

        tk.Label(self.root, text="Angle B").grid(row=4, column=0)
        self.entry_B = tk.Entry(self.root)
        self.entry_B.grid(row=4, column=1)

        tk.Label(self.root, text="Angle C").grid(row=5, column=0)
        self.entry_C = tk.Entry(self.root)
        self.entry_C.grid(row=5, column=1)

        # Buttons for calculations
        tk.Button(self.root, text="Law of Sines", command=self.calculate_law_of_sines).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Law of Cosines", command=self.calculate_law_of_cosines).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text="Area", command=self.calculate_area).grid(row=8, column=0, columnspan=2)
        tk.Button(self.root, text="Circumscribed Radius", command=self.calculate_circumscribed_radius).grid(row=9, column=0, columnspan=2)
        tk.Button(self.root, text="Draw Triangle", command=self.draw_triangle).grid(row=10, column=0, columnspan=2)

        # Output list box
        tk.Label(self.root, text="Results:").grid(row=11, column=0)
        self.listbox_output = tk.Listbox(self.root, height=10, width=40)
        self.listbox_output.grid(row=12, column=0, columnspan=2)

        # Canvas for triangle drawing
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.grid(row=0, column=2, rowspan=13)

    def get_input(self, entry):
        try:
            return float(entry.get()) if entry.get() else None
        except ValueError:
            return None
    
    def calculate_law_of_sines(self):
        a = self.get_input(self.entry_a)
        b = self.get_input(self.entry_b)
        c = self.get_input(self.entry_c)
        A = self.get_input(self.entry_A)
        B = self.get_input(self.entry_B)
        C = self.get_input(self.entry_C)
        self.listbox_output.delete(0, tk.END)
        
        if a and A:
            self.listbox_output.insert(tk.END, f"a / sin(A) = {a / math.sin(math.radians(A)):.2f}")
        if b and B:
            self.listbox_output.insert(tk.END, f"b / sin(B) = {b / math.sin(math.radians(B)):.2f}")
        if c and C:
            self.listbox_output.insert(tk.END, f"c / sin(C) = {c / math.sin(math.radians(C)):.2f}")
    
    def calculate_law_of_cosines(self):
        a = self.get_input(self.entry_a)
        b = self.get_input(self.entry_b)
        c = self.get_input(self.entry_c)
        C = self.get_input(self.entry_C)
        self.listbox_output.delete(0, tk.END)
        
        if a and b and C:
            c_calculated = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))
            self.listbox_output.insert(tk.END, f"Calculated side c: {c_calculated:.2f}")
        
        if a and b and c:
            cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
            self.listbox_output.insert(tk.END, f"cos(C) = {cos_C:.2f}")
    
    def calculate_area(self):
        a = self.get_input(self.entry_a)
        b = self.get_input(self.entry_b)
        C = self.get_input(self.entry_C)
        self.listbox_output.delete(0, tk.END)
        
        if a and b and C:
            area = 0.5 * a * b * math.sin(math.radians(C))
            self.listbox_output.insert(tk.END, f"Area = {area:.2f}")
    
    def calculate_circumscribed_radius(self):
        a = self.get_input(self.entry_a)
        b = self.get_input(self.entry_b)
        c = self.get_input(self.entry_c)
        try:
            s = (a + b + c) / 2
            radius = (a * b * c) / math.sqrt(s * (s - a) * (s - b) * (s - c))
            self.listbox_output.delete(0, tk.END)
            self.listbox_output.insert(tk.END, f"Circumscribed Circle Radius (R): {radius:.2f}")
        except (TypeError, ValueError):
            self.listbox_output.insert(tk.END, "Please enter valid side lengths")

    def draw_triangle(self):
        self.canvas.delete("all")
        
        # Get side lengths from entries
        a = self.get_input(self.entry_a)
        b = self.get_input(self.entry_b)
        c = self.get_input(self.entry_c)
        
        if not (a and b and c):
            self.listbox_output.insert(tk.END, "Please enter all three sides to draw the triangle")
            return

        # Scale factor to fit the triangle in the canvas
        scale = 200 / max(a, b, c)

        # Coordinates for the first point
        x1, y1 = 50, 300
        x2, y2 = x1 + b * scale, y1

        # Calculate third point using side a and c, and trigonometry
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        x3 = x1 + a * scale * math.cos(angle_C)
        y3 = y1 - a * scale * math.sin(angle_C)

        # Draw the triangle
        self.canvas.create_line(x1, y1, x2, y2, fill="blue")
        self.canvas.create_line(x2, y2, x3, y3, fill="blue")
        self.canvas.create_line(x3, y3, x1, y1, fill="blue")

        # Label the sides
        self.canvas.create_text((x1 + x2) / 2, y1 + 10, text="b")
        self.canvas.create_text((x1 + x3) / 2 - 10, (y1 + y3) / 2, text="c")
        self.canvas.create_text((x2 + x3) / 2 + 10, (y2 + y3) / 2, text="a")
        
        # Label the angles
        self.canvas.create_text(x1 - 10, y1 + 10, text="A")
        self.canvas.create_text(x2 + 10, y2 + 10, text="B")
        self.canvas.create_text(x3, y3 - 10, text="C")

# Initialize Tkinter and run the app
root = tk.Tk()
app = TriangleSolverApp(root)
root.mainloop()
