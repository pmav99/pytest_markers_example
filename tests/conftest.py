# content of conftest.py

import pytest


SKIP_SCHISM = pytest.mark.skip(reason="need --runshism option to run")
SKIP_DELFT = pytest.mark.skip(reason="need --rundelft option to run")


def pytest_addoption(parser):
    parser.addoption(
        "--runschism", action="store_true", default=False, help="run schism tests"
    )
    parser.addoption(
        "--rundelft", action="store_true", default=False, help="run delft tests"
    )


def pytest_collection_modifyitems(config, items):
    should_run_schism = config.getoption("--runschism")
    should_run_delft = config.getoption("--rundelft")

    for item in items:
        if "schism" in item.keywords and not should_run_schism:
            item.add_marker(SKIP_SCHISM)
        if "delft" in item.keywords and not should_run_delft:
            item.add_marker(SKIP_DELFT)
