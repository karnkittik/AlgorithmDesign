#include <iostream>
using namespace std;
int main(){
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        int x;cin>>x;
        a[i] = x;
    }
    //a(n+1) = 1+a(n+1-a(a(n)))

}