#include <iostream>
using namespace std;
class Rectangle{
    public:
    int l;
    int b;
    Rectangle(){ //Default Constructor
    l = 0;
    b = 0;
}
    Rectangle(int x, int y){ //Parameterized Constructor - when arguments needs to be passed
        l = x;
        b = y;
    }
    Rectangle(Rectangle &r){//Copy Constructor - intitalize an obj by another existing object
        l = r.l;
        b = r.b;
    }
    ~Rectangle(){ //Destructor
        cout<<"Destructor is called"<<endl;
    }
};



int main(){
    Rectangle *r1 = new Rectangle();
    cout<<r1->l<<r1->b<<endl;//Default
    delete r1;
    Rectangle r2(3,4);
    cout<<r2.l<<r2.b<<endl;//Parameterized
    Rectangle r3 = r2;
    cout<<r3.l<<r3.b<<endl;//Copy 
}