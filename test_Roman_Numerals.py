import unittest
from Roman_Numerals import Roman_Numerals
#
class TestRoman_Numerals(unittest.TestCase):
      def test_equal(self):
          self.assertEqual(Roman_Numerals("X"    ),   10)
          self.assertEqual(Roman_Numerals("II"   ),    2)
          self.assertEqual(Roman_Numerals("V"    ),    5)
          self.assertEqual(Roman_Numerals("C"    ),  100)
          self.assertEqual(Roman_Numerals("M"    ), 1000)
          self.assertEqual(Roman_Numerals("VI"   ),    6)
          self.assertEqual(Roman_Numerals("MXVII"), 1017)
      #
      def test_values(self):
          self.assertRaises(ValueError, Roman_Numerals("XWII"))
      #
      def test_empty(self):
          self.assertRaises(ValueError, Roman_Numerals(""))
#
if __name__ == "__main__":
    unittest.main()