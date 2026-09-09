#include <stdio.h> // use I/O library

int main() { // main function
	int age = 20;		// initialize age
    if (age >= 18) {		// if statement: 18+ -> Adult, else Minor 
        printf("Adult\n");	// output Adult 
    } else {			// otherwise
        printf("Minor\n");	// output minor
    }
    int day = 3;		// initialize day number
    switch (day) {		// switch statement: cases for days of the week
    case 1:			// if day == 1: 
        printf("Monday\n");	// output Monday
        break;			// break out
    case 2:			// if day == 2: 
        printf("Tuesday\n");	// output Tuesday
        break;			// break out
    case 3:			// if day == 3:
        printf("Wednesday\n");	// output Wednesday
        break;			// break out
    default:
        printf("Other day\n");	// default output in case of other/invalid input
    }
    for (int i = 0; i < 5; ++i) { // for loop: runs until break or reaches 5
        printf("for loop\n");  	  // outputs for loop 5 times
    }
    int counter = 0;		// initialize count variable
    while (counter < 3) {	// while loop: ends when counter >= 3
        printf("while loop\n"); // outputs 3 times
        counter++;		// increases counter by 1
    }
    int num = 0;		// initialize number to 0
    counter = 2;		// initialize counter to 2
    do {			// do-while: perform some code then check condition
        printf("do-while loop\n");	// output 1 time
        num++;				// num increases by 1 once
    } while (counter < 2);
    return 0;				// return an int to satisfy the int type main function
}
