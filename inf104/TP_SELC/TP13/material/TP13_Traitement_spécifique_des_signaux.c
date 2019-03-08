#include <stdio.h>
#include <signal.h>
#include <unistd.h>
int main(int argc, char *argv[]){

  void fonc (int Num);
  int Nb_Sig;
  int Val_Sig;

  for(Nb_Sig = 1; Nb_Sig < NSIG ; Nb_Sig ++)
  {
   signal(Nb_Sig , fonc);
  }

  return 0;
}

void fonc (int Num){
  printf("Recu signal %d\n", Num);
}
