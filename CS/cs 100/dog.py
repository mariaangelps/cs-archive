'''
Maria Angel Palacios
Cs 100-008
04/21/2023
HW 11

'''

class Dog:
    def __init__(sugar,name,breed):
        sugar.name=name
        sugar.breed=breed
        sugar.tricks=[]
    def teach(sugar,trick):
        sugar.tricks.append(trick)
        print(sugar.name, 'knows', trick)
    def knows(sugar,i):
        if i in sugar.tricks:
            print('Yes',sugar.name,'knows',i)
        else:
            print('No',sugar.name,'doesnt know',i)
    species='canis familiaris'
name='Sugar'
breed='border collie'
tricks=[]

