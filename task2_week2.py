a1=['7','1','4','3','2','6','5','9','8']
a2=a1
print(a1)
print(a2)
alen=len(a1)
tempval=0
for x in range (0, alen):
    print("cycle "+str(x))
    for y in range (0, alen-1):
        print("i work")
        if(a1[y] < a1[y+1]):
            print("i am exchanging "+str(a1[y])+" with "+str(a1[y+1]))
            tempval=a1[y+1]
            a2[y+1]=a1[y]
            a1[y]=tempval
        else:
            y=y+1

print(a1)
print(a2)

#questionable