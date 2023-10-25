#1.1 Implement a recursive function to calculate the factorial of a given number 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"Factorial of {num} is {result}")
except ValueError:
    print("Please enter a valid number.")