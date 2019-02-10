#include <iostream>
using namespace std;
int bsearch(int a[],int left,int right,int x,int past){
    if(left>=right) return past;
    int mid = (left+right)/2;
    if(a[mid]==x) return x;
    if(a[mid]>x){ //goleft
        return bsearch(a,left,mid,x,past);
    }else{
        return bsearch(a,mid+1,right,x,a[mid]);
    }
}
int main(){
    int n,m;cin>>n>>m;
    int a[n],b[m];
    for(int i=0;i<n;i++){
        int x;cin>>x;
        a[i]=x;
    }
    for(int i=0;i<m;i++){
        int x;cin>>x;
        b[i]=x;
    }
    int past =-1;
    for(int i=0;i<m;i++){
        cout<<bsearch(a,0,n,b[i],past)<<"\n";
    }
    
//==========================================
}