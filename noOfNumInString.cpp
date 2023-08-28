
#include <iostream>
#include <string>
using namespace std;
int main(){
    int num;
string myString = "Anjitha97001";
for (int i=0;i<myString.length();i++){
if(isdigit(myString[i])){
    num++;
}
}
// for(char c : myString){
//     if(isdigit(c)){
//         num++;
//     }
// }
cout<<num;
return 0;
}