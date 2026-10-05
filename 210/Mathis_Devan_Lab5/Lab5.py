# Name: Devan Mathis
# KUID: 3217985
# LAB Session (Day/Time): Friday 8am
# LAB Assignment: Lab 5
# Description: a program that takes an unordered set as input
# and recursively merge sorts it to output an ordered set
#
#
# Collaborators/Sources: Used Claude.ai only to bugfix, all lines of
#                        code (besides starter.py) were written by me, Devan Mathis
import re
def get_input_list(prompt="Enter numbers (use spaces and/or commas): ") -> list[int]: 
    user_input = input(prompt)
    # Split on commas or spaces (one or more of them)
    tokens = re.split(r"[,\s]+", user_input.strip())
    # Convert to integers, ignoring empty strings
    return [int(t) for t in tokens if t]
# Your Code Here
def floor_value(num): # floor function for splitting set
    return int((num / 2) // 1) # int(num // 1) -> int(float) -> int

def sort_lists(list_1, list_2): # sorts list simultaneously
    i = j = 0
    result = []

    # while loop ends when i or j reaches the end of their corresponding list
    while (i < len(list_1) and j < len(list_2)): 
        if list_1[i] < list_2[j]:
            result.append(list_1[i])
            i += 1
            continue
        result.append(list_2[j])
        j += 1

    # adds any leftover numbers from either list to result if a list finished before the other
    result.extend(list_1[i:]) 
    result.extend(list_2[j:]) 
    return result

def merge(set_list):
    length = len(set_list)
    if length > 1:
        l1 = set_list[:(floor_value(length))] # get first half, ex length=5: 2 -> [0,1]
        l2 = set_list[(floor_value(length)):] # get second half, ex length=5: 2 -> [2,3,4]
        return sort_lists(merge(l1), merge(l2))
    return set_list

def main():
    L1 = get_input_list()
    print(f"\nInput: {L1}")
    print(f"Ouput: {merge(L1)}\n")

main()