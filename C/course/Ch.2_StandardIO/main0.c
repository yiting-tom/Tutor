#include <stdio.h>

int main(void) {
  printf("~hello \n world~\n");
  printf("~hello \t world~\n");
  printf("~hello \b world~\n");

  printf("~hello \" world~\n");
  printf("~hello \' world~\n");
  printf("~hello \/ world~\n");
  printf("~hello \\ world~\n");

  printf("~hello \101 world~\n");
  printf("~hello \x41 world~\n");

  return 0;
}
