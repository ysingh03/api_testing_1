'''
for x in range(1,11):
    print(x)

else:
    print("it show after all the data of for")

for x in range(1, 11):
    print(x)
    if x == 5:
        break
else:
    print("it show after all the data of for")

'''
for x in range(1, 11):
    print(x)
    if x == 5:
        continue
        print("hello")
else:
    print("it show after all the data of for")