#include <stdio.h>
#include <string.h> // Required for string manipulation functions

int main(void) {
    char source[] = "Quantum Mechanics";
    char destination[30];

    printf("C String Library Functions (<string.h>)\n");

    // 1. strlen() - Calculates length of string excluding '\0'
    size_t length = strlen(source);
    printf("1. String Length of '%s': %zu characters\n", source, length);

    // 2. strcpy() - Copies source string to destination buffer
    strcpy(destination, source);
    printf("2. Copied String (destination): %s\n", destination);

    // 3. strcat() - Concatenates (appends) one string to another
    char greeting[50] = "Computational ";
    strcat(greeting, "Physics");
    printf("3. Concatenated String: %s\n", greeting);

    // 4. strcmp() - Compares two strings lexicographically
    // Returns 0 if strings are identical, <0 if str1 < str2, >0 if str1 > str2
    char str1[] = "Apple";
    char str2[] = "Banana";
    char str3[] = "Apple";

    printf("\n4. String Comparisons (strcmp):\n");
    printf("   strcmp('Apple', 'Banana') : %d (Negative -> 'Apple' comes before 'Banana')\n", strcmp(str1, str2));
    printf("   strcmp('Banana', 'Apple') : %d (Positive -> 'Banana' comes after 'Apple')\n", strcmp(str2, str1));
    printf("   strcmp('Apple', 'Apple')  : %d (Zero -> Strings are identical)\n", strcmp(str1, str3));

    return 0;
}
