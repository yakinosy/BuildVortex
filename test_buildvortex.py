# test_buildvortex.py
"""
Tests for BuildVortex module.
"""

import unittest
from buildvortex import BuildVortex

class TestBuildVortex(unittest.TestCase):
    """Test cases for BuildVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BuildVortex()
        self.assertIsInstance(instance, BuildVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BuildVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
