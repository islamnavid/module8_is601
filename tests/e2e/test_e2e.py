
# tests/e2e/test_e2e.py

"""
End-to-end tests for the FastAPI Calculator using Playwright.

These tests simulate real browser interactions with the calculator.
"""

import pytest
from playwright.sync_api import expect


BASE_URL = "http://localhost:8000"


def enter_numbers(page, a, b):
    """Enter two numbers into the calculator."""
    page.locator("#a").fill(str(a))
    page.locator("#b").fill(str(b))


def perform_calculation(page, a, b, operation):
    """Enter numbers and click the requested operation button."""
    page.goto(BASE_URL)
    enter_numbers(page, a, b)
    page.get_by_role("button", name=operation, exact=True).click()


@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """Verify that the calculator homepage loads."""
    page.goto(BASE_URL)

    expect(page.locator("h1")).to_have_text("Hello World")
    expect(page.get_by_role("button", name="Add")).to_be_visible()
    expect(page.get_by_role("button", name="Subtract")).to_be_visible()
    expect(page.get_by_role("button", name="Multiply")).to_be_visible()
    expect(page.get_by_role("button", name="Divide")).to_be_visible()


@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """Verify addition through the browser."""
    perform_calculation(page, 10, 5, "Add")

    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 15"
    )


@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    """Verify subtraction through the browser."""
    perform_calculation(page, 10, 5, "Subtract")

    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 5"
    )


@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    """Verify multiplication through the browser."""
    perform_calculation(page, 10, 5, "Multiply")

    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 50"
    )


@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    """Verify division through the browser."""
    perform_calculation(page, 10, 2, "Divide")

    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 5"
    )


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """Verify that division by zero displays an error."""
    perform_calculation(page, 10, 0, "Divide")

    expect(page.locator("#result")).to_have_text(
        "Error: Cannot divide by zero!"
    )


@pytest.mark.e2e
def test_calculator_negative_numbers(page, fastapi_server):
    """Verify calculations involving negative numbers."""
    perform_calculation(page, -5, 3, "Add")

    expect(page.locator("#result")).to_have_text(
        "Calculation Result: -2"
    )


@pytest.mark.e2e
def test_calculator_decimal_numbers(page, fastapi_server):
    """Verify multiplication involving decimal values."""
    perform_calculation(page, 2.5, 4, "Multiply")

    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 10"
    )


@pytest.mark.e2e
def test_multiple_calculations(page, fastapi_server):
    """Verify that a user can perform different operations consecutively."""
    page.goto(BASE_URL)
    enter_numbers(page, 12, 4)

    page.get_by_role("button", name="Add", exact=True).click()
    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 16"
    )

    page.get_by_role("button", name="Subtract", exact=True).click()
    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 8"
    )

    page.get_by_role("button", name="Multiply", exact=True).click()
    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 48"
    )

    page.get_by_role("button", name="Divide", exact=True).click()
    expect(page.locator("#result")).to_have_text(
        "Calculation Result: 3"
    )
