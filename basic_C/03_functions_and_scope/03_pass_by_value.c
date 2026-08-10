#include <stdio.h>

// Function that attempts to modify its argument
void modify_value(int x) {
    printf("  [Inside Function] Original x received : %d\n", x);
    x = x * 2; // Modify the local copy
    printf("  [Inside Function] Modified x inside   : %d\n", x);
}

// Function that attempts to swap two numbers
void swap_failed(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("  [Inside Swap] Swapped local copies: a = %d, b = %d\n", a, b);
}

int main(void) {
    printf("Pass-by-Value in C\n");
    int number = 10;

    printf("1. Before calling modify_value() : number = %d\n", number);
    modify_value(number);
    printf("   After calling modify_value()  : number = %d (UNCHANGED!)\n\n", number);

    printf("2. Attempting a swap using Pass-by-Value:\n");
    int val1 = 5, val2 = 99;
    printf("   Before swap: val1 = %d, val2 = %d\n", val1, val2);
    
    swap_failed(val1, val2);
    
    printf("   After swap : val1 = %d, val2 = %d (UNCHANGED!)\n", val1, val2);
    printf("\nNote: To modify original variables across functions, C uses POINTERS!\n");

    return 0;
}
