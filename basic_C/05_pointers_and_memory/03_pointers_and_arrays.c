#include <stdio.h>

int main(void) {
    int numbers[5] = {10, 20, 30, 40, 50};

    // In C, the array name 'numbers' acts as a pointer to its first element (&numbers[0])
    int *ptr = numbers;

    printf("Array and Pointer Equivalence\n");
    printf("Address of numbers[0] : %p\n", (void *)&numbers[0]);
    printf("Value of 'numbers'    : %p\n\n", (void *)numbers);

    printf("Accessing Array Elements via Pointer Arithmetic\n");
    // *(ptr + i) is exactly equivalent to numbers[i]
    for (int i = 0; i < 5; i++) {
        printf("Index %d -> Value via numbers[%d]: %d | Value via *(ptr + %d): %d | Address: %p\n",
               i, i, numbers[i], i, *(ptr + i), (void *)(ptr + i));
    }

    return 0;
}
