#include <iostream>
#include <string>
using namespace std;
int main() {
    string text = "test";
    string* textref = &text;
    cout << *textref;
}