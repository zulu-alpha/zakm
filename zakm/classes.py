from dataclasses import dataclass, field
from typing import List


@dataclass
class VisibilityCondition:
    pass


@dataclass
class TerrainCondition:
    name: str


@dataclass
class Specification:
    visibility_conditions: List[VisibilityCondition] = field(default_factory=list)
    terrain_conditions: List[TerrainCondition] = field(default_factory=list)
    kit_collection_definitions:
    crate_cargo
    group_types
