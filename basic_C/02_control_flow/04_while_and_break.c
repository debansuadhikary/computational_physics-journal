#include <stdio.h>

int main(void) {
    printf("1. Standard WHILE Loop\n");
    int countdown = 5;

    // Executes as long as the condition evaluates to true
    while (countdown > 0) {
        printf("T-minus %d seconds...\n", countdown);
        countdown--; // Decrement step
    }
    printf("Liftoff!\n");

    printf("\n2. DO-WHILE Loop\n");
    int number = 10;

    // A do-while loop ALWAYS runs at least once before checking the condition
    do {
        printf("This line runs at least once (number = %d)\n", number);
        number++;
    } while (number < 5);

    printf("\n3. BREAK and CONTINUE Control Statements\n");
    printf("Printing odd numbers up to 10, stopping if we hit 7:\n");

    for (int i = 1; i <= 10; i++) {
        // 'continue' skips the rest of the loop body for even numbers
        if (i % 2 == 0) {
            continue;
        }

        // 'break' terminates the entire loop when i reaches 7
        if (i == 7) {
            printf("Hit 7! Exiting loop early with 'break'.\n");
            break;
        }

        printf("Odd number: %d\n", i);
    }

    return 0;
}
