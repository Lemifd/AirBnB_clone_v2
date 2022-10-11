#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """Get cities by state"""
        city_list = []
        result = []
        cities = models.storage.all()
        for key in cities:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                city_list.append(cities[key])
        for i in city_list:
            if (i.state_id == self.id):
                result.append(i)
        return (result)
