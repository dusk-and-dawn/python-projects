import csv

def passwd_to_csv(file1, file2):
    readfile = open(file1, 'r')
    writefile = open(file2, 'w')
    writefile.write(readfile[0], readfile[1], sep='\t')
    print(writefile)
    
passwd_to_csv('/home/curiosity/python projects/input_file.txt', '/home/curiosity/python projects/ouput_file.txt')lt