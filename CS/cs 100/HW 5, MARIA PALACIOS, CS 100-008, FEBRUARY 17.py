
'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 05, February 17, 2023

'''
#Question 1:

months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months)
for month in months:
    if month.startswith('J'):
        print(month)

#Question 2:
        
for i in range(0,100):
    if i%2==0 and i%5==0:
        print(i)
        
#Question 3:

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for i in horton:
    if i in vowels:
        print(i)                                                                                
