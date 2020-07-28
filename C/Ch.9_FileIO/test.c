#include <stdio.h>
#include <stdlib.h>
#include "mySwap.h"

int main(int argc, char *argv[]) {
  for (int i=0; i<argc; i++)
    printString(argv[i]);

  return 0;
}
