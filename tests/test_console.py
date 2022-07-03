#!/usr/bin/python3
'# tests console'


from console import HBNBCommand
from models.base_model import BaseModel
import unittest
from models import storage
from models import base_model


class test_console(unittest.TestCase):
    '# test console'

    @classmethod
    def setUpClass(self):
        '# set class'
        self.model = BaseModel()

    def test_doc_mod(self):
        '# check doc'
        self.assertGreater(len(base_model.__doc__), 1)

    def test_doc_class(self):
        '# check doc class'
        self.assertGreater(len(BaseModel.__doc__), 1)

    def test_creat(self):
        self.assertIsInstance(self.model, BaseModel)

    def test_prompt(self):
        '# prompt test'
        self.assertEqual("(Cmd) ", HBNBCommand.prompt)

    def test_empty_line(self):
        '# test line'
        self.assertEqual("", "")
