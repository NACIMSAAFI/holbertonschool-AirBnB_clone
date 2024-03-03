#!/usr/bin/python3
"""
testing the base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_ing_init(self):
        """
        Test for __init__
        """
        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)

    def test_ing_save(self):
        """
        Test for save
        """
        instance = BaseModel()
        upat = instance.updated_at
        cupat = instance.save()
        self.assertNotEqual(upat, cupat)

    def test_ing_to_dict(self):
        """
        Test for to_dict
        """
        instance = BaseModel()
        mdict = instance.to_dict()
        self.assertIsInstance(mdict, dict)
        self.assertEqual(mdict["__class__"], 'BaseModel')
        self.assertEqual(mdict['id'], instance.id)
        self.assertEqual(mdict['created_at'], instance.created_at.isoformat())
        self.assertEqual(mdict["updated_at"], instance.updated_at.isoformat())

    def test_ing_str(self):
        """
        Test for string representation
        """
        instance = BaseModel()
        self.assertTrue(str(instance).startswith('[BaseModel]'))
        self.assertIn(instance.id, str(instance))
        self.assertIn(str(instance.__dict__), str(instance))


if __name__ == "__main__":
    unitt
