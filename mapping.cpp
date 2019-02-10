#include <iostream>
using namespace std;
int main(){
    int n;cin>>n;
    int a[n];int b[n];
    for(int i=0;i<n;i++){
        b[i]=0;
    }
    for(int i=0;i<n;i++){
        int x;cin>>x;
        if(x<1){
            cout<<"NO";return 0;
        }        
        a[i]=x;
        b[x-1]+=1;
    }
    for(int i=0;i<n;i++){
        if(b[i]!=1){
            cout<<"NO";return 0;
        }
    }
    cout<<"YES";
}