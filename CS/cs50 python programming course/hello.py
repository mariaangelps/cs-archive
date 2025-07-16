#print("hello world")#the hello world printed is the side effects 
#bug is  amistake in a program, such as writing python hello.py-->
#the correct way is python3 hello.py
#what if we misss the closed parenthesis? there will be an error, sduch as--> () is missing

#get info from the user
name= input("whats your name?")
print("hello" + name + "-->with + sign")
print("hola" , name + " --> with the \" \" sign")
print("holamaifrend + name" + "--> con el name dentro de las \"")

#salto de linea \n al igual que /""
print("hello, " , end="todo bien? \n" ) #lo pone al final, como un string
print("hello, \"friend\"")

#para separar con cualquier caracter, algo que ya ha sido escrito, se hace lo siguiente
print("hello, ", name, sep= " que gusto, ")

