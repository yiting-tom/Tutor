#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct date {
  int year;
  char* month;
  char* day;
} today = {2020, "Apr.", "Wen."};

int main(void) {

  printf("year: %d\t", today.year);
  printf("month: %s\t", today.month);
  printf("day: %s\n", today.day);

  return 0;
}
