
'''
tup1 = (1,2)
print(type(tup1))

tup2 = (1, 2, 4, 'green', False)
print(tup2[0])
print(tup2[4])
print(tup2[2:5:1])
print(tup2[-4])
print(tup2[6::-1])
print(tup2[::1])
print(tup2[::-1])
'''

# count method
tup1 = (1,2,3,2,4,5,2,10,213,1,2,3)
print(tup1.count(3))
print('total count of digit in tuple is ', tup1.count(2))

t1 = (10,20,30)
t2 = ()
t3 = (10,)
t4 = 10,20,30,40
t5 = 10,20,30,40,

print(type(t1))

#to add element in tuple
t1 = t1 + t3

print(t1)
print(type(t1))

print(sum(t1))












