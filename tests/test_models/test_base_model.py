#!/usr/bin/python3
"""
Unittest BaseModel class
"""
import unittest
import pep8
import json
import sys
from datetime import datetime
from models import base_model
from models.base_model import BaseModel


class TestPep8B(unittest.TestCase):
    """ Test pep8 style validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class BaseModelclassTests(unittest.TestCase):
    """ Test Case for base_model moudle """

    def setUp(self):
        """ Create instance global  """
        self.ins0 = BaseModel()
        self.ins1 = BaseModel()

    def test_instance(self):
        """ Test Case to check instance  """
        self.assertIsInstance(self.ins0, BaseModel)
        self.assertIsInstance(self.ins1, BaseModel)

    def test_id(self):
        """
        Test id of instances
        instance id will be not equal
        type, will be str
        """
        self.assertNotEqual(self.ins0.id, self.ins1.id)
        self.assertEqual(type(self.ins0.id), str)
        self.assertEqual(type(self.ins1.id), str)

    def test_datetime(self):
        """ Test datetime to compare format """
        cre1 = self.ins0.created_at
        up2 = self.ins0.updated_at
        self.assertEqual(type(cre1), datetime)
        self.assertEqual(type(up2), datetime)

    def test_str_rep(self):
        """   """
        pass

# Run Test
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_"name_module".py
