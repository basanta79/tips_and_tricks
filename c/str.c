#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "macros.h"

static char *lang[] = {"EN", "LO"};
static int ids_pkg_mnu_items[] = {1,2,3,4,5,6};

void example_concatenate(char* str1, char* str2){

    char* strFinal;
    strFinal = malloc(strlen(str1) + strlen(str2));
    strcpy(strFinal, str1);
    strcat(strFinal, str2);

    puts(strFinal);
    printf("%d \n", strlen(strFinal)); // Should be as long as the sum of string lengths of the strings
    printf("%d \n", sizeof(strFinal)); // Should be 4 because this variable is a pointer
}

void example_crontruct_string(int langugaje, int tipoTerminal){

    char strFinal[20];

    printf("tamaño del array lang: %d \n",sizeof(lang)/4);
    printf("tamaño del array ids_pkg_mnu_items: %d \n", sizeof(ids_pkg_mnu_items)/4);
    printf("tamaño del array ids_pkg_mnu_items using macro: %d \n", ARRLEN(ids_pkg_mnu_items));

    snprintf(strFinal, sizeof(strFinal), "mnu%s%02d.TXT",  lang[langugaje], tipoTerminal);
    puts(strFinal);

}

int main ()
{
  char str[80];
  char err[80];
  
  strcpy (str,"these ");
  strcat (str,"strings ");
  strcat (str,"are ");
  strcat (str,"concatenated.");
  puts (str);
  sprintf(err, "from sprintf %s", str);
  puts(err);
  printf("strlen de str: %d \n", strlen(str));
  printf("sizeof de str: %d \n", sizeof(str));

  example_concatenate("string 1 ", "string 2");
  example_crontruct_string(0,9);
  example_crontruct_string(1,9);
  return 0;
}