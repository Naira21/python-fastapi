from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Базовий клас для моделей
Base = declarative_base()

# Опис моделі таблиці
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)