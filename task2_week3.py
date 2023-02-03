a1=['5','3','1','7','9','0','4','2','1','8']
print(a1)
alen=len(a1)
a2=input("select target to which look for")
target=a2

for x in range(0, alen):
    if(target==a1[x]):
        print("target found in location: "+str(x))
        break


