// Simulate genetic inheritance of blood type

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    // TODO: Allocate memory for new person
    person *new_p = malloc(sizeof(person));

    // If memory allocation fails, return NULL
    if (new_p == NULL)
    {
        return NULL;
    }

    // If there are still generations left to create
    if (generations > 1)
    {
        // Create two new parents for current person by recursively calling create_family
        person *parent0 = create_family(generations - 1);
        person *parent1 = create_family(generations - 1);

        // Check if memory allocation for parents failed
        if (parent0 == NULL || parent1 == NULL)
        {
            // Free the allocated memory for the new person
            free(new_p);
            return NULL;
        }

        // TODO: Set parent pointers for current person
        new_p->parents[0] = parent0;
        new_p->parents[1] = parent1;


        // TODO: Randomly assign current person's alleles based on the alleles of their parents
        int r = rand() % 2;
        new_p->alleles[0] = parent0->alleles[r];
        r = rand() % 2;
        new_p->alleles[1] = parent1->alleles[r];
    }

    // If there are no generations left to create
    else
    {
        // TODO: Set parent pointers to NULL
        new_p->parents[0] = NULL;
        new_p->parents[1] = NULL;

        // TODO: Randomly assign alleles
        new_p->alleles[0] = random_allele();
        new_p->alleles[1] = random_allele();
    }

    // TODO: Return newly created person
    return new_p;
}

// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    // TODO: Handle base case
   // printf("%p\n",p);
    if (p==NULL)
    {
       // printf("p es nulo\n");
        return;

    }
    // TODO: Free parents recursively
    else
    {      // printf("en el else\n");
        free_family(p->parents[0]);
        free_family(p->parents[1]);
    }
    // TODO: Free child
    free(p);
    //printf("afuera del if\n");
}

// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }

    // Print parents of current generation
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Randomly chooses a blood type allele.
char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
