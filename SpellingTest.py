#  File: SpellingTest.py

#  Description: Determine whether a given string can be spelled using a combination of smaller strings.

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

def spelling_test(s, l):
    store = []
    idx = 0
    all_combo = spell_helper(l, store, idx)
    if s in store:
        return True
    else:
        return False
    
def spell_helper(l, store, idx):
    high = len(l)
    if idx == high:
        strng = ''
        for chars in l:
            strng += chars
            if strng not in store:
                store.append(strng)
    else:
        for i in range(idx, high):
            l[idx], l[i] = l[i], l[idx]
            spell_helper(l, store, idx + 1)
            l[idx], l[i] = l[i], l[idx]  

def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))

if __name__ == "__main__":
    main()

# python3 SpellingTest.py < R.txt