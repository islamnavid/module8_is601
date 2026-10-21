
# tests/integration/test_fastapi_calculator.py

"""
Integration tests for the FastAPI Calculator.

These tests verify arithmetic endpoints, request validation,
HTTP status codes, and error responses.
"""

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    with TestClient(app) as test_client:
        yield test_client


# Original arithmetic endpoint tests

def test_add_api(client):
    response = client.post("/add", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_subtract_api(client):
    response = client.post("/subtract", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_multiply_api(client):
    response = client.post("/multiply", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 50


def test_divide_api(client):
    response = client.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_divide_by_zero_api(client):
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json()["error"] == "Cannot divide by zero!"


# Additional arithmetic scenarios

@pytest.mark.parametrize(
    "endpoint, a, b, expected",
    [
        pytest.param("/add", -5, 3, -2, id="add_negative_number"),
        pytest.param("/add", 0.1, 0.2, 0.3, id="add_decimals"),
        pytest.param("/subtract", 5, -3, 8, id="subtract_negative"),
        pytest.param("/subtract", 0, 10, -10, id="subtract_from_zero"),
        pytest.param("/multiply", -4, -5, 20, id="multiply_negatives"),
        pytest.param("/multiply", 0, 100, 0, id="multiply_by_zero"),
        pytest.param("/divide", 10, -2, -5, id="divide_negative"),
        pytest.param("/divide", 5, 2, 2.5, id="divide_fractional"),
    ],
)
def test_api_additional_operations(client, endpoint, a, b, expected):
    response = client.post(endpoint, json={"a": a, "b": b})

    assert response.status_code == 200
    assert response.json()["result"] == pytest.approx(expected)


# Invalid and missing input tests

@pytest.mark.parametrize(
    "endpoint",
    ["/add", "/subtract", "/multiply", "/divide"],
)
def test_api_missing_second_number(client, endpoint):
    response = client.post(endpoint, json={"a": 10})

    assert response.status_code == 400
    assert "error" in response.json()
    assert "b" in response.json()["error"]


@pytest.mark.parametrize(
    "endpoint",
    ["/add", "/subtract", "/multiply", "/divide"],
)
def test_api_invalid_number(client, endpoint):
    response = client.post(
        endpoint,
        json={"a": "not-a-number", "b": 5},
    )

    assert response.status_code == 400
    assert "error" in response.json()


def test_api_missing_both_numbers(client):
    response = client.post("/add", json={})

    assert response.status_code == 400
    assert "error" in response.json()


def test_api_null_number(client):
    response = client.post("/multiply", json={"a": None, "b": 5})

    assert response.status_code == 400
    assert "error" in response.json()


# Homepage and API documentation tests

def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Hello World" in response.text
    assert "Calculator" in response.text


def test_openapi_documentation(client):
    response = client.get("/openapi.json")

    assert response.status_code == 200

    paths = response.json()["paths"]

    for endpoint in ["/add", "/subtract", "/multiply", "/divide"]:
        assert endpoint in paths
        assert "post" in paths[endpoint]
