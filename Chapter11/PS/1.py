class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"Vector2D: ({self.x}, {self.y})")


class Vector3D(Vector2D):  # Inherits from Vector2D
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Call Vector2D constructor
        self.z = z

    def display(self):
        print(f"Vector3D: ({self.x}, {self.y}, {self.z})")


# Example
v2 = Vector2D(3, 4)
v2.display()

v3 = Vector3D(1, 2, 3)
v3.display()
