
'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 03, February 05, 2023
'''

'''Question 1'''

#Triangle

import turtle
t=turtle. Turtle()
t.color('red')
t.width(5)
t.penup()
t.goto(0,-350)
t.pendown()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(60)
t.setheading(360)
t.penup()
t.forward(200) #length number to keep a space from the square


#Square
t.pendown()
t.color('violet')
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.penup()
t.forward(300) #length number to keep a space from the Pentagon
t.right(90)


#Regular Pentagon

t.color('Light Blue')
t.pendown()
t.setheading(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.setheading(360)
t.forward(100)
t.penup()
t.forward(100)
t.setheading(90)
t.goto(0,0)
t.setheading(360)



'''Question 2'''
#Circle

t.setheading(90)
t.width(5)
t.color('green')
t.pendown()
t.circle(50) #circle with radius of 50 
t.penup()
t.goto(50,0)
t.pendown()
t.circle(100)  #circle with radius of 100
t.penup()
t.goto(100,0)
t.pendown()
t.circle(150)  #circle with radius of 150
t.penup()
t.goto(150,0)
t.penup()
t.pendown()
t.circle(200) #circle with radius of 200
t.penup()
t.right(90)


'''Question 3'''

import math

#a

print("The factorial number of 100! is : " +str(math.factorial(100)))

#b
print("The log of 1,000,000 in base 2 is : " + str(math.log(1000000,2)))


#c
print("The greatest common divisor of 63 and 49 is : " +str(math.gcd(63,49)))






