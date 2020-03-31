#include <stdio.h>
#include <string.h>

int main(void) {
    char text[] = "hello";
    int length = sizeof(text) / sizeof(text[0]);

    for(int i = 0; i < length; i++) {
        if(text[i] == '\0') {
            puts("null");
        } else {
            printf("%c ", text[i]);
        }
    }
    printf("陣列長度 %d\n", length);
    printf("字串長度 %d", strlen(text));

    return 0;
}