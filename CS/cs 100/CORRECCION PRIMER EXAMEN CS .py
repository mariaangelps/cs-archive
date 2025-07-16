


                    "CORRECCION PRIMER COMMON 27 DE FEBRERO"



#Question 2:

a = 14
b = 3.0
c = a//b

print(c) #------> output: 4.0 con el float, porque tiene el float, cuando es float con int, la respuesta es con float. 

 
#question 11:


a = 'apple'

b = 'banana'

c = b[0] + a[-1] * 2 + a[2]

print(c) #------> beep

#question 17:

a = ['one', 'in', 'a', 'million']

b = ['time', 'flies', 'swiftly']

c = b[0]

print(c) #----> si es que no hay un :, etonces solo hubiera sido time


#q23:

score = int(input("Enter your score: "))
if score >= 70:
    print("You passed.")
elif score >= 80:
    print("You did well.")
elif score >= 90:
    print("Excellent!")
else:
    print("Did not compute.") #---> you passed, porque ese iba primero
    

#q26:


lst = ['M','a','r','c','h']
s = ''
for letter in lst:
    s += letter #---> s gets s + , we are not changing the str, output--> March

print(s)

#q28:
lst = ['M','a','y']
lst2 = []

for letter in lst:
    lst2.append(letter)

print(lst2*2)#---> ['M', 'a', 'y', 'M', 'a', 'y']




