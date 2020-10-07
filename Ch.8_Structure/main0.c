#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct date {
  int year;
  char* month;
  char* day;
};

int main(void) {
  struct date today;

  today.year = 2020;
  today.month = "Apr.";
  today.day = "Wen.";

  printf("year: %d\t", today.year);
  printf("month: %s\t", today.month);
  printf("day: %s\n", today.day);

  return 0;
}
