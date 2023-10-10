import pytest

import the_ideal_stocking_stuffer


@pytest.fixture
def script():
    return the_ideal_stocking_stuffer.TheIdealStockingStuffer("sample.in")


def test_sample_input_part1(script):
    expected_results = [609043, 1048970]
    actual_results = script.solve_part1()
    assert len(expected_results) == len(actual_results)
    for expected, actual in zip(expected_results, actual_results):
        assert expected == actual


def test_sample_input_part2(script):
    # No sample test data available
    pass
