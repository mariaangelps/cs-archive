
import string

hdList = ['Humpty Dumpty sat on a wall.',
           'Humpty Dumpty had a great fall.',
           "All the king's horses and all the king's men", 
            "Couldn't put Humpty together again!"]

humptyFile = open('humpty.txt', 'wt')
for line in hdList:
    humptyFile.write(line + '\n')

humptyFile.close()

def humptyStats(infile,outfile):
    ifile=open(infile,'rt')
    ofile=open(outfile,'wt')
    vowels='aeiouAEIOU'

    for i in ifile:
        numWords = 0
        numVowels = 0
        numConsonants= 0
        numSpaces = 0
        numPunctuation = 0
        unknown = 0

        words=line.split()
        numWords =len(words)
        

        for letter in line:
            if letter.isalpha(): #------------> lowercase
                if letter in vowels:
                    numVowels+=1
                else:
                    numConsonants+=1
            elif letter.isspace():#contar espacios o elif.letter.isspace():
                numSpaces+=1
            elif letter in string.punctuation:
                numPunctuation+=1
            else:
                unknown+=1
                
        ofile.write('Words:{}, Vowels:{}, Consonants:{}, Spaces:{}, P: {}\n'.format(
            numWords,numVowels,numConsonants,numSpaces,numPunctuation))
    ifile.close()
    ofile.close()

       
humptyStats('humpty.txt','humptystats.txt')








'''
Create a function named 'humptyStats' that takes two arguments:

1. the input filename: humpty.txt
2. the output filename: humptystats.txt

The function humptyStats should read the input file and write to the
output file the following stats per line: total words, vowels, consonants,
spaces and punctuation marks.

The contents of humptystats.txt should be:

Words: 6, Vowels: 6, Consonants: 16, Spaces: 5, Punctuation: 1
Words: 6, Vowels: 7, Consonants: 18, Spaces: 5, Punctuation: 1
Words: 9, Vowels: 10, Consonants: 24, Spaces: 8, Punctuation: 2
Words: 5, Vowels: 10, Consonants: 19, Spaces: 4, Punctuation: 2


'''







        
        


