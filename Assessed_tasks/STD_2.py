""" Basic BST code for inserting (i.e. building) and printing a tree
has: iterative, recursive search methods, has a remove method.
"""

import math

""" Node class
"""

class Node:                         #create class Node
    def __init__(self, data = None):#define init function
        self.data = data            #initialize data
        self.left = None            #initialize left node
        self.right = None           #initialize right node

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:                   #create class BinaryTree
    def __init__(self):             #define init
        self.root = None

    def insert(self, data):         #insert function
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):    #display function
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    def find_i(self, target):           #iterative find method
        cur_node=self.root              #set cur_node to the top element
        while cur_node != None:         #if its not None
            if(cur_node.data==target):  #if target is equal to the cur_node.data, return it
                return cur_node         #could be any 2 -> | return true | return cur_node.value
            elif (cur_node.data>target):#if it is more than the target, go to the left node
                cur_node=cur_node.left  #set it to be left node then keep looking
            else:
                cur_node=cur_node.right #otherwise set the node to be the one on the right and keep looking
        return False
    
    def find_r(self, target):                   #recursive find method
        if self.root:                           #if self.root exists
            if self._find_r(target, self.root): #call _find_r with the target and self.root values
                return True 
            return False                        #if found nothing, return False
        else:
            return None                         #if self.root does not exist, return None
    
    def _find_r(self, target, cur_node):                #submethod for recursive
        if target > cur_node.data and cur_node.right:   #if target is more than cur_node.data and cur_node.right
            return self._find_r(target, cur_node.right) #return call self._find_r(target, cur_node.right)
        elif target<cur_node.data and cur_node.left:    #else if target is less than cur_node.data and cur_node.left
            return self._find_r(target, cur_node.left)  #return call self._find_r(target, cur_node.left)
        if target == cur_node.data:                     #if target is found
            return True                                 #return True


    #advanced+task+1
    def remove(self, target):       #remove method for binary tree
        
        if self.root == None:       #if no tree
            return False            #return False
        elif self.root.data == target:  #if tree root is equal to target
            if (self.root.left == None) and (self.root.right == None):  #check left and right node to be equal to None
                self.root=None      #if they are, set root to None
            elif self.root.left and (self.root.right == None):  #else check if left node exists and right is equal to None
                self.root = self.root.left  #if condition reached set root to be left node
            elif (self.root.left == None) and self.root.right:  #else check if left node is None and right node exists
                self.root = self.root.right #set root node to root.right
            elif self.root.left and self.root.right:    #else if both left and right nodes exists call submethod
                self.if_left_and_right(self.root)
        #if root is not target
        parent = None
        node = self.root

        while node and node.data != target:             #while node and node.data are not equal to target
            parent = node
            if target < node.data:
                node=node.left
            elif target > node.data:
                node = node.right

        if (node == None) or (node.data != target):     #case 1: target not found
            return False

        elif (node.left == None) and (node.right==None):#case 2: target has no children
            if target < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True

        elif node.left and (node.right == None):        #case 3: target has left child only
            if target < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        elif node.right and (node.left == None):        #case 4: target has right child only
            if target > parent.data:                    #if target is more than parent.data
                parent.right = node.right               #set parent.right to node.right value
            else:                                       #else
                parent.left = node.right                #set parent.left to node.right value
            return True                                 #return True

        else:                                           #case 5: target has left and right children
            self.if_left_and_right(node)

    def if_left_and_right(self, node):
        delNodeParent = node
        delNode = node.right

        while delNode.left:
            delNodeParent = delNode
            delNode = delNode.left

        node.data = delNode.data

        if delNode.right:
            if delNodeParent.data > delNode.data:
                delNodeParent.left = delNode.right
            else:
                delNodeParent.right = delNode.right
        else:
            if delNode.data < delNodeParent.data:
                delNodeParent.left = None
            else:
                delNodeParent.right = None

        





#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
#bst.insert(8)
#bst.insert(9)
#bst.insert(10)
#bst.insert(11)
##bst.insert(12)
##bst.insert(13)
##bst.insert(14)
##bst.insert(15)
##bst.insert(100)
##bst.insert(200)

bst.display(bst.root) #display tree before removal
print(bst.find_i(2)) #call the iterative find method
print(bst.find_r(2)) #call the recursive find method
#print(bst.remove(3))  #call the remove method to remove 3 from the binary tree in this case
bst.display(bst.root) #display tree after removal




