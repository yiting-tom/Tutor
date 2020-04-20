#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int **arr = calloc(2, sizeof(int*));

  for(int i = 0; i < 2; i++) {
    arr[i] = calloc(3, sizeof(int));
  }

  for(int i = 0; i < 2; i++) {
    for(int j = 0; j < 3; j++) {
      scanf("%d", &arr[i][j]);
    }
  }

  for(int i = 0; i < 2; i++) {
    for(int j = 0; j < 3; j++) {
      printf("%d ", arr[i][j]);
    }
    putchar('\n');
  }

  for(int i = 0; i < 2; i++) {
    free(arr[i]);
  }
  free(arr); 

  return 0;
}
