#include <stdio.h>

int main(void) {
    int score = 0; 
    int sum = 0; 
    int count = -1; 

    while(score != -1) { 
        count++; 
        sum += score; 
        printf("please input socre (if input -1 will end)：");
        scanf("%d", &score);
    } 

    printf("the average socre is : %f\n", (double) sum / count ); 

    return 0;
}