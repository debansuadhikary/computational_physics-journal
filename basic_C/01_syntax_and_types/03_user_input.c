#include <stdio.h>

int main(void) {
    int student_id;
    double score;
    char letter_grade;

    printf("=== Interactive Input Demo ===\n");

    // Prompt for integer input
    printf("Enter your Student ID (integer): ");
    // scanf() reads formatted input from the keyboard.
    // The '&' operator gives the memory location of the variable so scanf can write to it.
    scanf("%d", &student_id);

    // Prompt for double input
    printf("Enter your test score (e.g. 88.5): ");
    scanf("%lf", &score);

    // Prompt for char input
    printf("Enter your grade letter (single character): ");
    // Note: The space before %c tells scanf to ignore any leftover newline/whitespace characters.
    scanf(" %c", &letter_grade);

    printf("\n--- Summary of Input Data ---\n");
    printf("Student ID : %d\n", student_id);
    printf("Score      : %.2lf\n", score);
    printf("Grade      : %c\n", letter_grade);

    return 0;
}
