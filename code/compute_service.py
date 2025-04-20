import logging
from typing import Dict, Any, Optional, Union, List
import time

class ComputeService:
    """
    A service for performing various computational tasks.
    """
    
    def __init__(self, log_level: int = logging.INFO):
        """
        Initialize the compute service with optional configuration.
        
        Args:
            log_level: The logging level to use
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        # Add a console handler if none exists
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            
        self.logger.info("ComputeService initialized")
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers together.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        self.logger.debug(f"Adding {a} and {b}")
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The result of a - b
        """
        self.logger.debug(f"Subtracting {b} from {a}")
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        self.logger.debug(f"Multiplying {a} and {b}")
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            The result of a / b
            
        Raises:
            ZeroDivisionError: If b is zero
        """
        self.logger.debug(f"Dividing {a} by {b}")
        if b == 0:
            self.logger.error("Division by zero attempted")
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    def process_batch(self, operation: str, data: List[Dict[str, Union[int, float]]]) -> List[Union[int, float]]:
        """
        Process a batch of operations on pairs of numbers.
        
        Args:
            operation: One of 'add', 'subtract', 'multiply', 'divide'
            data: List of dictionaries with 'a' and 'b' keys
            
        Returns:
            List of results from applying the operation to each pair
        """
        self.logger.info(f"Processing batch of {len(data)} operations")
        results = []
        
        op_map = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }
        
        if operation not in op_map:
            raise ValueError(f"Unsupported operation: {operation}")
        
        func = op_map[operation]
        
        for item in data:
            if 'a' not in item or 'b' not in item:
                self.logger.warning(f"Skipping invalid item: {item}")
                continue
                
            try:
                result = func(item['a'], item['b'])
                results.append(result)
            except Exception as e:
                self.logger.error(f"Error processing item {item}: {str(e)}")
                
        return results


# Example usage
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Create service
    service = ComputeService()
    
    # Simple operations
    print(f"Addition: 5 + 3 = {service.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {service.subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {service.multiply(6, 7)}")
    print(f"Division: 15 / 3 = {service.divide(15, 3)}")
    
    # Batch processing
    batch_data = [
        {'a': 10, 'b': 5},
        {'a': 20, 'b': 2},
        {'a': 30, 'b': 3}
    ]
    
    results = service.process_batch('multiply', batch_data)
    print(f"Batch multiplication results: {results}") 