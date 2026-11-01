
# Name: Devan Mathis
# KUID: 3217985
# LAB Session (Day/Time): Friday 8am
# LAB Assignment: Lab 07
# Description: A program that produces the next permutation (in lexicographic order)
#              of a user provided number.
#
#
# Collaborators/Sources: N/A; all code written by me (besides the starter.py)
#Function converts a valid user input into a list of ints
#Does not allow the user to input repeated digits or anything that is not a number
def get_input():
    while True:
        num_str = input("Enter a number with no repeated digits: ")

        #Check that all characters are digits
        if not num_str.isdigit():
            print("Input must be a number.")
            continue
        #Check for repeated digits
        if len(set(num_str)) != len(num_str):
            print("Number must not have repeated digits.")
            continue
        #Convert to list of integers
        digits = [int(ch) for ch in num_str]
        # '''
        #Check if it's the last permutation
        if all(digits[i] >= digits[i+1] for i in range(len(digits)-1)):
            print("Input is the last permutation, no next permutation exists.")
            continue
        # '''
        return digits # only returns once input is valid

def next_permutation(nums):
    # NOTE: the variable index variable names come from the Ch, 6 notes on pg. 50
    result = nums[:]
    j = len(result) - 2 # penultimate digit's index. nums:= [..., n-1 = j = len(n)-2, n = len(n)-1] 
    while (j != 0):
        if (result[j] < result[j+1]): # check for digit on left that < digit on right
            # result.append(f"j := digit: {nums[j]}, index: {j}") 
            # nums[j] := furthest right digit that < digit on its right
            break
        j -= 1 # decrement j by 1: move our focus to the next digit on the left
    ''' Recap: nums[j] is the first digit < (less than) the digit on its right '''

    k = len(result) - 1 # final digit's index. nums:= [..., n-1 = len(n)-2, n = k = len(n)-1] 

    while (k != 0):
        if (result[k] > result[j]): # check for digit on right of and > nums[j]
            # result.append(f"k := digit: {nums[k]}, index: {k}")
            # nums[j] := furthest right digit that > nums[j] and on its right
            break
        k -= 1 # decrement k by 1: move our focus to the next digit on the left
    ''' Recap: nums[k] is the first digit to the right of and > (greater than) nums[j] '''

    a_j = result[j]     # a subscript j: holds value of nums[j]
    result[j] = result[k] # replace nums[j] w/ nums[k] value
    result[k] = a_j     # replace nums[k] w/ a_j (old nums[j]) value
    ''' Recap: Switched digits at j and k indices '''

    r = len(result) - 1 # final digit's index. nums:= [..., n-1 = len(n)-2, n = r = len(n)-1] 
    s = j + 1         # index to the right of j

    while (r > s):
        a_r = result[r]     # a subscript r: holds value of nums[r] 
        result[r] = result[s] # replace nums[r] w/ nums[s] value
        result[s] = a_r     # replace nums[s] w/ a_r (old nums[r]) value
        r -= 1            # decrement r by 1: shift focus to left digit
        s += 1            # increment s by 1: shift focus to right digit
    ''' Recap: Sort digits after j index in increasing order '''

    return "".join([str(digit) for digit in result])

# prints given list as a string
def print_list(given): 
    print("".join([str(_) for _ in given]))

def main():
    #Input Example
    num_list = get_input()
    print_list(num_list)
    print_list(next_permutation(num_list))

if __name__ == "__main__":
    main()