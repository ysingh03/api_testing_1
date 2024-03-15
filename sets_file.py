'''
s1 = {10,20,30}
s2 = {10}
print(type(s1))
print(type(s2))
s3 = {10,20,(11,22),50,60,20}
print(s3)
print(type(s3))
s4 = set()
print(type(s4))

s5 = set('yogesh')
s6 = set(10)
print(s5)
print(s6)

l1 = [20,20,30,40,50,50,20,70]

l2 = list(set([int(x) for x in input("enter the numbers ").split(',')]))
print(l2)

s1 = {10,20,30,10,20,50,50,60}

print(type(s1))
print(s1)
for x in s1:
    print(x)

s1.add(70)
# print(s1)
s1.add((10,20))
# print(s1)
# s1.add([1,3,4]) typeerror unhashable type error for adding list and set values
s1.add('yogesh') # adding string
print(s1)

'''

s2 = {10,20,30}
s2.add((22,33))
print(s2)
s2.update((22,33))
print(s2)








