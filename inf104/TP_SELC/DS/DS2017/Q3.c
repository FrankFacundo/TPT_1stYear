#include <stdio.h>
#include <stdlib.h>
int stringlen(char*);
int * len;
int main(int argc, char*argv[]) {
   int ret = stringlen(argv[1]);
   // char copy[8];
   char	 *	 copy	=	 (char*)malloc(ret+1) ;
   int i;
   for(i=0; i<=ret-1; i++) {
      copy[i] = argv[1][i];
   }
   printf("Taille de la chaine à copier : %d\n", ret);
   printf("copy : %s\n", copy);
}

int stringlen(char * str) {
  int i = 0;
  while(str[i]!='\0') {
    i++;
  }
  return i;
}
