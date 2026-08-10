#include <stdio.h>

void track_execution_count(void) {
    // Normal local variable: Re-initialized every time the function is called.
    int normal_count = 0;

    // STATIC local variable: Initialized ONLY ONCE when the program starts.
    // Retains its value in memory between function calls!
    static int static_count = 0;

    normal_count++;
    static_count++;

    printf("Normal count: %d  |  Static count: %d\n", normal_count, static_count);
}

int main(void) {
    printf("Static Local Variables Demo\n");
    printf("Calling track_execution_count() 4 times:\n\n");

    for (int i = 1; i <= 4; i++) {
        printf("Call #%d -> ", i);
        track_execution_count();
    }

    return 0;
}
