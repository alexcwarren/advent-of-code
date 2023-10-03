import pytest

import i_was_told_there_would_be_no_math


@pytest.fixture
def script():
    return i_was_told_there_would_be_no_math.IWasToldThereWouldBeNoMath("sample.in")


def test_sample_input_part1(script):
    pass


def test_sample_input_part2(script):
    pass
