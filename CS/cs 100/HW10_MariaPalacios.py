
'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 10, April 17, 2023
'''

#Question Number 1:

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

def initialLetterCount(wordList):
    wordcount={}
    for i in wordList:
        starting_letter=i[0]
        if starting_letter in wordcount:
            wordcount[starting_letter]+=1
        else:
            wordcount[starting_letter]=1
    return wordcount
    
print(initialLetterCount(horton))

#Question Number 2:

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

def initialLetterCount(wordList):
    wordcount={}
    for i in wordList:
        starting_letter=i[0]    
        if starting_letter in wordcount:
            wordcount[starting_letter]=[i]
            a=wordcount[starting_letter]
        else:
            wordcount[starting_letter]= [i]
    return wordcount
    
print(initialLetterCount(horton))

#Question Number 3:

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

def shareOneLetter(wordList):
    wordcount = {}
    for i in wordList:
        starting_letter = []
        for word in wordList:
            for item in i:
                if item in word:
                    if word not in starting_letter:
                        starting_letter.append(word)
                        break
        if i not in wordcount:
            wordcount[i] = starting_letter
    return wordcount

print(shareOneLetter(horton))


