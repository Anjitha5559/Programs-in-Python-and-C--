#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int arr[] = {2,1,5,4,3,6,8};
    int arrlen = (sizeof(arr)/sizeof(arr[0]));
    cout<<"Hey";
    std::sort(arr,arr+arrlen);
    for(int i=0;i<arrlen;i++){
        cout<<arr[i] << " ";
    }
}