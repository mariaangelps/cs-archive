name = input("What's your name bbygirl?")
print("My name is: " + name +"--> generic one")

#What if I put the name after 3 or more spaces?
## we would havew to use the string method called "strip" --> which basicaly
# removes white spaces from the input, and stores it in a string called nameFized
print("\n")  
nameFixed = name.strip()  
print("My name is: " + nameFixed +":--> fixed one")    

#now what if we actually want to store the fixed value inside a variable that has the same name as the original name
#the strip method will create a copy, a fixed one and will print the str
print("\n") 
name=name.strip() 
print("My name is: " +name +"-->same variable name assignment")

#capitalize 
print("\n") 
name=name.capitalize()
print(name +"-->capitalize just first name")

#capitalize first and last name--> title method
print("\n") 
name=name.title()
print(name + "-->name and lastName using title method")

#concatination of two method by assigning two values with the dot operator the to the variable name
print("\n") 
name= name.strip().title()
print(name + "-->concatination of two methods in the same line")
print("\n") 

#ask for an input and do the strip and capitalization in one step
name=input("Whats your name? ").strip().title()
print(name + "--> All the methods in one")
print("\n")  
print(" * " +" Split method")
#split user's name into first and last name
print("\n") 

#split will take the order that the variables are named 
first,last = name.split(" ")
print(first, "--> just first name")


#replace method

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)