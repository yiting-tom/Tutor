#include <stdio.h>
#include <stdlib.h>

// Facto(5) -> 5! = 5*4*3*2*1
int Facto(int);

int main(void) {
  int n;
  printf("Please enter the Factorial num: ");
  scanf("%d", &n);
  printf("%d! = %d\n", n, Facto(n));

  return 0;
}

int Facto(int n) {
  if (n <= 1) return 1;
  else return n * Facto(n-1);
}
