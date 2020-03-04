#include <stdio.h>
#include <stdlib.h>

int main(void) {

  /*========== Data Types ==========*/ 
  //Charactor
  char c;

  //Integer
  short s;
  int i;
  long l;

  //Float
  float f;
  double d;
  /*===============================*/ 

  /*=========== Functions =========*/
  //scanf( , );
  scanf("%c", &c);

  scanf("%hd", &s);
  scanf("%d", &i);
  scanf("%ld", &l);

  scanf("%f", &f);
  scanf("%lf", &d);

  //printf( , );
  printf("%c\n", c);

  printf("%d\n", s);
  printf("%d\n", i);
  printf("%ld\n", l);
  
  printf("%f\n", f);
  printf("%lf\n", d);
  /*===============================*/ 


  return 0;
}
