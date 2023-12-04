import pytest

import trebuchet


@pytest.fixture
def script():
    return trebuchet.Trebuchet("sample.in")


def test_sample_input_part1(script):
    raise NotImplementedError


def test_sample_input_part2(script):
    raise NotImplementedError
