#include <stdio.h>
#include <cs50.h>

int collatz(int number);
int counter = 0;
int main(void) {
   int n = get_int("n?: ");
   collatz(n);
   printf("Iterations: %i \n",counter);
}

int collatz(int number){
    printf("%i -> ",number);
    if(number==1)
        return counter;
    else if(number%2==0)
        collatz(number/2);
    else if(number%2>0)
        collatz(3*number + 1);
    counter++;
    return 0;
}