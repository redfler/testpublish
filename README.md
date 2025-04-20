# Compute Service

A Python service for performing various computational tasks with comprehensive logging and error handling.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Batch processing of operations
- Comprehensive logging
- Type hints
- Error handling
- CI pipeline with GitHub Actions

## CI/CD Pipeline

This project includes a CI/CD pipeline implemented with GitHub Actions that automatically:

1. Runs on Python 3.8, 3.9, and 3.10
2. Lints the code with flake8
3. Runs unit tests with pytest
4. Generates test coverage reports
5. Uploads coverage reports to Codecov

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

```bash
git clone https://github.com/yourusername/compute-service.git
cd compute-service
pip install -r requirements.txt
```

### Running the Service

```bash
python code/compute_service.py
```

### Running Tests

```bash
pytest tests/
```

## Development

1. Create a feature branch from main
2. Make your changes
3. Write or update tests
4. Submit a pull request
5. The CI pipeline will automatically run checks against your changes
