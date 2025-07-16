a=4
b=3
print(a%b)
#casting to an int, instead of 1.333, just 1
print(int(a/b))
#round to the nearest integer
print(round(a/b))
#casting to a float but with a fixed number of decimals
print(round(a/b,4))

x=input("whats x?")
y=input("whats y?")
z=x+y
print("the sum of x and y is: " + z + "-->the plus sign will concatinate the two numbers as string, instead of adding them up")
 
#to add their input we must cast the str first
# error of concatinate str to num cannot be possible,
#print("Way Number 1 --> " + int(z))
# therefore now, we must 
#cast z to be a string

z = int(x) + int(y)
print("Way Number 1 --> " + str(z))

#way Nro 2
#concatinate the whole expression to str, cast the mathematical operation to str
print("Way Number 2-->" + str(int(x)+int(y)))

#way nro 3
#concatinate the whole input, by casting the inout to string and each input to an int
 

print("Way Number 3--> " + str(int(input("whats x?"))
+int(input("whats y?"))))


def main():
    x=int(input("whats x?"))
    print("x squared is: " , square(x))

def square(n):
    return n*n
main()