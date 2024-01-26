import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DB_USER = os.environ.get("DB_PG_USER")
DB_PASSWORD = os.environ.get("DB_PG_PASSWORD")
DB_HOST = os.environ.get("DB_PG_HOST")
DB_NAME = os.environ.get("DB_PG_NAME")

DATABASE_PG_URL = "postgresql+psycopg2://{}:{}@{}/{}".format(
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)

pg_session_local = sessionmaker(
    autocommit=False, autoflush=False, bind=create_engine(DATABASE_PG_URL)
)


def get_db_pgwea():
    db = pg_session_local()

    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
