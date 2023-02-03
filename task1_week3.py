a1=[]
a2=[]
hey=input("put a sentence in of your desire: ")
a1=hey.split()
a1len=len(a1)
xlenx=0
for x in range(0, a1len):
    xlenx=len(a1[x])
    for y in reversed(range(0, xlenx)):
        a2[y]=a2[y]+a1[y]


#print(a1)
