#include <stdio.h>

// Declaring functions before main() lets C know their names, return types, and parameters.
void print_welcome_message(void);
int add_integers(int a, int b);
double calculate_kinetic_energy(double mass, double velocity);

int main(void) {
    // 1. Calling a void function (no return value, no parameters)
    print_welcome_message();

    // 2. Calling a function that takes integers and returns an integer
    int x = 15;
    int y = 25;
    int sum = add_integers(x, y);
    printf("Sum of %d and %d = %d\n", x, y, sum);

    // 3. Calling a function with floating-point calculations
    double m = 2.0;  // 2 kg mass
    double v = 3.0;  // 3 m/s velocity
    double ke = calculate_kinetic_energy(m, v);
    printf("Kinetic Energy (m=%.1f kg, v=%.1f m/s) = %.2f Joules\n", m, v, ke);

    return 0;
}

// Function that performs an action but returns nothing (void)
void print_welcome_message(void) {
    printf("=== Modular Programming in C ===\n");
    printf("Functions keep code organized, clean, and reusable!\n\n");
}

// Function taking two int parameters and returning their sum
int add_integers(int a, int b) {
    return a + b;
}

// Function demonstrating a physical formula: KE = 0.5 * m * v^2
double calculate_kinetic_energy(double mass, double velocity) {
    double energy = 0.5 * mass * (velocity * velocity);
    return energy;
}
