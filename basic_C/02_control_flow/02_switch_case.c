#include <stdio.h>

int main(void) {
    char operator = '*';
    double num1 = 12.0;
    double num2 = 4.0;

    printf("=== Simple Calculator Using Switch-Case ===\n");
    printf("Expression: %.2lf %c %.2lf\n", num1, operator, num2);

    // The switch statement evaluates the variable inside parentheses.
    switch (operator) {
        case '+':
            printf("Result: %.2lf\n", num1 + num2);
            break; // 'break' exits the switch block immediately.

        case '-':
            printf("Result: %.2lf\n", num1 - num2);
            break;

        case '*':
            printf("Result: %.2lf\n", num1 * num2);
            break;

        case '/':
            if (num2 != 0.0) {
                printf("Result: %.2lf\n", num1 / num2);
            } else {
                printf("Error: Division by zero is not allowed.\n");
            }
            break;

        // Default block executes if no case matches
        default:
            printf("Error: Invalid operator '%c'\n", operator);
            break;
    }

    return 0;
}
