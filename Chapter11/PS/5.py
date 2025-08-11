class Vector:
    def __init__(self, components):
        self.components = components  # List of values

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))  # Dot product

    def __str__(self):
        # Special case for 3D: "7i + 8j + 10k"
        if len(self.components) == 3:
            return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"
        return str(self.components)


# Example
v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

print(v1 + v2)  # Vector sum
print(v1 * v2)  # Dot product
