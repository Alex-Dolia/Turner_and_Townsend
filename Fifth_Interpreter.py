def sub_Fifth_Interpreter(text, stack, isError):
    text = text.strip().upper() 
    #
    if len(text) > 0:
       buf     = text.split()
       command = buf[0]
       if command == "PUSH":
          if len(buf) == 2:
             try: 
               number = int(buf[1])  
               stack.append(number)
             except:
               isError = True   
          else:
            isError = True
       #         
       if command == "POP":
          if len(stack) > 0:
             stack.pop()   
          else:
             isError = True   
       #
       if command == "DUP":
          if len(stack) > 0:
             stack.append(stack[-1])
          else:
             isError = True
       # 
       if command in ["SWAP", "+", "-", "*" , "/"]:
          if len(stack) >= 2:
             number1 = stack.pop()
             number2 = stack.pop()  
             #
             if command == "SWAP":  
                stack.append(number1)
                stack.append(number2)  
             if command == "+":
                stack.append(number2 + number1)
             if command == "-":
                stack.append(number2 - number1)
             if command == "*":
                stack.append(number2 * number1)   
             if command == "/":
                stack.append(number2 // number1)       
          else:
            isError = True 
    #
    return command, stack, isError


def Fifth_Interpreter():
    stack = []
    #
    isError = False
    #
    command = ""
    while command != "EXIT":
          if isError:
             print("ERROR")
             isError = False
          else: 
             print("stack is ", stack)
          # 
          text = input("")
          #
          command, stack, isError = sub_Fifth_Interpreter(text, stack, isError)
