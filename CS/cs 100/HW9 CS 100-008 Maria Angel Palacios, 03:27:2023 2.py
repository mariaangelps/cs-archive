
'''Maria Angel Palacios
CS 100 2023S Section 008
HW 09, March 27, 2023
'''

#Problem 1:

def file_copy(in_file,out_file):
    
    ifile=open(in_file,'r')
    ofile=open(out_file,'wt')
    words=ifile.readline()
    ofile.close()
    ifile.close()

#Problem 2:

def file_stats(in_file):
    line_number= 0
    word_number=0
    characters=0  
    a= open(in_file,"r")
    b=a.readlines()
    for i in b:
        line_number+=1
        c= i.split()
        word_number+=len(c)
        characters+=len(i)

    print('Number of Lines:{0}'.format(line_number))    
    print('Number of Words:{0}'.format(word_number))    
    print('Number of Characters:{0}'.format(characters)) 

file_stats('humpty.txt')


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





