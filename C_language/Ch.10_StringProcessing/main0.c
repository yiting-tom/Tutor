#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[80];

    puts("please input the string");
    scanf("%s", buf);

    size_t length = strlen(buf);
    printf("the length of string : %lu\n", length);

    return 0;
}
