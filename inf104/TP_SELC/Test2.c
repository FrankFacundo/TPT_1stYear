/* scanf example */
#include <stdio.h>

int main ()
{
 char str [80];
 int i;

 printf ("Enter your family name: ");
 scanf ("%79s",str);
 printf ("Enter your age: ");
 scanf ("%d",&i);
 printf ("Mr. %s , %d years old.\n",str,i);
 printf ("Enter a hexadecimal number: ");
 scanf ("%x",&i);
 printf ("You have entered %#x (%d).\n",i,i);
 printf ("Enter your firstname and your promo seperated with a space (Example:Yves 1984)\n");
 int j = scanf ("%s %d", str, &i);
 if(j!=2)
   printf("format error when writing: your firstname your promo; found %d information(s)\n", j);
 else
   printf("Welcome %s, promo %d\n", str, i);
 return 0;
}
