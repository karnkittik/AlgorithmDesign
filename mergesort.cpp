#include <iostream>
using namespace std;
void merge(int d[],int left,int mid,int right){
    int t[right];
    int i = left;int j = mid+1;
    for(int k = left;k<=right;k++){
        if(i>mid){
            t[k] = d[j++]; continue;
        }
        if(j>right){
            t[k] = d[i++]; continue;
        }
        t[k] = (d[i]<d[j]) ? d[i++] : d[j++];
    }
    for(int k = left;k<=right;k++) d[k] = t[k];
}
void mergesort(int d[],int left,int right){
    if(left>=right) return;
    int mid = (left+right)/2;
    mergesort(d,left,mid);
    mergesort(d,mid+1,right);
    merge(d,left,mid,right);
}
int main(){
    int n[10];int x;
    for(int i=0;i<10;i++){
        cin>>x;
        n[i]=x;
    }
    mergesort(n,0,9);
    for(int i=0;i<10;i++){
        cout<<n[i]<<" ";
    }   
}
