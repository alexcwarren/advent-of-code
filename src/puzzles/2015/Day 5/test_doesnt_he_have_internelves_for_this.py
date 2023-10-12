import pytest

import doesnt_he_have_internelves_for_this


@pytest.fixture
def script():
    return doesnt_he_have_internelves_for_this.DoesntHeHaveInternelvesForThis(
        "sample.in"
    )


@pytest.mark.one
def test_sample_input_part1(script):
    assert script.solve_part1() == 2


@pytest.mark.two
def test_has_repeating_pairs(script):
    assert script.has_repeating_pairs("xyxy") == True
    assert script.has_repeating_pairs("aabcdefgaa") == True
    assert script.has_repeating_pairs("aaa") == False
    assert script.has_repeating_pairs("qjhvhtzxzqqjkmpb") == True
    assert script.has_repeating_pairs("xxyxx") == True
    assert script.has_repeating_pairs("uurcxstgmygtbstg") == True
    assert script.has_repeating_pairs("ieodomkazucvgmuy") == False


@pytest.mark.two
def test_has_bisected_pair(script):
    assert script.has_bisected_pair("abcdefg") == False
    assert script.has_bisected_pair("abccba") == False
    assert script.has_bisected_pair("xyx") == True
    assert script.has_bisected_pair("abcdefeghi") == True
    assert script.has_bisected_pair("aaa") == True
    assert script.has_bisected_pair("qjhvhtzxzqqjkmpb") == True
    assert script.has_bisected_pair("xxyxx") == True
    assert script.has_bisected_pair("uurcxstgmygtbstg") == False
    assert script.has_bisected_pair("ieodomkazucvgmuy") == True


@pytest.mark.two
def test_sample_input_part2(script):
    assert script.solve_part2() == 2
