from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WallInput(BaseModel):
    width_m: float
    height_m: float
    brick_width_cm: float
    brick_height_cm: float

@app.post("/kalkulator/pustaki")
def calculate_bricks(data: WallInput):
    area_m2 = data.width_m * data.height_m
    brick_area_m2 = (data.brick_width_cm / 100) * (data.brick_height_cm / 100)
    brick_count = int(area_m2 / brick_area_m2)
    return {
        "powierzchnia_m2": round(area_m2, 2),
        "liczba_pustakow": brick_count
    }
