#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int i, j, I, J;
    while(cin >> i >> j){
        if(i > j) I = j, J = i;
        else I = i, J = j;
        int Max=1;
        for(int X=I; X<=J; X++){
            int x = X, cycle=1;
            while(x != 1){
                if(x%2 == 0){
                    x = x/2;
                    cycle = cycle+1;
                }
                else{
                    x = x*3+1;
                    cycle = cycle+1;
                }
            }
            Max = max(Max, cycle);
        }
        cout << i << ' ' << j << ' ' << Max << endl;
    }
}
