
'''
Maria Angel Palacios
CS 100 2023S Section 008
HW 08, March 24, 2023
'''

#Problem 1:
def twoWords (l,firstletter):
    words=[]
    while True:
        word1= input('Enter a '+str(l)+' letter word please :')
        if (len(word1)==l):
            words.append(word1)
            break
    while True:
        word2= input('Enter a word beginning with ' + str(firstletter)+' please:')
        if word2[0] == firstletter.upper() or word2[0] == firstletter.lower():
            words.append(word2)
            break
    return [words]
print(twoWords(4,'B'))

#Problem 2:

def twoWordsV2(l,firstletter):
    words=[]
    
    condition_of_word1= True
    while condition_of_word1:
        word1= input('Enter a '+str(l)+' letter word please :')
        if (len(word1)==l):
            words.append(word1)
            condition_of_word1= False

    condition_of_word2= True
    while condition_of_word2:
        word2= input('Enter a word beginning with ' + str(firstletter)+' please:')
        if word2[0] == firstletter.upper() or word2[0] == firstletter.lower():
            words.append(word2)
            condition_of_word2= False

    return [words]

print(twoWordsV2(4,'B'))


#Problem 3:

def enterNewPassword():
    while True:
        try1= str(input('Enter your password:'))
        is_a_digit=False

        for i in try1:
            if i.isdigit():
                is_a_digit=True
                break
      
        if not len(try1)in range(8,16):
            print('Password must have 8-15 characters and
                  contain at least one digit:')
            continue
        if not is_a_digit:
            print('Password must include one digit')
            
        else:
            print(try1)
            break
        
enterNewPassword()

#Problem 4:

def GuessNumber():
    import random
    num=random.randrange(0,50)
    x= "I'm thinking of a number in the range 0-50. You have five tries to guess it."
    print(x)
    num_of_run=1
    while num_of_run<=5:
        guess= int(input("Guess " + str(num_of_run) + " : "))
        if  guess > num :
            print('It is too high')
        elif guess < num:
            print('It is too low')
        else:
            print('Congrats! You are right! I was thinking of ' + str(guess))
            
            break
        num_of_run+=1
    print('Sorry! The right number is: ' + str(num))
    
GuessNumber()
    


        




    
        
            
            
