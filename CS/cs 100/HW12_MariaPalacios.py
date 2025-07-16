'''
Maria Angel Palacios
CS 100-008
04/28/2023
HW 12'''

 
#PROBLEM 1:
def safeOpen(filename):
    try:
        inputFile=open(filename)
        strfile=inputFile.readline()
        return inputFile
    except FileNotFoundError:
        return None
    

#PROBLEM 2:

def safeFloat(x):
    try:
        num=float(x)
        return num
    except ValueError:
        return 0.0

#PROBLEM 3:
def averageSpeed():
    for num in range(1,3):
        file=input('Enter file name: ')
        newfile=safeOpen(file)
        if newfile==None:
            if num==2:
                print('File not found, yet another human error. Goodbye.')
                return
            print('File not found,Please try again.')

            continue
        else:
            sum=0
            counter=0
            average=0
            for i in newfile:
                if i.find(' ')>=0:
                    lst=i.split(' ')
                    
                    for element in lst:
                        mph=safeFloat(element)
    
                        if mph>2:
                            sum+=mph
                            counter+=1
                else:
                    mph=safeFloat(i)
                    if mph>2:
                        sum+=mph
                        counter+=1
                        break
    
            if counter>0:
                average=sum/counter
            print('Average speed is',(average), 'miles per hour')
            newfile.close()
