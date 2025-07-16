
'''Maria Angel Palacios
CS 100 2023S Section 008
HW 09, March 27, 2023
'''

#Problem 1:

def file_copy(in_file,out_file):
    
    ifile=open(in_file,'rt')
    ofile=open(out_file,'w')
    lines=ifile.readlines()
    a=''
    for i in lines:
        a+=i
    ofile.write(a)
    ofile.close()
    ifile.close()

file1='/Users/macbookpro/Desktop/codigo cs/HW9 CS 100-008 Maria Angel Palacios, 03:27:2023.py'
file2='/Users/macbookpro/Desktop/codigo cs/HW9 CS 100-008 Maria Angel Palacios, 03:27:2023copy.py'
file_copy(file1,file2)



#Problem 2:
filestats='/Users/macbookpro/Desktop/codigo cs/HW9 CS 100-008 Maria Angel Palacios, 03:27:2023copy.py'
def file_stats(in_file):
    openFile(open(in_file))
    linescount = 0
    wordscount=0
    characterscount=0
    for i in openFile:
        words=i.split()
        for i in words:
            linescount +=1
        for i in line:
            characterscount +=1
        linescount+=1
    print("number of lines: " , linescount)
    print("number of words: " , wordscount)
    print("number of characters :", characterscount)
    return ''
print(file_stats(filestats))

#Problem 3 :

import string

def repeat_words(in_file,out_file):
    
    ifile=open(in_file,'r')
    ofile=open(out_file,'wt')    
    for line in ifile:        
        counter=[]        
        for word in line.lower().split():            
            counter.append(word.strip(string.punctuation))
        
        word=[]
        for line in counter:
            if (counter.count(line)>1):
                word.append(line)
        c=[]    
        for i in word:
            if (word.count(i)>1):
                c.append(g)

        for a in c:            
            ofile.write(a+'')            
            ofile.write('\n')
    ifile.close()    
    ofile.close()
f1= '/Users/macbookpro/Desktop/codigo cs/HW9 CS 100-008 Maria Angel Palacios, 03:27:2023.py'
