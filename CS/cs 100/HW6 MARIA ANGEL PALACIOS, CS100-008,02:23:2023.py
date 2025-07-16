
'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 06, February 23, 2023

'''




#Question 1:

def hasFinalLetter(strlist, letters):
    result=[]
    for i in strlist:
        for letter in letters:
            if i.endswith(letter) or i.endswith(letter):
                result.append(i)
    return result

#Case 1:
strlist=["BunnY","Cow","luna"]
letters=("Ya")
print(hasFinalLetter(strlist,letters))

#Case 2:

strlist=["DogS","Cats","luna"]
letters=("gt")
print(hasFinalLetter(strlist,letters))


#Case 3:

strlist=["DogS","Cats","luna"]
letters=("aC")
print(hasFinalLetter(strlist,letters))


#Question 2:
def isDivisible(maxlnt,twolnts):
    result=[]
    for i in range(1,maxlnt):
        if i%twolnts[0]==0 and i%twolnts[1]==0 :
            result.append(i)
    return result


num1=(2,5)
num2=(13,11)
num3=(4,9)
a1=isDivisible(45,num1)
a2=isDivisible(45,num2)
a3=isDivisible(45,num3)
print("The number is divisible by ",a1)
print("The number is divisible by ",a2)
print("The number is divisible by ",a3)
