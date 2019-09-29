#include <iostream> // normal stuff
#include <vector> // vector
#include <numeric> // iota
#include <algorithm> // sort
using namespace std;

bool isPrime(int n){
    for (int x = 2; x < (n/2)+2; x++){
        if (n % x == 0)
        {
            return false;
        }
    }
    return true;
}

int numberOfThrees(int n){
    if (n < 10){
        if (n % 10 == 3){
            return 1;
        }
        return 0;
    }
    if (n % 10 == 3){
        return 1 + numberOfThrees(n /10);
    }
    return numberOfThrees(n / 10);
}

void vectorPrint(vector<auto> vec){
    for(auto i: vec){
        cout << i << ' ';
    }
    cout << endl;
}

bool sortingFunc(int x, int y){
    int xt = numberOfThrees(x);
    int yt = numberOfThrees(y);
    if(xt == yt){
        return x<y;
    }
    return xt < yt;
}

int main()
{
    vector<int> x(1000);
    iota(begin(x), end(x), 1);

    vector<int> good;

    for (int i = 0; i < x.size(); i++){
        if (isPrime(x[i])) {
            if (numberOfThrees(x[i]) > 0) {
                    good.push_back(x[i]);
            }
        }
    };
    sort(good.begin(), good.end(), sortingFunc);
    vectorPrint(good);
    return 0;
}
