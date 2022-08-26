from main import compare_numbers, draw


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


def test_draw_numbers():
    numbers = range(1, 50)
    for _ in range(501):
        drawn_numbers = draw(numbers)
        assert min(drawn_numbers) >= 1
        assert max(drawn_numbers) <= 49
        assert len(draw(numbers)) == 6
