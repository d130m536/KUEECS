#include "isEven.h"
#include "isOdd.h"

#include <stdio.h>

int main() {
	int num;
	printf("Enter an integer: "); // prompt user
	scanf("%d", &num); // receive input
	if (!isEven(num)){ // check if isEven returns w/ no error
		return 0;  // print is even and return
	}
    	isOdd(num); // if not print is odd
	return 0;   // and return
}
