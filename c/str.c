#include <stdio.h>
#include <string.h>

void example_concatenate(char* str1, char* str2){

    char* strFinal;
    strFinal = malloc(strlen(str1) + strlen(str2));
    strcpy(strFinal, str1);
    strcat(strFinal, str2);

    puts(strFinal);
    printf("%d \n", strlen(strFinal));
    printf("%d \n", sizeof(strFinal));

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
  printf("%d \n", strlen(str));
  printf("%d \n", sizeof(str));

  example_concatenate("string 1 ", "string 2");
  return 0;
}