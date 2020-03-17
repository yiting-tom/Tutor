#include <stdio.h>

int main(void) {
    int input = 0;
    int replay = 0;

    do {
        printf("please input integer : ");
        scanf("%d", &input);
        getchar();

        printf("This integer is odd or even? %c\n", ((input % 2) ? 'Y': 'N'));
        printf("continous? (1:keep going, 2:stop) : ");
        scanf("%d", &replay);
        getchar();
    } while(replay);

    return 0;
}