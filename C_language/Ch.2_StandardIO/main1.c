#include <stdio.h>

int main(void) {
  int i = 100;
  float f = 5.5;

  printf("input\t\tformat\t\toutput\n");
  printf("100\t\t%%10d\t\t`%10d`\n", i);
  printf("100\t\t%%+d\t\t`%+d`\n", i);
  printf("100\t\t%%-10d\t\t`%-10d`\n", i);
  printf("100\t\t%% d\t\t`% d`\n", i);
  printf("100\t\t%%010d\t\t`%010d`\n", i);
  printf("5.5\t\t%%7.2f\t\t`%7.2f`\n", f);
  printf("5.5\t\t%%010.3f\t\t`%010.3f`\n", f);
  printf("5.5\t\t%%+10.4f\t\t`%10.4f`\n", f);


  return 0;
}
