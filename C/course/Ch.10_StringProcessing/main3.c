#include <stdio.h>
#include <string.h>
#define LEN 80

int main(void) {
    char passwd[] = "123456";
    char buf[LEN];

    printf("please enter the password");
    fgets(buf, LEN, stdin);

    if(strncmp(passwd, buf, 6) == 0) {
        puts("correct password");
    }
    else {
        puts("invalid password");
    }

    return 0;
}
