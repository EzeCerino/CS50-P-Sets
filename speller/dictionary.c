// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26*2;

// Hash table
node *table[N];
//counter for size function
int words_counter;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hash_value = hash(word);
    node* cursor = table[hash_value];
    while(cursor!=NULL)
    {

        if(strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
            //printf("pointer: %p - \n",cursor);
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //assuring that the table is initialized as null pointers
    for(int i=0; i < N; i++) table[i] = NULL;
    words_counter = 0;

    //open file as read only
    FILE *inptr = NULL;
    inptr = fopen(dictionary, "r");
    //check if was able to open it
    if(inptr == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    //copy each word into a new node
       // printf("hola");

    char *tempword = malloc(sizeof(char) * LENGTH);
    if (tempword == NULL)
    {
        fclose(inptr);
        return false;
        free(tempword);
    }

    int hash_value;
    while (fscanf(inptr,"%s",tempword) != EOF)
    {
        hash_value = hash(tempword);
        //create a new node and check for null pointer
        node *newnode = malloc(sizeof(node));
        if (newnode == NULL) return false;

        strcpy(newnode->word,tempword);
        node *temp = table[hash_value];
        table[hash_value] = newnode;
        newnode->next = temp;
        words_counter++;
    }
    fclose(inptr);
    free(tempword);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return words_counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    bool boolean = false;
    for (int i=0; i<N; i++)
    {
        node* cursor = table[i];
        node* temp = cursor;
        while (cursor != NULL) {
            temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    boolean = true;
    }
    return boolean;
}
