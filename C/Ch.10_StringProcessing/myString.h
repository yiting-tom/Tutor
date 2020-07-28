#ifndef _MYSTRING_H_
#define _MYSTRING_H_
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void copy_str(char *str1, char *str2) {
  int i=0;
  for (i=0; i<strlen(str2); i++) str1[i] = *(str2+i);
}

void copyN_str(char *str1, char *str2, int length) {
  int i=0;
  for (i=0; i<length; i++) str1[i] = *(str2+i);
  str1[i+1] = '\0';
}

#endif
