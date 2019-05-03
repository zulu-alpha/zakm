"""Test the functionality of the ZAKM classes."""
from dataclasses import dataclass, field
from typing import Any
import pytest
from zakm.classes import Base
from zakm import config


class TestGetAllMissingRequiredKeys:
    """Test that a missing required keys are returned."""

    @dataclass
    class DummyClass(Base):
        required_1: Any = field(metadata={"spec_mapping": "Required 1"})
        required_2: Any = field(metadata={"spec_mapping": "Required 2"})
        optional: Any = field(default=any, metadata={"spec_mapping": "Optional"})

    def test_one_missing(self):
        """Test that one missing required field is returned."""
        result = self.DummyClass.get_all_missing_required_keys(
            {"Required 1", "Optional"}
        )
        assert result == {"Required 2"}

    def test_only_optional(self):
        """Test if only all required fields are given."""
        result = self.DummyClass.get_all_missing_required_keys(
            {"Required 1", "Required 2"}
        )
        assert result == set()

    def test_all_given(self):
        """Test if all fields are correctly given."""
        result = self.DummyClass.get_all_missing_required_keys(
            {"Required 1", "Required 2", "Optional"}
        )
        assert result == set()


class TestGetAllInvalidKeys:
    """Test that all invalid required keys are returned."""

    @dataclass
    class DummyClass(Base):
        key_1: Any = field(metadata={"spec_mapping": "Key 1"})
        key_2: Any = field(default=any, metadata={"spec_mapping": "Key 2"})

    def test_one_invalid_key(self):
        """Test that the one invalid key is returned."""
        result = self.DummyClass.get_all_invalid_keys({"Key 1", "Key 2", "Invalid"})
        assert result == {"Invalid"}

    def test_no_valid_keys(self):
        """Test that invalid keys are returned even though no valid ones are given."""
        result = self.DummyClass.get_all_invalid_keys({"Invalid 1", "Invalid 2"})
        assert result == {"Invalid 1", "Invalid 2"}

    def test_all_valid(self):
        """Test that no keys are returned (as all are valid)."""
        result = self.DummyClass.get_all_invalid_keys({"Key 1", "Key 2"})
        assert result == set()


class TestGetInvalidKeyValueTypes:
    """Test that all given keys with invalid value types are returned."""

    @dataclass
    class DummyClass(Base):
        key_1: str = field(metadata={"spec_mapping": "Key str"})
        key_2: int = field(metadata={"spec_mapping": "Key int"})
        key_3: list = field(default_factory=list, metadata={"spec_mapping": "Key list"})
        key_4: dict = field(default_factory=dict, metadata={"spec_mapping": "Key dict"})

    def test_one_wrong(self):
        """Test that the one key with the wrong value type gets returned."""
        result = self.DummyClass.get_invalid_key_value_types(
            {"Key str": "wee", "Key int": 5, "Key list": -1, "Key dict": {"wee": 1}}
        )
        assert result == {"Key list": config.READABLE_YAML_PYTHON_TYPES_MAPPING[list]}

    def test_all_wrong(self):
        """Test that all the keys with the wrong value types gets returned."""
        result = self.DummyClass.get_invalid_key_value_types(
            {"Key str": 21, "Key int": "Ahh", "Key list": {"wee": 1}, "Key dict": 50}
        )
        assert result == {
            "Key str": config.READABLE_YAML_PYTHON_TYPES_MAPPING[str],
            "Key int": config.READABLE_YAML_PYTHON_TYPES_MAPPING[int],
            "Key list": config.READABLE_YAML_PYTHON_TYPES_MAPPING[list],
            "Key dict": config.READABLE_YAML_PYTHON_TYPES_MAPPING[dict],
        }

    def test_all_correct(self):
        """Test that nothing is returned if nothing is wrong."""
        result = self.DummyClass.get_invalid_key_value_types(
            {
                "Key str": "wee",
                "Key int": 3,
                "Key list": [1, 2, 3],
                "Key dict": {"ahh": [1, 2]},
            }
        )
        assert result == dict()

    def test_partial_keys(self):
        """Test that it still functions if not all of the keys are provided."""
        result = self.DummyClass.get_invalid_key_value_types(
            {"Key str": 21, "Key list": {"wee": 1}}
        )
        assert result == {
            "Key str": config.READABLE_YAML_PYTHON_TYPES_MAPPING[str],
            "Key list": config.READABLE_YAML_PYTHON_TYPES_MAPPING[list],
        }

    def test_wrong_key(self):
        """Test that a key error is raised if an invalid key is provided."""
        with pytest.raises(KeyError):
            self.DummyClass.get_invalid_key_value_types(
                {"Key str": 21, "Key wrong": {"wee": 1}}
            )


def test_test():
    # from zakm.classes import KitObject
    # var = KitObject("wee")
    pass
