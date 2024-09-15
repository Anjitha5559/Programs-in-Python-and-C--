#include <iostream>
using namespace std;
class Stack // made the class
{
private:
    int top;
    int arr[5]; // we make stack as decreasing ordered array

public:
    Stack()
    {
        top = -1; // we decide and implement all operation with reference to the top keyword which is the address of the top stack value
        for (int i = 0; i < 5; i++)
        {
            arr[i] = 0;
        }
    }

    bool isEmpty() // isEmpty
    {
        if (top == -1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    bool isFull() // isFull
    {
        if (top == 4)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    void push(int val) // push
    {
        if (isFull())
        {
            cout << "Stack overflow" << endl;
        }
        else
        {
            top++;
            arr[top] = val;
        }
    }
    int pop() // pop
    {
        if (isEmpty())
        {
            cout << "Stack Underflow" << endl;
            return 0;
        }
        else
        {
            int popValue = arr[top];
            arr[top] = 0;
            top--;
            return popValue;
        }
    }
    int count() // count
    {
        return (top + 1);
    }
    int peek(int pos) // peek
    {
        if (isEmpty())
        {
            cout << "Stack Underflow" << endl;
        }
        else
        {
            return arr[pos];
        }
    }
    void change(int pos, int val) // changes
    {
        arr[pos] = val;
        cout << "value changed at location" << pos << endl;
    }
    void display() // display
    {
        for (int i = 4; i >= 0; i--)
        {
            cout << arr[i] << endl;
        }
    }
};
int main()
{
    Stack s1; // made object
    int option, position, value;
    do
    {
        cout << endl
             << "What operation do you want to perform? Select option number. Enter 0 to exit." << endl;
        cout << "1. Push()" << endl;
        cout << "2. Pop()" << endl;
        cout << "3. isEmpty" << endl;
        cout << "4. isFull" << endl;
        cout << "5. peek()" << endl;
        cout << "6. count()" << endl;
        cout << "7. change()" << endl;
        cout << "8. display()" << endl;
        cout << "9. Clear Screen" << endl
             << endl;

        cin >> option;
        switch (option) // making switch cases to choose from the options
        {
        case 0:
            break;
        case 1:
            cout << "Enter an item to push in the stack" << endl;
            cin >> value;
            s1.push(value);
            break;
        case 2:
            cout << "Pop function called and the poped value is :" << s1.pop() << endl;
            break;
        case 3:
            if (s1.isEmpty())
            {
                cout << "Stack is Empty" << endl;
                cout << endl;
            }
            else
            {
                cout << "Stack is not Empty" << endl;
                cout << endl;
            }
            break;
        case 4:
            if (s1.isFull())
            {
                cout << "Stack is Full" << endl;
                cout << endl;
            }
            else
            {
                cout << "Stack is not full" << endl;
                cout << endl;
            }
            break;
        case 5:
            cout << "Enter the position of item to peek :" << endl;
            cin >> position;
            cout << "peek function called and the value at position " << position << " is :" << endl
                 << s1.peek(position) << endl;
            break;
        case 6:
            cout << "The count function is called and the number of items in the Stack are " << s1.count() << endl;
            break;
        case 7:
            cout << "Change function called -" << endl;
            cout << "Enter the position of the item you have to change :";
            cin >> position;
            cout << endl;
            cout << "Enter the value of item you want to change :" << endl;
            cin >> value;
            s1.change(position, value);
            break;
        case 8:
            cout << "Display Function is called :" << endl;
            s1.display();
            break;
        case 9:
            system("cls");
            break;
        default:
            cout << "Enter Proper Option number" << endl;
        }

    } while (option != 0);

    return 0;
}
