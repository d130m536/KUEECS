# Name: Devan Mathis
# KUID: 3217985
# LAB Session (Day/Time): Friday 8:00am
# LAB Assignment: Lab 3
# Description: 
# This program takes the input of two binary matrices and
# outputs their boolean product.
#
# Collaborators/Sources: None
# Note: if you are working in python, you are
# REQUIRED to call this function to get your
# input, so all assignments are consistant
# Returns a matrix in standard matrix notation:
# M[x][y] is row x, (top to bottom, starting at 0)
# and column y (left to right, starting at 0)
# for example, a 3x3 matrix is
# |(0,0) (0,1) (0,2)|
# |(1,0) (1,1) (1,2)|
# |(2,0) (2,1) (2,2)|
def get_matrix(ints=False):
    """
    Takes a matrix of numbers from the user. Each row can be
    separated by commas and/or spaces. A blank line ends the input.
    If ints=False, the function returns a matrix of strings.
    If ints=True, they will be cast to int instead
    """
    print("Enter your matrix, with a blank line to end:")
    x = input()
    items = x.replace(","," ").split()
    length = len(items)
    matrix = []
    while(x.strip()):
        items = x.replace(","," ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
            return get_matrix(ints)
        if not ints:
            matrix.append(items)
        else:
            row = []
            for entry in items:
                row.append(int(entry))
            matrix.append(row)
        x = input()
    return matrix
# OPTIONAL: Helper function to print a 2-D matrix
def print_matrix(m):
    for row in m:
        for item in row:
            print(item, end=" ")
        print()

def product(m1, m2):
	result = []
	# take num in first row, then multiply by first num of each row
	for i in range(len(m1)):
		op = 0 # OR operation of current row's column, reset for each row
		for j in range(len(m1[i])):
			op = op | (m1[i][j] & m2[j][i]) # op ORs column products
		result.append(op)
	return result

def main():
	m = get_matrix(True) # matrix 1
	k = get_matrix(True) # matrix 2
	print(m)
	print(k)
	print("Got: ")
	print_matrix(m)
	print_matrix(k)	
	print(product(m,k)) # currently prints top row of 2x3 3x2 example
	
main()
