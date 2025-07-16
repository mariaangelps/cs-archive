

'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 02, February 2st, 2023
'''

''' QUESTION #1'''

grades = ['A', 'C', 'D', 'F', 'F', 'C' , 'B', 'C' , 'B', 'A']
a=grades.count('A')
b=grades.count('B')
c=grades.count('C')
d=grades.count('D')                
e=grades.count('F')

Frequency = [a,b,c,d,e]

print('Frequency = ' , Frequency)

'''Question #2'''

# Question a:

dogs_breeds = ['collie', 'Sheepdog', 'Chow', 'Chihuahua' ]
herding_dogs = dogs_breeds[0:2]

#Question b:

print('Herding dogs = '+str(herding_dogs))

#Question c:

tiny_dogs = dogs_breeds[3:4]
print('Tiny dogs = ' + str(tiny_dogs))

#Question d:
print("Persian is inside the dogs breads list = " ,'Persian' in dogs_breeds)



