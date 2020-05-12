#include <stdio.h>
#include <string.h>
#define LEN 80

int main(void) {
    char source[LEN];
    char search[LEN];

    printf("string : ");
    fgets(source, LEN, stdin);

    printf("substring : ");
    fgets(search, LEN, stdin);

    // remove "\n" charactor
    search[strlen(search) - 1] = '\0';

    char *loc = strstr(source, search);

    if(loc == NULL) {
        printf("can't find substring\n");
    }
    else {
        printf("at [%lu] find substring\n", loc - source);
    }

    return 0;
}
