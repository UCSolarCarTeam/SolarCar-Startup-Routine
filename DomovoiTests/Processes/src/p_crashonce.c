#include <stdio.h>
#include <stdlib.h>

#define CRASHFILE "crash_file.txt"
#define NO_CRASH 1

int main (void)
{
	int chk; //Check value of crash file. If 0, program will write 1 to crash_file.txt and crash. If 1, program will run to completion.
	FILE *fp = fopen(CRASHFILE, "r");
	if (fp == NULL)
	{
		fprintf (stderr, "Unable to open %s. Test results are invalid.\n", CRASHFILE);
		exit(1);
	}
	if (!fscanf(fp, "%d", &chk))
	{
		fprintf (stderr, "Unable to read check value. Test results are invalid.\n");
		exit(1);
	}
	
	fclose(fp);
	
	if(chk == 0)
	{
		fp = fopen(CRASHFILE, "w");
		fprintf (fp, "%d", NO_CRASH);
		fclose(fp);
		exit(1);
	}

	return 0;
}
	

	

