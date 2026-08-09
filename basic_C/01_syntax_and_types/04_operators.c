#include <stdio.h>

int main(void) {
    int a = 17;
    int b = 5;

    printf("=== Basic Arithmetic Operators ===\n");
    printf("a = %d, b = %d\n\n", a, b);

    printf("Addition       (a + b) : %d\n", a + b);
    printf("Subtraction    (a - b) : %d\n", a - b);
    printf("Multiplication (a * b) : %d\n", a * b);

    // Integer Division: Truncates decimal part because both operands are integers
    printf("Integer Div    (a / b) : %d\n", a / b);

    // Modulo Operator (%): Finds the remainder of integer division
    printf("Modulo         (a %% b) : %d\n", a % b);

    // Type Casting: Converting integers to double before dividing to get exact decimal result
    double exact_div = (double)a / (double)b;
    printf("Float Division (explicit cast) : %.2lf\n", exact_div);

    printf("\n=== Increment and Decrement Operators ===\n");
    int count = 10;
    printf("Original count : %d\n", count);

    count++; // Equivalent to count = count + 1
    printf("After count++  : %d\n", count);

    count--; // Equivalent to count = count - 1
    printf("After count--  : %d\n", count);

    return 0;
}
