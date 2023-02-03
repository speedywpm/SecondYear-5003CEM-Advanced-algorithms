'''
linked list
builds a list with provided nodes
inputs a new node with a value after the requested node
'''

class Node: #initialize node
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None #initialize headvalue

    def listprint(self): #function to print list
        printval = self.headval #set top value (Mon) in this case
        while printval is not None: #until list is not empty
            print (printval.dataval) #print list element
            printval = printval.nextval #set printval with the element to be printed next, if there is not the loop will be terminated
            
    def AtBeginning(self,newdata): 
        NewNode = Node(newdata)

    def AtEnd(self, newdata): #function for the last element of the list
        NewNode = Node(newdata) #create node
        if self.headval is None: #if there is no first list value
            self.headval = NewNode #set it to be the first value
            return #halt
        last = self.headval #list position to be set to be the first element
        while(last.nextval): #while nextval exisits
            last = last.nextval #set the last visited position to be it
        last.nextval = NewNode #last visited position to be put in the new node
    
    def Insert(self,val_before,newdata): #function to insert the node
        if val_before is None: #if there is no match, that can not be inserted
            print("No node to insert after")
            return
        else:
            NewNode=Node(newdata) #create node
            asc=self.headval #initialize a headvalue
            while(asc.nextval): #while nextval exists
                asc = asc.nextval #consistently save it
                if asc.dataval==val_before: #until it reaches the position where we want to insert
                    break;
            ab=asc.nextval #put the nextval into buffer
            asc.nextval=NewNode #set that to be the new node
            NewNode.nextval=ab #set the new node with the buffer value

         

list = SLinkedList() #initialize list
list.headval = Node("Mon") #set headvalue to be Mon

e2 = Node("Tue") 
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5


list.AtEnd("Sun") #set end list value
list.Insert("Tue","Weds") #insert Weds after Tue
list.listprint() #print list
