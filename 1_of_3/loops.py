even = [2, 4, 6, 8, 10, 12]
total = 0
for element in even:
    total = total + element
print(total)

sum = 0
for i in range(1, 10):
    sum += i

print(sum)

#adding just even
sum1 = 0
for i in range(1, 10):
    if i % 2 == 0:
        sum1 += i

print(sum1)

#compute all multiples of 3 and 5
total1 = 0
for num in range(1, 100):
    if num % 5 == 0 and num % 3 == 0:
        total1 += num

print(total1)
