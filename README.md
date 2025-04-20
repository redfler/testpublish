# Compute Service

A Python service for performing various computational tasks with comprehensive logging and error handling.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Batch processing of operations
- Comprehensive logging
- Type hints
- Error handling
- CI pipeline with GitHub Actions
- Helm chart for Kubernetes deployment

## CI/CD Pipeline

This project includes a CI/CD pipeline implemented with GitHub Actions that automatically:

1. Runs on Python 3.8, 3.9, and 3.10
2. Lints the code with flake8
3. Runs unit tests with pytest
4. Generates test coverage reports
5. Uploads coverage reports to Codecov
6. Packages and publishes Helm chart on push to main/master

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask for API service
- Kubernetes and Helm for deployment

### Installation

```bash
git clone https://github.com/yourusername/compute-service.git
cd compute-service
pip install -r requirements.txt
```

### Running the Service

```bash
# Run the compute service directly
python code/compute_service.py

# Run the API service
python code/service_api.py
```

### Running Tests

```bash
pytest tests/
```

## Kubernetes Deployment

The project includes a Helm chart for deploying to Kubernetes:

```bash
# Install the chart
helm install compute-service ./charts/compute-service

# Upgrade an existing deployment
helm upgrade compute-service ./charts/compute-service

# Uninstall
helm uninstall compute-service
```

### Helm Chart Configuration

The Helm chart can be configured through the `values.yaml` file or via command-line parameters. Key configuration options include:

- `replicaCount`: Number of pod replicas
- `image.repository`: Docker image repository
- `image.tag`: Docker image tag
- `service.type`: Kubernetes service type (ClusterIP, NodePort, LoadBalancer)
- `computeService.logLevel`: Logging level for the service

## Development

1. Create a feature branch from main
2. Make your changes
3. Write or update tests
4. Submit a pull request
5. The CI pipeline will automatically run checks against your changes
