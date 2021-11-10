#  File: tug_of_war.py

#  Description: Given a list of each student’s body weight as non-zero integers and an integer threshold T, 
#				determine if it is possible for these students to separate into two teams 
#				where the strength difference between the two teams is lower than the threshold.

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


# Input: weight_lst is a list of integers which represent the weight of each student
#		 T is the threshold
# Output: Boolean. True means that it is possible for these students 
#		to separate into two teams where the strength difference 
#		between the two teams is lower than the threshold. 
import sys


# Input: weight_lst is a list of integers which represent the weight of each student
#		 T is the threshold
# Output: Boolean. True means that it is possible for these students 
#		to separate into two teams where the strength difference 
#		between the two teams is lower than the threshold. 
def tugofwar(weight_lst, T):
	teamA, teamB = [], []
	return tug_helper(weight_lst, T, teamA, teamB)
	
def tug_helper(weight_lst, T, teamA, teamB):
	if len(weight_lst) == 0:
		if teamA != [] and teamB != []:
			return abs(sum(teamA) - sum(teamB)) < T 
	else:
		curr_person = weight_lst.pop()
		teamA.append(curr_person)
		if tug_helper(weight_lst, T, teamA, teamB):
			return True
		teamA.pop()
		teamB.append(curr_person)
		if tug_helper(weight_lst, T, teamA, teamB):
			return True
		teamB.pop()
		return False


if __name__ == '__main__':


	# Read input list of weight
	weight_str = sys.stdin.readline().split()
	weight_lst = [ int(x) for x in weight_str ]

	# Read threshold
	T = int(sys.stdin.readline())

	# Output
	result = tugofwar(weight_lst, T)

	print(result)

# python3 tug_of_war.py < R.txt

	

