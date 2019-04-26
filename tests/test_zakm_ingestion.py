from pathlib import Path

# from yaml import load, Loader


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


def test_ingest_top_level():
    pass
