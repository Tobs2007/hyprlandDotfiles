#include <iostream>
#include <regex>
#include <string>
#include <fstream>
#include <unistd.h>
#include <glob.h>
#include <string.h>
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
    cout << "no dhcp\n";
    cout.flush();
    return 1;
}

int main() {
    while (true) {
        // read log from file
        if (gl() == 0) {
            
            ifstream inFile;
            inFile.open("/var/dhcpd.leases");
            string target;
            string content;
            while (getline (inFile,target)){content += target + "\n";}
            inFile.close();
            
            // get latest lease from log
            smatch res;
            regex ipRegex ("lease (([0-9]{1,3}\\.){3}[0-9]{1,3})[^\\}]*\\}\n$");
            
            
            if (regex_search(content,res,ipRegex)) {
                int count = 0;
                for (auto i : res) {
                    count++;
                    if (count == 2) {
                        cout << i << "\n";
                        cout.flush();
                    }
                }
            }
        }
        sleep(10);
    }
}