import json
import re
from functools import wraps
import inspect
import logging
from base_module import type_db
from sqlalchemy import create_engine
from logging_module import logging_module


def get_db_schema(type_db, connection):
    """Get schema db"""

    #schema =

    return


def parse_connection(type, connection):
    """Get format connection string"""
    frame = inspect.currentframe()
    logging.info(f"Module {inspect.getframeinfo(frame).function} with params {type}, {connection}")
    try:
        driver = type_db.dict_db_conn.get(type)
    except TypeError as err:
        return err

    username = connection
    return f"{driver}://"
