#include <iostream>
using namespace std;
int modexpo(int a,int k,int m){
    if(k == 0) return 1;
    int c =  modexpo(a,k/2,m);
    int x = (c*c)%m;
    if(k%2 ==1) x = (a*x)%m;
    return x;
}
int main(){
    int x,n,k;
    cin>>x>>n>>k;
    cout<< modexpo(x,n,k);
}
