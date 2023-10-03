import pytest

import i_was_told_there_would_be_no_math


@pytest.fixture
def script():
    return i_was_told_there_would_be_no_math.IWasToldThereWouldBeNoMath("sample.in")


def test_sample_input_part1(script):
    expected_result = 58 + 43
    actual_result = script.solve_part1()
    assert expected_result == actual_result


def test_sample_input_part2(script):
    raise NotImplementedError
