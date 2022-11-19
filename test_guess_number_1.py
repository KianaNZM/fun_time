import unittest
from guess_number_1 import GuessNumber1
# import StringIO
# import sys

class TestGuessNumber1(unittest.TestCase):
  def setUp(self):
    self.guess_number = GuessNumber1(0, 20, 10)
    self.guess_number.random_number = 10

  def test_evaluate(self):
    self.assertEqual(self.guess_number.evaluate(15), 1, 'should be -1')
    self.assertEqual(self.guess_number.evaluate(10), 0, 'should be 0')
    self.assertEqual(self.guess_number.evaluate(5), -1, 'should be 1')
    self.guess_number.tries = 1000

  def test_result_interaction(self):
    self.assertEqual(self.guess_number.result_interaction(-1), 'Less', 'should be Less')
    self.assertEqual(self.guess_number.result_interaction(1), 'Greater', 'should be Greater')
    self.assertEqual(self.guess_number.result_interaction(0), f'Win after 0', 'should be Win after 0')

  # @patch('guess_number.get_input', return_value='10')
  # def test_interact(self):
  #   capturedOutput = StringIO.StringIO()          # Create StringIO object
  #   sys.stdout = capturedOutput                   #  and redirect stdout.
  #   sys.stdout = sys.__stdout__                   # Reset redirect.
  #   print('Captured', capturedOutput.getvalue() )  # Now works as before.

    


if __name__ == '__main__':
  unittest.main()