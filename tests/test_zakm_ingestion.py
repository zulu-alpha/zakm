from pathlib import Path
from yaml import load, Loader


SPEC_PATH = Path(__file__).parent / "test_mission.VR" / "kit_specification.yml"


def test_import():
    with open(SPEC_PATH, "r") as open_file:
        data = load(open_file.read(), Loader=Loader)
        pass


def test_class():
    import inspect
    from dataclasses import fields, MISSING
    from zakm.classes import VisibilityCondition

    vis_cond = VisibilityCondition(name="wee")
    var2 = fields(VisibilityCondition)
    var3 = id(var2[0].default)
    var4 = vis_cond.__str__()
    pass


def test_ingest_top_level():
    pass
