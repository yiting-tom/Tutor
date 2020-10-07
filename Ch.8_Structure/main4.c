#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int number;
  struct node* next;
} Node;

void printNode(Node);

int main(void) {
  Node A;
  Node B;

  A.number = 1;
  B.number = 2;

  A.next = &B;
  B.next = NULL;

  printNode(A);
  printNode(B);

  return 0;
}

void printNode(Node node) {
  printf("Node : %d >>> Node : %d\n", node.number, (node.next)->number);
}
