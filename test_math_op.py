import unittest
from math_op import MathOp

class TestMathOp(unittest.TestCase):
  def setUp(self):
    self.math_op_obj = MathOp()


  def test_sum(self):
    self.assertEqual(self.math_op_obj.sum(1,2), 3, 'should be 3')
  
  def test_minus(self):
    self.assertEqual(self.math_op_obj.minus(5,1), 4, 'should be 4')
    self.assertEqual(self.math_op_obj.minus(1,5), -4, 'should be -4')
  
  def test_divide(self):
    self.assertEqual(self.math_op_obj.divide(1,5), 0.2, 'should be -4')
    with self.assertRaises(ZeroDivisionError):
      self.math_op_obj.divide(1,0)


if __name__ == '__main__':
  unittest.main()