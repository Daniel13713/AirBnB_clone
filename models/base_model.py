#!/usr/bin/python3
""" Class BaseModel"""

import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Class BaseModel that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], time
                )
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], time
                )
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel class"""
        class_name = self.__class__.__name__
        return "[{0}] ({1}) {2}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictorionary of all keys and values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
