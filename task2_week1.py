a1=input("Write in your number: ")
a2=len(a1)
a1=int(a1)
a3=0
#print(a2)
for a in range(a2):
    a3=a3+(a1[a]*a1[a]*a1[a])
if(a3==a1):
    print("Yes")
else:
    print("No")

#next