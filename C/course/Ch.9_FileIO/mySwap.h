#ifndef _MYSWAP_H_
#define _MYSWAP_H_

void swap(int *a, int *b) {
  int t = *b;
  *b = *a;
  *a = t;
}

void printString(char *str) {
  printf("%s\n", str);
}

#endif
