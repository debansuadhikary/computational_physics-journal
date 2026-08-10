#include <stdio.h>

// GLOBAL VARIABLE: Declared outside all functions.
// Accessible from anywhere in this file. (Use sparingly in good C practice!)
int global_counter = 100;

void demonstrate_local_scope(void) {
    // LOCAL VARIABLE: Only exists inside this function block.
    int local_val = 50;

    printf("[Inside Function] Local variable  : %d\n", local_val);
    printf("[Inside Function] Global variable : %d\n", global_counter);

    // Modifying global variable inside a function
    global_counter += 10;
}

int main(void) {
    printf("=== Variable Scope Demonstration ===\n");
    printf("[In main] Initial Global counter : %d\n\n", global_counter);

    demonstrate_local_scope();

    printf("\n[In main] Global counter after function call: %d\n", global_counter);

    // Trying to access 'local_val' here would cause a compilation ERROR:
    // printf("%d", local_val); // Error: 'local_val' undeclared here

    printf("\n=== Variable Shadowing Example ===\n");
    int global_counter = 5; // Local variable with the SAME NAME as the global one!

    // The local variable "shadows" (overrides) the global variable within this scope.
    printf("[In main] Shadowed local 'global_counter': %d\n", global_counter);

    return 0;
}
