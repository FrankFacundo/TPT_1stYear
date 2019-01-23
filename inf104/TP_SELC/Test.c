#include <stdio.h>
int main(int argc, char* argv[]){
  int J=0;
  int m = 10;
  int * p;
  p = &m;
  // int tab[5];
  // tab[0]= 10;
  //
  // printf("decimal : %d\n", *p);
  // printf("puntero : %p\n", p);
  // printf("puntero : %p\n", p+1);
  // printf("puntero : %p\n", *&p);
  // printf("puntero : %d\n", p);

  // printf("puntero : %p\n", tab);
  // printf("puntero : %d\n", *tab);
  // printf("puntero : %p\n\n", &tab);

  typedef struct competitor
{
 char * name[80];
 int time;
}competitor_t;

competitor_t tab[10];


 *(tab[0].name) = "Frank";
 tab[0].time = 20;
 printf("valor : %s\n", *(tab[0].name) );
 printf("puntero : %p\n", tab[0].name );

 printf("valor : %d\n", tab[0].time );
 printf("puntero : %p\n", &tab[0].time );
 //printf("puntero : %d\n", *tab[0].time );
 printf("puntero : %p\n", &tab[0] );
 printf("puntero : %p\n", tab[1] );
 //printf("puntero : %d\n", *tab[0] );
 //printf("puntero : %d\n", tab[0]);
}
