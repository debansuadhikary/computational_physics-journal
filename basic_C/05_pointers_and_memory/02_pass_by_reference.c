#include <stdio.h>

// Function that receives pointer arguments (memory addresses)
void swap(int *a, int *b) {
    int temp = *a; // Store value at address 'a' into temp
    *a = *b;       // Put value at address 'b' into address 'a'
    *b = temp;     // Put temp into address 'b'
}

// Function that returns multiple results by modifying pointed values
void compute_stats(double x, double y, double *sum, double *product) {
    *sum = x + y;
    *product = x * y;
}

int main(void) {
    printf("Swapping Variables via Pointers\n");
    int x = 10, y = 99;

    printf("Before swap : x = %d, y = %d\n", x, y);
    // Pass the addresses of x and y using '&'
    swap(&x, &y);
    printf("After swap  : x = %d, y = %d (SUCCESSFULLY SWAPPED!)\n\n", x, y);

    printf("Returning Multiple Values via Pointers\n");
    double num1 = 4.0, num2 = 5.0;
    double total_sum, total_prod;

    // Pass addresses where the function should write its answers
    compute_stats(num1, num2, &total_sum, &total_prod);

    printf("Numbers : %.1f and %.1f\n", num1, num2);
    printf("Sum     : %.1f\n", total_sum);
    printf("Product : %.1f\n", total_prod);

    return 0;
}
