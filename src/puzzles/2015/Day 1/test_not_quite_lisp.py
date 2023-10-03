import pytest

import not_quite_lisp


@pytest.fixture
def script():
    return not_quite_lisp.NotQuiteLisp("sample.in")


def test_sample_input_part1(script):
    assert script.solve_part1() == 0


def test_sample_input_part2(script):
    raise NotImplementedError
