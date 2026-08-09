#include <stdio.h>

int main(void) {
    printf("1. Basic Counting FOR Loop\n");
    // Syntax: for (initialization; condition; update)
    for (int i = 1; i <= 5; i++) {
        printf("Step %d\n", i);
    }

    printf("\n2. Accumulating a Sum\n");
    int total_sum = 0;
    int limit = 10;

    for (int n = 1; n <= limit; n++) {
        total_sum += n; // Equivalent to: total_sum = total_sum + n
    }
    printf("Sum of numbers from 1 to %d = %d\n", limit, total_sum);

    printf("\n3. Nested FOR Loops (2D Grid / Matrix)\n");
    int rows = 3;
    int cols = 3;

    for (int r = 1; r <= rows; r++) {
        for (int c = 1; c <= cols; c++) {
            printf("(%d,%d) ", r, c);
        }
        printf("\n"); // New line after completing each row
    }

    return 0;
}
