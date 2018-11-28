#include <stdio.h>
#include <string.h>

void display_message(char * message1)
{
  printf("%s", message1);
  //printf("\n");
}

int main(int argc, char *argv[]) {
  /* to be completed */
  // next line just shows how to use display_message; could be removed
  if(argc != 3){
  display_message("Wrong usage, 2 parameters expected: ./sum param1 param2\n");
  return 0;
  }


  // now, check that parameters represent integer values
  // declare, implement, and use function isCharInteger
  for (size_t i = 1; i < argc; i++) {
    int j = 0;
    const char* arg = argv[i];

    while (arg[j]!='\0')
    {
        if(isCharInteger(arg[j])==0)
        {
          display_message("Wrong usage, parameters param1 and param2 should be integers when executing ./sum param1 param2\n");
          return -2;
        }
        j++;
    }

  }

  /* arguments have been checked, we can proceed to the sum:
     1 - convert string into an integer value
     2 - sum obtained values
  */
  for (size_t i = 1; i < argc; i++) {
    int j = 0;
    const char* arg = argv[i];

    while (arg[j]!='\0')
    {
        if(isCharInteger(arg[j])==0)
        {
          display_message("Wrong usage, parameters param1 and param2 should be integers when executing ./sum param1 param2\n");
          return -2;
        }
        j++;
    }

  }

  return 0;


}

char isCharInteger(char c)
{
  switch (c) {
    case '0':
      return 1;
    case '1':
      return 1;
    case '2':
      return 1;
    case '3':
      return 1;
    case '4':
      return 1;
    case '5':
      return 1;
    case '6':
      return 1;
    case '7':
      return 1;
    case '8':
      return 1;
    case '9':
      return 1;
    }
}

char charToInteger(char c)
{
  switch (c) {
    case '0':
      return 0;
    case '1':
      return 1;
    case '2':
      return 2;
    case '3':
      return 3;
    case '4':
      return 4;
    case '5':
      return 5;
    case '6':
      return 6;
    case '7':
      return 7;
    case '8':
      return 8;
    case '9':
      return 9;
    }
}

char stringToInteger(char * c)
{
  /* to be completed */
  return 0;
}
