#include <iostream>
#include <string>

using namespace std;
string coffeebeans(string sentence)
{
    if (sentence.find("coffee") != -1) {
        return "Coffee Beans";
    };
    if (sentence.find("beans") != -1) {
        return "Coffee Beans";
    };
    return "sleepy";
}

string lowercase(string input){
    for (char &c : input){
        if (c >= 'A' && c <= 'Z'){
            c = c + 32;
        };
    };
    return input;
}

int main()
{
    string sentence;
    cout << " : ";
    getline(cin, sentence);
    cout << coffeebeans(lowercase(sentence)) << endl;
    return 0;
}
