from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Налаштування URL для MariaDB (без pymysql)
DATABASE_URL = "mariadb+mariadbconnector://root:@localhost:3306/python-fastapi-study"

# Підключення до бази даних
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)