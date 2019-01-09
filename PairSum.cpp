#include <iostream>
#include <vector>
#include <set>

using namespace std;
int main(){
    int a,b;
    cin >> a >> b;
    vector<int> c;
    set<int> d;    
    int u;
    for(int i=0;i<a;i++){
        cin >> u;
        d.insert(u);
    }

    for(int i=0;i<b;i++){
        cin >> u;
        c.push_back(u);
    }
    for(auto v:c){
        string out = "NO";
       for(auto u:d) {
           if(d.count(v-u)>0){
               out = "YES"; 
               break;
           }
        } 
        cout << out <<endl;
    }
    return 0;
}