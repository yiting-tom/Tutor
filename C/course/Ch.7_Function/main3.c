#include <stdio.h>
#include <stdlib.h>

int Filbonacci(int n) {
    if (n <= 2) return 1;
    return Filbonacci(n-1) + Filbonacci(n-2);
}

int main(void) {
    int i;

    for (i=3; i<10; i++) {
      printf("F(%d) : %d\n",i , Filbonacci(i));
    }

    return 0;
}
