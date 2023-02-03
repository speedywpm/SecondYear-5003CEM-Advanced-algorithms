'''
adjacency matrix
has additional user interactive option, retains user input
user can add vertex, add edge(also checks if there is one already),
remove edge(checks if there is none), display matrix(prints it) 
'''

class Graph(object):
    
    def __init__(self, size):  #function to initialize the matrix
        self.adjMatrix = []    #matrix array itself, will contain multiple arrays inside then
        for i in range(size):  #this loop builds the matrix
            self.adjMatrix.append([0 for i in range(size)])
        self.printmatrix()     #print the matrix
        self.size = size       

    def addvertex(self, vert1):#function to add vertex, if we have 3 already, and want 2 more those will be added
        for i in range(vert1): #will runt as much as many vertexes required
            self.adjMatrix.append([0 for i in range(self.size)]) 
        self.printmatrix()

    def addedge(self, vertx2, verty2): #function to add edge
        if(self.adjMatrix[vertx2-1][verty2-1]==1): #check if there is already an edge
            print("Whoopsie the edge already exists") #if there is notify the user
        elif vertx2==verty2: #x==y can't be a valid edge
            print("no")
        else: #if there is no edge
            self.adjMatrix[vertx2-1][verty2-1]=1 #makes the edge part on x y
            self.adjMatrix[verty2-1][vertx2-1]=1 #makes the edge part on y x
            self.printmatrix()

    def remove_edge(self, vertxx, vertyy): #function to remove an edge
        if(self.adjMatrix[vertxx-1][vertyy-1] & self.adjMatrix[vertyy-1][vertxx-1] ==1): #check if there is an edge on x y and y x (if those coordinates for the multiple array are equal to 1)
            self.adjMatrix[vertxx-1][vertyy-1]=0 #if there is set the x y part to be 0
            self.adjMatrix[vertyy-1][vertxx-1]=0 #if there is set the y x part to be 0
            self.printmatrix()
        elif vertxx==vertyy: #x==y can not be a valid edge
            print("no")
        else: #else if both coordinates did not have a value of 1 or one of them, there is nothing to remove
            print("Whoopsie there is no edge")
            self.printmatrix()

    def printmatrix(self): #function to display the matrix
        print(*self.adjMatrix, sep="\n")
    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here

    def matrixselector(self): #function for user to interact
        selection=0 #selector variable
        print("Select (1) adding a vertex; (2) adding an edge; (3) removing an edge; (4) printing the matrix; (5) to stop the program")
        selection1=input(" ") #users choice
        selection=int(selection1) #convert str to int
        #below is very primitive, takes user choice and calls a specific function with user inputs or without them then calls the selection again as program would not terminate intstantly
        if(selection==1):
            vert=input("Insert how many vertixes do you want to add: ")
            vert1=int(vert)
            self.addvertex(vert1)
            self.matrixselector()
        elif(selection==2):
            vertx1=input("Insert the x coordinate: ")
            verty1=input("Insert the y coordinate: ")
            vertx2=int(vertx1)
            verty2=int(verty1)
            self.addedge(vertx2,verty2)
            self.matrixselector()
        elif(selection==3):
            vertx3=input("Insert the x coordinate: ")
            verty3=input("Insert the y coordinate: ")
            vertxx=int(vertx3)
            vertyy=int(verty3)
            self.remove_edge(vertxx,vertyy)
            self.matrixselector()
        elif(selection==4):
            self.printmatrix()
            self.matrixselector()
        else:
            quit()



#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
    g = Graph(6) #runs through the __init__ function to build the basic matrix with no edges
    g.matrixselector() #will run the basic menu, which will retain users progress until they decide to exit the program
        
       

if __name__ == '__main__':
   main()
