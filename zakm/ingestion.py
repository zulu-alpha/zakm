"""Functions to load data."""
import json
from pathlib import Path
from jsonschema import validate
from zakm import config


def load_db(path: Path) -> dict:
    """Load and validate the DB file from the given path."""
    with open(path, "r") as open_file:
        db = json.load(open_file)
    validate(instance=db, schema=config.DB_SCHEMA)
    return db
