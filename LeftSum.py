#  File: LeftSum.py

#  Description: Get the left sum of the BST

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610


import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***

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
          left_height = 1 + self.height_helper(qNode.lchild)
          right_height = 1 + self.height_helper(qNode.rchild)
      return max(left_height, right_height)
  
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
          # moves down levels in both right and left side
          else:
              if qNode.lchild != None:
                  self.level_helper(qNode.lchild, level - 1, store_nodes)
              if qNode.rchild != None:
                  self.level_helper(qNode.rchild, level -1, store_nodes) 
              return
          return

  # Returns an integer for the left sum of the BST
  def get_left_sum(self):
    num_levels = self.get_height()
    store = []
    for i in range (num_levels):
      store.append(self.get_level(i))
    values = []
    for level in store:
      values.append(level[0].data)
    return sum(values)

# ***There is no reason to change anything below this line***

def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_left_sum())

if __name__ == "__main__":
  main()

#python3 LeftSum.py < R.txt