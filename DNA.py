#  File: DNA.py

#  Description: This program DNA sequences and compares pairs of strands.
#   The program returns the longest common sequence if possible. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Partner Name: Maxwell Kretschmer

#  Partner UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6/3/21

#  Date Last Modified: 6/7/21

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.
import sys

def len_sort(lst): 
    final_matches = sorted(lst, idx=len)
    return final_matches

def longest_subsequence (s1, s2):
  s1, s2, = s1.upper().strip("\n"), s2.upper().strip("\n")
  current_strand = []
  matches = []
  
  # matches = all common pairs
  for i in range(len(s1) - 1):
    j = i + 1
    _isExpanding = True
    #SUCCESS
    while _isExpanding == True:
      
      if s1[i:j] in s2:
        current_strand = s1[i:j]
        j += 1
        if j > len(s1):
          matches.append(current_strand)
          _isExpanding = False

      elif s1[i:j] not in s2 and len(s1[i:j]) > 2:
        matches.append(current_strand)
        _isExpanding = False
      
      else:
        _isExpanding = False
  
  #sort matches in Len order
  final_matches = len_sort(matches)
  
  #select all matches with the highest len
  if len(final_matches) >= 1:
    longest = final_matches[-1]
    longestLen = len(longest)
    temporaryPairLst = []
    longestPairLst = []
    for n in range(len(final_matches)-1, -1, -1):
      if len(final_matches[n]) >= longestLen :
        temporaryPairLst.append(final_matches[n])
    for i in temporaryPairLst:
        if i not in longestPairLst:
            longestPairLst.append(i)
    return longestPairLst
  else:
    return list([-1])

#python DNA.py < dna.in

def main():
  # read the data
  inList = sys.stdin.readlines()
  
  num_pairs = inList[0]
  del inList[0]
  # for each pair
  for i in range(1, len(inList), 2):
    # call longest_subsequence
    s1 = inList[i-1]
    s2 = inList[i]
    outList = list(longest_subsequence(s1, s2))
    outList.sort()
    # write out result(s)
    if -1 in outList:
      print("No Common Sequence Found")
      print()
    else:
      for pair in outList:
        print(pair)
      print()

if __name__ == "__main__":
  main()
