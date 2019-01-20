#include <iostream>
#include <vector>
#include <sstream>
using namespace std;
template <class T>
vector<T> input_split() {
    cin >> ws;
    string line;
    getline(cin, line);
    stringstream ss(line);
    T buf;
    vector<T> tokens;
    while (ss >> buf)
        tokens.push_back(buf);
    return tokens;
}
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    int n;
    cin>>n;
    vector<vector<int> > a;
    vector<int> b;
    int ans = 0;
    for(int i=0;i<n;i++){
        b = input_split<int>();
        a.push_back(b);
    }
    for(int i=0;i<n;i++){
        bool knowother = false;
        bool knownallnotme = true;
        for(int j=0;j<n;j++){
            if(a[i][j]!=0) {
                knowother = true;
                break;
            }
            if( (i!=j && a[j][i] == 0) ||
                (i==j && a[j][i] != 0)) {
                knownallnotme = false;
                break;
            }
        }
        if(!knowother&&knownallnotme) cout<<i+1;
    }
    return 0;
}