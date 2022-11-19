## write a calculator
print("Enter a number")
number1 = int(input())
print("Enter another number")
number2 = int(input())
## enter the operator
print("Enter the operator")
operator = input()

## select the algrothim
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Invalid operator")