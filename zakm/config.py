"""Global variables and configuration."""
from typing import Dict


READABLE_YAML_PYTHON_TYPES_MAPPING: dict = {
    str: "String",
    int: "Number",
    list: "Array",
    dict: "Object",
}

NAME_NAME: str = "name"
NAME_TITLE: str = "title"
NAME_DESCRIPTION: str = "description"

VISIBILITY_CONDITION_CLASS_STR: str = "Visibility Condition"
NAME_VISIBILITY_CONDITION_DEFINITIONS: str = "visibility_condition_definitions"
NAME_VISIBILITY_CONDITIONS: str = "visibility_conditions"
TERRAIN_CONDITION_CLASS_STR: str = "Terrain Condition"
NAME_TERRAIN_CONDITION_DEFINITIONS: str = "terrain_condition_definitions"
NAME_TERRAIN_CONDITIONS: str = "terrain_conditions"
NAME_TERRAIN_CONDITION_WORLDS: str = "worlds"

NAME_GROUP_TYPES: str = "group_types"
NAME_GROUP_NAMES: str = "group_names"
NAME_GROUP_CONDITION_DEFINITIONS: str = "group_condition_definitions"
NAME_GROUP_CONDITIONS: str = "group_conditions"

NAME_ROLES: str = "roles"
NAME_IN_ROLE_DESCRIPTION: str = "in_role_description"
NAME_ROLE_CONDITION_DEFINITIONS: str = "role_condition_definitions"
NAME_ROLE_CONDITIONS: str = "role_conditions"
NAME_ON_PERSON: str = "on_person"

NAME_KIT_COLLECTION_DEFINITIONS: str = "kit_collection_definitions"
NAME_KIT_COLLECTIONS: str = "kit_collections"

NAME_CRATE: str = "crate"

NAME_CRATE_CARGO: str = "crate_cargo"
NAME_UNIFORM_CARGO: str = "uniform_cargo"
NAME_VEST_CARGO: str = "vest_cargo"
NAME_BACKPACK_CARGO: str = "backpack_cargo"

NAME_KIT_OBJECT_TYPE: str = "type"
NAME_KIT_OBJECT_COUNT: str = "count"

NAME_KIT_ON_BINOCULARS: str = "on_binoculars"
NAME_KIT_ON_PRIMARY_WEAPON: str = "on_primary_weapon"
NAME_KIT_ON_SECONDARY_WEAPON: str = "on_secondary_weapon"
NAME_KIT_ON_SIDEARM: str = "on_sidearm"
NAME_KIT_PRIMARY_MUZZLE_MAGAZINES: str = "primary_muzzle_magazines"
NAME_KIT_SECONDARY_MUZZLE_MAGAZINES: str = "secondary_muzzle_magazines"

NAME_KIT_CAT_BACKPACKS: str = "backpacks"
NAME_KIT_CAT_BINOCULARS: str = "binoculars"
NAME_KIT_CAT_BIPOD_ATTACHMENTS: str = "bipod_attachments"
NAME_KIT_CAT_COMPASSES: str = "compasses"
NAME_KIT_CAT_EXPLOSIVES: str = "explosives"
NAME_KIT_CAT_GOGGLES: str = "goggles"
NAME_KIT_CAT_GRENADES: str = "grenades"
NAME_KIT_CAT_HEADGEAR: str = "headgear"
NAME_KIT_CAT_INTERFACES: str = "interfaces"
NAME_KIT_CAT_MAGAZINES: str = "magazines"
NAME_KIT_CAT_MAPS: str = "maps"
NAME_KIT_CAT_MISCELLANEOUS: str = "miscellaneous"
NAME_KIT_CAT_MUZZLE_ATTACHMENTS: str = "muzzle_attachments"
NAME_KIT_CAT_NVGS: str = "nvgs"
NAME_KIT_CAT_OPTIC_ATTACHMENTS: str = "optic_attachments"
NAME_KIT_CAT_PRIMARY_WEAPONS: str = "primary_weapons"
NAME_KIT_CAT_SECONDARY_WEAPONS: str = "secondary_weapons"
NAME_KIT_CAT_SIDE_ATTACHMENTS: str = "side_attachments"
NAME_KIT_CAT_SIDEARMS: str = "sidearms"
NAME_KIT_CAT_UNIFORMS: str = "uniforms"
NAME_KIT_CAT_VESTS: str = "vests"
NAME_KIT_CAT_WATCHES: str = "watches"

KIT_CATEGORIES: tuple = (
    NAME_KIT_CAT_BACKPACKS,
    NAME_KIT_CAT_BINOCULARS,
    NAME_KIT_CAT_BIPOD_ATTACHMENTS,
    NAME_KIT_CAT_COMPASSES,
    NAME_KIT_CAT_EXPLOSIVES,
    NAME_KIT_CAT_GOGGLES,
    NAME_KIT_CAT_GRENADES,
    NAME_KIT_CAT_HEADGEAR,
    NAME_KIT_CAT_INTERFACES,
    NAME_KIT_CAT_MAGAZINES,
    NAME_KIT_CAT_MAPS,
    NAME_KIT_CAT_MISCELLANEOUS,
    NAME_KIT_CAT_MUZZLE_ATTACHMENTS,
    NAME_KIT_CAT_NVGS,
    NAME_KIT_CAT_OPTIC_ATTACHMENTS,
    NAME_KIT_CAT_PRIMARY_WEAPONS,
    NAME_KIT_CAT_SECONDARY_WEAPONS,
    NAME_KIT_CAT_SIDE_ATTACHMENTS,
    NAME_KIT_CAT_SIDEARMS,
    NAME_KIT_CAT_UNIFORMS,
    NAME_KIT_CAT_VESTS,
    NAME_KIT_CAT_WATCHES,
)

