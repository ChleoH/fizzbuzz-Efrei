import unittest

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
        with self.assertLogs() as log:
            fizzbuzz() 
        self.assertIn("Fizz", log.output[0])
        self.assertIn("Buzz", log.output[0])
