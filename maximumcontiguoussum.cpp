#include <iostream>
#include <climits>
using namespace std;
int maxSubArraySum(int a[], int size) 
{ 
    int maxall = INT16_MIN, maxhere = 0;
    for(int i=0;i<size;i++){
        maxhere += a[i];
        if(maxhere>maxall) maxall = maxhere;
        if(maxhere<0) maxhere = 0;
    }
    return maxall;
} 
  
/*Driver program to test maxSubArraySum*/
int main() 
{ 
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        int x;cin>>x;
        a[i]=x;
    }
    int max_sum = maxSubArraySum(a, n); 
    cout << max_sum; 
    return 0; 
} 