

#ESTE VA A ESTAR SI O SI EN EL FINAL EXAM! MEMORIZATE ESTO

def readAge(filename):
    strAge=None
    while True:
        try:
            if strAge==None:
                infile = open(filename)
                strAge = infile.readline()
            age = int(strAge)
            print('Next year you will be', age+1)
            break
        except ValueError:
            print('Value cannot be converted to integer.')
            strAge=input('Enter your age in digits: ')
        except FileNotFoundError:
            print('Input file is missing:', "'" + filename + "'")
            filename=input('Enter a correct file name: ')
               
        


readAge('inputfile.txt')
