
from stepik_exercise import sum_finder

def test_sum_finder():
    assert sum_finder(0) == 0
    assert sum_finder(1, 2) == 3
    assert sum_finder("1", "2") == 3
    assert sum_finder("-2", 2) == 0
