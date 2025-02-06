import unittest
from main import fizzbuzz  

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")  
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")  
    def test_nbr(self):
        self.assertEqual(fizzbuzz(7), "7") 

if __name__ == '__main__':
    unittest.main()