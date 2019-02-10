#include <iostream>
#include <vector>
using namespace std;
int aresult(vector<pair<int,int> > &v,int start,int n){
    int result =1;
    int max = v[start].first;
    //cout<<max<<" ";
    for(int i=start+1;i<n;i++){
        if(v[i].first > max ){
            result+=1;
            max = v[i].first;
        }

    }
    return result;
}
int bresult(vector<pair<int,int> > &v,int end,int n){
    int result =1;
    int min = v[end].first;
    //cout<<max<<" ";
    for(int i=end-1;i>0;i--){
        if(v[i].first < min ){
            result+=1;
            min = v[i].first;
        }

    }
    return result;
}
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    int n,b;
    int maxresult = 1;
    int result;
    vector< pair<int,int> > a;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>b;
        a.push_back(make_pair(b,0));
    }
    for(int i=0;i<n;i++){
        result = aresult(a,i,n);
        //cout<<result;
        if(result>maxresult) maxresult = result;
    }
    for(int i=n-1;i>0;i--){
        result = bresult(a,i,n);
        //cout<<result;
        if(result>maxresult) maxresult = result;
    }
    cout<<maxresult;
}