/* heavily influenced by an unnamed challenge */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#define PASSFILE "./vuln.pass"

int main(int argc, char **argv)
{
        char realpasswd[32];
        char givenpasswd[32];
        FILE *passfile;
        char *result;
        uid_t old_uid;

        printf("---WELCOME TO EXECUTOR---\n");
        if (argc!=2)
        {
                exit(1);
        }

        old_uid = getuid();
        setresuid(geteuid(), geteuid(), old_uid);
        printf("Enter the password:\n");
        
        result = fgets(givenpasswd, sizeof(givenpasswd), stdin);
        if (result==NULL)
        {
                perror("reading password");
                exit(1);
        }
        *(strchr(result, '\n')) = 0;

        passfile = fopen(PASSFILE, "r");
        if (passfile==NULL)
        {
                perror("openning password file");
                exit(1);
        }
        
        result = fgets(realpasswd, sizeof(realpasswd), passfile);
        if (result==NULL)
        {
                perror("reading from password file");
                exit(1);
        }
        *(strchr(result, '\n')) = 0;

        if (strcmp(realpasswd, givenpasswd)) 
        {
                printf("wrong password...\n");
                printf("lowering your priviledges\n");
                fflush(stdout);
                setreuid(old_uid, old_uid);
        }

        system(argv[1]);
}
