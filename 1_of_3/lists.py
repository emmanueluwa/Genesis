a = ["bitcoin", "blockchain", "crypto"]

# swap the first and last values 
x = a[0]
a[0] = a[2]
a[2] = x
print(a)

a[0], a[2] = a[2], a[0]
print(a)

print(len(a))