KIT_EQUIPPABLE: tuple = (
    NAME_KIT_CAT_BACKPACKS,
    NAME_KIT_CAT_BINOCULARS,
    NAME_KIT_CAT_COMPASSES,
    NAME_KIT_CAT_GOGGLES,
    NAME_KIT_CAT_HEADGEAR,
    NAME_KIT_CAT_INTERFACES,
    NAME_KIT_CAT_MAPS,
    NAME_KIT_CAT_NVGS,
    NAME_KIT_CAT_PRIMARY_WEAPONS,
    NAME_KIT_CAT_SECONDARY_WEAPONS,
    NAME_KIT_CAT_SIDEARMS,
    NAME_KIT_CAT_UNIFORMS,
    NAME_KIT_CAT_VESTS,
    NAME_KIT_CAT_WATCHES,
)

KIT_EQUIPPABLE_WITH_EQUIPPABLE: tuple = (
    NAME_KIT_ON_BINOCULARS,
    NAME_KIT_ON_PRIMARY_WEAPON,
    NAME_KIT_ON_SECONDARY_WEAPON,
    NAME_KIT_ON_SIDEARM,
)

KIT_KIT_FOR_EQUIPPABLE_WITH_EQUIPPABLE: tuple = (
    NAME_KIT_CAT_BIPOD_ATTACHMENTS,
    NAME_KIT_CAT_MUZZLE_ATTACHMENTS,
    NAME_KIT_CAT_OPTIC_ATTACHMENTS,
    NAME_KIT_CAT_SIDE_ATTACHMENTS,
    NAME_KIT_PRIMARY_MUZZLE_MAGAZINES,
    NAME_KIT_SECONDARY_MUZZLE_MAGAZINES,
)

KIT_MUZZLES: tuple = (
    NAME_KIT_PRIMARY_MUZZLE_MAGAZINES,
    NAME_KIT_SECONDARY_MUZZLE_MAGAZINES,
)

KIT_MUZZLE_KIT: tuple = tuple(NAME_KIT_CAT_MAGAZINES)

KIT_CARGO_CONTAINERS: tuple = (
    NAME_CRATE_CARGO,
    NAME_UNIFORM_CARGO,
    NAME_VEST_CARGO,
    NAME_BACKPACK_CARGO,
)

DB_NAME_DESCRIPTION: str = "description"
DB_NAME_DISPLAY_NAME: str = "display_name"

# https://json-schema.org/learn/getting-started-step-by-step.html
_schema_kit_rows = {
    "^.*$": {
        "type": "object",
        "properties": {
            DB_NAME_DESCRIPTION: {"type": "string"},
            DB_NAME_DISPLAY_NAME: {"type": "string"},
        },
        "required": [DB_NAME_DESCRIPTION, DB_NAME_DISPLAY_NAME],
    }
}
DB_SCHEMA = {
    "type": "object",
    "properties": {
        i: {"type": "object", "patternProperties": _schema_kit_rows}
        for i in KIT_CATEGORIES
    },
    "required": list(KIT_CATEGORIES),
}

DB_TYPE = Dict[str, Dict[str, Dict[str, str]]]


# TOP_KEYS: tuple = (
#     NAME_VISIBILITY_CONDITION_DEFINITIONS,
#     NAME_TERRAIN_CONDITION_DEFINITIONS,
#     NAME_KIT_COLLECTION_DEFINITIONS,
#     NAME_CRATE_CARGO,
#     NAME_GROUP_TYPES
# )

# GROUP_KEYS: tuple = (
#     NAME_TITLE,
#     NAME_DESCRIPTION,
#     NAME_GROUP_NAMES,
#     NAME_GROUP_CONDITION_DEFINITIONS,
#     NAME_KIT_COLLECTION_DEFINITIONS,
#     NAME_ROLES
# )

# ROLE_KEYS: tuple = (
#     NAME_TITLE,
#     NAME_DESCRIPTION,
#     NAME_IN_ROLE_DESCRIPTION,
#     NAME_ROLE_CONDITION_DEFINITIONS,
#     NAME_ON_PERSON,
#     NAME_CRATE_CARGO
# )

# COMMON_CONDITION_DEFINITION_KEYS: tuple = (
#     NAME_NAME
# )

# TERRAIN_CONDITION_DEFINITION_KEYS: tuple = (
#     NAME_NAME,
#     NAME_TERRAIN_CONDITION_WORLDS
# )

# KIT_OBJECT_KEYS: tuple = (
#     NAME_KIT_OBJECT_TYPE,
#     NAME_KIT_OBJECT_COUNT
# )

# KIT_OBJECT_EQUIPPABLE_KEYS: tuple = (
#     NAME_KIT_OBJECT_TYPE
# )

# CRATE_CARGO_KEYS: tuple = (
#     NAME_CRATE,
#     NAME_KIT_COLLECTIONS,
#     *KIT_CATEGORIES
# )
# UNIFORM_CARGO_KEYS: str = (
#     NAME_KIT_COLLECTIONS,
#     *KIT_CATEGORIES
# )
# VEST_CARGO_KEYS = UNIFORM_CARGO_KEYS
# BACKPACK_CARGO_KEYS = UNIFORM_CARGO_KEYS

# KIT_COLLECTION_KEYS: tuple = (
#     NAME_NAME,
#     NAME_KIT_COLLECTIONS,
#     *KIT_CATEGORIES
# )
