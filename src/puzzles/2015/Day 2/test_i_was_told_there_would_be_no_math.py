import pytest

import i_was_told_there_would_be_no_math


@pytest.fixture
def script():
    return i_was_told_there_would_be_no_math.IWasToldThereWouldBeNoMath("sample.in")


def test_sample_input_part1(script):
    expected_results = [58, 43]
    actual_results = script.solve_part1()
    assert len(expected_results) == len(actual_results)

    for expected, actual in zip(expected_results, actual_results):
        assert expected == actual


def test_sample_input_part2(script):
    raise NotImplementedError
