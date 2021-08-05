import pytest

def test_always_passes():
    assert True


@pytest.mark.login
def test_always_fails():
    assert False