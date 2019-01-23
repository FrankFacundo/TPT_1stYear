#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[])
{
 char * name1 = "Adrien";
 char * name2 = "Adrien";
 if(name1==name2)
 {
   printf("Is this ok?\n");
   name2 = "Adriennnnn";
   name2 = "Adrien";
   if(name1==name2)
   {
   printf("Is this ok2222?\n");
   }
 }
 return 0;
}
