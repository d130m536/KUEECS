# Name: Devan Mathis
# KUID: 3217985
# Lab session: Friday 8am
# Description:
# Computes the transitive closure of a zero-one matrix using Boolean matrix operations.
# Collaborators:
# Outside sources: N/A
#This function is similar to Lab 3, but now it will keep running until the user inputs a square matrix
def get_square_matrix(ints=False):
    """
    Takes a square matrix of numbers from the user. Each row can be
    separated by commas and/or spaces. Automatically ends after the last row.
    If ints=False, the function returns a matrix of strings.
    If ints=True, they will be cast to int instead
    """
    print("Enter your matrix:")
    matrix = []

    x = input()
    #If blank line, try again
    if not x.strip():
        return get_square_matrix(ints=ints)
    items = x.replace(",", " ").split()
    length = len(items)
    matrix = []

    #Save the first row
    if not ints:
        matrix.append(items)
    else:
        try:
            row = [int(entry) for entry in items]
            matrix.append(row)
        except ValueError:
            print("Error: all entries must be numbers! Try again:")
            #If first row is bad, try again
            return get_square_matrix(ints=ints)
        
    #Get the rest of the rows
    while True:
        x = input()
        items = x.replace(",", " ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
            continue # re-try the line
        if not ints:
            matrix.append(items)
        else:
            try:
                row = [int(entry) for entry in items]
                matrix.append(row)
            except ValueError:
                print("Error: all entries must be numbers! Try again:")
                continue # re-try the line
        #Check if matrix has been completed (is square)
        if len(matrix) == length:
            return matrix

#Manditory helper function to print a 2-D matrix
def print_matrix(M1, M2):
    print("Algorithm 1, Transitive Closure")
    for row in M1:
        for item in row:
            print(item, end=" ")
        print()
    print("Algorithm 2, Warshall Algorithm")
    for row in M2:
        for item in row:
            print(item, end=" ")
        print()
# ----------------- YOUR ADDED CODE BELOW -----------------
def boolean_product(A, B):
    n = len(A) # rows of A
    result = [[0] * n for _ in range(n)] # create result matrix of nxn 0s
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i][k] == 1 and B[k][j] == 1:
                    result[i][j] = 1
                    break
    return result

def transitive_closure(matrix_r):
    n = len(matrix_r)
    A = [row[:] for row in matrix_r] # A:=matrix_r (copy)
    B = [row[:] for row in matrix_r] # B:=A (copy)
    for i in range(2, n + 1): # for i := 2 to n
        A = boolean_product(A, matrix_r)
        for row in range(n):
            for col in range(n):
                B[row][col] = B[row][col] | A[row][col] # B = B v A

def warshall(matrix_r):
    n = len(matrix_r)
    W = [row[:] for row in matrix_r] # W:=matrix_r (copy)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = W[i][j] | (W[i][j] & W[k][j])
    return W
    

def main():
    matrix = get_square_matrix(ints=True) #use this for both algorithms
    t_closure = transitive_closure(matrix)
    w_closure = warshall(matrix)
    print_matrix(t_closure, w_closure)

if __name__ == "__main__":
    main()
