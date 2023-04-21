# Function to calculate the factorial of a number
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Ask the user for input
num = int(input("Enter a number: "))

# Call the factorial function and print the result
result = factorial(num)
print(f"The factorial of {num} is {result}")