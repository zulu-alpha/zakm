"""Test the functionality of the ingestion functions."""
from pathlib import Path
import jsonschema
import pytest
from zakm import config


SPEC_PATH = Path(__file__).parent / "test_mission.VR" / "kit_specification.yml"


def test_import():
    #     with open(SPEC_PATH, "r") as open_file:
    #         data = load(open_file.read(), Loader=Loader)
    pass


def test_class():
    # from dataclasses import fields
    # from zakm.classes import VisibilityCondition

    # var = fields(VisibilityCondition)
    pass


class TestLoadDB:
    """Test that the load_db function correctly loads and validates DBs"""

    from zakm.ingestion import load_db

    def test_good_load(self):
        """Test that it loads correctly and raises no validation errors"""
        simple_db_path = Path(__file__).parent / "test_dbs" / "simple_db.json"
        try:
            db = type(self).load_db(simple_db_path)
        except jsonschema.exceptions.ValidationError:
            pytest.fail("Unexpected exception jsonschema.exceptions.ValidationError")

        assert config.NAME_KIT_CAT_NVGS in db
        assert "CUP_NVG_PVS14" in db[config.NAME_KIT_CAT_NVGS]
        assert "description" in db[config.NAME_KIT_CAT_NVGS]["CUP_NVG_PVS14"]

    def test_bad_load(self):
        """Test that a validation error is raised if a bad DB is loaded."""
        faulty_db_path = Path(__file__).parent / "test_dbs" / "faulty_db.json"
        with pytest.raises(jsonschema.exceptions.ValidationError):
            type(self).load_db(faulty_db_path)
