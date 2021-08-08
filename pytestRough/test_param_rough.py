import pytest


@pytest.mark.parametrize("num, result", [(1, 11), (2, 22), (3, 33)])
def test_calculation(num,result):
    """
    this method uses the concept of parameterization
    :param num:
    :param result:
    :return:
    """
    assert 11*num == result
