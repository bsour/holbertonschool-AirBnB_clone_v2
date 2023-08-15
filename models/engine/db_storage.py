#!/usr/bin/python3
""" Use sqlAlchemy to declare a database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Start link class to table in database"""
        username = os.getenv("HBNB_MYSQL_USER", default=None)
        password = os.getenv("HBNB_MYSQL_PWD", default=None)
        hostname = os.getenv("HBNB_MYSQL_HOST", default=None)
        database = os.getenv("HBNB_MYSQL_DB", default=None)
        env = os.getenv("HBNB_ENV", default=None)

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    username, password, hostname, database),
                pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of models currently in database"""
        if cls is None:
            classes = [User, State, City, Place, Amenity, Review]
        else:
            classes = [cls]

        obj_dict = {}
        for cls in classes:
            query = self.__session.query(cls).all()
            for obj in query:
                class_name = obj.__class__.__name__
                obj_id = obj.id
                key = f"{class_name}.{obj_id}"
                obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close a session"""
        self.__session.close()
