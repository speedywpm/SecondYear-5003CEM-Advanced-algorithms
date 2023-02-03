#Use pseudocode to describe an algorithm that counts the number of letters, digits and special characters in a string. Anything between ‘a’ or ‘A’ and ‘z’ or ‘Z’ is considered a letter, anything between 0 and 9 is considered a digit, while anything else is considered a special character. 
#Input: a string s read from the keyboard, for example s = ‘3 beautiful days.’
#Output: letter count l = 13, digit count d = 1, special character count c = 3
#For solving this task, consider the string to be an array of characters and do not use any predefined functions that would make this task trivial.


#s=input()
#
#def COUNTER(s)
#   xa= i for every i in s
#   xi
#   l
#   d
#   c
#   for x in xa
#   if xa[xi].isalpha():
#            l=l+1
#        elif xa[xi].isnumeric():
#            if xa[xi]>=0 and intxa[xi]<=9:
#                d=d+1
#        elif xa[xi].isalpha() == False and xa[xi].isnumeric() == False:
#                c=c+1
#        xi=xi+1
#    return(l, d, c)
#result=counter(s)





s=input()
xa=[]

def counter(s):
    xa=[i for i in s]
    xi=0
    l=0
    d=0
    c=0
    for x in xa:
        if xa[xi].isalpha()==True:
            l=l+1
        elif xa[xi].isnumeric()==True:
            if int(xa[xi])>=0 and int(xa[xi])<=9:
                d=d+1
        elif xa[xi].isalpha() == False and xa[xi].isnumeric() == False:
                c=c+1
        xi=xi+1
    return(l, d, c)

result=counter(s)
print("letter count l = ")
print(result[0])
print(" digit count d = ")
print(result[1])
print(" special character count c = ")
print(result[2])