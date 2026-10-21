
# Module 8 - FastAPI Calculator

## Project Overview

This project is a web-based calculator built using Python and FastAPI for NJIT IS601 Module 8.

The application allows users to perform four basic arithmetic operations through a browser interface and REST API.

The project includes automated unit tests, integration tests, end-to-end tests using Playwright, application logging, and continuous integration using GitHub Actions.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero error handling
- Input validation
- Web-based calculator interface
- REST API endpoints
- Application logging
- Automated testing
- GitHub Actions CI workflow

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- Jinja2
- Pytest
- Playwright
- pytest-cov
- Git and GitHub
- GitHub Actions

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/islamnavid/module8_is601.git
cd module8_is601
```

### 2. Create a Virtual Environment

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install Playwright Browser

```bash
python -m playwright install chromium
```

## Running the Application

Start the FastAPI development server:

```bash
python -m uvicorn main:app --reload
```

Open the calculator in your browser:

http://127.0.0.1:8000

FastAPI automatically generates interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Display calculator interface |
| POST | /add | Add two numbers |
| POST | /subtract | Subtract two numbers |
| POST | /multiply | Multiply two numbers |
| POST | /divide | Divide two numbers |

### Example API Request

POST /add

```json
{
  "a": 10,
  "b": 5
}
```

Expected response:

```json
{
  "result": 15
}
```

### Division by Zero

POST /divide

```json
{
  "a": 10,
  "b": 0
}
```

The application returns HTTP 400 with an error response:

```json
{
  "error": "Cannot divide by zero!"
}
```

## Automated Testing

The application uses three levels of automated testing.

### Unit Tests

Unit tests verify the arithmetic functions independently.

They cover:

- Positive and negative numbers
- Integer and decimal calculations
- Zero values
- Large numbers
- Decimal precision
- Division by zero

Total: 39 unit tests.

Run:

```bash
python -m pytest tests/unit -v
```

### Integration Tests

Integration tests verify FastAPI endpoints and their responses.

They cover:

- Successful arithmetic requests
- Negative and decimal inputs
- Missing request fields
- Invalid input types
- Null values
- Division-by-zero errors
- Homepage availability
- OpenAPI documentation

Total: 25 integration tests.

Run:

```bash
python -m pytest tests/integration -v
```

### End-to-End Tests

Playwright tests simulate real browser interactions.

They cover:

- Loading the homepage
- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero errors
- Negative numbers
- Decimal numbers
- Multiple consecutive calculations

Total: 9 end-to-end tests.

Run:

```bash
python -m pytest tests/e2e -v --no-cov
```

### Run All Tests

```bash
python -m pytest -v
```

Latest verified local result:

```text
73 passed
```

The arithmetic operations module achieved 100% statement coverage.

Coverage is generated using pytest-cov and can be viewed in the `htmlcov` directory after running tests.

## Application Logging

Python's logging module records important application events.

The application logs:

- Homepage access
- Successful arithmetic operations
- Validation errors
- Division-by-zero errors
- Other operation errors

Logging helps developers monitor application behavior and troubleshoot problems.

## Continuous Integration

GitHub Actions automatically executes tests whenever changes are pushed to the main branch or a pull request targets main.

The workflow is defined in:

`.github/workflows/test.yml`

The workflow:

1. Checks out the repository.
2. Configures Python 3.12.
3. Installs project dependencies.
4. Installs Playwright Chromium and its dependencies.
5. Runs unit and integration tests.
6. Runs Playwright end-to-end tests.
7. Uploads the HTML coverage report as an artifact.

The latest verified GitHub Actions workflow completed successfully.

View workflow results:

https://github.com/islamnavid/module8_is601/actions

## Project Structure

```text
module8_is601/
├── .github/
│   └── workflows/
│       └── test.yml
├── app/
│   └── operations/
│       └── __init__.py
├── templates/
│   └── index.html
├── tests/
│   ├── unit/
│   │   └── test_calculator.py
│   ├── integration/
│   │   └── test_fastapi_calculator.py
│   └── e2e/
│       └── test_e2e.py
├── main.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Development Process

The project was developed and tested incrementally using Git commits.

Major improvements included:

1. Configuring and running the FastAPI application.
2. Enhancing application logging.
3. Configuring GitHub Actions.
4. Expanding arithmetic unit tests.
5. Adding API validation and edge-case integration tests.
6. Expanding Playwright browser tests.
7. Verifying all 73 tests locally and through CI.

## Author

Navid Islam

NJIT - IS601 Python Programming

GitHub: https://github.com/islamnavid
