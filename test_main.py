from main import compare_numbers


def test_compare_numbers():
    set1 = {1, 2, 3, 4}
    set2 = {1, 2, 3, 4}
    assert compare_numbers(set1, set2)


def test_compare_numbers_order():
    set1 = {1, 3, 2, 5}
    set2 = {5, 2, 3, 1}
    assert compare_numbers(set1, set2)


def test_compare_numbers_len():
    set1 = {1, 2, 3, 4}
    set2 = {1, 2}
    assert compare_numbers(set1, set2) is False


