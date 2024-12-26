from abc import ABC, abstractmethod

# Implementor Interface
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

# Concrete Implementors
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} with vector rendering"

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} with raster rendering"

# Abstraction
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)

# Client Code
if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle1 = Circle(vector_renderer, 10)
    print(circle1.draw())  # Outputs: Drawing a circle of radius 10 with vector rendering

    circle2 = Circle(raster_renderer, 20)
    print(circle2.draw())  # Outputs: Drawing a circle of radius 20 with raster rendering
