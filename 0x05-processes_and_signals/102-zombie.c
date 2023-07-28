#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * infinite_while - function to be called after child process
 * is created
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main function to create the required number of zombie
 * processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
		{
			printf("Zombie process created, PID: %u\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
