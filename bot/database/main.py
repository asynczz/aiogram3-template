from typing import Final
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bot.misc.env import settings

class Database:
    BASE: Final = declarative_base()

    def __init__(self):
        self.__engine = create_engine(settings.database_url)
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine