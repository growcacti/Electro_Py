import tkinter as tk
from tkinter import ttk
import math

# Assuming the Point2D, Vector2D, and Triangle2D classes have already been defined.

class Point2D(object):
    """
    This class represents a 2D point in space.
    Uses several methods to translate, rotate, scale, and reflect the point in space
    """
    def __init__(self, x, y):
        """
        Initializes the point class with x and y coordinates as floating point values
        :param x: A value representing the x coordinate
        :param y: A value representing the y coordinate
        :return:
        """
        self._x = float(x)
        self._y = float(y)

    def copy(self):
        """
        Returns a new Point class with the same x and y coordinates
        :return Point: new Point class
        """
        return Point2D(self.x, self.y)
    def translate(self):
       
        try:
            dx = float(self.dx_entry.get()) if self.dx_entry.get() else 0.0
            dy = float(self.dy_entry.get()) if self.dy_entry.get() else 0.0

            if self.object_var.get() == "Point":
                self.point.translate(dx, dy)
            elif self.object_var.get() == "Triangle":
                for point in self.triangle._points:
                    point.translate(dx, dy)

            self.draw_shapes()
        except ValueError:
            print("Please enter valid numeric values for dx and dy.")



    def rotate_clockwise(self, x, y, angle_radians):
        """
        Rotates the point about another point (x, y) clockwise by a given angle in radians.
        This assumes a left-handed coordinate system, in which the y-axis is positive downwards and positive upwards.

        :param x: X coordinate about which to rotate the point
        :param y: Y coordinate about which to rotate the point
        :param angle_radians: Angle to rotate the point, defined in radians
        :return: Returns None
        """

        nx = math.cos(angle_radians) * (self.x - x) - math.sin(angle_radians) * (self.y - y) + x
        ny = math.sin(angle_radians) * (self.x - x) + math.cos(angle_radians) * (self.y - y) + y

        self.x = nx
        self.y = ny

    def rotate_counterclockwise(self, x, y, angle_radians):
        """
        Rotates the point about another point (x, y) counter-clockwise by a given angle in radians.
        This assumes a left-handed coordinate system, in which the y-axis is positive downwards and positive upwards.

        :param x: X coordinate about which to rotate the point
        :param y: Y coordinate about which to rotate the point
        :param angle_radians: Angle to rotate the point, defined in radians
        :return: Returns None
        """

        self.rotate_clockwise(x, y, -1 * angle_radians)

    def scale(self, x, y, scalar):
        """
        Scales the point about point (x, y) by a constant scalar.  Scalar of 1 means the point stays in the same
        location.  A scalar of 2 doubles the distance between the point (x, y) and the current point.

        :param x: X coordinate about which to scale the point
        :param y: Y coordinate about which to scale the point
        :param scalar: floating point number about which to scale the point.
        :return: Returns None
        """
        # Scales about the point (x, y) by a constant scalar
        self.x = math.fabs(self.x - x) * scalar + x
        self.y = math.fabs(self.y - y) * scalar + y

    def reflect(self, axis):
        """
        Reflects the point about the x or y axis
        :param axis: 'x', 'X', 'y', 'Y'
        :return: Returns None
        """
        if axis is 'x' or axis is 'X':
            self.x *= -1
        elif axis is 'y' or axis is 'Y':
            self.y *= -1

    def __eq__(self, other):
        """
        Determines if two points are equal.
        :param other: Point2D or tuple
        :return: Point2D (self)
        """
        if isinstance(other, type(self)):
            return (self.x == other.x) and (self.y == other.y)
        elif isinstance(other, type((1, 0))) or isinstance(other, type((1., 2.))):
            return (self.x == other[0]) and (self.y == other[1])

        raise ValueError('Invalid Values For Comparison')

    def __ne__(self, other):
        """
        Determines if two points are not equal.
        :param other: Point2D or tuple
        :return: Point2D (self)
        """
        if isinstance(other, type(self)):
            return (self.x != other.x) or (self.y != other.y)
        elif isinstance(other, type((1, 0))) or isinstance(other, type((1., 2.))):
            return (self.x != other[0]) or (self.y != other[1])

        raise ValueError('Invalid Values For Comparison')

    def _prop_get_x(self):
        return self._x
    def _prop_set_x(self, new_x):
        self._x = float(new_x)

    def _prop_get_y(self):
        return self._y
    def _prop_set_y(self, new_y):
        self._y = float(new_y)

    x = property(_prop_get_x, _prop_set_x)
    y = property(_prop_get_y, _prop_set_y)


