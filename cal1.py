#to return int values according to input operations
def select_op(choice):
   "select arithmetic operation"
   if choice == "+":
      return 1
   if choice == "-":
      return 2
   if choice == "*":
      return 3
   if choice == "/":
      return 4
   if choice == "^":
      return 5
   if choice == "%":
      return 6
   if choice == "#":
      return -1
   if choice == "$":
      return 0
   return 9

#to add number1 and number2
def add(number1, number2):
  "adding two numbers"
  answer = number1 + number2
  return answer
  
#to substract number2 from number1    
def substract(number1, number2):
  "substracting two numbers"
  answer = number1 - number2
  return answer

#to multiply number1 and number2   
def multiply(number1, number2):
  "multiplying two numbers"
  answer = number1 * number2
  return answer

#to divide number1 by number2    
def divide(number1, number2):
  "dividing first number by second number"
  #avoiding divide by zero error
  if(number2 == 0):
    print("float division by zero")
    answer = "None"
  else: answer = number1 / number2
  return answer

#to get given power of a number   
def power(number, power):
  "calculating power of number"
  answer = number ** power
  return answer

#to get reminder when number1 divided by number2    
def remainder(number1, number2):
  "get remainder"
  answer = number1 % number2
  return answer

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  




  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  
  #to avoid entering invalid operations  
  if not(int(-2)<(select_op(choice)) or (select_op(choice))<7):
    print("Unrecognized operation")
    continue

  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
    
  if(select_op(choice) == 0):
    #program resets here
    print("Done. Resetting")
    continue

    #getting operands as inputs
  n1 = input("Enter first number: ")
  print(n1)
  #check whether user only entered numeric values
  if(str.isnumeric(n1)):
    num1=float(n1)
    

  else:
    
      if(select_op(n1) == -1):
        #program ends here
        print("Done. Terminating")
        exit()
    
      if(select_op(n1) == 0):
        #program resets here
        print("Done. Resetting")
        continue
      continue
      
  
  
  n2 = input("Enter second number: ")
  print(n2)
  #check whether user only entered numeric values
  if(str.isnumeric(n2)):
    num2=float(n2)

  else:
    
      if(select_op(n2) == -1):
        #program ends here
        print("Done. Terminating")
        exit()
    
      if(select_op(n2) == 0):
        #program resets here
        print("Done. Resetting")
        continue
      continue
  
  
  
  
 
  
  
 
  
   
  if(select_op(choice) == 1):
  #calling add function and print answer
    print(num1, "+", num2,"=", add(num1,num2))    
    
  if(select_op(choice) == 2):
  #calling substract function and print answer
    print(num1, "-", num2,"=", substract(num1,num2)) 
    
  if(select_op(choice) == 3):
  #calling multiply function and print answer
    print(num1, "*", num2,"=", multiply(num1,num2)) 
    
  if(select_op(choice) == 4):
  #calling divide function and print answer
    print(num1, "/", num2,"=", divide(num1,num2)) 
    
  if(select_op(choice) == 5):
  #calling power function and print answer
    print(num1, "^", num2,"=", power(num1,num2)) 
    
  if(select_op(choice) == 6):
  #calling remainder function and print answer
    print(num1, "%", num2,"=", remainder(num1,num2)) 
    
