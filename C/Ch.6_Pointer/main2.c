#include <stdio.h>
#define LEN 5

int main(void) {
    int arr[LEN] = {10, 20, 30, 40, 50};
    int *p = arr;
    int i,k;

    arr[0];


    // Using pointer
    for(int i = 0; i < LEN; i++) {
        printf("*(p + %d): %d\n", i , *(p + i));
    }
    putchar('\n');

    // Using array pointer 
    for(int i = 0; i < LEN; i++) {
        printf("arr[%d]: %d\n", i , arr[i]);
    }

    // Using sizeof() to get interval
    for (i = 0; i < LEN; i++) {
      printf("*(*p + sizeof(int)) = %d\n", *p);
      k = p;
      p = k + sizeof(int);
    }


    return 0;
}
