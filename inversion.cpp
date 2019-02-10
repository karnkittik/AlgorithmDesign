#include <iostream>
using namespace std;
int main(){
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        int x;cin>>x;
        a[i]=x;
    }
    int inv = 0;
    for(int i =0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(a[j]<a[i]) inv+=1;
        }
    }
    cout<<inv;
}