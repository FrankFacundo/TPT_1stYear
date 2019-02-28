#include <stdio.h>
#include <signal.h>
#include <unistd.h>
int main(int argc, char *argv[]){

  int Nb_Sig;
  int Val_Sig;

  printf("NSIG = %d", NSIG);
  sleep(3);


  for(Nb_Sig = 1; Nb_Sig < NSIG ; Nb_Sig ++)
  {
   Val_Sig = signal(Nb_Sig , SIG_IGN);
   printf("Valeur renvoyée pour : %d %d\n",Nb_Sig , Val_Sig );
  }


  while(1)
  {
    sleep(5);
  } /* Wait for receiving signals */


  return 0;
}
