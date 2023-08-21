#include <iostream>
#include <string>
using namespace std;
int main(){
bool isPalindrome;
string myString = "malayalam";
for(int i=0;i<myString.length();i++){
    if(myString[i]!=myString[myString.length()-i-1]){
        isPalindrome = false;
    }
    else{
        isPalindrome = true;
    }
}
if(isPalindrome){
    cout<<myString<<" Is A Pallindrome";
}
else{
    cout<<myString<<" Is not a Pallindrome";
}

return 0;
}