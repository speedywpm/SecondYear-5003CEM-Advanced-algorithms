n=input()
d=input()
c=0
na=[]
def occurence(n, d, c):
    na=[i for i in n]
    g=0
    for x in na:
        if(na[g] == d):
            c=c+1
        g=g+1
    return c

print(int(occurence(n, d, c)))
