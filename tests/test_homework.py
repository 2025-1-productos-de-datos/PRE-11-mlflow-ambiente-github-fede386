import os


def test_01():
    assert os.path.exists("MLproject"), "El archivo MLproject no existe."
