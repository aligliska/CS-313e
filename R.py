#  File: TestBinaryTree.py

#  Description: This program further develops on the classes
#  for nodes and trees. The program can check if the binary
#  tree are similar, returns the nodes at a specified level, 
#  gets the height of the binary tree, and counts the number
#  of nodes in the binary tree. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/24/2021

#  Date Last Modified: 8/2/2021

import sys


class Node (object):
    # constructor 
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

class Tree (object):
    # constructor 
    def __init__ (self):
        self.root = None
    
    # inserts data into l/r based on comparison with parent node
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return 
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node 
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node 
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return 

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        self_node = self.root
        pNode = pNode.root
        if self_node == None and pNode == None:
            return True
        return self.similar_helper(self_node, pNode)
    
    # returns a boolean if the two nodes are identical while moving down 
    def similar_helper(self, qNode, pNode):
        '''
        Compares each node's data while traversing through tree
        '''
        if qNode == None and pNode == None:
            return True 
        # compares each value at each node while traversing down 
        elif qNode.data != None and pNode.data != None:
            return qNode.data == pNode.data and \
            self.similar_helper(qNode.lChild, pNode.lChild) and \
            self.similar_helper(qNode.rChild, pNode.rChild)
        else:
            return False 

    # Returns a list of nodes at a given level from left to right
    def get_level (self, level): 
        store_nodes = []
        self_node = self.root 
        if self_node == None:
            return store_nodes
        else:
            self.level_helper(self_node, level, store_nodes)
        return store_nodes
    
    # moves down levels until reaching target level 
    def level_helper(self, qNode, level, store_nodes):
        '''
        Adds each node into a list for a given level
        '''
        if qNode != None:
            if level == 0:
                store_nodes.append(qNode)
                return 
            # moves down levels in both right and left side
            else:
                self.level_helper(qNode.lChild, level - 1, store_nodes)
                self.level_helper(qNode.rChild, level -1, store_nodes)
            return 
        return 

    # Returns the height of the tree
    # should height include root? or root = 0, so height - 1? 
    def get_height (self): 
        self_node = self.root 
        return self.height_helper(self_node)
        
    # returns both heights as a tuple
    def height_helper(self, qNode):
        '''
        Traverses to farthest leaf node and sums number of levels
        '''
        if qNode == None:
            return 0
        # increments count for each level reached
        else:
            left_height = 1 + self.height_helper(qNode.lChild)
            right_height = 1 + self.height_helper(qNode.rChild)
        return max(left_height, right_height)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        self_node = self.root 
        return self.num_helper(self_node)
    
    def num_helper(self, qNode):
        '''
        Traverses through the tree and counts number of nodes
        '''
        if qNode == None:
            return 0
        else:
            return 1 + self.num_helper(qNode.lChild) \
                + self.num_helper(qNode.rChild)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints

    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    tree2 = Tree()
    for i in tree2_input:
        tree2.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints

    tree3 = Tree()
    for i in tree3_input:
        tree3.insert(i)

    # Test your method is_similar()
    print(tree1.is_similar(tree2))
    print(tree2.is_similar(tree3))

    # Print the various levels of two of the trees that are different
    print(tree3.get_level(0))
    print(tree3.get_level(1))
    print(tree3.get_level(2))
    print(tree3.get_level(3))
    print(tree3.get_level(4))
    print(tree3.get_level(5))

    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    print(tree1.num_nodes())
    print(tree3.num_nodes())

if __name__ == "__main__":
    main()

# python3 R.py < bst.in.txt