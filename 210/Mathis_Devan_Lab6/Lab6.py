# Name: Devan Mathis
# KUID: 3217985
# LAB Session (Day/Time): Friday 8am
# LAB Assignment: Lab 6
# Description: Program uses the binomial theorem to output
#              the calculation of each binomial coefficient
#              from terminal input
#
# Collaborators/Sources: N/A
import sys
def get_input(mode):
    """
    Reads the (x+y)^n expression from command line arguments if provided,
    otherwise prompts the user. Strips all whitespace.
    mode == 1: returns the full cleaned expression as a string, e.g. "(x+y)^4"
    mode == 0: returns only the exponent n as an int, e.g. 4
    """
    if len(sys.argv) > 1:
        raw = " ".join(sys.argv[1:])
    else:
        raw = input("Enter expression (e.g. (x+y)^4): ")
    # Remove all whitespace
    cleaned = "".join(raw.split())
    if mode == 0:
        # Keep only digit characters, then convert to int
        digits = "".join(ch for ch in cleaned if ch.isdigit())
        return int(digits)
    return cleaned

def factorial(num):
    if num < 1:
        return 1
    return num * factorial(num - 1)

def binomial_print(n):
    print(f"x^{n}", end=' + ')
    for i in range(1,n):
        print(f"{int((factorial(n)/(factorial(i) * (factorial(n-i)))))}x^{n-i}y^{i}", end=" + ")
    print(f"y^{n}")
    

def main():
    # full_expr = get_input(1) # e.g. "(x+y)^4" (string)
    # print(full_expr) # type string
    n = get_input(0) # e.g. 4 (int)
    print(n) # type int
    binomial_print(n)

main()