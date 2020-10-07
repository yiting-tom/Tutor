#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int size = 0;

  printf("please input the length for arr");
  scanf("%d", &size);

  int *arr = malloc(size * sizeof(int));

  printf("setting value: \n");
  for(int i = 0; i < size; i++) {
    printf("arr[%d] = ", i);
    scanf("%d" , arr + i);
  }

  printf("display element: \n");
  for(int i = 0; i < size; i++) {
    printf("arr[%d] = %d\n", i, *(arr+i));
  }

  free(arr);

  return 0;
}
