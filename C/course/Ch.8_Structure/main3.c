#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//struct date {
//  int year;
//  char* month;
//  char* day;
//};
//typedef (struct date) Date;

typedef struct date {
  int year;
  char* month;
  int day;
} Date;

void printDate(Date);
void swapDay(Date *, Date *);

int main(void) {
  Date today = {2020, "Apr.", 3};
  Date tomorrow = {.month = "Apr.", .day = 4, .year = 2020};

//  int tempDay = today.day
//  (. ) : 從變數取得屬性
//  (->) : 從指標變數取得變數裡的屬性

  printf("Today:\n");
  printDate(today);
  printf("Tomorrow:\n");
  printDate(tomorrow);

  swapDay(&today, &tomorrow); 

  printf("\n\nToday:\n");
  printDate(today);
  printf("Tomorrow:\n");
  printDate(tomorrow);

  return 0;
}

void printDate(Date date) {
  printf("%d/%s/%d\n", date.year, date.month, date.day);
}

void swapDay(Date* today, Date* tomorrow) {
  int tempDay = today->day;
  today->day = tomorrow->day;
  tomorrow->day = tempDay;
}


