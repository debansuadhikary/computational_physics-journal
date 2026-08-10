#include <stdio.h>

int main(void) {
    // In C, strings are character arrays terminated by a special null character '\0'.
    // "Physics" has 7 letters, so the array size must be at least 8 to fit '\0'.
    char subject[] = "Physics";

    printf("C Strings Basics\n");
    printf("String content : %s\n", subject);

    printf("Displaying character-by-character with ASCII codes:\n");
    for (int i = 0; subject[i] != '\0'; i++) {
        printf("  Index %d: '%c' (ASCII %d)\n", i, subject[i], subject[i]);
    }

    printf("\nString Input with fgets()\n");
    char name[50]; // Buffer to store up to 49 characters + '\0'

    printf("Enter your name: ");
    // fgets(buffer, max_size, input_stream) is safer than scanf("%s") because it prevents buffer overflows.
    fgets(name, sizeof(name), stdin);

    printf("Hello, %s", name);

    return 0;
}
