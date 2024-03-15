# create a string
'''
s1 = ''
s2 = ""
s3 = 'MysirJi'
s4 = "Mysirji"
s5 = """Mysirji"""
s6 = str()
s7 = str(123)
s8 = str(85.33)
s9 = str([10, 20])
print(s9)
'''

# Indexing
'''
s1 = "MySirji"
print(s1[0])
print(s1[3])
print(s1[-2])
print(s1[-5])
'''

# Accessing str elements
'''
s1 = "MySirji"
# s1[index]
# print(s1[2])

# print(s1)
# print(s1)

# for loop
for e in s1:
    print(e)
# or 
for e in s1:
    print(e, end=' ')

# slicing
s1 = 'mysirji'

print(s1[::1])
print(s1[::-1])
print(s1[::])
print(s1[6::-1])
print(s1[2:5:1])
print(s1[1:6:2])
print(s1[1:6:-1])
'''

s1 = 'mysirg education services private limited'
s2 = s1.split(' ')
print(s2)

s3 = s2[::-1]
s4 = ' '.join(s3)
print(s4)



