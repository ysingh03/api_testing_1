"""
g = 12 # global variable

class Test():
    l = 20  # local variable
    print("local variable = ", l)
    print("global variable = ", g)

Test()
print("global variable = ", g)

#=============================================
g = 12 # global variable

class Test():
    g = 20  # local variable
    print("local variable = ", g)
    print("global variable = ", g)

Test()
print("global variable = ", g)

# ===============================================
g = 12 # global variable

class Test():
    global g
    g = 20 # global variable
    print("local variable = ", g)
    print("global variable = ", g)

Test()
print("global variable = ", g)
"""
#========================================================

g = 12 # global variable

class Test():
    g = 20 # local variable
    x = globals()
    print("local variable = ", g)
    print("global variable = ", x['g'])

Test()
print("global variable = ", g)
