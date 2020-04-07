#include <stdio.h>
#define LEN 5

int main(void) {
    int arr[LEN] = {10, 20, 30, 40, 50};
    int *p = arr;

    // Using pointer
    for(int i = 0; i < LEN; i++) {
        printf("*(p + %d): %d\n", i , *(p + i));
    }
    putchar('\n');

    // Using array
    for(int i = 0; i < LEN; i++) {
        printf("*(arr + %d): %d\n", i , *(arr + i));
    }

    return 0;
}