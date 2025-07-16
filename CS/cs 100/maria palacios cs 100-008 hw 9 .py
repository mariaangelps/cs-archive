'''
Maria Angel Palacios
CS 100- 008 HW 09,
March 28, 20223
'''
def file_copy(in_file ,out_file):
    infile= open(in_file, 'rt')
    outfile=open(out_file, "w")
    words= infile.readline()
    x=''
    for i in words:
        x+=i
    outfile.write(x)
    infile.close()
    outfile.close()
print(file_copy('created_equal.txt','copy.txt'))
