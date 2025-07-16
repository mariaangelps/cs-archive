def cities(cityList):
    lst = []
    i = 0
    while True:
        city = cityList[i]
        i += 1
        if city == 'Boston':
            break
        lst.append(city)
    return lst


lst = ['Lisbon', 'San Francisco', 'Boston', 'Hong Kong']

print(cities(lst))


greeting = "Hello World"
print(greeting[1:3])

fruit='hola mari'
if 'h' in fruit:
    print(fruit.index('h'))

    
s= "'(hello!)'"
print(s.strip("()!")) #output hello sin tanta cosa



def iSquaredPlus10(x):
    result = x**2 + 10
    print(result)
    
def iSquaredPlus10(x):
    result = x**2
    return result, 10



def hello(name):
    line = input('Welcome, ' + julie + ', to the world of Python.')
    return line
def myFunction(aStr):
    result = len(aStr.split(' '))
    return result
exclamation = "That makes me !#? "
print(myFunction(exclamation))


def myFunction(aStr):
    return len(aStr)

s = 'my cat is catatonic\n'
print(myFunction(s))


def myFunction(aStr):
    result = aStr.split()
    return aStr

exclamation = "That makes me !#? "
print(myFunction(exclamation))

def myFunction(aStr):
    counter = 0
    for char in aStr:
        if char.isspace():
            counter += 1
    return counter

exclamation = "That makes me \"upset\"\n"
print(myFunction(exclamation))


def myFunction():
    n = -1
    while n%2 == 1:
        n = int(input("Enter an even number: "))
    return n

print(myFunction())

def myFunction():
    n = -1
    while n < 0:
        n = int(input("Enter a positive number: "))
    return n

print(myFunction())


def myFunction(rows, cols):
    result = 0
    for i in range(rows):
        for j in range(cols):
            result += 1 
    return result

print(myFunction(3, 4))
 

 
