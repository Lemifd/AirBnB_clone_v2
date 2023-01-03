#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, obj=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            new_dict = {}
            for k, v in FileStorage.__objects.items():
                if cls.__name__ in k:
                    new_dict[k] = v
            return new_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
            
    def delete(self, obj=None):
        """delete obj from __objects"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[key]

   def reload(self):
        """serialize the file path to JSON file path"""
        try:
            temp = {}
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, val in (json.load(f)).items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass

    def close(self):
        """Deserialize the JSON file to objects"""
        self.reload()
