#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define Nparticles 11
#define Nsteps 11

void brownian(float vector[Nsteps])
{

	int j, random_value;

	for(j = 0; j < Nsteps; j++)
	{
		random_value = rand()%2;
		if(random_value == 0)
		{
			vector[j+1] = vector[j] - 0.1;
		}else
		{
			vector[j+1] = vector[j] + 0.1;
		}
	}

}

void zeros(float vector[Nsteps])
{
	int j;

	for(j = 0; j < Nsteps; j++)
	{
		vector[j] = 1;
	}
}

int main()
{
	srand(time(NULL));

	int i, j;
	float vector[Nsteps];
	
	char *filename = "test.txt";
	FILE *fp = fopen(filename, "w");


	

	//Loop of i-particle
	for(i = 0; i < Nparticles; i++)
	{
		zeros(vector);
		brownian(vector);
		
		for(j = 0; j < Nsteps; j++)
		{
			fprintf(fp, "%f ",vector[j]);			
		}
		fprintf(fp,"\n");

	}

	
	fclose(fp);


	return 0;
}