from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from project.settings.database import get_db

from project.app.views import product_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}


@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    # Example query (replace with your logic)
    return {"message": "Query database here"}

app.include_router(product_router)