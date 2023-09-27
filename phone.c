#include <stdio.h>
#include <cs50.h>

int main(void) {
    string name = get_string("Name: ");
    int age = get_int("age: ");
    long phone_number = get_long("Phone Number: ");

    printf("Name %s\n:", name);
    printf("Age %i\n:", age);
    printf("Phone Number %li\n:", phone_number);
}