#include <stdio.h>

#define ROWS 3
#define COLS 3

// Function prototype: Function taking a 2D array matrix and displaying it
void print_matrix(int mat[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%4d ", mat[i][j]);
        }
        printf("\n"); // New line after printing each row
    }
}

int main(void) {
    // Declaring and initializing 3x3 matrices
    int matrix_A[ROWS][COLS] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int matrix_B[ROWS][COLS] = {
        {9, 8, 7},
        {6, 5, 4},
        {3, 2, 1}
    };

    int result[ROWS][COLS]; // Matrix to store the sum

    printf("Matrix A\n");
    print_matrix(matrix_A);

    printf("\nMatrix B\n");
    print_matrix(matrix_B);

    // Matrix Addition: C[i][j] = A[i][j] + B[i][j]
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            result[i][j] = matrix_A[i][j] + matrix_B[i][j];
        }
    }

    printf("\nMatrix A + Matrix B\n");
    print_matrix(result);

    return 0;
}
