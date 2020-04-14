#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int a = 1;
  int* pa = &p;

  printf("a = %d\t&a = %p\n", a, &a);
  printf("*pa = %d\tpa = %p\n", *pa, pa);

  return 0;
}
