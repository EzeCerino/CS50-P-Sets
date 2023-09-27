#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int n = 0;
    do
    {
        n = get_int("How many numbers: ");
    } while (n < 1);

    int numbers[n];
    
    numbers[0]=1;
    int i=0;
    printf("%i\n", numbers[i]);

    for (i=1;i<n;i++)
    {
        numbers[i] = numbers[i-1]*2;
        printf("%i\n", numbers[i]);
    }
}