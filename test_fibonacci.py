import unittest
import fibonacci

class TestFibonacci (unittest.TestCase):
	def test_fib1(self):
		self.assertEqual(fibonacci.fib(0), 0)

	def test_fib2(self):
		self.assertEqual(fibonacci.fib(1), 1)

	def test_fib3(self):
		self.assertEqual(fibonacci.fib(4), 3)

class TestFactorial (unittest.TestCase):
	def test_fac1(self):
		self.assertEqual(fibonacci.fac(0), 1)

	def test_fac2(self):
		self.assertEqual(fibonacci.fac(7), 5040)

	def test_fac3(self):
		self.assertEqual(fibonacci.fac(1), 1)

if __name__ == '__main__':
    unittest.main()