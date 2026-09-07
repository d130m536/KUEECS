# Name:
# KUID:
# LAB Session: Fri 8am
# LAB Assignment: Lab 01
# Description:
# This program returns the result of the input binary numbers and
# bitwise operators.
#
# Collaborators/Sources: Me, myself, I, and the Starter.py code
def get_string_arrays(num_arrays):
    valid_operators = {"AND", "OR", "XOR"}
    while True:
        user_input = input("Enter your calculation string seperated by spaces (EX=1 AND 1): ")
        values = user_input.split()
        if len(values) == 1 or len(values) % 2 == 0:
            print("Error: Input length must be an odd number >= 3")
            continue
        cleaned_values = []
        bit_length = None
        valid = True
# Valid Checker
        for val in values:
            if val.isalpha():
                if val.upper() not in valid_operators:
                    print(f"Error: Only valid opporators are (AND, OR, XOR).")
                    valid = False
                    break
                cleaned_values.append(val.upper())
            else:
                if not all(char in "01" for char in val):
                    print(f"Error: Binary numbers must be only 0s and 1s")
                    valid = False
                    break
                if bit_length is None:
                    bit_length = len(val)
                elif len(val) != bit_length:
                    print(f"Error: All binary numbers must be the same length")
                    valid = False
                    break
                cleaned_values.append(val)
        if not valid:
            continue
        values = cleaned_values
        break
    if num_arrays == 1:
        return values
    elif num_arrays == 2:
        list1, list2 = [], []
        for i, val in enumerate(values):
            if i % 2 == 0:
                list1.append(val)
            else:
                list2.append(val)
        return list1, list2
    else:
        raise ValueError("num_arrays must be 1 or 2")

#Your code here:
# In-line comments:
#   For complex code: a brief comment explaining each line
#   For simple code blocks: a brief explanation of the block

def operator(bin_nums, operators = None): # runs operator functions on binary nums

    if operators == None: # if single array, sift for operators and binary nums

        for i in range(2): # loops once, checks length of list --> if 3, return result
                           # if not, loops again after using result from first loop to use in the second

            # if statements used as match/case function, since I don't have latest python update
            if bin_nums[1] == "AND": # check for AND operator
                end_result = AND(bin_nums[0], bin_nums[2]) # perform AND operation
                
            if bin_nums[1] == "OR": # check for OR operator
                end_result = OR(bin_nums[0], bin_nums[2]) # perform OR operation
            
            if bin_nums[1] == "XOR": # check for XOR operator
                end_result = XOR(bin_nums[0], bin_nums[2]) # perform XOR operation

            if len(bin_nums) == 3: # if only three items in list, return result
                return end_result

            bin_nums = bin_nums[3:] # redefine list with last two items

            bin_nums.insert(0, end_result) # insert operation result at front of list to be used in next operation

    for i in range(2): # loops once, checks operator list length --> if 1, return operation result
                       # if not, loops again after using result from first operation to use in the second

        # if statements used as match/case function, since I don't have latest python update
        if operators[0] == "AND": # check for AND operator
            end_result = AND(bin_nums[0], bin_nums[1]) # perform AND operation
            
        if operators[0] == "OR": # check for OR operator
            end_result = OR(bin_nums[0], bin_nums[1]) # perform OR operation
        
        if operators[0] == "XOR": # check for XOR operator
            end_result = XOR(bin_nums[0], bin_nums[1]) # perform XOR operation

        if len(operators) == 1: # if only one operator in list, return operation result
            return end_result

        bin_nums = [bin_nums[-1]] # redefine list with last item

        operators = [operators[-1]] # shorten list to final operator

        bin_nums.insert(0, end_result) # insert operation result at front of list to be used in next operation

def AND(num1, num2): # runs bitwise AND operation
    result = ""
    for i in range(len(num1)):
        if num1[i] == "1" and num2[i] == "1":
            result += "1"
        else:
            result += "0"
    return result

def OR(num1, num2): # runs bitwise OR operation
    result = ""
    for i in range(len(num1)):
        if int(num1[i]) + int(num2[i]) >= 1:
            result += "1"
        else:
            result += "0"
    return result

def XOR(num1, num2): # runs bitwise XOR operation
    result = ""
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            result += "0"
        else:
            result += "1"
    return result

def main():
    # Example usage:
    binary_nums = get_string_arrays(1)
    print("Single array:", binary_nums)
    print(f"Single Array Result: {operator(binary_nums)}\n")

    binary_nums, operators = get_string_arrays(2)
    print("Array 1 (binary numbers):", binary_nums)
    print("Array 2 (operators):", operators)
    print(f"Dual Array Result: {operator(binary_nums, operators)}")

if __name__ == "__main__":
    main()