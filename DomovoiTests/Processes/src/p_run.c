#include <stdio.h>


int main (void)
{
	char c = '\0';
	printf("To exit this program, press q\n");
	while (1)
	{
		scanf("%c", &c);
		if (c == 'q'){
			break;
		}
	}

	return 0;
}
