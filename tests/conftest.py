"""
Pytest configuration file.
"""
import sys
import os

# Add the parent directory to sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 