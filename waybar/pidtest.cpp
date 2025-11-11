/* Compile cmd: gcc -std=gnu99 -W -Wall -Werror -s -o getpids getpids.c */

#include <cstddef>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <glob.h>
using namespace std;

int gl() {
    glob_t g;
    glob("/proc/[1-9]*",0,0,&g);
    
    int count = 0;
    char **names = g.gl_pathv;
    static char *line;
    static size_t line_len;
    string phrase = "dhcpd";
    const char* search = phrase.c_str();
    while (count++ < g.gl_pathc) {
        char buff[100];
        FILE *fp = fopen(strcat(strcpy(buff,*names++),"/stat"),"r");

        getline(&line, &line_len,fp);
        fclose(fp);
        // cout << strchr(line,'(') + 1;
        *strrchr(line,')') = 0;
        if (!strcmp(strchr(line,'(') + 1,search)) {
            return 0;
        }
        
    }
    cout << "\n";
    return 1;
}
int main(void)
{
    gl();
    // std::string sname = "dhcpd";
    // const char* name = sname.c_str();
    // cout << getpids(name);
}