from .db_item import DBItem
from .storage import Storage
from webserver import db
from flask import g


def get_storage():
    if 'storage' not in g:
        g.storage = Storage(db)
    return g.storage


__all__ = [
    "DBItem",
    "get_storage"
]
