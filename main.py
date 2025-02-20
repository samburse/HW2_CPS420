from fastapi import FastAPI

app = FastAPI()


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        """Compute and return the rectangle's area."""
        return self.width * self.height

    @property
    def circumference(self) -> float:
        """Compute and return the rectangle's circumference."""
        return 2 * (self.width + self.height)


@app.get("/rectangle")
def get_rectangle_info(width: float, height: float):
    """
    Provide width and height as query parameters:
    e.g. /rectangle?width=8&height=15
    """
    rect = Rectangle(width=width, height=height)
    return {
        "width": rect.width,
        "height": rect.height,
        "area": rect.area,
        "circumference": rect.circumference
    }
