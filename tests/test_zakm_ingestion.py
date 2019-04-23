from pathlib import Path
from yaml import load


SPEC_PATH = Path(__file__).parent.parent / "zakm" / "kit_specification.yml"


def test_test():
    with open(SPEC_PATH, "r") as open_file:
        data = load(open_file.read())
        pass


def test_ingest_top_level():
    pass
