def function1():
    print('hello hello')
    print('hi hey')

function1()

def function2(x):
    print('you have ' + str(x - 1) + ' shots left')
    if x <= 15:
      return('low on ammo! ' + str(x - 1) + ' bullets left.')
    else:
      return('keep going')

# print(function2(6))
a = function2(10)
print(a)

# multiple arguments in a single function

def function3(x, y):
    return('plot position x = ' + str(x) + ' and y = ' + str(y) + ' on the graph.' )

f = function3(3, 5)
print(f)


#convert km to miles, considering km = 1.6 * miles

def convert(miles):
    print(str(miles) + ' miles is the same as:')
    return 1.6 * miles

km = convert(5)
print(str(km) + 'km')


def max_of_3(x, y, z):
    if x > y and z:
        return(x)
    elif y > z and x:
        return(y)
    else:
        return(z)

max = max_of_3(10, 20, 32)
print(max)

      
