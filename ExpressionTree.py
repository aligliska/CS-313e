#  File: ExpressionTree.py

#  Description: This program inputs a line of mathematical expression and 
#  builds an expression tree. This tree places the operand nodes as the
#  leaves of the tree, with each operator node have 2 children. The output 
#  returns the calculated expression value and a top to bottom and 
#  bottom to top read of the expression tree. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/24/2021

#  Date Last Modified: 7/28/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

# converts string operator and returns operation value 
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)
    

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0
    

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree (object):
    def __init__ (self):
        self.root = Node(None)
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        characters = expr.split()
        tree_stack = Stack()
        curr = self.root

        for char in characters:
            # create new left child node
            if char == "(":
                tree_stack.push(curr)
                curr.lChild = Node(None)
                curr = curr.lChild
            # make current node equal to parent node 
            elif char == ")":
                if not tree_stack.is_empty():
                    curr = tree_stack.pop()
            # sets operator into current node 
            elif char in operators:
                curr.data = char
                tree_stack.push(curr)
                curr.rChild = Node(None)
                curr = curr.rChild
            # sets operand into current node 
            else:
                if float(char) // 1 != float(char):
                    curr.data = float(char)
                else:
                    curr.data = int(char)
                curr = tree_stack.pop()
        return 
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # no operator found
        if aNode.data == None:
            return 0
        # node has no children 
        elif aNode.lChild == None and aNode.rChild == None:
            return aNode.data

        left = float(self.evaluate(aNode.lChild))
        right = float(self.evaluate(aNode.rChild))
        if aNode.data not in operators:
            return aNode.data
        else:
            return operation(aNode.data, left, right)

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        pre_ord_lst = self.pre_order_helper(aNode, [])
        pre_ord_strng = ""

        for element in pre_ord_lst:
            pre_ord_strng += str(element) + " "
        return pre_ord_strng
    
    # adds each element in order of root, left child, and right child
    def pre_order_helper(self, aNode, store):
        '''
        Adds elements into a list in order from the root, left child, 
        and the right child. 
        '''
        # adds each element to list, if aNode is not empty
        if aNode != None:
            store.append(aNode.data)
            self.pre_order_helper(aNode.lChild, store)
            self.pre_order_helper(aNode.rChild, store)
        return store

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        post_ord_lst = self.post_order_helper(aNode, [])
        post_ord_strng = ""

        for element in post_ord_lst:
            post_ord_strng += str(element) + " "
        return post_ord_strng 
    
    # adds each element in order of left child, right child, and root
    def post_order_helper(self, aNode, store):
        '''
        Adds elements into a list in order of left child, right child, 
        and the root. 
        '''
        # adds each element to list, if aNode is not empty
        if aNode != None:
            self.post_order_helper(aNode.lChild, store)
            self.post_order_helper(aNode.rChild, store)
            store.append(aNode.data)
        return store


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()

# python3 ExpressionTree.py < expression.in.txt