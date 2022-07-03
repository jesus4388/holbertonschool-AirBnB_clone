#!/usr/bin/python3
'# test module for BaseModel'

from models.base_model import BaseModel
from models import base_model
import unittest
import datetime
import os
import uuid


class Test_BaseModel(unittest.TestCase):
    '# test module for BaseModel'

    @classmethod
    def setUpClass(self):
        '# set class'
        self.model = BaseModel()

    def test_file(self):
        os.path.isfile("../../models/base_model.py")

    def test_doc_class(self):
        '# check documentation'
        expected = "Base class"
        self.assertEqual(expected, BaseModel.__doc__)

    def test_doc_file(self):
        '# check create'
        expected = "Airbnb clone project"
        self.assertEqual(expected, base_model.__doc__)

    def test_generation(self):
        '# check generation'
        self.assertIsInstance(self.model, BaseModel)

    def test_attr(self):
        '# check atribute'
        self.model.name = "My First Model"
        self.model.my_number = 89
        self.assertIn("name", self.model.to_dict())
        self.assertIn("my_number", self.model.to_dict())
        self.dict = self.model.to_dict()
        self.assertEqual(self.dict["my_number"], 89)
        self.assertEqual(self.dict["name"], "My First Model")


if __name__ == "__main__":
    '# BaseModel'
    unittest.main()
