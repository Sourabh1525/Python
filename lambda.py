x = lambda a,b: a+b
print(x(5,4))


def f1(n):
    return lambda a: a*n

doub = f1(2)

print(doub(11))

def prime(x):
    for n in range  (2,x):
        if x%n == 0:
            return False
        else:
         return True
filtered = filter(prime,range(10))

print("Prime no. are: ", list(filtered))

###
def fun(variable):
    letters = ['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False

sequence = ['g','e','e','j','k','s','p','r']
filtered = filter(fun,sequence)
print('The filtered letters are: ')

for s in filtered: print(s)