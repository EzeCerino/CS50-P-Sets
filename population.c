#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //preguntar por el numero incial de llamas
    long llamas_init;
    do
    {
        llamas_init = get_long("How many llamas do you have?: ");
    } while (llamas_init < 0);

    //preguntar por el objetivo de llamas
    long llamas_goal;
    do
    {
        llamas_goal = get_long("How many llamas do you want?: ");
    } while (llamas_goal < llamas_init);

    //cuantos años pasan hasta que la cantidad de llamas llega al objetivo
    // n/3 nacieron
    // n/4 murieron

    long llamas_actual = llamas_init;
    int years = 0;
    while(llamas_actual <= llamas_goal) {
        llamas_actual = llamas_actual + llamas_actual/3 - llamas_actual/4;
        //printf("%li\n",llamas_actual);
        years ++;
    }
    printf("the number of years to get %li llamas is %i years",llamas_actual, years);
}