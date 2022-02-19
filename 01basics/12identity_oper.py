'''
identity operator -> is

It returns True if data is present at same location in memory
'''

# a=300
# print(id(a))

# b=300
# print(id(b))

# print(a is b)

# n1=[1,2,3]
# print(id(n1))

n2=[1,2,3]
print(id(n2))

n3=n2
print(id(n3))

print(n2 is n3)
# print(n1 is n2)