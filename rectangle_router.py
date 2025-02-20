from fastapi import APIRouter, Query
from domain.rectangle import Rectangle

rectangle_router = APIRouter()

@rectangle_router.get("/")
def get_rectangle_info(
    width: float = Query(..., description="Width of the rectangle"),
    height: float = Query(..., description="Height of the rectangle")
):
    
    rect = Rectangle(width=width, height=height)
    return {
        "width": rect.width,
        "height": rect.height,
        "area": rect.area,
        "circumference": rect.circumference
    }
