import unittest
import prime

class TestPrimeMethods(unittest.TestCase):
  def test_is_prime(self):
    self.assertTrue(prime.isPrime(5))
    self.assertFalse(prime.isPrime(10))

  def test_check_all(self):
    self.assertTrue(type(prime.checkAll(3,5)) == list)
    self.assertTrue(type(prime.checkAll(3,5)[0]) == list)
    self.assertTrue(type(prime.checkAll(3,5)[0][0]) == int)
    self.assertTrue(type(prime.checkAll(3,5)[0][1]) == bool)
    self.assertTrue(len(prime.checkAll(5,3)) == 0)

  def test_big_prime(self):
    self.assertTrue(prime.isPrime(prime.bigPrime()))

if __name__ == '__main__':
  unittest.main()