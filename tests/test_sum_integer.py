import pytest

from main import sum_integers
from first_task import sum_numbers


@pytest.mark.parametrize("a, b, result", [(10, 2, 12),
                                          (11, 16, 27),
                                          (0, 0, 0)])
def test_func_sum_integer(a, b, result):
    assert sum_integers(a, b) == result


@pytest.mark.parametrize("a, result", [(10, 1),
                                       (99, 18),
                                       (541, 10),
                                       (5, 5)])
def test_func_sum_numbers(a, result):
    assert sum_numbers(a) == result
