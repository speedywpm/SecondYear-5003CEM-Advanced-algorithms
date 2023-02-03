#Input: a string s, for example s = ‘A beautiful day!’
#a character c, for example c = ‘a’
#Output: occurrences count nr = 3

#s="A beautiful day!"
#int xd=[]
#xd=str.split(s)
#int a=0
#for x in xd:
#   a=a+1
#print("occurences count "+str(a))
#
#
#

#s="A beautiful day!"
#xd=[i for i in "A beautiful day!"]
#print(xd)
#a=0
#y=-1
#if(xd[0]!=" "):
#    a=a+1
#for x in xd:
#    y=y+1
#    if xd[y]==" ":
#        a=a+1
#print("occurences count"+str(a))

##Input: a string s read from the keyboard, for example s = ‘beautiful’
##Output: a string s = ‘lufituaeb’

u=-1
s2=""
s=[i for i in "beautiful"]
s1=s[::-1]
for k in s1:
    u=u+1
    s2=s2+str(s1[u])
print(s2)
