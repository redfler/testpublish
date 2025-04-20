import sys
import os
import unittest
from unittest.mock import patch
import math

# Add the parent directory to the path so we can import the code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Try the direct import
try:
    from code.compute_service import ComputeService
except ImportError:
    # Alternative import approach
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from code.compute_service import ComputeService


class TestComputeService(unittest.TestCase):
    def setUp(self):
        self.service = ComputeService()

    def test_add(self):
        self.assertEqual(self.service.add(5, 3), 8)
        self.assertEqual(self.service.add(-1, 1), 0)
        self.assertAlmostEqual(self.service.add(0.1, 0.2), 0.3, places=10)

    def test_subtract(self):
        self.assertEqual(self.service.subtract(5, 3), 2)
        self.assertEqual(self.service.subtract(3, 5), -2)
        self.assertEqual(self.service.subtract(1, 1), 0)

    def test_multiply(self):
        self.assertEqual(self.service.multiply(5, 3), 15)
        self.assertEqual(self.service.multiply(-2, 3), -6)
        self.assertEqual(self.service.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.service.divide(6, 3), 2)
        self.assertEqual(self.service.divide(5, 2), 2.5)
        
        # Test division by zero raises exception
        with self.assertRaises(ZeroDivisionError):
            self.service.divide(5, 0)

    def test_process_batch(self):
        test_data = [
            {'a': 10, 'b': 5},
            {'a': 20, 'b': 2},
            {'a': 30, 'b': 3}
        ]
        
        # Test add operation
        results = self.service.process_batch('add', test_data)
        self.assertEqual(results, [15, 22, 33])
        
        # Test multiply operation
        results = self.service.process_batch('multiply', test_data)
        self.assertEqual(results, [50, 40, 90])
        
        # Test with invalid operation
        with self.assertRaises(ValueError):
            self.service.process_batch('invalid_op', test_data)
            
        # Test with invalid data item - correct expected value
        with patch('logging.Logger.warning') as mock_warning:
            results = self.service.process_batch('add', [{'a': 1}, {'a': 2, 'b': 2}])
            self.assertEqual(results, [4])
            mock_warning.assert_called_once()


if __name__ == '__main__':
    unittest.main() 