class Vector2D:
    """
    Represents a 2D Vector.  Origin is at (0, 0).  Uses built-in methods for vector math
    """
    def __init__(self, x, y):
        """
        Initializes the point class with x and y coordinates as floating point values
        :param x: A value representing the x coordinate
        :param y: A value representing the y coordinate
        :return:
        """
        self.x = float(x)
        self.y = float(y)

    def copy(self):
        """
        Returns a Vector2D with the same x and y values
        :return: Vector2D
        """
        return Vector2D(self.x, self.y)

    def magnitude(self):
        """
        Gets the magnitude of the vector.  Same as length
        :return: Float
        """
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def length(self):
        """
        Gets the length of the vector.  Same as magnitude
        :return: Float
        """
        return self.magnitude()

    def normalize(self):
        """
        Returns a new vector with the same direction as the current vector, but with a magnitude of 1
        :return: Vector2D
        """
        return Vector2D(self.x/self.length(), self.y/self.length())

    def scale(self, scalar):
        """
        Scales the vector by a given scalar
        :param scalar: Floating point number representing how much to scale vector
        :return: None
        """
        self.x *= scalar
        self.y *= scalar

    def dot(self, other):
        """
        Returns the dot product of the two vectors.
        :param other: Vector2D or tuple
        :return: Float
        """
        if isinstance(other, type(self)):
            return self.x*other.x + self.y*other.y
        elif isinstance(other, type((0, 0))) and len(other) is 2:
            return self.x*other[0] + self.y*other[1]
        raise ValueError("Other vector not of appropriate type")

    def get_angle_between_vectors(self, other):
        """
        Returns the angle between two vectors.
        :param other: Vector2D
        :return: Float
        """
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def get_radians(self):
        """
        Returns angle of vector in radians
        :return: Float
        """
        result = math.atan2(self.y, self.x)
        if result < 0:
            result += 2 * math.pi
        return result

    def get_degrees(self):
        """
        Returns angle of vector in degrees
        :return: Float
        """
        return math.degrees(self.get_radians())

    def __iadd__(self, other):
        """
        Adds two vectors together.
        :param other: Vector2D or tuple
        :return: Vector2D (self)
        """
        if isinstance(other, type(self)):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, type((1, 0))) or isinstance(other, type((1., 0.))):
            self.x += other[0]
            self.y += other[1]
        return self

    def __isub__(self, other):
        """
        Subtracts other vector from self.
        :param other: Vector2D or tuple
        :return: Vector2D (self)
        """
        if isinstance(other, type(self)):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, type((1, 0))) or isinstance(other, type((1., 2.))):
            self.x -= other[0]
            self.y -= other[1]
        return self

    def __imul__(self, num):
        """
        Scalar multiplier.
        :param num: Number (can be floating point or integer)
        :return: Vector2D (self)
        """
        self.x = self.x * num
        self.y = self.y * num
        return self

    def __idiv__(self, num):
        """
        Scalar division.
        :param num: Number (can be floating point or integer)
        :return: Vector2D (self)
        """
        self.x = self.x / num
        self.y = self.y / num
        return self

    def __mul__(self, other):
        """
        Dot product between two vectors.
        :param other: Vector2D or tuple
        :return: Vector2D (self)
        """
        if isinstance(other, type(self)):
            return self.x*other.x + self.y*other.y
        elif isinstance(other, type((1, 0))) or isinstance(other, type((1., 2.))):
            return self.x*other[0] + self.y*other[1]

        raise ValueError('Invalid Values For Dot Product')

    def __eq__(self, other):
        """
        Determines if two vectors are equal.
        :param other: Vector2D or tuple
        :return: Vector2D (self)
        """
        if isinstance(other, type(self)):
            return (self.x == other.x) and (self.y == other.y)
        elif isinstance(other, type((1, 0))) or isinstance(other, type((1., 2.))):
            return (self.x == other[0]) and (self.y == other[1])

        raise ValueError('Invalid Values For Comparison')

    def __ne__(self, other):
        """
        Determines if two vectors are not equal.
        :param other: Vector2D or tuple
        :return: Vector2D (self)
        """
        if isinstance(other, type(self)):
            return (self.x != other.x) or (self.y != other.y)
        elif isinstance(other, type((1, 0))) or isinstance(other, type((1., 2.))):
            return (self.x != other[0]) or (self.y != other[1])

        raise ValueError('Invalid Values For Comparison')


