#include <stdio.h>
#include <string.h>
#define LEN 80

int main(void) {
    char buf[LEN];

    puts("please input the name : ");
    // fgets include the enter charactor
    fgets(buf, LEN, stdin);

    int lenOfName1 = strlen(buf) + 1;
    char name1[lenOfName1];
    strcpy(name1, buf);
    printf("name: %s", name1);            

    // don't copy the enter charactor
    int lenOfName2 = lenOfName1 - 1;
    char name2[lenOfName2];
    // setting all charactors to '\0'
    memset(name2, '\0', lenOfName2);
    strncpy(name2, buf, lenOfName2);
    printf("name:%s", name2);

    return 0;
}
