import pytest

import perfectly_spherical_houses_in_a_vacuum


@pytest.fixture
def script():
    return perfectly_spherical_houses_in_a_vacuum.PerfectlySphericalHousesInAVacuum("sample.in")


def test_sample_input_part1(script):
    expected_results = [2, 4, 2]
    actual_results = script.solve_part1()
    assert len(expected_results) == len(actual_results)
    for expected, actual in zip(expected_results, actual_results):
        assert expected == actual


def test_sample_input_part2(script):
    expected_results = [3, 3, 11]
    actual_results = script.solve_part2()
    assert len(expected_results) == len(actual_results)
    for expected, actual in zip(expected_results, actual_results):
        assert expected == actual
