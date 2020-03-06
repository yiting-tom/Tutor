#include <stdio.h>
#include <stdlib.h>

int main(void) {

  /*========== Basic Data Types ==========*/
  /*========== 基本資料型態 ==========*/
  //Charactor(字元)
  char c;

  //Integer(整數)
  short s;
  int i;
  long l;

  //Float(浮點數)
  float f;
  double d;

  /*=========== Functions =========*/
  /*=========== 函數 =========*/
  //scanf( , );
  printf("input\n");
  printf("c ");
  scanf("%c", &c);  //%c : 以字元型態

  printf("d ");
  scanf("%d", &i);  //%d : 以十進制型態

  printf("f ");
  scanf("%f", &f);  //%f : 以浮點數型態

  //printf( , );
  printf("output\n");
  printf("%c\n", c);

  printf("%d\n", i);  //%d : 以十進制型態
  printf("%x\n", i);  //%x : 以十六進制型態

  printf("%f\n", f);
  printf("%lf\n", f);
  /*===============================*/


  return 0;
}
