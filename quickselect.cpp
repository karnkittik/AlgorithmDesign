#include <iostream>
using namespace std;
int partition(int d[],int left,int right){
    int p = d[left];
    int i = left; int j = right+1;
    while(i<j){
        while(d[--j]>p);
        while(d[++i]<p){
            if(i==right) break;
        }
        if(i<j){
            int a = d[i];d[i]=d[j];d[j]=a;
        }
    }
    int b=d[left];d[left]=d[j];d[j]=b;
    return j;
}
int quickSelect(int d[],int left,int right,int k){
    if(left==right) return d[left];
    int j = partition(d,left,right);
    int m = j-left+1; //m = number right of j
    if(k==m) return d[j];
    if(k<m) return quickSelect(d,left,j-1,k);
    else return quickSelect(d,j+1,right,k-m);
}
int main(){
    int n;cin>>n;
    int a[n];int x;
    for(int i=0;i<n;i++){
        cin>>x;
        a[i]=x;
    }
    int k;cin>>k;
    cout<< quickSelect(a,0,n-1,k);
}