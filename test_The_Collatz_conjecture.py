import unittest
from The_Collatz_Conjecture import The_Collatz_Conjecture
#
class TestThe_Collatz_Conjecture(unittest.TestCase):
      def test_equal(self):
          self.assertEqual(The_Collatz_Conjecture( 1 ),  0 )
          self.assertEqual(The_Collatz_Conjecture( 2 ),  1 )
          self.assertEqual(The_Collatz_Conjecture( 3 ),  7 )
          self.assertEqual(The_Collatz_Conjecture( 4 ),  2 )
          self.assertEqual(The_Collatz_Conjecture( 5 ),  5 )
          self.assertEqual(The_Collatz_Conjecture( 6 ),  8 )
          self.assertEqual(The_Collatz_Conjecture( 7 ),  16)
          self.assertEqual(The_Collatz_Conjecture( 8 ),  3 )
          self.assertEqual(The_Collatz_Conjecture( 9 ),  19)
      #
      def test_negative(self):
          self.assertRaises(ValueError, The_Collatz_Conjecture(-11))
      #
      def test_not_integer(self):
          self.assertRaises(ValueError, The_Collatz_Conjecture("not number"))
#
if __name__ == "__main__":
    unittest.main()
