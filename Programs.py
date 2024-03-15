"""
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


# =======================================================================

# coding for calculate the BMI of a person

x = int(input("enter the person weight "))
y = float(input("enter the height of the person "))

bmi = x / (y ** 2)
print("bmi of the person is ", round(bmi,2))
print("bmi of the person is ", round(bmi))

a = 7.5
print(round(a))
print(type(a))

# =======================================================================

import random

a = random.randint(1, 2)
if a == 1:
    print("tails")
else:
    print("heads")

"""
# ===========================================================================

# pay the food bill by using random in the list
import random

names = input("Enter the names separated by comma")
names_list = names.split(",")
#print(names_list)
# biller_num = random.randint(0, len(names_list)-1)
# print(f"The food bill pay by {names_list[biller_num]}")

# or we can use below coding
selected_person = random.choice(names_list)
print(f"The food bill pay by {selected_person}")









