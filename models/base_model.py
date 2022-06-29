#!/usr/bin/python3

'''BaseModel that defines all common attributes/methods for other classes'''

import uuid
from datetime import datetime
import time


class BaseModel:
    '''creating BaseModel'''
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) != 0:
            for arg in kwargs:
                if (arg != "__class__"):
                    setattr(self, arg, kwargs[arg])
        else:
            new_id = uuid.uuid4()
            self.id = str(new_id)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''defining __str__'''
        return (f"[<{__class__.__name__}>] <{self.id}> <{self.__dict__}>")

    def save(self):
        '''defining save'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''defining to_dict'''
        dictio = self.__dict__.copy()
        dictio["__class__"] = __class__.__name__
        return(dictio)
