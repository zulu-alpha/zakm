from dataclasses import dataclass, field, fields, MISSING
from typing import List, ClassVar, Dict, Set, Union
from zakm import config


TYPE_OBJECT_VALUE = Union[str, int, list, dict]
TYPE_OBJECT = Dict[str, TYPE_OBJECT_VALUE]


class Base:
    @classmethod
    def get_all_missing_required_keys(cls, keys: Set[str]) -> Set[str]:
        """Return all the required spec file keys not present in the given set."""
        required = set(
            [
                _field.metadata["spec_mapping"]  # type: ignore
                for _field in fields(cls)
                if _field.default is MISSING
            ]
        )
        return required.difference(keys)

    @classmethod
    def get_all_invalid_keys(cls, keys: Set[str]) -> Set[str]:
        """Return all the given spec file keys that are not valid."""
        valid = set(
            [_field.metadata["spec_mapping"] for _field in fields(cls)]  # type: ignore
        )
        return keys.difference(valid)

    @classmethod
    def get_invalid_key_value_types(cls, key_values: TYPE_OBJECT) -> Dict[str, str]:
        """Return a mapping of keys with incorrect value types and their expected value
        types in human readable form.
        """
        correct_key_types = {
            _field.metadata["spec_mapping"]: _field.type  # type: ignore
            for _field in fields(cls)
        }
        return {
            key: config.READABLE_YAML_PYTHON_TYPES_MAPPING[correct_key_types[key]]
            for key, value in key_values.items()
            if not isinstance(value, correct_key_types[key])
        }


@dataclass
class VisibilityCondition(Base):
    __class_str__: ClassVar[str] = config.NAME_VISIBILITY_CONDITION_CLASS_STR
    name: str = field(metadata={"spec_mapping": config.NAME_NAME})

    def __str__(self) -> str:
        return f"{self.name} {config.NAME_VISIBILITY_CONDITION_CLASS_STR}"


@dataclass
class TerrainCondition(Base):
    name: str
    pass


@dataclass
class Specification(Base):
    visibility_conditions: List[VisibilityCondition] = field(default_factory=list)
    terrain_conditions: List[TerrainCondition] = field(default_factory=list)
    pass
