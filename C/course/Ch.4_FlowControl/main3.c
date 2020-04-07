#include <stdio.h>

int main(void) {
    for(int j = 1; j < 10; j++) {
        for(int i = 2; i < 10; i++) {

						if (i == 2) break;

            printf("%d*%d=%2d ", i, j, i * j);


        }
        puts("");
    }

    return 0;
}
