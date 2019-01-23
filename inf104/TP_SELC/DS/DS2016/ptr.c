

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
  int a = 5;
  int b = 10;
  int * ptr = &b;
  //int c = ptr;
  printf("Is this ok?%d\n",*(ptr)); //10 valor de b
  printf("Is this ok?%p\n",ptr); //
  printf("Is this ok?%d\n",*(ptr+a)); //145091981 addr
  printf("Is this ok?%d\n",ptr[0]); //145091981 addr
  return 0;
}
