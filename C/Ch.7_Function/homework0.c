#include <stdio.h>
#include <stdlib.h>

int ageQuestion(int);

int main(void) {
  int n;    //第幾人

  printf("Please which person you want ask? ");
  scanf("%d", &n);
  printf("the age of %dth person is : %d\n", n, ageQuestion(n));

  return 0;
}

int ageQuestion(int n) {
  if (n == 1) return 10;
  if (n >  1) return ageQuestion( n-1 ) + 2;
}
