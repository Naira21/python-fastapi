from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Integer

from sqlalchemy.orm import Session

from database import SessionLocal, engine
from model import User, Base


# Ініціалізація FastAPI
app = FastAPI()

# Створення таблиць при запуску
@app.on_event("startup")
async def startup_event():
    # Створення таблиць у базі даних
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()  # Створення нового сеансу
    try:
        yield db
    finally:
        db.close()  # Закриття сеансу після завершення запиту

# Приклад API-ендпойнта для роботи з базою даних
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.post("/users/")
def create_user(name:str, email:str, db: Session = Depends(get_db)):
    new_user=User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.patch("/users/{id}")
def update(id: int, email:str, db: Session = Depends(get_db)):
    user=db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.email=email
    db.commit()
    db.refresh(user)

@app.delete("/user/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"ok": True}