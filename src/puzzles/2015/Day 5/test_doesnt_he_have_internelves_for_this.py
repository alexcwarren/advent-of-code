import pytest

import doesnt_he_have_internelves_for_this


@pytest.fixture
def script():
    return doesnt_he_have_internelves_for_this.DoesntHeHaveInternelvesForThis("sample.in")


def test_sample_input_part1(script):
    assert script.solve_part1() == 2


def test_sample_input_part2(script):
    assert script.solve_part2() == 2
