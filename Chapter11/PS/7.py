class VectorN:
    def __init__(self, components):
        self.components = components

    def __len__(self):
        return len(self.components)  # Dimension of vector


# Example
v = VectorN([7, 8, 10])
print(len(v))  # Displays dimension: 3
