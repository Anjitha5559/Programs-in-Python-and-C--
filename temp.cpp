#include <iostream>
#include <vector>
using namespace std;
class Solution{
public:
    vector <int> leaders(int a[] ,int n){
        vector <int> k;
        int r = a[n-1];
        for(int i=n-2;i>=0;i--){
            if(a[i]>=r){
                r = a[i];
                k.insert(k.begin(),a[i]);
            }
            
        }
        k.push_back(a[n-1]);
        return k;
    }
};
int main(){
    int n;
    cout<<"Plz enter the number of elements in the array : ";
    cin>>n;
        int a[n];

    cout<<"Plz enter the elements in the array :";
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    Solution solution;
    vector <int> results = solution.leaders(a,n);
    cout<<"The leaders of the above array are :"<<endl;
    for(int i=0;i<results.size();i++){
        cout<<" "<<results[i]<<endl;
    }

return 0;
}