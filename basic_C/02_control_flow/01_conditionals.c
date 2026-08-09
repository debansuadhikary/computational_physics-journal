#include <stdio.h>

int main(void) {
    int score = 85;

    printf("Basic IF / ELSE IF / ELSE Statements\n");
    printf("Student Score: %d\n", score);

    // Single conditional checks
    if (score >= 90) {
        printf("Grade: A (Excellent)\n");
    } else if (score >= 80) {
        printf("Grade: B (Good)\n");
    } else if (score >= 70) {
        printf("Grade: C (Satisfactory)\n");
    } else if (score >= 60) {
        printf("Grade: D (Pass)\n");
    } else {
        printf("Grade: F (Fail)\n");
    }

    printf("\n=== Logical Operators (&& = AND, || = OR, ! = NOT) ===\n");
    int age = 20;
    int has_id = 1; // 1 represents True in C, 0 represents False

    // AND operator (&&) requires BOTH conditions to be true
    if (age >= 18 && has_id == 1) {
        printf("Access Granted: Age is 18+ AND valid ID present.\n");
    } else {
        printf("Access Denied.\n");
    }

    // OR operator (||) requires AT LEAST ONE condition to be true
    int is_weekend = 0;
    int is_holiday = 1;

    if (is_weekend || is_holiday) {
        printf("No classes today! (It is either a weekend or a holiday)\n");
    }

    return 0;
}
