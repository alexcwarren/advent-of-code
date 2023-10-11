import pytest

import doesnt_he_have_internelves_for_this


@pytest.fixture
def script():
    return doesnt_he_have_internelves_for_this.DoesntHeHaveInternelvesForThis("sample.in")


def test_sample_input_part1(script):
    expected_results = [True, True, False, False, False]
    actual_results = script.solve_part1()
    assert len(expected_results) == len(actual_results)
    for expected, actual in zip(expected_results, actual_results):
        assert expected == actual


def test_sample_input_part2(script):
    raise NotImplementedError
