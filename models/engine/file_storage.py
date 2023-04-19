#!/usr/bin/python3
"""
    Define class FileStorage
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        '''
            Return the dictionary
        '''
        fs_objects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for key, val in self.__objects.items():
                    if cls == key.split('.')[0]:
                        fs_objects[key] = val
            elif cls.__name__ in classes:
                for key, val in self.__objects.items():
                    if cls.__name__ == key.split('.')[0]:
                        fs_objects[key] = val
        else:
            return self.__objects
        return fs_objects
=======
        """
        Returns a dictionary of models currently in storage.
        Update that returns the list of objects of one type of class (optional)
        """
        if cls is None:
            return FileStorage.__objects
        else:
            cls_dict = {}
            for key, obj_val in FileStorage.__objects.items():
                if isinstance(obj_val, cls):
                    cls_dict[key] = obj_val
            return cls_dict
>>>>>>> 67222fa3eed6ee3a63f2e40b5d547effd1c2e051

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
<<<<<<< HEAD
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
=======
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {'BaseModel': BaseModel,
                   'User': User,
                   'Place': Place,
                   'State': State,
                   'City': City,
                   'Amenity': Amenity,
                   'Review': Review}
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
>>>>>>> 67222fa3eed6ee3a63f2e40b5d547effd1c2e051
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """
        delete object from __objects if it's inside
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
        self.save()

    def close(self):
        """
        call reload
=======
        """Method to delete obj from __objects if it’s inside"""
        if obj is not None:
            obj_cls = str(obj).split(" ")[0]
            obj_cls = obj_cls[1:-1]
            key = obj_cls + "." + obj.id
            if key in FileStorage.__objects:
                del(self.all()[key])
                self.save()

    def close(self):
        """method for deserializing the JSON file to objects
>>>>>>> 67222fa3eed6ee3a63f2e40b5d547effd1c2e051
        """
        self.reload()
