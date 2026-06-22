# test_chainedge.py
"""
Tests for ChainEdge module.
"""

import unittest
from chainedge import ChainEdge

class TestChainEdge(unittest.TestCase):
    """Test cases for ChainEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainEdge()
        self.assertIsInstance(instance, ChainEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
