#!/usr/bin/python3
"""This module instantiates an object of class DBStorage or FileStorage"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


# Determine storage type based on the environment variable
storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Load data from the storage (FileStorage or DBStorage)
storage.reload()
