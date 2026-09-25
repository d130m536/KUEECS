# Name: Devan Mathis
# KUID: 3217985
# LAB Session (Day/Time): Friday 8am
# LAB Assignment: Lab 4
# Description: 
# Returns the modulus result of 3 numbers:
# the first multipled by the second mod the third
#
# Collaborators/Sources: N/A
#Function to get b, n, and m
#They should all be on the same line
#If you want, you can put commas in between

def get_values():
	i = input("Please enter b, n, and m: ")
	items = i.replace(","," ").split()
	if(len(items) != 3):
		print("Invalid input, try again")
		return get_values()
	return (int(items[0]),int(items[1]),int(items[2]))
#For the output, you can just print the number:
# e.g. print(result)

#Your code here:
def main(): # main function
	b, n, m = get_values() # get input values
	print("Got ", b, ", ", n, ", ", m, sep="") # print values
	print(f"Result: {(b ** n) % m}") # print modulus result b^n mod m
main() # run main function
