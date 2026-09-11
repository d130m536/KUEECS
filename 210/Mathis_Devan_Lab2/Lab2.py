# Name: Devan Mathis
# KUID: 3217985
# LAB Session: Fri 8am
# LAB Assignment: Lab 02
# Description:
# This program returns whether the input mapping
# describes a function, and if it is one-to-one and/or onto.
# Collaborators/Sources: Myself and Lab_2_Starter.py

def get_mapping_pairs() -> str:
	x = input("Enter your mapping pairs: ")
	items = x.replace("(","").replace(" ","").strip(")").split(")")
	pairs = []
	for item in items:
		pairs.append(item.split(","))
	return pairs

# Your Code Here
pair_list = get_mapping_pairs() # get 2D list

one_to_one = True # set one_to_one to True, change later if False
copy_list = [] # copies list to find duplicates while looping
num_set = [str(num) for num in range(0, 4)] # numeric mapping

for i in range(len(pair_list)): # loop through pair_list
	for j in range(len(pair_list[i])): # loop through individual mappings
		if pair_list[i][j] in copy_list: # checks for duplicates w/ copy_list
			one_to_one = False
		if pair_list[i][j] in num_set: # checks if num present in mapping
			num_set.remove(pair_list[i][j]) # if so, removes it from num_list
		copy_list.append(pair_list[i][j]) # append element to copy_list to be checked

if len(num_set) != 0: # all nums must be present in mapping for len(num_set) == 0
	print("not a function") # otherwise, not a function
	exit() # exit program 

print("function", end=", ")
# Since len(mapping) and len(num_set) both == 4, the function has to be both one-to-one and onto, or neither
print("one-to-one, onto" if one_to_one else "not one-to-one, not onto")
