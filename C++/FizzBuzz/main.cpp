#include <iostream>
using namespace std;

int main()
{
    for (int x=1; x <= 30; x++){
        if (x % 15 == 0) {
                cout << "FizzBuzz" << endl;
                continue;
        };
        if (x % 3 == 0) {
            cout << "Fizz" << endl;
            continue;
        };
        if (x % 5 == 0) {
            cout << "Buzz" << endl;
            continue;
        };
        cout << x << endl;
    };
    return 0;
}
