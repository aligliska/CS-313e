'''
UniqChar
'''
def unique(n, alphabet):
    num_letters = len(alphabet)
    lst, strng = [], ""
    unique_helper(n, alphabet, num_letters, lst, strng)
    
    return lst
  
def unique_helper(n, alphabet, num_letters, lst, strng):
    if n == 0:
        lst.append(strng)

    for i in range(num_letters):
        if alphabet[i] in strng:
            continue
        else:
            temp_strng = strng + alphabet[i] 
            unique_helper(n-1, alphabet, num_letters, lst, temp_strng)

'''
Balancing Pairs
'''
def balancingPairs(strng):
    '''
    input type: String
    return type: Int
    '''

    right_parantheses = 0
    left_paranthesis = 0
    for char in strng:
        if char == "(":
            right_parantheses += 1
        else:
            left_paranthesis += 1
    
    return len(strng) - 2*min(right_parantheses, left_paranthesis)

'''
Balancing Pairs 2
'''
def balancingPairs(strng):
    '''
    input type: String
    return type: Int
    '''
    store = []
    first_char = strng[0]

    for char in strng:
        if char == first_char or len(store) == 0:
            store.append(char)
        else:
            store.pop()
    return len(store)

'''
Coin Change
'''
import sys
def canMakeChange(target_amount, coin_values, coin_amount, i):
    num_unique_coins = len(coin_values)

    for i in range(i, num_unique_coins):
        # met target amount 
        if target_amount == 0:
            return True
        # ran out of current coin, move to next coins
        if coin_amount[i] == 0:
            continue
        # current coin equals target amount
        if coin_values[i] == target_amount:
            return True
        # coin value too large to use 
        elif coin_values[i] > target_amount:
            continue
        # try to use current coin
        elif coin_values[i] < target_amount: 
            coin_amount[i] -= 1
            if canMakeChange(target_amount-coin_values[i], coin_values, coin_amount, i):
                return True
            # backtracking if cannot use current coin 
            coin_amount[i] += 1     
            
    return False  

def main():
    f = sys.stdin
    num_coins, target_amount = [int(x.strip()) for x in f.readline().split()]
    coin_values = []
    coin_amount = []

    for i in range(num_coins):
        coin_val, coin_amt = [int(x.strip()) for x in f.readline().split()]
        coin_values.append(coin_val)
        coin_amount.append(coin_amt)
    coin_combo = canMakeChange(target_amount, coin_values, coin_amount, i=0)
    
    print(coin_combo)

if __name__ == "__main__":
    main()

'''
Stack Class layout
'''
class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len(self.stack))

'''
Queue Class Layout
'''
class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

'''
Single Linked List
'''
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
    def __init__ (self):
        self.first = None

    def insert_first (self, data):
        new_link = Link (data)

        new_link.next = self.first
        self.first = new_link

    def insert_last (self, data):
        new_link = Link (data)

        current = self.first
        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link
