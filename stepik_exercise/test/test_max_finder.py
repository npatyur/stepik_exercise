
from stepik_exercise import max_finder

def test_max_finder():
    assert max_finder(1) == 1
    assert max_finder(1, 2, 3) == 3
    assert max_finder("1", 2, "10") == 10
