a1=['2', '4', '7', '4', '1']
xa=len(a1)
a2=a1[::-1]
y=0
for x in range(0, xa):
    if(a1[x]==a2[x]):
        y=1
    else:
        y=0
        print("not a palindrome")
        break

if(y==1):
    print("its a palindrome")
