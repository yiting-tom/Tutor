#include <stdio.h>
#include <stdlib.h>

void SWAP(int*, int*);

int main(void) {
  int a, b;
  printf("Please enter the value of A: ");
  scanf("%d", &a);
  printf("Please enter the value of B: ");
  scanf("%d", &b);

  SWAP(&a, &b);
  printf("After SWAP(a, b):\n");
  printf("A = %d\tB = %d\n", a, b);

    return 0;
}

void SWAP(int* s, int* t) {
  int temp = *s;
  *s = *t;
  *t = temp;
}

