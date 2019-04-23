"""Test that configuration data is sane"""
from zakm import config


def test_kit_category_spec_db_mapping():
    """DB category names should have uppercase first letters and there should be the same
    number of categories in both the specification file and DB.
    """
    for key, value in config.SPEC_DB_MAPPING.items():
        assert value == key[0].upper() + key[1:]
    assert len(config.SPEC_DB_MAPPING) == len(config.SPEC_KIT_CATEGORIES)
