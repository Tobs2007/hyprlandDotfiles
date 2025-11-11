#include <unistd.h>
#include <cmath>
#include <sys/types.h>
#include <pwd.h>
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <thread>
#include <unistd.h>
using namespace std;

string target;
int targetTime;

int getRemaining() {
    auto curtimeclock = chrono::system_clock::now();
    int curtime = chrono::duration_cast<chrono::seconds>(curtimeclock.time_since_epoch()).count();
    int targetdiff = targetTime - curtime;
    return targetdiff;
}

int main() {
    struct passwd *pw = getpwuid(getuid());
    string homedir = pw->pw_dir;
    
    
    while (true) {
        ifstream inFile;
        inFile.open(homedir + "/dotfiles/waybar/targetTime.json");
        getline (inFile,target);
        inFile.close();
        targetTime = stoi(target);
        
        int diff = getRemaining();
        
        if (diff < 0) {
            cout << "Timer\n";
        } else {
            int hour = floor(diff / 3600);
            int minute = floor((diff % 3600)/60);
            int seconds = diff % 60;
            
            if (hour <= 0) {
                cout << minute << ":" << seconds << "\n";
            } else {
                cout << hour << ":" << minute << ":" << seconds << "\n";
            }
        }
        cout.flush();
        sleep(1);
    }
}
