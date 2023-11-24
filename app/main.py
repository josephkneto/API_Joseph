from typing import List  # Add this line for the List type
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/quotes/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db=db, member=member)

@app.get("/")
def hello_world():
    return "Hello World"

@app.get("/quotes/", response_model=List[schemas.Member])  # Fix the response_model here
def read_members(db: Session = Depends(get_db)):
    members = crud.get_members(db)
    return members

@app.get("/quotes/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.put("/quotes/{member_id}", response_model=schemas.Member)
def update_member(member_id: int, member: schemas.MemberUpdate, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return crud.update_member(db=db, member=member, member_id=member_id)

@app.delete("/quotes/{member_id}", response_model=schemas.DeletedResponse)
def delete_member(member_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_member(db=db, member_id=member_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"message": "Member deleted successfully", "deleted_member_id": member_id}
