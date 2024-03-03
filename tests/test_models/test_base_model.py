#!/usr/bin/python3
"""
unit tests for the BaseModel
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_save(self):
        """Test save method"""
        instance = BaseModel()
        upat = instance.updated_at
        cupat = instance.save()
        self.assertNotEqual(upat, cupat)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_id(self):
        """Test id attribute"""
        self.assertTrue(hasattr(self.model, 'id'))

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertIsInstance(self.model.created_at, datetime)

    def test_str(self):
        """Test __str__ method"""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)


if __name__ == '__main__':
    unittest.main()
