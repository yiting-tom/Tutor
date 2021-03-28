#include <stdio.h>

int main(void) {
  int i = 100;
  float f = 5.5;

  printf("Before chaged\n");
  printf("i is %d\t", i);
  printf("f is %f\n", f);

  printf("Now please enter an interger for i : ");
  scanf("%d", &i);
  printf("\nplease enter another float for f : ");
  scanf("%f", &f);

  printf("\nAfter chaged\n");
  printf("i is %d\t\t", i);
  printf("f is %f", f);

  return 0;
}
