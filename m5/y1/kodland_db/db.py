from os import path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ROOT = path.dirname(path.realpath(__file__))

SQLALCHEMY_DATABASE_URL = f"sqlite:///{ROOT}/db.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
sess = local_session()

Base = declarative_base()
