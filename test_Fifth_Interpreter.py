import unittest
from Fifth_Interpreter import sub_Fifth_Interpreter
#def sub_Fifth_Interpreter(text, stack, isError):
#
class Testsub_Fifth_Interpreter(unittest.TestCase):
      def test_PUSH(self):
          text, stack, isError = "PUSH 11", [22], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "PUSH")
          self.assertEqual(stack,   [22, 11])
          self.assertEqual(isError, False)
      #
      def test_POP(self):
          text, stack, isError = "POP", [22, 11], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "POP")
          self.assertEqual(stack,   [22])
          self.assertEqual(isError, False)
      #
      def test_SWAP(self):
          text, stack, isError = "SWAP", [22, 11], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "SWAP")
          self.assertEqual(stack,   [11, 22])
          self.assertEqual(isError, False)
      #
      def test_DUP(self):
          text, stack, isError = "DUP", [22, 11], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "DUP")
          self.assertEqual(stack,   [22, 11, 11])
          self.assertEqual(isError, False)
      #
      def test_sum(self):
          text, stack, isError = "+", [22, 11], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "+")
          self.assertEqual(stack,   [33])
          self.assertEqual(isError, False)
      #
      def test_minus(self):
          text, stack, isError = "-", [22, 11], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "-")
          self.assertEqual(stack,   [11])
          self.assertEqual(isError, False)
      #
      def test_mult(self):
          text, stack, isError = "*", [2, 11], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "*")
          self.assertEqual(stack,   [22])
          self.assertEqual(isError, False)
      #
      def test_div(self):
          text, stack, isError = "/", [110, 55], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "/")
          self.assertEqual(stack,   [2])
          self.assertEqual(isError, False)
      #
      def test_PUSH_error(self):
          text, stack, isError = "PUSH A", [22], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "PUSH")
          self.assertEqual(stack,   [22])
          self.assertEqual(isError, True)
      #
      def test_pop_empty(self):
          text, stack, isError = "POP", [], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "POP")
          self.assertEqual(stack,   [])
          self.assertEqual(isError, True)
      #
      #
      def test_dup_empty(self):
          text, stack, isError = "DUP", [], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "DUP")
          self.assertEqual(stack,   [])
          self.assertEqual(isError, True)
      #
      def test_swap_error(self):
          text, stack, isError = "SWAP", [1], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "SWAP")
          self.assertEqual(stack,   [1])
          self.assertEqual(isError, True)
      #
      def test_sum_error(self):
          text, stack, isError = "+", [1], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "+")
          self.assertEqual(stack,   [1])
          self.assertEqual(isError, True)
      #
      def test_minus_error(self):
          text, stack, isError = "-", [1], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "-")
          self.assertEqual(stack,   [1])
          self.assertEqual(isError, True)
      #
      def test_mult_error(self):
          text, stack, isError = "*", [1], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "*")
          self.assertEqual(stack,   [1])
          self.assertEqual(isError, True)
      #
      def test_div_error(self):
          text, stack, isError = "/", [1], False
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
          self.assertEqual(command, "/")
          self.assertEqual(stack,   [1])
          self.assertEqual(isError, True)
#
if __name__ == "__main__":
    unittest.main()