# test_fuseember.py
"""
Tests for FuseEmber module.
"""

import unittest
from fuseember import FuseEmber

class TestFuseEmber(unittest.TestCase):
    """Test cases for FuseEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FuseEmber()
        self.assertIsInstance(instance, FuseEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FuseEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
