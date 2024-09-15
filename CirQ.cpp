#include <iostream>
using namespace std;
class CircularQueue
{
private:
    int front;
    int rear;
    int arr[5];
    int itemCount;

public:
    CircularQueue()
    {	itemCount = 0;
        front = -1;
        rear = -1;
        for (int i = 0; i < 5; i++)
        {
            arr[i] = 0;
        }
    }
    bool isEmpty()
    {
        if (front == -1 && rear == -1)
            return true;
        else
            return false;
    }
    bool isFull()
    {
        if ((rear+1)%5 == front)
            return true;
        else
            return false;
    }
    void enqueue(int val)
    {
        if (isFull())
        {
            cout << "Queue is Full\n";
            return;
        }
        else if (isEmpty())
        {
            rear = 0;
            front = 0;
            arr[rear] = val;
        }
        else
        {
			rear = (rear+1)%5;
			arr[rear]=val;

        }
        itemCount++;

    }
    int dequeue()
    {
        int x;
        if (isEmpty())
        {
            cout << "The Queue is Empty\n";
            return 0;
        }
        else if (front == rear)
        {
            x = arr[front];
            arr[front] = 0;
            rear = -1;
            front = -1;
            itemCount--;
            return x;
        }
        else
        {
            x = arr[front];
            arr[front] = 0;
            front = (front+1)%5;
            itemCount--;
            return x;
        }
    }
    int count()
    {
		return (itemCount);
    }
    void display()
    {
        cout << "All Values in the Queue are \n";
        for (int i = 0; i < 5; i++)
        {
            cout << arr[i] << "\n";
        }
    }
};
int main()
{
    CircularQueue q1;
    int option, value;
    do
    {
        cout << "\n\n What Operation do you want to perform? Select Option Number. Enter 0 to exit.\n";
        cout << "1. Enqueue()\n";
        cout << "2. Dequeue()\n";
        cout << "3. isEmpty()\n";
        cout << "4. isFull()\n";
        cout << "5. cout()\n";
        cout << "6. display()\n";
        cout << "7. Clear Screen\n";

        cin >> option;

        switch (option)
        {
        case 0:
            break;
        case 1:
            cout << "Enqueue Operation \n Enter an item to Enqueue in the Queue\n";
            cin >> value;
            q1.enqueue(value);
            break;
        case 2:
            cout << "Dequeue Operation \n Dequeue value is" << q1.dequeue() << "\n";
            break;
        case 3:
            if (q1.isEmpty())
                cout << "Queue is Emoty\n";
            else
                cout << "Queue is not Full\n";
            break;
        case 4:
            if (q1.isFull())
                cout << "Queue is Full\n";
            else
                cout << "Queue is not Full\n";
            break;
        case 5:
            cout << "Count Operation \n Count of items in Queue" << q1.count() << "\n";
            break;
        case 6:
            cout << "Display Function called \n";
            q1.display();
            break;
        case 7:
            printf("\033c");
            break;
        default:
            cout << "Enter Proper Option Number";
            break;
        }
    } while (option != 0);
    return 0;
}
