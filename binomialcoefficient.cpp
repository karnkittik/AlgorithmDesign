#include <iostream>
#include <vector>
using namespace std;
int d[30][30];
int cnk(int n,int k){
    if(k==0 || k==n) return 1;
    if(k<0 || k>n) return 0;
    if(d[n][k]>0) return d[n][k];
    return d[n][k] = cnk(n-1,k)+ cnk(n-1,k-1);
}
int main(){
    for(int i=0;i<30;i++){
        for(int j=0;j<30;j++){
            d[i][j]=0;
        }
    }
    int n,k;
    cin>>n>>k;
    cout<<cnk(n,k);
}