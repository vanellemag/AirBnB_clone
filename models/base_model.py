#!/usr/bin/python3
""" Module base_model that defines all common attributes
for other classes
"""

import datetime as d
import uuid


class BaseMode:
    """Class that defines all common attributes/methods for other classes
    """

    id = str(uuid.uuid4())
    created_at = d.date.today()
    updated_at = d.date.today()

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__
        """
        name = self.__class__.__name__
        dic = self.__class__.__dict__
        print("[{:}] ({:}) <{:}>".format(name, self.id, dic))

    def save(self):
        """methods that updates the public instance
        attribute with current datetime
        """

        update_at = d.date.today()

    def to_dict(self):
        """method that returns dictionnary containing
        all keys/values of __dict__ of the instance
        """

        self.__dict__ = __dict__
        self.__dict__.append(__class__)
        self.created_at = d.isoformat()
        self.updated_at = d.isoformat()
