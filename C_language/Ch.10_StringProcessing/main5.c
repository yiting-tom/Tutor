#include <stdio.h>
#include <string.h>
#define LEN 80

int main(void) {
    char str1[LEN];
    char str2[LEN];

    printf("string : ");
    fgets(str1, LEN, stdin);

    printf("substring : ");
    fgets(str2, LEN, stdin);

    // remove '\n' charactor
    str2[strlen(str2) - 1] = '\0';

    size_t loc = strspn(str1, str2);

    if(loc == strlen(str1)) {
        printf("completily match\n");
    }
    else {
        printf("at [%lu] beging different\n", loc);
    }

    return 0;
}
