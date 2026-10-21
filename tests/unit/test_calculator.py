
# tests/unit/test_calculator.py

"""
Unit tests for the FastAPI Calculator arithmetic operations.

Tests cover positive and negative numbers, decimals, zeros,
large numbers, and division by zero.
"""

import pytest

from app.operations import add, subtract, multiply, divide


# Addition tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(2, 3, 5, id="add_two_positive_integers"),
        pytest.param(-2, -3, -5, id="add_two_negative_integers"),
        pytest.param(2.5, 3.5, 6.0, id="add_two_positive_floats"),
        pytest.param(-2.5, 3.5, 1.0, id="add_negative_and_positive_float"),
        pytest.param(0, 0, 0, id="add_zeros"),
        pytest.param(0, 12, 12, id="add_zero_and_positive"),
        pytest.param(-10, 10, 0, id="add_opposite_numbers"),
        pytest.param(0.1, 0.2, 0.3, id="add_decimal_precision"),
        pytest.param(1000000, 2000000, 3000000, id="add_large_numbers"),
    ],
)
def test_add(a, b, expected):
    result = add(a, b)
    assert result == pytest.approx(expected)


# Subtraction tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(5, 3, 2, id="subtract_two_positive_integers"),
        pytest.param(-5, -3, -2, id="subtract_two_negative_integers"),
        pytest.param(5.5, 2.5, 3.0, id="subtract_two_positive_floats"),
        pytest.param(-5.5, -2.5, -3.0, id="subtract_two_negative_floats"),
        pytest.param(0, 0, 0, id="subtract_zeros"),
        pytest.param(5, -3, 8, id="subtract_negative_number"),
        pytest.param(0, 8, -8, id="subtract_from_zero"),
        pytest.param(3, 10, -7, id="subtract_larger_number"),
        pytest.param(0.3, 0.1, 0.2, id="subtract_decimal_precision"),
    ],
)
def test_subtract(a, b, expected):
    result = subtract(a, b)
    assert result == pytest.approx(expected)


# Multiplication tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(2, 3, 6, id="multiply_two_positive_integers"),
        pytest.param(-2, 3, -6, id="multiply_negative_and_positive_integer"),
        pytest.param(2.5, 4.0, 10.0, id="multiply_two_positive_floats"),
        pytest.param(-2.5, 4.0, -10.0, id="multiply_negative_float_and_positive_float"),
        pytest.param(0, 5, 0, id="multiply_zero_and_positive_integer"),
        pytest.param(-4, -5, 20, id="multiply_two_negative_numbers"),
        pytest.param(8, 0, 0, id="multiply_by_zero"),
        pytest.param(0.5, 0.2, 0.1, id="multiply_decimal_precision"),
        pytest.param(1000, 1000, 1000000, id="multiply_large_numbers"),
    ],
)
def test_multiply(a, b, expected):
    result = multiply(a, b)
    assert result == pytest.approx(expected)


# Division tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(6, 3, 2.0, id="divide_two_positive_integers"),
        pytest.param(-6, 3, -2.0, id="divide_negative_integer_by_positive_integer"),
        pytest.param(6.0, 3.0, 2.0, id="divide_two_positive_floats"),
        pytest.param(-6.0, 3.0, -2.0, id="divide_negative_float_by_positive_float"),
        pytest.param(0, 5, 0.0, id="divide_zero_by_positive_integer"),
        pytest.param(10, -2, -5.0, id="divide_by_negative_number"),
        pytest.param(-10, -2, 5.0, id="divide_two_negative_numbers"),
        pytest.param(5, 2, 2.5, id="divide_fractional_result"),
        pytest.param(1, 3, 1 / 3, id="divide_repeating_decimal"),
    ],
)
def test_divide(a, b, expected):
    result = divide(a, b)
    assert result == pytest.approx(expected)


# Division by zero tests
@pytest.mark.parametrize(
    "a",
    [
        pytest.param(6, id="positive_dividend"),
        pytest.param(-6, id="negative_dividend"),
        pytest.param(0, id="zero_dividend"),
    ],
)
def test_divide_by_zero(a):
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(a, 0)
