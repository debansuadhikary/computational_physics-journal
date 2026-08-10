#include <stdio.h>

int main(void) {
    // A regular integer variable stored at some address in RAM
    int number = 42;

    // A pointer variable that stores the MEMORY ADDRESS of an integer.
    // The '*' in the declaration tells C that 'ptr' is a pointer.
    int *ptr = &number; // & is the address-of operator

    printf("Pointer Fundamentals\n");
    printf("Value of 'number'                     : %d\n", number);
    printf("Memory address of 'number' (&number)  : %p\n", (void *)&number);
    printf("Value stored in pointer 'ptr'         : %p\n", (void *)ptr);

    // DEREFERENCING: Using '*' on an existing pointer gets the value AT that address.
    printf("Value pointed to by 'ptr' (*ptr)      : %d\n\n", *ptr);

    // Modifying the value using the pointer
    printf("Modifying value via pointer (*ptr = 100)...\n");
    *ptr = 100;

    printf("New value of 'number'                 : %d\n", number);
    printf("New value via dereferencing (*ptr)    : %d\n", *ptr);

    return 0;
}
