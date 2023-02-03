x1=input("Factorial: ")
x2=input("Divide by: ")
#lenx=len(x1)
x3=int(x1)
x4=int(x2)
x5=1
#print(lenx)
for x in range(1,x3+1):
    x5=x5*x
    print(x5)
    print(x)

if(x5%x4) == 0:
    print("yes")
else:
    print("no")

#print(x5)