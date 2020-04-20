#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int a = 1;
  int* p1 = &a;
  int** p2 = &p1;
  int*** p3 = &p2;

  printf("a = %d\t\t\t\t\t&a = %p\n", a, &a);
  printf("p1 = %p\t*p1 = %d\t\t\t&p1 = %p\n", p1, *p1, &p1);
  printf("p2 = %p\t*p2 = %p\t&p2 = %p\n", p2, *p2, &p2);
  printf("p3 = %p\t*p3 = %p\n", p3, *p3);

  return 0;
}
