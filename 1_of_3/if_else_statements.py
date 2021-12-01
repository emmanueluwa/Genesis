from typing import overload


b = 7
a = 7

if a < b:
    print('clearly a is less than b')
elif a == b:
    print('they are equal')
elif a > b + 30:
    print('a is bigger than 30')
else:
    print('no, a is greater than b')


# print(b)

# dealing w 3 or more seperated cases without using elif clause

even = 3
odd = 3

if even < odd:
    print('even is less')
else:
    if even > odd:
        print('even is more than odd')
    else:
        print('even and odd are equal')

#simpler?

if even < odd:
    message = 'even is less'
else:
    if even > odd:
        message = 'even is more than odd'
    else:
        message = 'even and odd are equal'

message = 'even is less' if even < odd else "even is more " if even > odd else "even and odd are equal"
print("message: " + message)


trimmed = True
not_trimmed = False


if not trimmed:
    print("How was your haircut yesterday?")
else:
    print("We looked forward to seeing you soon for your appointment with clip")





# bmi calculator
weight_kg = 110
height_m = 2
name = "ova"

bmi = weight_kg / (height_m ** 2)

print(name + " your bmi is: " + str(bmi))
if bmi >= 25.0:
    print(name)
    print("consider a healthier lifestyle")
else:
    print(name)
    print("according to your bmi you are on the right track")




#chanining comparison operators
#age should be 24 to 30

age = 25
if age >= 24 and age < 30:
    print("thank you, we will be with you shortly")

if 24 <= age < 30:
    print("We will be with you in 5mins")
