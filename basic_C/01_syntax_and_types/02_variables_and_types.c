#include <stdio.h>

int main(void) {
    // 1. Integer type (whole numbers, usually 4 bytes)
    int age = 21;

    // 2. Single-precision floating-point number (approx. 6-7 decimal places)
    float temperature = 36.6f;

    // 3. Double-precision floating-point number (approx. 15-17 decimal places)
    // Preferred in computational physics for higher accuracy.
    double pi = 3.141592653589793;

    // 4. Character type (stores a single ASCII character in single quotes)
    char grade = 'A';

    // Print values using format specifiers:
    // %d  -> integer
    // %f  -> float
    // %lf -> double (long float)
    // %c  -> character
    printf("=== Basic Data Types in C ===\n");
    printf("Integer (age)          : %d\n", age);
    printf("Float (temperature)    : %.1f °C\n", temperature);  // %.1f limits output to 1 decimal place
    printf("Double (pi)            : %.15lf\n", pi);          // %.15lf limits to 15 decimal places
    printf("Character (grade)      : %c\n", grade);

    return 0;
}
