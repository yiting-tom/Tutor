#include <stdio.h>
#include <stdlib.h>

void swap(int* apple, int* banana) {
  int temp;
  temp = *apple;
  *apple = *banana;
  *banana = temp;
}
  

int main(void) {
  int a = 1;
  int b = 2;
  int temp;
  int* pa = &a;

  printf("Before swap : \na = %d\tb = %d\n", a, b);
  swap(&a, &b);
  printf("After swap : \na = %d\tb = %d\n", a, b);

//  printf("a = %d\t&a = %p\n", a, &a);
//  printf("*pa = %d\tpa = %p\n", *pa, pa);

  return 0;
}
