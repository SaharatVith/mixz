from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models
from pydantic import BaseModel
from datetime import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

template = Jinja2Templates(directory="templates")


class Place(BaseModel):
    name: str
    image_cover: str
    description: str
    address: str
    latitude: float
    longitude: float
    tag: str
    open_time: time
    close_time: time


@app.get("/")
async def index_page(request: Request, db: Session = Depends(get_db)):
    family_places = db.query(models.Place).filter_by(tag="family").all()
    recommended_places = db.query(models.Place).filter_by(tag="recommended").all()
    return template.TemplateResponse(
        "index.html",
        {
            "request": request,
            "family_places": family_places,
            "recommended_places": recommended_places,
        },
    )


@app.get("/detail/{place_id}")
async def place_detail(place_id: int, request: Request, db: Session = Depends(get_db)):
    place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="Post not found")

    return template.TemplateResponse(
        "detail.html",
        {
            "request": request,
            "place": place,
        },
    )


@app.get("/place")
async def test_page(
    request: Request, place_name: str | None = None, db: Session = Depends(get_db)
):
    print(place_name)
    places = db.query(models.Place).filter_by(tag=place_name).all()
    return template.TemplateResponse(
        "maps.html",
        {"request": request, "places": places},
    )


@app.post("/create")
async def create_new_place(place: Place, db: Session = Depends(get_db)):
    new_place = models.Place(**place.model_dump())
    db.add(new_place)
    db.commit()
    db.refresh(new_place)


@app.put("/{place_id}")
async def update_place(
    place_id: int, update_place: Place, db: Session = Depends(get_db)
):
    place = db.query(models.Place).filter(models.Place.id == place_id)
    place.update()
