import pytest

import perfectly_spherical_houses_in_a_vacuum


@pytest.fixture
def script():
    return perfectly_spherical_houses_in_a_vacuum.PerfectlySphericalHousesInAVacuum("sample.in")


def test_sample_input_part1(script):
    raise NotImplementedError


def test_sample_input_part2(script):
    raise NotImplementedError
