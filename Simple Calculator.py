#taking values
num1 = float(input("Enter the first value: "))
num2 = float(input("Enter another value: "))
#selecting operator
print("""
      Please Select:\n
      1 for addition
      2 for subtraction
      3 for multiplication 
      4 for division 
            
      """)
operator = input("Choose an operation: ")

def add (num1, num2):
    return num1 + num2
    
def sub (num1, num2):
    return num1 - num2

def mult (num1, num2):
    return num1 * num2

def div (num1, num2): return num1 / num2

if operator == '1':
    print(f"The Sum of {num1} and {num2} is: ", add (num1,num2))
elif operator == '2':
    print(f"The Difference between {num1:.2f} and {num2:.2f} is: ", sub (num1,num2))
elif operator == '3':
    print(f"The multiple of {num1} and {num2} is: ", mult (num1,num2))
elif operator == '4':
    print(f"The quotient of {num1} and {num2} is: ", div (num1,num2))
else:
    print("Please check your values!")