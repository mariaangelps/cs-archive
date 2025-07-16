##strip is used to remove the whitespaces, not the ones between strings
##only the spaces from the end and the beginning
name = input("What's your name bbygirl?")
print("My name is: " + name +"--> generic one")

#What if I put the name after 3 or more spaces?
## we would havew to use the string method called "strip" --> which basicaly
# removes white spaces from the input, and stores it in a string called nameFized
print("\n") 
print("Strip Method") 
nameFixed = name.strip()  
print("My name is: " + nameFixed +":--> fixed one")    

#split method
#it will return a list, an array of one element
print("\n")
print("Split method")
nameFixed = name.split(" --- ")
print("My name with split is: " + str(nameFixed)) 
print("The length of the array is: -->" + str(len(nameFixed)))
print("The index of the array is: " + str(nameFixed[0]))
#this will give me an error
#print("The index of the array is: " + str(nameFixed[1]))

#replace method

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)
