#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
import json
import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.db_storage import DBStorage
import os
import sys
import MySQLdb


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'file')
class TestDBStorage(unittest.TestCase):
    """TestDBStorage resume
    Args:
        unittest (): Propertys for unit testing
    """
    def setUp(self):
        """ Set up test environment """
        db_user = "hbnb_test"
        db_password = "hbnb_test_pwd"
        db_name = "hbnb_test_db"
        # Open database connection

    maxDiff = None

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/db_storage.py'
        file2 = 'tests/test_models/test_engine/test_db_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_executable_file(self):
        """ Check if file have permissions to execute"""
        # Check for read access
        is_read_true = os.access('models/engine/db_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/engine/db_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/engine/db_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)

    # def test_sql_creation(self):
    #    """ checks if sql can create a new row """
    #    initial_value = ("""SELECT count(*) FROM City""")
    #    initial_value = cursor.execute(initial_value)
    #    self.assertTrue(type(initial_value) is str)
