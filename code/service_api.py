"""
REST API for the Compute Service.
This module provides HTTP endpoints for interacting with the ComputeService.
"""
import os
import json
import logging
from flask import Flask, request, jsonify
from code.compute_service import ComputeService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the Flask app
app = Flask(__name__)

# Get configuration from environment variables
LOG_LEVEL = os.environ.get('COMPUTE_SERVICE_LOG_LEVEL', 'INFO')
ENABLE_BATCH_PROCESSING = os.environ.get('COMPUTE_SERVICE_ENABLE_BATCH_PROCESSING', 'True').lower() == 'true'
MAX_BATCH_SIZE = int(os.environ.get('COMPUTE_SERVICE_MAX_BATCH_SIZE', '1000'))

# Create the compute service
compute_service = ComputeService(log_level=getattr(logging, LOG_LEVEL))

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for the service."""
    return jsonify({
        'status': 'ok',
        'service': 'compute-service',
        'version': getattr(app, 'version', '0.1.0')
    })

@app.route('/add', methods=['POST'])
def add():
    """Add two numbers."""
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing required parameters: a, b'}), 400
    
    try:
        result = compute_service.add(data['a'], data['b'])
        return jsonify({'result': result})
    except Exception as e:
        logger.error(f"Error in add operation: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/subtract', methods=['POST'])
def subtract():
    """Subtract one number from another."""
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing required parameters: a, b'}), 400
    
    try:
        result = compute_service.subtract(data['a'], data['b'])
        return jsonify({'result': result})
    except Exception as e:
        logger.error(f"Error in subtract operation: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/multiply', methods=['POST'])
def multiply():
    """Multiply two numbers."""
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing required parameters: a, b'}), 400
    
    try:
        result = compute_service.multiply(data['a'], data['b'])
        return jsonify({'result': result})
    except Exception as e:
        logger.error(f"Error in multiply operation: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/divide', methods=['POST'])
def divide():
    """Divide one number by another."""
    data = request.json
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing required parameters: a, b'}), 400
    
    try:
        result = compute_service.divide(data['a'], data['b'])
        return jsonify({'result': result})
    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    except Exception as e:
        logger.error(f"Error in divide operation: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/batch', methods=['POST'])
def batch_process():
    """Process a batch of operations."""
    if not ENABLE_BATCH_PROCESSING:
        return jsonify({'error': 'Batch processing is disabled'}), 403
    
    data = request.json
    if not data or 'operation' not in data or 'data' not in data:
        return jsonify({'error': 'Missing required parameters: operation, data'}), 400
    
    if len(data['data']) > MAX_BATCH_SIZE:
        return jsonify({'error': f'Batch size exceeds maximum allowed ({MAX_BATCH_SIZE})'}), 400
    
    try:
        operation = data['operation']
        batch_data = data['data']
        results = compute_service.process_batch(operation, batch_data)
        return jsonify({'results': results})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Error in batch operation: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000) 