#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n; 
    int cnt;
    int n1=0,n2=0,n3=0;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        int v;cin>>v;
        if(v==1) n1+=1;
        if(v==2) n2+=1;
        if(v==3) n3+=1;
        a[i]= v;
    }
   int n1in2=0,n1in3=0,n2in1=0,n2in3=0,n3in1=0,n3in2=0;

   for(int i=0;i<n;i++){
        if(n1<=i && i<n1+n2 && a[i]==1) {n1in2+=1;
        }
        else if(n1+n2<=i && i<n &&a[i]==1) {n1in3+=1; 
        }
        else if(0<=i && i<n1 && a[i]==2) {n2in1+=1;
        }
        else if(n1+n2<=i && i<n && a[i]==2) {n2in3+=1;
        }
        else if(0<=i && i<n1 && a[i]==3) {n3in1+=1; 
        }
        else if(n1<=i && i<n1+n2 && a[i]==3) {n3in2+=1;
        }
   }
   cnt = (max(n2in1-n1in2,n1in2-n2in1) + 
         max(n2in3-n3in2,n3in2-n2in3) + 
         max(n3in1-n1in3,n1in3-n3in1) )+
         (min(n2in1,n1in2) + 
         min(n2in3,n3in2) + 
         min(n3in1,n1in3)
         )- 1;
   //cout<<n1in2<<" "<<n1in3<<" "<<n2in1<<" "<<n2in3<<" "<<n3in1<<" "<<n3in2<<"\n";
   //cout<<n1<<n2<<n3<<"-"<<cnt;
   cout<<cnt;

}