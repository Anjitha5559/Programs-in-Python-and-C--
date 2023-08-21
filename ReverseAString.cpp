#include <iostream>
#include <string>
using namespace std;
int main(){
string myString = "Anjitha";
for(int i=0;i<myString.length();i++){
    cout<<myString[myString.length()-i-1]<<endl;
}
return 0;
}