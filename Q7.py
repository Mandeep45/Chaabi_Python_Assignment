'''
Calculate the factorial of a number using lambda function
'''

def factorial(num):
    return (lambda f: lambda x: f(f, x))(lambda f, x: 1 if x == 0 else x * f(f, x - 1))(num)


number = int(input("Enter the number: "))
result = factorial(number)
print(result)
