#include <iostream>
using namespace std;
int binarySearch(int d[],int left,int right,int m,int k){
    int mid = (left+right)/2;
    if(left>=right) return m;
    if(d[mid]==k) return mid;
    if(d[mid]<k)
        return binarySearch(d,left,mid,mid,k);
    else    
        return binarySearch(d,mid+1,right,m,k);
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
    for(int i=0;i<m;i++){
        cout<<binarySearch(a,0,m,-1,b[i])<<"\n";
    }
}