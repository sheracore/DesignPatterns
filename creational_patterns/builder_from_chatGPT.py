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
    def build_foundation(self):
        pass

    def build_structure(self):
        pass

    def build_roof(self):
        pass

    def build_interior(self):
        pass

    def get_house(self):
        pass

# Concrete Builder: Implements the steps
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = "Concrete, brick, and stone"

    def build_structure(self):
        self.house.structure = "Wooden and brick walls"

    def build_roof(self):
        self.house.roof = "Concrete and shingles"

    def build_interior(self):
        self.house.interior = "Modern interior design"

    def get_house(self):
        return self.house

# Director: Orchestrates the building process
class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_interior()

# Client Code
if __name__ == "__main__":
    # Create a Concrete Builder
    builder = ConcreteHouseBuilder()

    # Director takes the builder
    director = Director(builder)

    # Construct the house
    director.construct_house()

    # Get the final product
    house = builder.get_house()
    print(house)
