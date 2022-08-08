import unittest
import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

	def test_fizz(self):
		number = 6
		result = FizzBuzz.get_reply(number)
		self.assertEquals(result, 'Fizz')

	def test_buzz(self):
		number = 10
		result = FizzBuzz.get_reply(number)
		self.assertEquals(result, 'Buzz')

	def test_fizzbuzz(self):
		number = 15
		result = FizzBuzz.get_reply(number)
		self.assertEquals(result, 'FizzBuzz')

	def test_null(self):
		number = 1
		result = FizzBuzz.get_reply(number)
		self.assertEquals(result, '')

if __name__ == '__main__':
	unittest.main()