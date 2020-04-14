#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int a = 1;
  int* p1 = &a;
  int** p2 = &pa;
  int*** p3 = &p2;

  printf("a = %d\t&a = %p\n", a, &a);
  printf("p1 = %d\t*p1 = %d\t&p1 = %p\n", p1, *p1, &p1);
  printf("p2 = %d\t*p2 = %p\t&p2 = %p\n", p2, *p2, &p2);
  printf("p3 = %d\t*p3 = %p\n", p3, *p3);

  return 0;
}
