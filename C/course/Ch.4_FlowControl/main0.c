#include <stdio.h>

int main(void) {
    int input = 0;

    printf("please input an integer：");
    scanf("%d", &input);

    if(input % 2) {
        printf("%d is odd\n", input);
    }
    else {
        printf("%d is even\n", input);
    }

    return 0;
}