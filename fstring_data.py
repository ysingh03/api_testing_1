
'''
letter = "Hey my {}, how are you. Are you from {}"
name = 'Yogesh'
city = 'Mathura'

print(letter.format(name, city))

letter1 = "Hey my {1}, how are you. Are you from {0}"

print(letter1.format(city, name))
print(f"Hey my {name}, how are you. Are you from {city}")
'''

# def fib(n):
#     if (n == 1):
#         return 1
#     else:
#         a = fib(n - 1) + fib(n - 2)
#         return a
#
#
# print(fib(5))


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter the number for fib series "))
if terms <= 0:
    print("please enter the grater than 0 ")
else:

    for i in range(terms):
        print(fibonacci(i), end=',')

