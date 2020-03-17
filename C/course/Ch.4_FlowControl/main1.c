#include <stdio.h>

int main(void) {
    int score = 0;

    printf("plese input score：");
    scanf("%d", &score);

    if(score >= 90) {
        puts("get A");
    } else if(score >= 80 && score < 90) {
        puts("get B");
    } else if(score >= 70 && score < 80) {
        puts("get C");
    } else if(score >= 60 && score < 70) {
        puts("get D");
    } else {
        puts("get E(fail)");
    }

    return 0;
}