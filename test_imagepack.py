# test_imagepack.py
"""
Tests for ImagePack module.
"""

import unittest
from imagepack import ImagePack

class TestImagePack(unittest.TestCase):
    """Test cases for ImagePack class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ImagePack()
        self.assertIsInstance(instance, ImagePack)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ImagePack()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
