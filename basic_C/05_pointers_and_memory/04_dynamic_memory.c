#include <stdio.h>
#include <stdlib.h> // Required for malloc(), calloc(), free()

int main(void) {
    int n = 5;

    printf("Dynamic Memory Allocation (malloc & free)\n");
    printf("Allocating memory on the heap for %d integers...\n", n);

    // malloc allocates raw bytes on the heap.
    // sizeof(int) ensures portable memory sizing across systems.
    int *array = (int *)malloc(n * sizeof(int));

    // ALWAYS check if malloc returned NULL (meaning allocation failed due to out-of-memory)
    if (array == NULL) {
        printf("Error: Memory allocation failed!\n");
        return 1; // Exit program with failure code
    }

    // Populate and use the dynamically allocated array
    for (int i = 0; i < n; i++) {
        array[i] = (i + 1) * 10;
    }

    printf("Dynamically allocated array contents:\n");
    for (int i = 0; i < n; i++) {
        printf("array[%d] = %d\n", i, array[i]);
    }

    // ALWAYS free dynamically allocated memory when finished to prevent memory leaks!
    free(array);

    // Set pointer to NULL after freeing so it cannot be accidentally used again (dangling pointer)
    array = NULL;

    printf("\nMemory freed successfully!\n");

    return 0;
}
