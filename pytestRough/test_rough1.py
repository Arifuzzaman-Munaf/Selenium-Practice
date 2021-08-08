import pytest


def test_total_division_5(input_total):
    assert input_total % 5 == 0


def test_total_division_10(input_total):
    assert input_total % 10 == 0


def test_total_division_11(input_total):
    assert input_total % 11 == 0