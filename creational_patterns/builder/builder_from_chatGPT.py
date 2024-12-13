# Product: The complex object being built
class House:
    def __init__(self):
        self.foundation = None
        self.structure = None
        self.roof = None
        self.interior = None

    def __str__(self):
        return (f"Foundation: {self.foundation}, Structure: {self.structure}, "
                f"Roof: {self.roof}, Interior: {self.interior}")

# Builder: Abstract Builder Interface
class HouseBuilder:
    def build_foundation(self, foundation):
        pass

    def build_structure(self, structure):
        pass

    def build_roof(self, roof):
        pass

    def build_interior(self, interior):
        pass

    def get_house(self):
        pass

# Concrete Builder: Implements the steps
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self, foundation):
        self.house.foundation = foundation
        return self  # Return self for method chaining

    def build_structure(self, structure):
        self.house.structure = structure
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_interior(self, interior):
        self.house.interior = interior
        return self

    def get_house(self):
        return self.house


# Client Code
if __name__ == "__main__":
    # Create a Concrete Builder
    builder = ConcreteHouseBuilder()
    builder.build_foundation("Concrete, brick, and stone")\
           .build_roof("Concrete and shingles")\
           .build_structure("Wooden and brick walls")\
           .build_interior("Modern interior design")
    print(builder.get_house())


