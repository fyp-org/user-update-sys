from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ucs.core.database import get_db
from . import schemas, crud, models

router = APIRouter(prefix="/create-project", tags=["Projects"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=int)  # вернём ID
def register_project(payload: schemas.ProjectCreate, db: Session = Depends(get_db)):
    project = crud.create_project(db, payload)
    return project.id_project