class Triangle2D(object):
    """
    A class to represent a collision within three points.
    """
    def __init__(self, point_a, point_b, point_c):
        """
        Takes in three points of class Point2D to use as corners of a 2D triangle.  First point is reference point
        :param point_a: First point
        :param point_b: Second point
        :param point_c: Third point
        :return:
        """

        self._points = []
        if isinstance(point_a, Point2D):
            self._points.append(point_a)
        elif isinstance(point_a, type((2, 2))) or isinstance(point_a, type((2., 2.))):
            self._points.append(Point2D(point_a[0], point_a[1]))
        else:
            raise ValueError("Not a tuple of 2 points or a Point2D class")

        if isinstance(point_b, Point2D):
            self._points.append(point_b)
        elif isinstance(point_b, type((2, 2))) or isinstance(point_b, type((2., 2.))):
            self._points.append(Point2D(point_b[0], point_b[1]))
        else:
            raise ValueError("Not a tuple of 2 points or a Point2D class")

        if isinstance(point_c, Point2D):
            self._points.append(point_c)
        elif isinstance(point_c, type((2, 2))) or isinstance(point_c, type((2., 2.))):
            self._points.append(Point2D(point_c[0], point_c[1]))
        else:
            raise ValueError("Not a tuple of 2 points or a Point2D class")

    def copy(self):
        """
        Creates a new Triangle2D class with the same points as the old triangle class
        :return:
        """
        return Triangle2D(self._points[0], self._points[1], self._points[2])

    def collidepoint(self, *args):
        """
        The collide point takes in two different arguments.  One is a tuple, and the other is a Point.
        :param args: Either (x, y) or Point
        :return: Returns True if point is inside the triangle
        """
        # Length of 2 implies the input is a tuple
        if len(args) is 2:
            x = args[0]
            y = args[1]
        # Length of 1 implies input is a point
        elif len(args) is 1:
                x = args[0].x
                y = args[0].y

        else:
            raise ValueError("Improper values passed in")

        point_a = self._points[0]
        point_b = self._points[1]
        point_c = self._points[2]

        # Compute vectors
        v0 = Vector2D(point_c.x - point_a.x, point_c.y - point_a.y)
        v1 = Vector2D(point_b.x - point_a.x, point_b.y - point_a.y)
        v2 = Vector2D(x - point_a.x, y - point_a.y)

        # Compute dot products
        dot00 = v0 * v0
        dot01 = v0 * v1
        dot02 = v0 * v2
        dot11 = v1 * v1
        dot12 = v1 * v2

        # Compute barycentric coordinates
        denominator = 1 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * denominator
        v = (dot00 * dot12 - dot01 * dot02) * denominator

        # Check if point is in triangle
        return (u >= 0) and (v >= 0) and (u + v < 1)

    def collidetriangle(self, triangle):
        """
        Takes another Triangle class and returns whether either triangle collides with each other
        :param triangle: Triangle class
        :return: Returns true if either Triangle intersect the other
        """
        for point in triangle._points:
            if self.collidepoint(point):
                return True
        for point in self._points:
            if triangle.collidepoint(point):
                return True
        return False

    def __eq__(self, other):
        if isinstance(other, type(self)):
            point_a = other.pointa
            point_b = other.pointb
            point_c = other.pointc
        else:
            raise ValueError("Comparison inputs not valid")

        if point_a == self.pointa and point_b == self.pointb and point_c == self.pointc:
            return True
        if point_a == self.pointa and point_b == self.pointc and point_c == self.pointb:
            return True
        if point_a == self.pointb and point_b == self.pointa and point_c == self.pointc:
            return True
        if point_a == self.pointb and point_b == self.pointc and point_c == self.pointa:
            return True
        if point_a == self.pointc and point_b == self.pointa and point_c == self.pointb:
            return True
        if point_a == self.pointc and point_b == self.pointb and point_c == self.pointa:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    def _prop_getpointa(self):
        return self._points[0]
    def _prop_setpointa(self, pointa):
        self._points[0] = pointa

    def _prop_getpointb(self):
        return self._points[1]
    def _prop_setpointb(self, pointb):
        self._points[1] = pointb

    def _prop_getpointc(self):
        return self._points[2]
    def _prop_setpointc(self, pointc):
        self._points[2] = pointc

    pointa = property(_prop_getpointa, _prop_setpointa)
    pointb = property(_prop_getpointb, _prop_setpointb)
    pointc = property(_prop_getpointc, _prop_setpointc)


class TransformApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2D Transformation GUI")
        self.geometry("800x600")

        # Initialize variables and UI elements
        self.selected_object = None
        self.point = Point2D(100, 100)
        self.triangle = Triangle2D(Point2D(200, 200), Point2D(250, 250), Point2D(300, 200))
        
        # Canvas for displaying shapes
        self.canvas = tk.Canvas(self, width=600, height=400, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Control Frame
        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=1, column=0, columnspan=4, pady=10)

        # Buttons and inputs for transformations
        self.create_controls()

        # Display initial shapes
        self.draw_shapes()

    def create_controls(self):
        # Object selection
        tk.Label(self.control_frame, text="Select Object:").grid(row=0, column=0)
        self.object_var = tk.StringVar(value="Point")
        ttk.Combobox(self.control_frame, textvariable=self.object_var, values=["Point", "Triangle"], state="readonly").grid(row=0, column=1)

        # Translate controls
        tk.Label(self.control_frame, text="Translate dx, dy:").grid(row=1, column=0)
        self.dx_entry = tk.Entry(self.control_frame, width=5)
        self.dx_entry.grid(row=1, column=1)
        self.dy_entry = tk.Entry(self.control_frame, width=5)
        self.dy_entry.grid(row=1, column=2)
        tk.Button(self.control_frame, text="Translate", command=self.translate).grid(row=1, column=3)

        # Rotation controls
        tk.Label(self.control_frame, text="Rotate (angle in degrees):").grid(row=2, column=0)
        self.angle_entry = tk.Entry(self.control_frame, width=5)
        self.angle_entry.grid(row=2, column=1)
        tk.Button(self.control_frame, text="Rotate", command=self.rotate_object).grid(row=2, column=2)

        # Scale controls
        tk.Label(self.control_frame, text="Scale (factor):").grid(row=3, column=0)
        self.scale_entry = tk.Entry(self.control_frame, width=5)
        self.scale_entry.grid(row=3, column=1)
        tk.Button(self.control_frame, text="Scale", command=self.scale_object).grid(row=3, column=2)

   
    def translate(self, dx, dy):
        try:
            dx = float(self.dx_entry.get()) if self.dx_entry.get() else 0.0
            dy = float(self.dy_entry.get()) if self.dy_entry.get() else 0.0

            if self.object_var.get() == "Point":
                self.point.translate(dx, dy)
            elif self.object_var.get() == "Triangle":
                for point in self.triangle._points:
                    point.translate(dx, dy)

            self.draw_shapes()
        except ValueError:
            print("Please enter valid numeric values for dx and dy.")

            """
            Moves the point (dx, dy).
            :param dx: Moves the point dx units in the x direction
            :param dy: Moves the point dy units in the y direction
            :return new_location: The new location of the point
            """
        self.x += dx
        self.y += dy

        new_location = (self.x, self.y)
        return new_location

    def rotate_object(self):
        angle = float(self.angle_entry.get())
        angle_radians = math.radians(angle)
        center_x, center_y = 300, 200  # Rotating around a fixed center point
        
        if self.object_var.get() == "Point":
            self.point.rotate_clockwise(center_x, center_y, angle_radians)
        elif self.object_var.get() == "Triangle":
            for point in self.triangle._points:
                point.rotate_clockwise(center_x, center_y, angle_radians)
        
        self.draw_shapes()

    def scale_object(self):
        factor = float(self.scale_entry.get())
        center_x, center_y = 300, 200  # Scaling around a fixed center point

        if self.object_var.get() == "Point":
            self.point.scale(center_x, center_y, factor)
        elif self.object_var.get() == "Triangle":
            for point in self.triangle._points:
                point.scale(center_x, center_y, factor)
        
        self.draw_shapes()

    def draw_shapes(self):
        # Clear canvas
        self.canvas.delete("all")

        # Draw Point
        if self.object_var.get() == "Point":
            x, y = self.point.x, self.point.y
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue", outline="black")

        # Draw Triangle
        if self.object_var.get() == "Triangle":
            points = [(p.x, p.y) for p in self.triangle._points]
            self.canvas.create_polygon(points, fill="", outline="green")

# Run the app
app = TransformApp()
app.mainloop()
