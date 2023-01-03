#!/usr/bin/python3
"""DBStorage Module"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """Class for DB storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize db storage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current dataase session"""

        dic = {}
        if cls:
            cls = eval(cls) if isinstance(cls, str) else cls
            objs = self.__session.query(cls)
            for element in query:
                key = "{}.{}".format(type(element).__name__, element.id)
                dic[key] = element
        else:
            cls_list = [State, City, User, Place, Review, Amenity]
            for clsl in cls_list:
                objs = self.__session.query(clsl)
                for element in objs:
                    key = "{}.{}".format(type(element).__name__, element.id)
                    dic[key] = element
        return (dic)

    def new(self, obj):
        """adds object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine,
                            expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """Closes and stops the session"""
        self.__session.close()
