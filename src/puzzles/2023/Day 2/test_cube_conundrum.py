import cube_conundrum
import pytest


@pytest.fixture
def script():
    return cube_conundrum.CubeConundrum("sample.in")


def test_sample_input_part1(script):
    raise NotImplementedError


def test_sample_input_part2(script):
    raise NotImplementedError
