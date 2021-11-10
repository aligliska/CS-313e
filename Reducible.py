#  File: Reducible.py

#  Description: This program inputs a list of words and determines 
#  if each word can be reduced in characters, yet still form a word. 
#  From a list of reducible words, the program outputs the longest words.

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/08/2021

#  Date Last Modified: 7/14/2021

import sys


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    '''
    Checks if a positive integer is prime or not 
    '''
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# makes a next prime number
def make_prime(n):
    '''
    Takes an input integer, returns the next prime number
    '''
    while not is_prime(n):
        n += 1
    return n


# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    '''
    Returns the hash index of a string 
    '''
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    '''
    Creates the stepsize to increment when hashing 
    '''
    return const - hash_word(s,const)


# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    '''
    Inserts a string into a hash table, double hashing if collision
    '''
    idx = hash_word(s, len(hash_table))
    
    # hash location is available
    if hash_table[idx] == "":
        hash_table[idx] = s
        return

    # hash location is occupied; double hashing 
    step = step_size(s, 5)
    for i in range(1,len(hash_table)):
        key = (idx + i*step) % len(hash_table)
        if hash_table[key] == "":
            hash_table[key] = s
            return
   
 
# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    '''
    Finds a string in the hash table, linearly probes if not at index 
    '''
    idx = hash_word(s, len(hash_table))

    # word found at given index
    if hash_table[idx] == s:
        return True

    # word not found at given index
    step = step_size(s, 5)
    key = (idx + step) % len(hash_table)
    while hash_table[key] != "":
        # word found at different index
        if hash_table[key] == s:
            return True
        key = (key + step) % len(hash_table)
    return False 


# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    '''
    Checks if a string can be reduced to "a, i, o"
    '''
    # word is already in the hash_memo
    if find_word(s, hash_memo) == True:
        return True
    # word is not found in hash_table
    elif not find_word(s, hash_table):
        return False 
    # removes one letter from word at a time and checks recursively
    else:
        for i in range(len(s)):
            new_s = s[:i] + s[i+1:]
            if is_reducible(new_s, hash_table, hash_memo):
                insert_word(s,hash_memo) 
                return True 
        return False 


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    '''
    From a list of words, returns a list of words with the longest length
    '''
    longest_words = []
    string_list.sort(key = len, reverse = True)
    longest_length = len(string_list[0])

    for word in string_list:
        # checks for duplicates
        if word not in longest_words:
            if len(word) == longest_length:
                longest_words.append(word)
            else:
                break
    return longest_words


def main():
  # create an empty word_list
    word_list = []

  # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append (line)

  # find length of word_list
    length_list = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
    larger_length_list = make_prime(2 * length_list)

  # populate the hash_list with N blank strings
    hash_list = ["" for i in range(larger_length_list)]

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
    for word in word_list:
        insert_word(word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
    m = make_prime(int(0.2 * length_list))
    
  # populate the hash_memo with M blank strings
  # inserts acceptable last letters for reduced words
    hash_memo = ["" for i in range(m)]
    insert_word("a", hash_memo)
    insert_word("i", hash_memo)
    insert_word("o", hash_memo)

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
    reducible_words = []

    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)

  # find the largest reducible words in reducible_words
    longest_words = get_longest_words(reducible_words)
    sorted(longest_words)

  # print the reducible words in alphabetical order
  # one word per line
    for word in longest_words:
        print(word)

if __name__ == "__main__":
  main()

# python3 Reducible.py < words.txt