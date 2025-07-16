


'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 01, January 26, 2023
'''

''' Exercise 5b'''

water=7
tea= 15
pepsi=4

print ('5b) 1. Water is ' + str(water))
print('5b) 2. Tea is ' + str(tea))
print ('5b) 3. Pepsi is ' +str (pepsi))



'''Exercise 5c'''

liters= 2.50
cost= 2.75
tax= 2.15

print('5c) 1. # Of Liters is ' +str(liters))
print('5c) 2. The cost value is ' + str(cost))
print('5c) 3. The tax value is '+ str(tax))

'''Exercise 5d'''

Out_of_State_Fee = "International Student"

Australian_Marsupial= "Kangaroo"

Most_common_music_platform = "Spotify"

print('5d) 1. The Out of State fee applies to '+ str(Out_of_State_Fee))
print('5d) 2. An Australian Marsupail is '+ str(Australian_Marsupial))
print('5d) 3. The Most Common Platformof Music is '+ str(Most_common_music_platform))



'''Exercise 1.1 from the book'''

# 1. If one or two of the parenthesis are left out, For example: " print(x or print x".
#An announcement pops up as '(' never closed  or 'mising parenthesis' '''


# 2. If the quotation marks are left out while trying to print a string, For example: Dollar = 'money or Dollar = money  without the strings.
# The result goes by as an unterminated string literal error or as undefined name.

# 3. If a plus sign is put before a number, it does not affect the operation at all. It follows the regular law of signs. For example if the operation is a 2 plus
# a negative four, the result would stay the same as 2-4. The same happens if we write 2++2, the result is going to be 4'''

x=2++2
print('Ex 1.1) #3. x = '+ str(x))

# 4. If we try to write a math notation with leading zeros. For example x= 011, in Python, an error announcement will pop up on the screen stating that leading zeros in decimal
# integer literals are not permitted.

# 5. If we have two values with no operator between them, such as : x=2 y=3 print(xy). The result would be a syntax error, which basically means that the program is not going to
# let the code run from the beginning.



''' Exercise 1.2 from the book'''

#Exercise 1.2 a


minutes= 42
seconds_in_total= (42*60)+42
print('Ex 1.2) #1. There are ' +str(seconds_in_total )+ ' in 42 minutes and 42 seconds')

#Exercise 1.2 b

kilometers= 10  
km_per_mile= 1.61
miles= kilometers/km_per_mile
print('Ex 1.2) #2. There are ' +str(miles) + 'miles in 10 km')

#Exercise 1.2 c

time1= seconds_in_total/miles           #Average pace in seconds/ miles
print('Average pace in sec/miles = '+str(time1))

time2= time1/60                         #Average pace in minutes/miles
print('Average pace in min/ miles = '+str(time2))


miles_per_hour= 60/time2                #Final conversion for the speed in miles per hour
print('Ex.1.2) #3. The average speed in miles/ hour is : ' + str(miles_per_hour) )


'''Exercise 2.1 from the book'''


# Problem 1.  If we assign a variable n a value of 42, the output will work. However when it is assigned to 42 a variable of n, it would be a syntax error. And even If
# we would like to write a double "==" sign, we would still have to define what "n" is equal to. -> n=42 works -> 42=n does not.

# Problem 2.  If we write  "x=y=1" it is a value that just does not pop up on the screen; however if we write the double "==" sign we may write a line that states that would evaluate the expression as
# true or false. We have to assign a value to "y" first in order to compute this operation.

y=3
x=(y==1)
print('Ex 2.1) #2 x=(y==1) is ' +str (x))

# Problem 3.  If we add a semicolon to our statement, in comparison to other languages,the code will still run and appear on the shell.

x=5;
print('Ex 2.1) #3 is ' +str (x**3));

# Problem 4.  If we add a period at the end of a statement it converts to float as showed below.
# However, if we write, x=5. and then the print statement is written on a form of -> print(x*4). with the period at the end, 
# the code will not run. 

x=5.
print('Ex 2.1) #4 is ' +str (x*4))


# Problem 5. If we try to multiply x and y like this-> xy , the code is not going to run because this is not the right way to multiply variables in a program.
# Therefore, the right syntax would be -> (x*y) with the operator between the two variables.


x=2
y=6
print('Ex 2.1) #5 is ' +str (x*y))


'''Exercise 2.2 from the book'''

#Problem 1

import math
math.pi
3.141592653589793
pi= math.pi
r=5  #radius value of the sphere
v= 4/3*(pi)*(r**3)   #volume of a sphere formula
print('Ex 2.2) #1. The volume of a sphere with radius 5 is ' +str(v))

#Problem 2 

Price= 24.95
Copies= 60
Discount= 60/100
Additional_copy= 0.75
First_copy= 3

Price_no_discount = Price* Copies       # Price without the discount

Price_with_discount =  Price*Discount  # Price including the discount

Price_of_the_book = Price_no_discount - Price_with_discount

print ('Ex 2.2) #2 Price of the book out of fees is: ' +str(Price_of_the_book))

shipping_additional_copies_= Additional_copy * 59  # The additional copy fee get multiplied by the 59 copies because the first one already costs $3 and we are just
                                                   # counting the shipping for the additional ones.
print('Ex 2.2) #2 Price of Additional copies shipping is : ' +str(shipping_additional_copies_))

finalprice= Price_of_the_book + shipping_additional_copies_ + First_copy

print('Ex 2.2) #2 The final price for 60 copies is '+ str ( finalprice ))

#Problem 3


time1= ((60*6)+52)  #starting time 6h and 52 min
time2= ((8)+15/60)  # Conversion to seconds of 8:15 min

time3= ((7)+12/60)   # Conversion to seconds of 7h:12 min 

time_in_total_minute= ((2*time2)+(3.*time3))
print('The total time in minutes is ' +str(time_in_total_minute))


time_running= int((time1+time_in_total_minute)/60) 
     
print('The time running is ' + str(time_running))
mins=(time1+time_in_total_minute)%60
print('The time in minutes is ' +str(mins))
print('The time arriving home is about '+  str(time_running)+":"+str(mins)+ " am")
