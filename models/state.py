#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns the list of City instances that belong to the state"""
            from models import storage
            cities_dict = storage.all(City)
            city_list = []
            for val in cities_dict.values():
                if self.id == val.state_id:
                    city_list.append(val)
            return city_list
    else:
        cities = relationship(
                "City",
                back_populates="state",
                cascade="all, delete, delete-orphan")

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        new_dict['updated_at'] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        return new_dict
