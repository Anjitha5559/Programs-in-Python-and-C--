#include <iostream>
using namespace std;
class student{
    string name;
    public:
    int age;
    bool gender;

    student(){
        cout<<"Default Constructor";
    }//Default Constructor

    student(string s, int a, int g){
        cout<<"Parameterized Constructor";
        name = s;
        age = a;
        gender = g;
    }// Parameterized Constructor
    student (student &a){
        cout<<"Copy Constructor";
        name = a.name;
        age = a.age;
        gender = a.gender;
        }
  
    void setName(string s){
        name = s;
    }
    void getName(){
        cout<<name<<endl;
    }
    void printInfo(){
        cout<<"Name :"<<name<<endl;
        cout<<"Age :"<<age<<endl;
        cout<<"Gender :"<<gender<<endl;
    }
};
int main(){
    student arr[3];
    for (int i=0;i<3;i++){
        string s;
        cout<<"Name :";
        cin>>s;
        arr[i].setName(s);
        cout<<"Age :";
        cin>>arr[i].age;
        cout<<"Gender :";
        cin>>arr[i].gender;
    }
    for(int i=0;i<3;i++){
        arr[i].printInfo();
    }

    student a("Anjitha",20,1);
    // a.printInfo();
    return 0;
    student b;
    student c = a;

}
~student(){
    cout<<"Destructor is called";
}
