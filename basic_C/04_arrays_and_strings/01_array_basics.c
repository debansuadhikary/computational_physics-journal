#include <stdio.h>

int main(void) {
    // 1. Declaring and initializing a 1D array of fixed size (5 elements)
    // Indices in C are 0-based: elements are stored at index 0, 1, 2, 3, 4
    double temperatures[5] = {22.5, 24.0, 19.8, 25.2, 21.1};

    printf("1D Array Basics\n");
    printf("First element  [index 0] : %.1f °C\n", temperatures[0]);
    printf("Third element  [index 2] : %.1f °C\n", temperatures[2]);
    printf("Last element   [index 4] : %.1f °C\n\n", temperatures[4]);

    // Modifying an element
    temperatures[2] = 20.5;
    printf("Updated element [index 2]: %.1f °C\n\n", temperatures[2]);

    // 2. Traversing an array using a for loop to calculate the average
    int num_elements = 5;
    double sum = 0.0;

    printf("Reading all elements using a loop:\n");
    for (int i = 0; i < num_elements; i++) {
        printf("Day %d temperature: %.1f °C\n", i + 1, temperatures[i]);
        sum += temperatures[i];
    }

    double average = sum / num_elements;
    printf("\nTotal Sum : %.2f °C\n", sum);
    printf("Average   : %.2f °C\n", average);

    return 0;
}
