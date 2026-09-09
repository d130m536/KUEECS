#include "isEven.h"

#include <stdio.h>

int isEven(int num)
{
	if (num % 2 == 0){
		 printf("%d is even.\n", num);
		 return 0; // num was even
	}
	return 1; // num was not even
}
