import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        ''' Generate a unique ID for the instance.'''
        self.id = str(uuid.uuid4())
        # Set the created_at and updated_at attributes to the current datetime
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''' Return a string representation of the object.'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' Update the updated_at attribute with the current datetime.'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Create a dictionary containing the object's attributes.'''
        obj_dict = self.__dict__.copy()
        ''' Add the class name to the dictionary.'''
        obj_dict['__class__'] = self.__class__.__name
        ''' Convert created_at and updated_at to ISO format strings.'''
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
