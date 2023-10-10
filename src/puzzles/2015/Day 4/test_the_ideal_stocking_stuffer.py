import pytest

import the_ideal_stocking_stuffer


@pytest.fixture
def script():
    return the_ideal_stocking_stuffer.TheIdealStockingStuffer("sample.in")


def test_sample_input_part1(script):
    raise NotImplementedError


def test_sample_input_part2(script):
    raise NotImplementedError
