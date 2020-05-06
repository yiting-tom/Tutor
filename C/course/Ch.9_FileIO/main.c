#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    FILE* src = fopen(argv[1], "r");
    if(!src) {
        perror("open file failure");
        return EXIT_FAILURE;
    }

    FILE* dest = fopen(argv[2], "w");
    if(!dest) {
        perror("create file failure");
        return EXIT_FAILURE;
    }

    int c;
    while ((c = fgetc(src)) != EOF) { 
       fputc(c, dest);
    }

    if (ferror(src) || ferror(dest)) {
        puts("IO error");
    }

    fclose(src);
    fclose(dest);
}