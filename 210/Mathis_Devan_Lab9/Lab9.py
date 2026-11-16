# Name: Devan Mathis
# KUID: 3217985
# Lab session: Friday 8am
# Lab #9
# Description: Program that determines the connectivity of a user-provided undirected graph
#
# Collaborators:
# Outside sources:
#This function is similar to Lab 3, but now it will keep running until the user
#inputs a square matrix
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
        
#Helper function to print a 2-D matrix
def print_matrix(m):
    n = len(m)
    # Create labels (a, b, c, ...)
    labels = [chr(ord('a') + i) for i in range(n)]

    # Print top header row
    print(" ", end="") # space for corner
    for label in labels:
        print(label, end=" ")
    print()

    # Print each row with its corresponding label
    for i, row in enumerate(m):
        print(labels[i], end=" ") # row label
        for item in row:
            print(item, end=" ")
        print()

def connected(matrix):
    n = len(matrix)
    visited = set()
    stack = [0]  # start depth-first search at first vertex

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        for i in range(n):
            if matrix[vertex][i] == 1 and i not in visited:
                stack.append(i) # add to stack to explore later

    return len(visited) == n


def main():
    matrix = get_square_matrix(ints=True)
    print("connected" if connected(matrix) else "not connected")


if __name__ == "__main__":
    main()