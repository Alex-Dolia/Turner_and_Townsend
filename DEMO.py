from The_Collatz_Conjecture import The_Collatz_Conjecture
from Roman_Numerals         import Roman_Numerals
from Fifth_Interpreter import Fifth_Interpreter, sub_Fifth_Interpreter



if __name__ == "__main__":
   #	
   for n in range(1, 10):
       #print("!!! n: ", n)
       how_many_steps = The_Collatz_Conjecture(n)
       print("self.assertEqual(The_Collatz_Conjecture(",  n, "), ", how_many_steps, ")")
   #
   for Roman_Numbers in ["VXII", "XCMII", "VXIIXCMII"]:
       number = Roman_Numerals(Roman_Numbers)
       print("Roman_Numbers: ", Roman_Numbers, ", number: ", number)
   #
   print("""Fifth also supports the following commands:
PUSH x - push x onto the top of the stack, where x is a valid integer
POP - remove the top element of the stack
SWAP - swap the top two elements of the stack
DUP - duplicate the top element of the stack""")
   print("""\nExample:
stack is []
PUSH 3
stack is [3]
PUSH 11
stack is [3, 11]
+
stack is [14]
DUP
stack is [14, 14]
PUSH 2
stack is [14, 14, 2]
*
stack is [14, 28]
SWAP
stack is [28, 14]
/
stack is [2]
+
ERROR """)
   print("\n\n")
   print("Type command for Fifth Interpeter")
   print("If you want to quit from Fifth Interpeter then type EXIT")
   Fifth_Interpreter()
