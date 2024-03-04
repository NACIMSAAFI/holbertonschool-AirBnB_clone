#!/usr/bin/python3
"""Unit tests for FileStorage and BaseModel"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_file_path(self):
        """Test __file_path attribute"""
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))

    def test_objects(self):
        """Test __objects attribute"""
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))

    def test_all(self):
        """Test all() method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new() method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test reload() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test __init__() method of BaseModel"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_save(self):
        """Test save() method of BaseModel"""
        obj = BaseModel()
        obj.save()
        self.assertIsNotNone(obj.updated_at)
    

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(["models/engine/file_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

if __name__ == "__main__":
    unittest.main()
