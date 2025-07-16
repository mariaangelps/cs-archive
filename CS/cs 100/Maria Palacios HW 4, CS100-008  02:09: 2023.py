


'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 04, February 9, 2023
'''

"Question 1 "

a= 3
b= 4
c= 5

if a<b:
    print("OK, (a<b)")
if c<b:
    print("OK that C less than B ")
if a+b==c:
    print("OK that Sum of and B is equal to c")
if (a**2)+(b**2) == (c**2):
    print("OK that Sum of ^2 and b^2 is equal to c^2")

"Question 2 "

a= 3
b= 4
c= 5

if a<b:
    print("OK, (a<b)")
else:
    print("NOT OK that a<b")
if c<b:
    print("OK, that c<b )")
else :
    print("NOT OK that c<b ")
if a+b==c:
        print("OK that Sum of and B is equal to c")
else :
    print("NOT OK that b=c")

if (a**2)+(b**2) == (c**2):
    print("OK that Sum of ^2 and b^2 is equal to c^2")
else:
    print("NOT OK that a^2 + b^2 =c^2 ")

"Question 3"

import turtle
t= turtle. Turtle()

c =input("What color? : ")
line_width = int(input("What line width? : "))
length = int(input("What line length? : "))
type_of_figure= input("Select one: line, square or triangle? : ")


"Line"
if type_of_figure == "line" :
    t.color(c)
    t.width(line_width)
    t.forward(length)

"square"
if type_of_figure == "square" :
    t.color(c)
    t.width(line_width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)


"triangle"
if type_of_figure == "triangle" :
    t.color(c)
    t.width(line_width)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)


