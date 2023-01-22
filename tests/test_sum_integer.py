import pytest

from main import sum_integers


@pytest.mark.parametrize("a, b, result", [(10, 2, 12),
                                          (11, 16, 27),
                                          (0, 0, 0)])
def test_func_sum_integer(a, b, result):
    assert sum_integers(a, b) == result


