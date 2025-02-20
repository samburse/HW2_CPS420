from fastapi import FastAPI
from web.rectangle_router import rectangle_router

app = FastAPI()

app.include_router(rectangle_router, prefix="/rectangle", tags=["Rectangle"])
