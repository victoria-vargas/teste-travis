import pytest
from testetravis import somar
from testetravis import subtrair


def test_somar():
    assert somar(2, 4) == 6


def test_subtrair():
    assert subtrair(4, 2) == 2
