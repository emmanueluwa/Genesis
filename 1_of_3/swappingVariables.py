v1 = "first 2 strings"
v2 = "secondstring"

## make v1 v2 and make v2 v1
'''
v1 = v2
v2 = v1
wrong 
'''
'''
a = v1 
b = v2 
v1 = b
v2 = a
correct
'''

# faster solution though, just use one temp variable

a = v1
v1 = v2
v2 = a 

# print(v1)
# print(v2)
print(len(v2))
