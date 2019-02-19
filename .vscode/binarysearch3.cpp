#include <iostream>
using namespace std;
int bsearch(int a[],int left,int right,int k,int past){
    if(left>=right) return past;
    int mid = (left+right)/2;
    if(a[mid]<=k){//go right
        return bsearch(a,mid+1,right,k,mid);
    }
    else{
        return bsearch(a,left,mid,k,past);
    }
}
int main(){
    int m,n,x;
    cin>>m>>n;
    int a[m],b[n];
    for(int i=0;i<m;i++){
        cin>>x;
        a[i]=x;
    }
    for(int i=0;i<n;i++){
        cin>>x;
        b[i]=x;
    }
    for(int i=0;i<n;i++){
        cout<<bsearch(a,0,m,b[i],-1)<<"\n";
    }
}