#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        int v;cin>>v;
        a[i]= v;
    }
    int in1=-1;int in2=-1;int in3=-1;
    for(int i=0;i<n;i++){
        if(a[i]==1){ in1=i;break;}
    }
    for(int i=0;i<n;i++){
        if(a[i]==2){ in2=i;break;}
    }
    for(int i=0;i<n;i++){
        if(a[i]==3){ in3=i;break;}
    }
    cout<<in1<<in2<<in3;
}