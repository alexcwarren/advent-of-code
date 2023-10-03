import pytest

import not_quite_lisp


@pytest.fixture
def script():
    return not_quite_lisp.NotQuiteLisp("sample.in")


def test_sample_input_part1(script):
    expected_results = [0, 0, 3, 3, 3, -1, -1, -3, -3]
    actual_results = script.solve_part1()
    assert len(expected_results) == len(actual_results)

    for expected, actual in zip(actual_results, expected_results):
        assert expected == actual


def test_sample_input_part2(script):
    raise NotImplementedError
