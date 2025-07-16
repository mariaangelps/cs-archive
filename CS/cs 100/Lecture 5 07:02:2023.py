name= input("Enter your name : ")
age = int(input('Enter your age : '))



if age>=62 :   #siempre siempre, se pone los dos puntos,
               #tanto en el if como en el else
    print(name , ', you can collect social security benefits. ')
    
else:
    print(name + ', sorry, you are too young to get ss. ')


# poner atención a este


report= 'prueba de codigo 1 Large bonuses'

if 'large bonuses' in report:
    print('vacation time')

if 'large bonuses' in report  or 'Large Bonuses' in report:
    print('vacation time')

if age >18 and age<21: #hay que ponerle el age en ambos lados, porque sino no funciona
    print( 'You can vote but not drink!')

hits =12
shield =0

if hits>10 and shield==0:
    print("You screamed \"AHHHH\" WHEN YOU DIED")
    #print("You're dead!") #o tb puede escribirse como 'You\'re dead!)
    
credit = int(input("Enter the number of credits completed : "))
if credit>=18 and credit>15:
    print("You are a senior")

elif credit>=6 and credit<18:
    print("You are a junior ")
elif credit>=4 and credit<6:
    print("You are a sophore")
else:
    print("Undefined number of credits")


f = 1.0
g = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1

diff=f-g
theta = 0.001

if diff<theta:
    print("Equal")
else:
    print("Not Equal")

