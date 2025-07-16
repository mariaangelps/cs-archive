


pets = ['ant', 'bat', 'cod', 'dogs']
lst=[0,1,'two','three',[4,'five']]
nums= [0,1,2,3,4,5,6,7,8,9,10]

print('ant' not in nums)


s=''


#print ('ant' not in nums)

tup=()
r='rock'
c='climbing'

res =r+c
print(res)
print(r)
print(c)

b='hello'
print(b)

b='hi'
print(c)  #sale de output esta y tb la anterior, porque no se cambian las string


d='hello'

print(d)

d= d +'there'

print(d)


print(2*pets) # me daria toda la lista por las veces que yo escriba
print(pets[0])

print(pets[-1])

#whats the length of pets

print(len(pets))

# min of the list "el que está más a la derecha"

print(min(pets))


#sum of nums

print(sum(nums))



print(pets[-3])

pets[2]='cow' #only work with lists, it means that 2 is replacing the third
# element, cod by cow

print(pets)

#its not gonna work, porque se quiere cambair el string, y eso es imposuble hacer.

#  s='cod'
#  s[2]='w' 
#  print(S)

lst=[1,2,3]
lst.append(7)  #para agregar un numero al final se utiliza esta palabra
lst.append(3)
print(lst)

print(lst.count(3))  #numero de veces que se repite un item
print(lst.index(1))
print(lst.index(3))
print(lst.pop())
print(lst.remove(3))
print(lst)

lst =[159.99, 160.00 , 205.95 , 128.83 , 175.49]
lst.append(160.00)
print(lst)
print(lst.count(160.00))
minLst=min(lst)
index=lst.index(minLst)
print(index)
lst.remove(minLst)
print(lst)
lst.sort()
print(lst)

pets = ('ant', 'bat', 'cod', 'dog', 'elk')
tple = (0, 1, 'two', 'three', [4, 'five'])
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(pets.index('ant')
)

print(tple[4]) #or -1, se cuenta desde 0, pero para ponerle por el segundo metodo,

#contar de derecha a izquierda

print(tple[-1][1]) # del -1 escribir solo el 1 element 

print(tple[4][0]) # ir al 4 pero solo quiero el 0 element

print('three' not in nums)

print(pets[0:3]) #indicates a range, from en este casi 0 to 3
print(pets[0:5])
print(pets[2:2])  #this will give us a empty ()


