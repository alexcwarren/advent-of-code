import pytest

import trebuchet


@pytest.fixture
def script():
    return trebuchet.Trebuchet("sample.in")


def test_sample_input_part1(script):
    assert script.solve_part1() == 142


def test_sample_input_part2(script):
    assert script.solve_part2() == 281
