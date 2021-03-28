#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "myString.h"

int main(void) {
  char *str2 = "James Shen";
  char *str1 = (char*) malloc(strlen(str2));
  char *str3 = "student";

  free(str1);
  printf("before copy str2 = %s\n", str2);
  printf("before copy str3 = %s\n", str3);
//  copyN_str(str1, str2, 5);

//  strcpy(str1, str2);

  char *str4 = (char*) valloc(strlen(str3) + strlen(str2));

  strcpy(str4, str3);
  strcat(str4, str2);
  printf("after copy str4 = %s\n", str4);

  return 0;
}
