def hello():
    name=input("What is your name?")
    print("hello! Welcome " + name)
def hello2(guest2):
    print("hello! Guest2 " + guest2 )

#punto de entrada va a ser cuando se llama a la function
hello()


#punto de entrada va a ser right here, name is inserted in guest2 and guest 2 is printed inside the function 
name=input("What is your name?")
hello2(name)

#scope definition--> global variable, no error
name=input("Whats your name scope trial")

def main():
    hello3()
    
def hello3():
    print("hello! "+ name + "--> no errors because name is a global variable")
    
#punto de entrada
main()

#scope error, when trying to call a local variable as a global one
def main2():
    name2=input("Whats your name scope trial 2: ")
    hello4()

def hello4():
    print("Hello! " + name2 + "---> error")
    
main2()



