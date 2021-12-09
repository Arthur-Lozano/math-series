from math_series import __version__
from math_series import series


def test_version():
    assert __version__ == "0.1.0"


def test_ten():
    actual = series.fibonacci(10)
    expected = 55
    assert actual == expected


def test_twentytwo():
    actual = series.fibonacci(22)
    expected = 17711
    assert actual == expected


def test_negative_number():
    actual = series.fibonacci(-7)
    expected = print("Sorry wrong input")
    assert actual == expected


def test_zero():
    actual = series.fibonacci(0)
    expected = 0
    assert actual == expected


def test_one_lucas():
    actual = series.lucas(1)
    expected = 1
    assert actual == expected


def test_three_lucas():
    actual = series.lucas(3)
    expected = 4
    assert actual == expected


def test_seven_lucas():
    actual = series.lucas(7)
    expected = 29
    assert actual == expected


def test_two_sumseries():
    actual = series.sum_series(7, 0, 2)
    expected = 29
    assert actual == expected


def test_zero_sumseries():
    actual = series.sum_series(3, 0, 2)
    expected = 29
    assert actual == expected
