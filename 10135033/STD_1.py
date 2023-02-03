#a = [11, 22, 14, 67, 2, 9]
#print(a)
#alen=len(a)
#minn=0
#tempva=0
#for x in range(0, alen-1):
#    minn=x
#    for y in range(x+1, alen):  
#        #print(y)
#        if(a[y] < a[minn]): 
#            #print(a[y])
#            minn=y
#            print(a[minn])
#    tempva=a[x]
#    a[x]=a[y]
#    a[y]=tempva
#    print(a[minn])
#    #print(a)


#print(a)
'''
selection sort
input is unsorted array
output is sorted array
find the minimum value location
put the minimum into the first available element
the first available element has to go back to (minimum value place where it was before)
so on
'''

abc = [11, 22, 14, 67, 2, 9]              #defined array to sort

def Selection_sort(abc):                  #defining sorting function, passing the array to sort inside
    for i in range(0, len(abc)-1):        #declaring for loop with range of the array but subtracted with 1
        minn=i                            #set the minn position (position of value in array to swap)
        print(abc)                        #print to see the sorting process
        for j in range(i+1, len(abc)):    #another for loop but with the starting range of +1
            if(abc[j]<abc[minn]):         #check if the abc[j] is less than abc[minn]
                minn=j                    #if abc[j] lower than abc[minn] set minn to j
        SWAP(abc, i, minn)                #call SWAP function with abc, i, minn parameters
    return abc                            #return result

def SWAP(abc, i, minn):                   #defining SWAP function
    tempval=abc[i]                        #use buffer to store abc[i]
    abc[i]=abc[minn]                      #set abc[i] to abc[minn]
    abc[minn]=tempval                     #assign buffer value to abc[minn]

print(Selection_sort(abc))                #print final result


#