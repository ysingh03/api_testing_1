'''
def average(a, b=20, c=40):
    print("The avagrage is ", (a+b+c)/2)


average(10, 30, 40)

# default argument
average(20)
'''
'''
# Keyword argument
def average(a, b, c):
    print("The avagrage is ", (a+b+c)/2)

average(a=20, b=40, c=60)


# Required arguments
def average(a, b, c):
    print("The avagrage is ", (a+b+c)/2)

average(20, 40, 60)

'''
# Variable-length arguments
# ==============================================

def average(*number):
    s = 0
    for i in number:
        s = s + i
        return s / len(number)

c = average(100,20,23,25,26)
print(c)


