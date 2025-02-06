import unittest
from main import is_fizz, is_buzz, fizzbuzz 

class TestFizzBuzz(unittest.TestCase):
    def test_is_fizz(self):
        self.assertTrue(is_fizz(3))  
        self.assertTrue(is_fizz(13))  
        self.assertFalse(is_fizz(5)) 
    
    def test_is_buzz(self):
        self.assertTrue(is_buzz(5))  
        self.assertTrue(is_buzz(15))  
        self.assertTrue(is_buzz(51))  
        self.assertFalse(is_buzz(3))  
    
    def test_fizzbuzz(self):
        results = fizzbuzz()
        self.assertIn("Fizz", results[0])  # Ex: 3, 6, 9, etc.
        self.assertIn("Buzz", results[4])  # Ex: 5, 10, 20, etc.
        self.assertIn("FizzBuzz", results[14])  # Ex: 15, 30, 45, etc.

if __name__ == '__main__':
    unittest.main()
