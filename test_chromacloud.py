# test_chromacloud.py
"""
Tests for ChromaCloud module.
"""

import unittest
from chromacloud import ChromaCloud

class TestChromaCloud(unittest.TestCase):
    """Test cases for ChromaCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChromaCloud()
        self.assertIsInstance(instance, ChromaCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChromaCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
