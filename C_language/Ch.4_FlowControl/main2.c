#include <stdio.h>

int main(void) {
    int score = 0; 
    int level = 0; 

    printf("please input score："); 
    scanf("%d", &score); 
    level = score / 10; 

    switch(level) { 
        case 10: 
        case 9: 
            puts("get A");
            break; 
        case 8: 
            puts("get B");
            break; 
        case 7: 
            puts("get C");
            break; 
        case 6: 
            puts("get D");
            break; 
        default: 
            puts("get E(fail)");
    } 

    return 0;
} 