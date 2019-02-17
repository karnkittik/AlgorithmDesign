#include <iostream>
using namespace std;
int partition(int d[],int left,int right){
    int p = d[left]; //pivot
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
    int b = d[left];d[left]=d[j];d[j]=b;
    return j;
}
void quicksort(int d[],int left,int right){
    if(left>=right) return;
    int j = partition(d,left,right);
    quicksort(d,left,j-1);
    quicksort(d,j+1,right);
}
int main(){
    int n;cin>>n;
    int d[n];int x;
    for(int i=0;i<n;i++){
        cin>>x;
        d[i]=x;
    }
    quicksort(d,0,n-1);
    for(int i=0;i<n;i++){
        cout<<d[i]<<" ";
    }
}
