#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct date {
  int year;
  char* month;
  char* day;
};

int main(void) {
  struct date today = {2020, "Apr.", "Wen."};
  struct date tomorrow = {.month = "Apr.", .day = "Thr.", .year = 2020};

  printf("Today:\n");
  printf("year: %d\t", today.year);
  printf("month: %s\t", today.month);
  printf("day: %s\n", today.day);

  printf("Tomorrow:\n");
  printf("year: %d\t", tomorrow.year);
  printf("month: %s\t", tomorrow.month);
  printf("day: %s\n", tomorrow.day);

  return 0;
}
